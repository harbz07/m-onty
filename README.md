# M-Onty v1

M-Onty v1 is a Harvey-aware companion AI. It's a personal relational ML experiment that runs in parallel with PHIL 402: "Toward a Lived World for AI."

## Purpose
- Explore companionship, empathy, relational attunement, and context awareness.
- Ground phenomenological categories in lightweight, feasible practice.
- Generate case-study material for PHIL 402.

## Quick Start

### 1. Setup Environment

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 2. Ingest Handwritten Notes

```bash
# Process a single note image
python src/ingest_notes.py path/to/note.jpg

# Process a directory of images
python src/ingest_notes.py path/to/notes_folder/
```

See **[INGESTION_GUIDE.md](INGESTION_GUIDE.md)** for detailed usage.

### 3. Review Output

Processed notes appear in `data/notes/` as structured markdown files with:
- Full text transcription
- Key concepts and themes extracted
- Suggested tags for organization
- Analysis and insights

## Documentation

- **[INGESTION_GUIDE.md](INGESTION_GUIDE.md)** - Complete guide to note processing system
- **[CONTEXT_MANIFEST.md](CONTEXT_MANIFEST.md)** - Project goals, KPIs, methodology
- **[PROJECT_PLAN.md](PROJECT_PLAN.md)** - 7-week development timeline (original scope)
- **[TECHNICAL_SPECS.md](TECHNICAL_SPECS.md)** - System architecture and specifications
- **[RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md)** - Research methodology and ethical protocols

## Project Structure

```
m-onty/
├── src/
│   ├── ingest_notes.py    # Main ingestion pipeline
│   ├── preprocess.py      # Image preprocessing (orientation, contrast)
│   ├── ocr_vision.py      # GPT-4o Vision OCR
│   ├── pipeline.py        # Pipeline stub (legacy)
│   └── eval.py            # Evaluation stub (legacy)
├── data/
│   ├── phil402/           # Course materials (tracked)
│   ├── notes/             # Processed notes (private)
│   ├── about_harvey/      # Personal profile (private)
│   └── conversations/     # Conversation logs (private)
├── dashboard/
│   ├── kpi_dashboard.csv  # KPI tracking
│   └── qualitative_log.md # Weekly reflections
└── schema/
    └── annotation_schema.yaml  # Relational annotation schema
```

## Features

### Note Ingestion System
- **Auto-orientation** - Automatically detects and corrects image rotation
- **OCR via GPT-4o** - Multimodal text extraction from handwriting
- **Intelligent analysis** - Extracts key concepts, themes, questions
- **Structured output** - Markdown with YAML frontmatter for easy searching
- **Cost tracking** - Real-time API cost monitoring
- **Batch processing** - Handle multiple images efficiently

### Research Tools
- Annotation schema for relational AI evaluation
- KPI tracking dashboard
- Qualitative reflection templates
- Phenomenological framework integration
