#!/usr/bin/env python3
"""
Note Ingestion Pipeline for M-Onty v1

Processes handwritten note images:
1. Preprocesses images (orientation, contrast, denoising)
2. Extracts text and analysis using GPT-4o Vision
3. Saves structured markdown output with metadata

Usage:
    python src/ingest_notes.py <image_or_directory> [options]
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import List, Optional
from datetime import datetime

import yaml
from dotenv import load_dotenv

from preprocess import ImagePreprocessor
from ocr_vision import VisionOCR

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NoteIngestionPipeline:
    """Complete pipeline for ingesting handwritten notes."""

    def __init__(self,
                 output_dir: Path,
                 preprocess: bool = True,
                 save_processed_images: bool = True):
        """
        Initialize ingestion pipeline.

        Args:
            output_dir: Directory to save processed notes
            preprocess: Whether to preprocess images
            save_processed_images: Whether to save preprocessed images
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.preprocess_enabled = preprocess
        self.save_processed = save_processed_images

        # Initialize processors
        self.preprocessor = ImagePreprocessor() if preprocess else None
        self.ocr = VisionOCR()

        # Create subdirectories
        self.notes_dir = self.output_dir / "notes"
        self.notes_dir.mkdir(exist_ok=True)

        if save_processed_images:
            self.processed_images_dir = self.output_dir / "processed_images"
            self.processed_images_dir.mkdir(exist_ok=True)

    def process_single_image(self,
                            image_path: Path,
                            custom_prompt: Optional[str] = None) -> dict:
        """
        Process a single note image through complete pipeline.

        Args:
            image_path: Path to image file
            custom_prompt: Optional custom analysis prompt

        Returns:
            Processing result dict
        """
        logger.info(f"Processing: {image_path}")

        result = {
            'source_image': str(image_path),
            'timestamp': datetime.now().isoformat(),
            'success': False
        }

        try:
            # Step 1: Preprocess image if enabled
            if self.preprocess_enabled:
                logger.info("Preprocessing image...")
                processed_image, preprocess_metadata = self.preprocessor.process_image(
                    image_path,
                    auto_orient=True,
                    enhance=True,
                    denoise=True
                )

                # Save processed image
                if self.save_processed:
                    processed_path = self.processed_images_dir / f"{image_path.stem}_processed.jpg"
                    self.preprocessor.save_processed_image(processed_image, processed_path)
                    ocr_input_path = processed_path
                    result['preprocessed_image'] = str(processed_path)
                    result['preprocessing'] = preprocess_metadata
                else:
                    # Use temp file
                    import tempfile
                    import cv2
                    temp_fd, temp_path = tempfile.mkstemp(suffix='.jpg')
                    cv2.imwrite(temp_path, processed_image)
                    ocr_input_path = Path(temp_path)
            else:
                ocr_input_path = image_path

            # Step 2: OCR and analysis with GPT-4o
            logger.info("Running OCR and analysis...")
            ocr_result = self.ocr.extract_text_and_analyze(
                ocr_input_path,
                analysis_prompt=custom_prompt
            )

            result['ocr'] = ocr_result
            result['success'] = True

            # Step 3: Generate output filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = f"{timestamp}_{image_path.stem}"
            output_md = self.notes_dir / f"{base_name}.md"
            output_json = self.notes_dir / f"{base_name}.json"

            # Step 4: Create markdown output
            markdown_content = self._create_markdown(ocr_result, image_path)
            output_md.write_text(markdown_content, encoding='utf-8')
            result['output_markdown'] = str(output_md)

            # Step 5: Save full JSON
            output_json.write_text(json.dumps(result, indent=2), encoding='utf-8')
            result['output_json'] = str(output_json)

            logger.info(f"✓ Successfully processed: {image_path.name}")
            logger.info(f"  Output: {output_md}")

        except Exception as e:
            logger.error(f"✗ Failed to process {image_path}: {e}")
            result['error'] = str(e)

        return result

    def _create_markdown(self, ocr_result: dict, source_path: Path) -> str:
        """
        Create structured markdown from OCR results.

        Args:
            ocr_result: OCR and analysis results
            source_path: Original image path

        Returns:
            Markdown string with YAML frontmatter
        """
        # Create frontmatter
        frontmatter = {
            'date': datetime.now().strftime("%Y-%m-%d"),
            'source': str(source_path.name),
            'tags': ocr_result.get('suggested_tags', []),
            'themes': ocr_result.get('themes', []),
            'key_concepts': ocr_result.get('key_concepts', []),
            'quality_rating': ocr_result.get('quality_rating'),
            'course': 'PHIL402'
        }

        # Build markdown
        md_parts = [
            "---",
            yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True).strip(),
            "---",
            "",
            f"# Notes from {source_path.stem}",
            "",
            "## Transcription",
            "",
            ocr_result.get('transcription', ''),
            ""
        ]

        # Add questions/insights if present
        insights = ocr_result.get('questions_or_insights', [])
        if insights:
            md_parts.extend([
                "## Questions & Insights",
                ""
            ])
            for insight in insights:
                md_parts.append(f"- {insight}")
            md_parts.append("")

        # Add analysis notes
        notes = ocr_result.get('notes', '')
        if notes:
            md_parts.extend([
                "## Analysis Notes",
                "",
                notes,
                ""
            ])

        # Add metadata footer
        metadata = ocr_result.get('metadata', {})
        md_parts.extend([
            "---",
            "",
            "**Processing Info:**",
            f"- Model: {metadata.get('model', 'N/A')}",
            f"- Timestamp: {metadata.get('timestamp', 'N/A')}",
            f"- Tokens: {metadata.get('tokens_used', {}).get('total', 'N/A')}",
            f"- Cost: ${metadata.get('estimated_cost', 0):.4f}"
        ])

        return "\n".join(md_parts)

    def process_directory(self,
                         directory: Path,
                         pattern: str = "*.jpg",
                         custom_prompt: Optional[str] = None) -> List[dict]:
        """
        Process all images in a directory.

        Args:
            directory: Directory containing images
            pattern: File pattern to match (default: *.jpg)
            custom_prompt: Optional custom analysis prompt

        Returns:
            List of processing results
        """
        image_paths = sorted(directory.glob(pattern))

        if not image_paths:
            logger.warning(f"No images found matching {pattern} in {directory}")
            return []

        logger.info(f"Found {len(image_paths)} images to process")

        results = []
        for i, image_path in enumerate(image_paths, 1):
            logger.info(f"\n{'='*60}")
            logger.info(f"Processing {i}/{len(image_paths)}: {image_path.name}")
            logger.info(f"{'='*60}")

            result = self.process_single_image(image_path, custom_prompt)
            results.append(result)

        # Summary
        successful = sum(1 for r in results if r.get('success'))
        logger.info(f"\n{'='*60}")
        logger.info(f"BATCH COMPLETE: {successful}/{len(results)} successful")
        logger.info(f"Total cost: ${self.ocr.total_cost:.4f}")
        logger.info(f"{'='*60}")

        # Save batch summary
        summary_path = self.output_dir / f"batch_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        summary = {
            'timestamp': datetime.now().isoformat(),
            'total_images': len(results),
            'successful': successful,
            'failed': len(results) - successful,
            'total_cost': self.ocr.total_cost,
            'results': results
        }
        summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
        logger.info(f"Batch summary saved to: {summary_path}")

        return results


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Ingest handwritten notes using image preprocessing and GPT-4o Vision",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process single image
  python src/ingest_notes.py photo.jpg

  # Process directory of images
  python src/ingest_notes.py photos/ --pattern "*.png"

  # Skip preprocessing
  python src/ingest_notes.py photo.jpg --no-preprocess

  # Custom output directory
  python src/ingest_notes.py photo.jpg --output data/notes_processed
        """
    )

    parser.add_argument(
        'input',
        type=str,
        help='Input image file or directory'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='data',
        help='Output directory (default: data/)'
    )

    parser.add_argument(
        '--pattern',
        type=str,
        default='*.jpg',
        help='File pattern for directory mode (default: *.jpg)'
    )

    parser.add_argument(
        '--no-preprocess',
        action='store_true',
        help='Skip image preprocessing'
    )

    parser.add_argument(
        '--no-save-images',
        action='store_true',
        help='Do not save preprocessed images'
    )

    parser.add_argument(
        '--prompt',
        type=str,
        help='Custom analysis prompt file (text file)'
    )

    args = parser.parse_args()

    # Load environment variables
    load_dotenv()

    # Load custom prompt if specified
    custom_prompt = None
    if args.prompt:
        prompt_path = Path(args.prompt)
        if prompt_path.exists():
            custom_prompt = prompt_path.read_text(encoding='utf-8')
            logger.info(f"Loaded custom prompt from {prompt_path}")
        else:
            logger.warning(f"Prompt file not found: {prompt_path}")

    # Initialize pipeline
    pipeline = NoteIngestionPipeline(
        output_dir=Path(args.output),
        preprocess=not args.no_preprocess,
        save_processed_images=not args.no_save_images
    )

    # Process input
    input_path = Path(args.input)

    if not input_path.exists():
        logger.error(f"Input path does not exist: {input_path}")
        sys.exit(1)

    if input_path.is_file():
        # Single file mode
        result = pipeline.process_single_image(input_path, custom_prompt)
        sys.exit(0 if result.get('success') else 1)
    elif input_path.is_dir():
        # Directory mode
        results = pipeline.process_directory(input_path, args.pattern, custom_prompt)
        successful = sum(1 for r in results if r.get('success'))
        sys.exit(0 if successful == len(results) else 1)
    else:
        logger.error(f"Invalid input: {input_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
