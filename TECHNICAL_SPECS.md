# M-Onty v1 — Technical Specifications

## System Architecture

### High-level overview
```
┌─────────────────┐
│ Handwritten     │
│ Notes (scans)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ OCR Pipeline    │
│ (preprocess.py) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Knowledge Base  │
│ (text corpus)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐       ┌──────────────┐
│ Context         │◄──────┤ PHIL 402     │
│ Retrieval       │       │ Materials    │
└────────┬────────┘       └──────────────┘
         │
         ▼
┌─────────────────┐
│ Fine-tuned LLM  │
│ (Harvey-aware)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ User Interface  │
│ (CLI/notebook)  │
└─────────────────┘

    Feedback loop ──────┐
         │              │
         ▼              │
┌─────────────────┐     │
│ Annotation &    │     │
│ Evaluation      │─────┘
└─────────────────┘
```

---

## Component Specifications

### 1. OCR Pipeline (`src/pipeline.py`)

**Purpose**: Convert handwritten notes to machine-readable text

**Inputs**:
- Scanned images (JPEG, PNG)
- Target DPI: ≥ 300
- Format: Grayscale or color

**Processing steps**:
1. **Deskew**: Correct rotational misalignment
   - Algorithm: Hough transform or projection profile
   - Angle threshold: ±10°
2. **Crop**: Remove margins and artifacts
   - Border detection via edge analysis
   - Preserve content boundaries
3. **Contrast normalization**: Enhance text visibility
   - Adaptive histogram equalization
   - Binarization threshold: Otsu's method
4. **OCR**: Text extraction
   - Primary: Tesseract OCR (open-source)
   - Fallback: Google Cloud Vision API (if accuracy < 85%)
   - Language: English
   - Mode: Handwriting recognition

**Outputs**:
- Plain text files (.txt)
- Structured markdown (.md) with metadata
- Confidence scores per block
- Manual correction flags for low-confidence regions

**Dependencies**:
```python
- opencv-python (deskew, crop, contrast)
- pytesseract (OCR)
- pillow (image loading)
- numpy (array operations)
```

**Performance targets**:
- OCR accuracy: ≥ 85% (validated against manual transcription)
- Processing speed: ~30 seconds per page
- Batch processing: 50+ pages unattended

---

### 2. Knowledge Base

**Purpose**: Structured storage of Harvey's personal context

**Data sources**:
1. OCR-processed handwritten notes
2. PHIL 402 course materials (syllabus, readings)
3. Conversational history logs
4. Explicit "about Harvey" metadata

**Format**:
- Primary: Markdown files with YAML frontmatter
- Structure:
  ```markdown
  ---
  date: 2025-11-15
  topic: phenomenology
  course: PHIL402
  tags: [merleau-ponty, embodiment, perception]
  ---

  # Note title

  Content here...
  ```

**Organization**:
```
data/
├── notes/
│   ├── 2025-11-15_phenomenology.md
│   ├── 2025-11-18_ethics.md
│   └── ...
├── phil402/
│   ├── syllabus.md
│   ├── reading_summaries/
│   └── lecture_notes/
├── about_harvey/
│   └── profile.yaml
└── conversations/
    ├── session_001.json
    └── ...
```

**Metadata schema**:
- Date/time
- Topic tags
- Course relevance
- Emotional valence (if applicable)
- Cross-references

**Privacy controls**:
- All data stored locally only
- Redaction list for sensitive terms (names, IDs, etc.)
- No cloud sync without explicit consent

---

### 3. Context Retrieval

**Purpose**: Surface relevant context for LLM prompts

**Methods**:
1. **Keyword search**: Simple string matching
2. **Semantic search**: Embedding-based similarity (optional v2 feature)
3. **Temporal search**: Date-range queries
4. **Tag-based filtering**: Topic/course filters

**Retrieval pipeline**:
1. Parse user query
2. Extract keywords and intent
3. Search knowledge base (multi-method)
4. Rank results by relevance score
5. Select top K chunks (K=3-5)
6. Format for LLM context window

**Relevance scoring**:
```python
score = (
    0.4 * keyword_match +
    0.3 * recency_weight +
    0.2 * tag_overlap +
    0.1 * conversational_continuity
)
```

**Context limits**:
- Max context length: 2000 tokens
- Fallback: Summarize if exceeds limit
- Always include: Harvey profile, current date, session history

---

### 4. Fine-tuned LLM

**Purpose**: Harvey-aware conversational agent

**Base model options**:
| Model | Pros | Cons | Cost |
|-------|------|------|------|
| GPT-3.5-turbo | Fast, cheap fine-tuning | Less capable | ~$3/1M tokens |
| GPT-4 | High quality | Expensive fine-tuning | ~$30/1M tokens |
| Llama 3 8B | Open-source, local | Requires GPU | Free (compute) |
| Mistral 7B | Good quality/size tradeoff | Less tested | Free (compute) |

**Fine-tuning approach**:
- Method: Supervised fine-tuning on personal corpus
- Format: Conversational examples (user/assistant pairs)
- Dataset size: 50-200 examples (start small)
- Epochs: 3-5
- Validation split: 20%

**Training data structure**:
```json
{
  "messages": [
    {"role": "system", "content": "You are M-Onty, Harvey's companion AI..."},
    {"role": "user", "content": "What did I write about Merleau-Ponty last week?"},
    {"role": "assistant", "content": "Last Tuesday you explored..."}
  ]
}
```

**System prompt template**:
```
You are M-Onty, a companion AI for Harvey. You have access to:
- Harvey's handwritten notes on phenomenology and AI ethics
- PHIL 402 course materials
- Previous conversation history

Your goals:
- Be empathetic and relationally attuned
- Provide context-aware responses
- Balance support with autonomy
- Engage in genuine, non-transactional dialogue

Harvey's background: [insert from about_harvey/profile.yaml]
Current context: [insert retrieved chunks]
```

**Inference parameters**:
- Temperature: 0.7 (balanced creativity/consistency)
- Top-p: 0.9
- Max tokens: 500 (conversational length)
- Presence penalty: 0.3 (reduce repetition)

---

### 5. Annotation & Evaluation (`src/eval.py`)

**Purpose**: Measure KPIs and track relational quality

**Annotation workflow**:
1. Export conversation logs to JSON
2. Load into annotation interface
3. Apply schema labels to each turn
4. Record KPI ratings per session
5. Write qualitative reflections

**Annotation schema** (see `schema/annotation_schema.yaml`):
- **Tone**: empathetic | neutral | directive
- **Context recall**: strong | weak | absent
- **Relational fit**: attuned | mismatched
- **Synthesis quality**: coherent | fragmented

**KPI measurement**:
| KPI | Measurement method | Scale | Cadence |
|-----|-------------------|-------|---------|
| Rapport Quality | Post-session Likert rating | 1-7 | Weekly |
| Flexibility | Response to novel requests | 1-7 | Per session |
| Concept Synthesis | Cross-domain integration quality | 1-10 | Per complex query |
| Autonomy | Guidance vs. over-direction balance | 1-10 | Weekly |

**Evaluation functions**:
```python
def compute_rapport(session_ratings: list[int]) -> float:
    """Average Likert ratings for the week"""
    return sum(session_ratings) / len(session_ratings)

def compute_context_recall(test_queries: list[tuple]) -> float:
    """% of context test queries answered correctly"""
    correct = sum(1 for q, a in test_queries if is_correct(a))
    return correct / len(test_queries)

def compute_synthesis(annotations: list[str]) -> float:
    """% of 'coherent' vs 'fragmented' annotations"""
    coherent = sum(1 for a in annotations if a == 'coherent')
    return (coherent / len(annotations)) * 10  # Scale to 1-10
```

**Dashboard updates**:
- Weekly: Update `dashboard/kpi_dashboard.csv`
- Qualitative: Update `dashboard/qualitative_log.md`
- Visualizations: Generate charts (matplotlib/seaborn)

---

## Data Flow

### Interaction lifecycle

1. **User input** → CLI/notebook interface
2. **Context retrieval** → Search knowledge base for relevant chunks
3. **Prompt construction** → System prompt + context + user input
4. **LLM inference** → Generate response using fine-tuned model
5. **Response delivery** → Display to user
6. **Logging** → Save conversation turn to session log
7. **Annotation** → Label turn with schema (async)
8. **Evaluation** → Compute KPIs weekly

### Training iteration lifecycle

1. **Collect data** → OCR new notes, add PHIL 402 materials
2. **Prepare dataset** → Format as conversational examples
3. **Fine-tune** → Run training job
4. **Validate** → Test on held-out examples
5. **Deploy** → Replace production model
6. **Evaluate** → Measure KPIs, collect feedback
7. **Iterate** → Repeat cycle

---

## Infrastructure Requirements

### Compute
- **Development**: MacBook / Linux workstation
- **OCR**: CPU (1-2 cores sufficient)
- **Fine-tuning**: GPU (8GB+ VRAM) or cloud API
- **Inference**: CPU for smaller models; GPU for Llama 13B+

### Storage
- **Data corpus**: ~500 MB (text + scans)
- **Models**: 2-10 GB per fine-tuned checkpoint
- **Logs**: ~100 MB for 7-week project
- **Total**: ~5-15 GB

### APIs (optional)
- OpenAI (fine-tuning + inference): ~$50-200 for 7 weeks
- Google Cloud Vision (OCR fallback): ~$1-5/1000 images
- Anthropic Claude (alternative LLM): ~$10-50 for 7 weeks

### Local alternatives
- Tesseract (OCR): Free, open-source
- Ollama (LLM inference): Free, local
- Llama/Mistral (base models): Free, open-source

---

## Security & Privacy

### Data handling
- **Storage**: Local filesystem only (no cloud)
- **Transmission**: No external API calls for personal data
- **Backup**: Encrypted external drive
- **Disposal**: Secure deletion after project (if needed)

### Redaction protocol
1. Maintain redaction list: `data/redaction_list.txt`
2. Automated scan for sensitive terms before any export
3. Manual review of all shared materials
4. No real names, IDs, addresses, phone numbers, etc.

### Model safety
- No malicious prompt injection (validate inputs)
- Rate limiting to prevent abuse
- Content filtering for harmful outputs
- Clear boundaries in system prompt

---

## Testing Strategy

### Unit tests
- OCR accuracy on known samples
- Context retrieval relevance scoring
- Annotation schema consistency

### Integration tests
- End-to-end pipeline (scan → OCR → retrieval → response)
- KPI computation accuracy
- Data logging integrity

### Evaluation tests
- Context recall test set (20 queries)
- Empathy test scenarios (10 cases)
- Autonomy balance tests (5 scenarios)
- Synthesis cross-domain prompts (10 queries)

### Continuous monitoring
- Weekly KPI tracking
- Qualitative log review
- Error rate monitoring
- User satisfaction check-ins

---

## Version Control

### Git workflow
- Main branch: `main` (stable releases)
- Development branch: `dev` (active work)
- Feature branches: `feature/ocr-pipeline`, etc.
- Tag releases: `v1.0`, `v1.1`, etc.

### Commit conventions
```
feat: Add OCR deskew functionality
fix: Correct context retrieval scoring bug
docs: Update TECHNICAL_SPECS with API details
data: Add Week 2 handwritten notes
eval: Week 3 KPI measurements
```

### Backup strategy
- Git push to GitHub (code + docs only, no data)
- Weekly backup to external drive (full project)
- Critical milestones: Export archive (zip)

---

## Future Extensions (v2+)

### Potential features
- **Semantic search**: Embedding-based context retrieval (Sentence-BERT)
- **Voice interface**: Speech-to-text input/output
- **Visual integration**: Image understanding of diagrams in notes
- **Multi-modal fine-tuning**: Images + text
- **Active learning**: Request clarification when uncertain
- **Long-term memory**: More sophisticated session history
- **Proactive engagement**: Scheduled check-ins or reminders

### Scalability considerations
- Vector database for semantic search (Pinecone, Weaviate)
- Cloud deployment for collaboration
- Web interface for easier access
- Mobile companion app

---

## Dependencies & Environment

### Python version
- Required: Python 3.9+
- Recommended: Python 3.11

### Core dependencies
```txt
# requirements.txt
numpy>=1.24.0
pandas>=2.0.0
pillow>=10.0.0
opencv-python>=4.8.0
pytesseract>=0.3.10
pyyaml>=6.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyter>=1.0.0  # for notebook interface
```

### Optional dependencies
```txt
# requirements-optional.txt
openai>=1.0.0  # for API-based fine-tuning
transformers>=4.35.0  # for local models
torch>=2.1.0  # for local training
sentence-transformers>=2.2.0  # for semantic search
```

### Development environment setup
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-optional.txt  # if using local models

# Install Tesseract (system dependency)
# macOS: brew install tesseract
# Ubuntu: sudo apt-get install tesseract-ocr
# Windows: download from GitHub releases
```

---

## Documentation Standards

### Code documentation
- Docstrings for all functions (Google style)
- Inline comments for complex logic
- Type hints for function signatures
- README in each src/ subdirectory

### Research documentation
- Weekly updates to PROJECT_PLAN.md
- Qualitative reflections in dashboard/qualitative_log.md
- Annotation guidelines in ANNOTATION_GUIDE.md (to be created)
- Final case study in docs/ directory

### Changelog
- Maintain CHANGELOG.md for version history
- Document breaking changes
- Note data format migrations

---

*This specification is a living document. Update as the project evolves.*
