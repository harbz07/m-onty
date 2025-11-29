# Note Ingestion System — User Guide

## Overview

The M-Onty v1 note ingestion system processes handwritten notes using:
1. **Image preprocessing** - Automatic orientation detection, contrast enhancement, denoising
2. **GPT-4o Vision OCR** - Multimodal text extraction and intelligent analysis
3. **Structured output** - Markdown files with YAML frontmatter for easy searching

## Setup

### 1. Install Dependencies

```bash
# Activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# Get your key from: https://platform.openai.com/api-keys
```

Your `.env` file should look like:
```
OPENAI_API_KEY=sk-proj-...your-key-here...
```

### 3. Prepare Note Images

- Take photos or scan handwritten notes
- Supported formats: JPG, PNG
- Recommended: 300+ DPI for scans, good lighting for photos
- Don't worry about orientation - the system auto-corrects

## Usage

### Process a Single Image

```bash
python src/ingest_notes.py path/to/note.jpg
```

Output will be in `data/notes/` as markdown and JSON files.

### Process Multiple Images

```bash
# Process all JPG files in a directory
python src/ingest_notes.py path/to/photos/

# Process PNG files
python src/ingest_notes.py path/to/photos/ --pattern "*.png"

# Process all common image formats
python src/ingest_notes.py path/to/photos/ --pattern "*.{jpg,jpeg,png}"
```

### Advanced Options

```bash
# Custom output directory
python src/ingest_notes.py note.jpg --output custom/output/dir

# Skip preprocessing (if images are already clean/oriented)
python src/ingest_notes.py note.jpg --no-preprocess

# Don't save processed images (saves disk space)
python src/ingest_notes.py note.jpg --no-save-images

# Use custom analysis prompt
python src/ingest_notes.py note.jpg --prompt my_prompt.txt
```

## Output Structure

After processing `handwritten_note.jpg`, you'll get:

```
data/
├── notes/
│   ├── 20251129_143022_handwritten_note.md    # Structured markdown
│   └── 20251129_143022_handwritten_note.json  # Full processing data
├── processed_images/
│   └── handwritten_note_processed.jpg         # Preprocessed image
└── batch_summary_20251129_143022.json         # Batch processing summary
```

### Markdown Format

```markdown
---
date: 2025-11-29
source: handwritten_note.jpg
tags: [phenomenology, merleau-ponty, embodiment]
themes: [perception, lived-experience]
key_concepts: [intersubjectivity, bodily-awareness]
quality_rating: 4
course: PHIL402
---

# Notes from handwritten_note

## Transcription

[Full text of your handwritten notes...]

## Questions & Insights

- Why does Merleau-Ponty prioritize perception?
- Connection to AI embodiment problem

## Analysis Notes

[GPT-4o's observations about the notes...]

---

**Processing Info:**
- Model: gpt-4o
- Timestamp: 2025-11-29T14:30:22
- Tokens: 1523
- Cost: $0.0145
```

## Understanding the Analysis

GPT-4o analyzes your notes and provides:

- **Transcription**: Accurate text extraction from handwriting
- **Key Concepts**: Important ideas mentioned (e.g., "phenomenology", "embodiment")
- **Themes**: Overarching topics (e.g., "lived experience", "perception")
- **Questions/Insights**: Questions you posed or insights you noted
- **Suggested Tags**: Useful tags for organizing (philosophers, topics, course keywords)
- **Quality Rating**: 1-5 scale on note clarity/completeness

## Cost Tracking

The system tracks API costs in real-time:

```
Processing image 1/5
  Cost: $0.0142 (Session total: $0.0142)
Processing image 2/5
  Cost: $0.0138 (Session total: $0.0280)
...
BATCH COMPLETE: 5/5 successful
Total cost: $0.0712
```

**Typical costs (GPT-4o, Nov 2024 pricing):**
- Single high-resolution image: ~$0.01-0.02
- Batch of 10 images: ~$0.10-0.20
- Batch of 50 images: ~$0.50-1.00

## Customizing Analysis

Create a custom prompt file to change how GPT-4o analyzes your notes:

**my_prompt.txt:**
```
You are analyzing notes for a philosophy student.

Focus on:
1. Transcribe text accurately
2. Identify arguments and their structure
3. Note any references to other philosophers
4. Highlight connections between ideas

Output as JSON with: transcription, arguments, references, connections
```

Then use:
```bash
python src/ingest_notes.py note.jpg --prompt my_prompt.txt
```

## Tips for Best Results

### Photography Tips
- Good lighting (natural light or bright lamp)
- Avoid shadows across text
- Hold camera/phone steady and parallel to page
- Capture entire page in frame
- Multiple focused shots better than one blurry panorama

### Note Organization
- Date your notes (system will tag by processing date)
- Use consistent headers/structure
- One topic per page works better than dense multi-topic pages
- Highlight key concepts in notes (GPT-4o will notice)

### Processing Strategy
1. Start with 1-2 test images to check quality
2. Adjust photo technique if OCR accuracy is low
3. Process in batches of 10-20 for manageable costs
4. Review first few outputs to ensure analysis meets needs

## Troubleshooting

### "OpenAI API key required" Error
- Check that `.env` file exists and contains `OPENAI_API_KEY=...`
- Ensure you've activated the virtual environment

### Poor OCR Accuracy
- Try better lighting when photographing
- Ensure text is in focus
- Use `--no-preprocess` if your images are already clean
- Consider using scans instead of photos for critical notes

### High Costs
- Use `--no-save-images` to reduce storage (won't affect OCR)
- Process selectively rather than all notes
- Use lower resolution images (still readable but fewer tokens)

### Orientation Issues
- The system should auto-detect, but if failing:
  - Manually rotate images before processing
  - Use `--no-preprocess` and ensure images are upright

## Integration with M-Onty Research

The structured markdown output is designed to integrate seamlessly:

1. **Tags and themes** - Searchable for context retrieval
2. **YAML frontmatter** - Parseable for building knowledge base
3. **Quality ratings** - Identify which notes to prioritize
4. **JSON output** - Full data for custom analysis scripts

You can build on this to:
- Create a searchable note database
- Feed context into Claude conversations
- Track concept evolution over time
- Generate study guides from themes

## Examples

### Example 1: Quick Single Note

```bash
# Take a photo of today's reading notes
python src/ingest_notes.py ~/Desktop/today_reading.jpg

# Output in data/notes/ ready for review
```

### Example 2: Batch Process Week's Notes

```bash
# Process all this week's photos
python src/ingest_notes.py ~/Documents/phil402_week5/ --pattern "*.jpg"

# Review batch_summary_*.json for overview
# Open individual .md files to read transcriptions
```

### Example 3: Focused Analysis

```bash
# Create prompt focused on Merleau-Ponty concepts
cat > merleau_prompt.txt << 'EOF'
Analyze these phenomenology notes focusing on Merleau-Ponty.
Identify: 1) Key M-P concepts, 2) Connections to embodiment,
3) Relevance to AI/technology, 4) Questions raised.
Output structured JSON.
EOF

# Process with custom prompt
python src/ingest_notes.py lecture_notes.jpg --prompt merleau_prompt.txt
```

## Next Steps

After ingesting your notes:

1. **Review outputs** - Check `data/notes/*.md` files
2. **Organize** - Move notes to themed subdirectories if desired
3. **Build context** - Use transcriptions in your paper research
4. **Iterate** - Adjust prompts or processing based on results
5. **Integrate** - Reference notes when working with Claude on your paper

The goal is to make your handwritten notes **searchable, analyzable, and useful** for your research - while keeping you in control of the actual thinking and writing.

---

**Questions or issues?** Check the main README.md or TECHNICAL_SPECS.md for more details.
