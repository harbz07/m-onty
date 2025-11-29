"""
Image preprocessing for handwritten notes.
Handles orientation correction and basic image cleanup.
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Tuple, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImagePreprocessor:
    """Preprocesses images of handwritten notes for OCR."""

    def __init__(self, target_dpi: int = 300):
        """
        Initialize preprocessor.

        Args:
            target_dpi: Target DPI for processed images
        """
        self.target_dpi = target_dpi

    def detect_orientation(self, image: np.ndarray) -> float:
        """
        Detect image orientation using text line detection.

        Args:
            image: Input image as numpy array

        Returns:
            Rotation angle in degrees (0, 90, 180, 270)
        """
        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        # Apply binary threshold
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Detect edges
        edges = cv2.Canny(binary, 50, 150, apertureSize=3)

        # Detect lines using Hough transform
        lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

        if lines is None:
            logger.warning("No lines detected for orientation, assuming 0°")
            return 0.0

        # Analyze line angles
        angles = []
        for rho, theta in lines[:, 0]:
            angle = np.degrees(theta)
            angles.append(angle)

        # Find dominant angle
        angles = np.array(angles)

        # Determine which quadrant most lines fall into
        # 0°, 90°, 180°, or 270°
        bins = [0, 45, 135, 225, 315, 360]
        hist, _ = np.histogram(angles, bins=bins)

        dominant_bin = np.argmax(hist)

        if dominant_bin == 0 or dominant_bin == 4:
            return 0.0
        elif dominant_bin == 1:
            return 90.0
        elif dominant_bin == 2:
            return 180.0
        else:
            return 270.0

    def rotate_image(self, image: np.ndarray, angle: float) -> np.ndarray:
        """
        Rotate image by specified angle.

        Args:
            image: Input image
            angle: Rotation angle in degrees

        Returns:
            Rotated image
        """
        if angle == 0:
            return image

        # Get image dimensions
        height, width = image.shape[:2]

        # Handle 90-degree rotations efficiently
        if angle == 90:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            return cv2.rotate(image, cv2.ROTATE_180)
        elif angle == 270:
            return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # For arbitrary angles (shouldn't happen with detect_orientation)
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, rotation_matrix, (width, height),
                                 flags=cv2.INTER_CUBIC,
                                 borderMode=cv2.BORDER_REPLICATE)
        return rotated

    def enhance_contrast(self, image: np.ndarray) -> np.ndarray:
        """
        Enhance image contrast for better OCR.

        Args:
            image: Input image

        Returns:
            Contrast-enhanced image
        """
        # Convert to LAB color space
        if len(image.shape) == 3:
            lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)
        else:
            l = image

        # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_l = clahe.apply(l)

        # Merge back
        if len(image.shape) == 3:
            enhanced_lab = cv2.merge([enhanced_l, a, b])
            enhanced = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
        else:
            enhanced = enhanced_l

        return enhanced

    def remove_noise(self, image: np.ndarray) -> np.ndarray:
        """
        Remove noise from image while preserving text.

        Args:
            image: Input image

        Returns:
            Denoised image
        """
        # Apply bilateral filter (preserves edges while smoothing)
        denoised = cv2.bilateralFilter(image, 9, 75, 75)
        return denoised

    def process_image(self,
                     image_path: Path,
                     auto_orient: bool = True,
                     enhance: bool = True,
                     denoise: bool = True) -> Tuple[np.ndarray, dict]:
        """
        Complete preprocessing pipeline for a single image.

        Args:
            image_path: Path to input image
            auto_orient: Whether to auto-detect and correct orientation
            enhance: Whether to enhance contrast
            denoise: Whether to remove noise

        Returns:
            Tuple of (processed image, metadata dict)
        """
        logger.info(f"Processing image: {image_path}")

        # Load image
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")

        metadata = {
            'original_path': str(image_path),
            'original_size': image.shape[:2],
            'rotation_applied': 0.0,
            'steps': []
        }

        # Auto-orient
        if auto_orient:
            angle = self.detect_orientation(image)
            if angle != 0:
                image = self.rotate_image(image, angle)
                metadata['rotation_applied'] = angle
                metadata['steps'].append(f'rotated_{angle}deg')
                logger.info(f"Rotated image by {angle}°")

        # Denoise
        if denoise:
            image = self.remove_noise(image)
            metadata['steps'].append('denoised')

        # Enhance contrast
        if enhance:
            image = self.enhance_contrast(image)
            metadata['steps'].append('contrast_enhanced')

        metadata['final_size'] = image.shape[:2]

        logger.info(f"Completed processing: {', '.join(metadata['steps'])}")

        return image, metadata

    def save_processed_image(self,
                            image: np.ndarray,
                            output_path: Path,
                            quality: int = 95) -> None:
        """
        Save processed image to disk.

        Args:
            image: Processed image
            output_path: Output file path
            quality: JPEG quality (0-100)
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save with high quality
        cv2.imwrite(str(output_path), image,
                   [cv2.IMWRITE_JPEG_QUALITY, quality])

        logger.info(f"Saved processed image to: {output_path}")


if __name__ == "__main__":
    # Simple test
    import sys

    if len(sys.argv) < 2:
        print("Usage: python preprocess.py <image_path>")
        sys.exit(1)

    preprocessor = ImagePreprocessor()
    image_path = Path(sys.argv[1])

    processed, metadata = preprocessor.process_image(image_path)

    # Save to temp location
    output_path = image_path.parent / f"{image_path.stem}_processed{image_path.suffix}"
    preprocessor.save_processed_image(processed, output_path)

    print(f"Metadata: {metadata}")
