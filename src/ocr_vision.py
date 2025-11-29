"""
GPT-4o Vision-based OCR and analysis for handwritten notes.
"""

import base64
import json
import logging
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime
import os

from openai import OpenAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VisionOCR:
    """OCR and analysis using GPT-4o vision capabilities."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        """
        Initialize Vision OCR.

        Args:
            api_key: OpenAI API key (or use OPENAI_API_KEY env var)
            model: Model to use (default: gpt-4o)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable.")

        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.total_cost = 0.0

    def encode_image(self, image_path: Path) -> str:
        """
        Encode image to base64 string.

        Args:
            image_path: Path to image file

        Returns:
            Base64-encoded image string
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def extract_text_and_analyze(self,
                                 image_path: Path,
                                 analysis_prompt: Optional[str] = None) -> Dict:
        """
        Extract text from image and perform analysis.

        Args:
            image_path: Path to image file
            analysis_prompt: Custom analysis instructions (optional)

        Returns:
            Dict with extracted text, analysis, and metadata
        """
        logger.info(f"Processing image with GPT-4o: {image_path}")

        # Encode image
        base64_image = self.encode_image(image_path)

        # Default analysis prompt
        if analysis_prompt is None:
            analysis_prompt = """
You are analyzing handwritten notes for a phenomenology student named Harvey working on PHIL 402.

Please:
1. Transcribe all handwritten text accurately (preserve formatting, lists, emphasis)
2. Identify key concepts and themes
3. Note any questions, insights, or connections mentioned
4. Suggest relevant tags (e.g., topics, philosophers, course concepts)
5. Rate the quality/clarity of the notes (1-5 scale)

Format your response as structured JSON with these fields:
{
  "transcription": "Full text transcription...",
  "key_concepts": ["concept1", "concept2"],
  "themes": ["theme1", "theme2"],
  "questions_or_insights": ["question/insight1"],
  "suggested_tags": ["tag1", "tag2"],
  "quality_rating": 4,
  "notes": "Any additional observations..."
}
"""

        # Make API call
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": analysis_prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=2000,
                temperature=0.3  # Lower temperature for more accurate transcription
            )

            # Extract response
            content = response.choices[0].message.content

            # Try to parse as JSON
            try:
                # Look for JSON in markdown code blocks
                if "```json" in content:
                    json_str = content.split("```json")[1].split("```")[0].strip()
                elif "```" in content:
                    json_str = content.split("```")[1].split("```")[0].strip()
                else:
                    json_str = content

                result = json.loads(json_str)
            except json.JSONDecodeError:
                logger.warning("Could not parse response as JSON, using raw text")
                result = {
                    "transcription": content,
                    "key_concepts": [],
                    "themes": [],
                    "questions_or_insights": [],
                    "suggested_tags": [],
                    "quality_rating": 3,
                    "notes": "Response was not in expected JSON format"
                }

            # Add metadata
            result['metadata'] = {
                'model': self.model,
                'timestamp': datetime.now().isoformat(),
                'image_path': str(image_path),
                'tokens_used': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens,
                    'total': response.usage.total_tokens
                }
            }

            # Estimate cost (GPT-4o pricing as of late 2024)
            # Input: ~$2.50 per 1M tokens, Output: ~$10 per 1M tokens
            input_cost = (response.usage.prompt_tokens / 1_000_000) * 2.50
            output_cost = (response.usage.completion_tokens / 1_000_000) * 10.00
            call_cost = input_cost + output_cost
            self.total_cost += call_cost

            result['metadata']['estimated_cost'] = round(call_cost, 4)
            result['metadata']['total_session_cost'] = round(self.total_cost, 4)

            logger.info(f"Extracted {len(result.get('transcription', ''))} characters")
            logger.info(f"Cost: ${call_cost:.4f} (Session total: ${self.total_cost:.4f})")

            return result

        except Exception as e:
            logger.error(f"Error processing image: {e}")
            raise

    def batch_process(self,
                     image_paths: List[Path],
                     analysis_prompt: Optional[str] = None) -> List[Dict]:
        """
        Process multiple images in batch.

        Args:
            image_paths: List of image file paths
            analysis_prompt: Custom analysis instructions

        Returns:
            List of results for each image
        """
        results = []

        for i, image_path in enumerate(image_paths, 1):
            logger.info(f"Processing image {i}/{len(image_paths)}")

            try:
                result = self.extract_text_and_analyze(image_path, analysis_prompt)
                results.append(result)
            except Exception as e:
                logger.error(f"Failed to process {image_path}: {e}")
                results.append({
                    'error': str(e),
                    'image_path': str(image_path),
                    'metadata': {'timestamp': datetime.now().isoformat()}
                })

        logger.info(f"Batch processing complete. Total cost: ${self.total_cost:.4f}")

        return results


if __name__ == "__main__":
    # Simple test
    import sys
    from dotenv import load_dotenv

    load_dotenv()

    if len(sys.argv) < 2:
        print("Usage: python ocr_vision.py <image_path>")
        sys.exit(1)

    ocr = VisionOCR()
    image_path = Path(sys.argv[1])

    result = ocr.extract_text_and_analyze(image_path)

    print("\n" + "="*60)
    print("TRANSCRIPTION:")
    print("="*60)
    print(result.get('transcription', ''))

    print("\n" + "="*60)
    print("ANALYSIS:")
    print("="*60)
    print(f"Key Concepts: {', '.join(result.get('key_concepts', []))}")
    print(f"Themes: {', '.join(result.get('themes', []))}")
    print(f"Tags: {', '.join(result.get('suggested_tags', []))}")
    print(f"Quality: {result.get('quality_rating', 'N/A')}/5")

    print("\n" + "="*60)
    print("METADATA:")
    print("="*60)
    print(json.dumps(result.get('metadata', {}), indent=2))
