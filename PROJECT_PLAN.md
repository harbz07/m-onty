# M-Onty v1 — 7-Week Project Plan

## Overview
This document breaks down the 7-week development cycle for M-Onty v1, a Harvey-aware companion AI aligned with PHIL 402: "Toward a Lived World for AI."

**Total duration**: 7 weeks
**Effort model**: Personal research project (flexible hours, ~10-15 hrs/week)
**Key deliverable**: Functional companion AI prototype + case study for PHIL 402

---

## Week 1: Foundation & Schema Design

### Goals
- Establish project infrastructure
- Finalize annotation schema
- Begin data collection
- Set up development environment

### Tasks

**Infrastructure (Days 1-2)**
- [x] Create project structure (dashboard, schema, data, src)
- [x] Set up version control
- [ ] Initialize Python virtual environment
- [ ] Install dependencies (numpy, pandas, pillow)
- [ ] Configure development tools

**Schema finalization (Days 3-4)**
- [ ] Review annotation_schema.yaml
- [ ] Test schema on 10 sample interactions
- [ ] Refine label definitions based on ambiguities
- [ ] Document annotation guidelines (create ANNOTATION_GUIDE.md)
- [ ] Establish inter-rater reliability baseline (if applicable)

**Data collection (Days 5-7)**
- [ ] Gather handwritten notes corpus (target: 50+ pages)
- [ ] Scan/photograph notes (300 DPI minimum)
- [ ] Organize by topic/date in data/ directory
- [ ] Create data inventory spreadsheet
- [ ] Review privacy considerations; redact sensitive content

### Deliverables
- ✓ Project repository with all scaffolding
- Annotation guidelines document
- Initial data corpus (50+ pages scanned)
- Baseline KPI measurement framework

### KPI targets (Week 1)
- N/A (baseline establishment week)

---

## Week 2: OCR Pipeline & Baseline Interactions

### Goals
- Build OCR preprocessing pipeline
- Extract text from handwritten notes
- Establish baseline interaction patterns
- Begin qualitative logging

### Tasks

**OCR development (Days 1-4)**
- [ ] Research OCR options (Tesseract, Google Vision, etc.)
- [ ] Implement deskew and crop functions (src/preprocess.py)
- [ ] Implement contrast normalization
- [ ] Test OCR accuracy on sample pages
- [ ] Build batch processing pipeline
- [ ] Create OCR output validation workflow

**Text processing (Days 4-5)**
- [ ] Extract text from first 20 pages
- [ ] Manual correction of OCR errors
- [ ] Structure extracted text (markdown format)
- [ ] Tag content by theme/course concept
- [ ] Create searchable knowledge base format

**Baseline interactions (Days 6-7)**
- [ ] Conduct 5 baseline interaction sessions with standard LLM
- [ ] Annotate interactions using schema
- [ ] Record qualitative observations in dashboard/qualitative_log.md
- [ ] Identify key gaps in context awareness
- [ ] Document desired vs. actual behavior patterns

### Deliverables
- Functional OCR pipeline (src/pipeline.py)
- 20+ pages of processed notes
- 5 annotated baseline interactions
- First qualitative log entry

### KPI targets (Week 2)
- Baseline measurements for all 4 KPIs (no targets yet)
- OCR accuracy ≥ 85% (manual validation)

---

## Week 3: First Fine-Tune & Initial Evaluation

### Goals
- Prepare fine-tuning dataset
- Execute first model fine-tune
- Collect and annotate 100 interaction samples
- First KPI measurement cycle

### Tasks

**Fine-tuning preparation (Days 1-3)**
- [ ] Convert OCR output to training format
- [ ] Create "about Harvey" system prompts
- [ ] Augment with PHIL 402 context (syllabus, key readings)
- [ ] Format conversational examples (if available)
- [ ] Split into train/validation sets
- [ ] Select base model and fine-tuning approach

**Model fine-tuning (Days 3-4)**
- [ ] Execute fine-tuning run (cloud or local)
- [ ] Validate model outputs
- [ ] Compare to baseline model
- [ ] Document training parameters and results
- [ ] Deploy fine-tuned model for testing

**Interaction collection (Days 5-7)**
- [ ] Conduct 20 sessions with fine-tuned model
- [ ] Annotate 100 conversational turns
- [ ] Measure KPIs using evaluation rubric
- [ ] Compare to Week 2 baseline
- [ ] Update kpi_dashboard.csv with Week 3 data

### Deliverables
- Fine-tuned model v1
- 100 annotated interaction samples
- First KPI measurement cycle complete
- Training documentation

### KPI targets (Week 3)
- Rapport Quality: ≥ 4.0 (approaching target)
- Flexibility: ≥ 4.0
- Concept Synthesis: ≥ 5.0
- Autonomy: ≥ 6.0

---

## Week 4: Schema Iteration & Empathy Focus

### Goals
- Refine annotation schema based on edge cases
- Deep dive on empathy dimension
- Expand training data with emotional context
- Improve tone calibration

### Tasks

**Schema refinement (Days 1-2)**
- [ ] Review Week 3 annotations for ambiguities
- [ ] Identify edge cases not well-captured by schema
- [ ] Add new labels or refine existing definitions
- [ ] Update annotation_schema.yaml (version 2)
- [ ] Re-annotate challenging samples with new schema
- [ ] Update ANNOTATION_GUIDE.md

**Empathy enhancement (Days 3-5)**
- [ ] Analyze empathy failures from Week 3
- [ ] Create empathy-focused training examples
- [ ] Expand emotional context in knowledge base
- [ ] Test tone variations (empathetic vs. neutral vs. directive)
- [ ] Conduct A/B testing on empathy responses
- [ ] Collect user feedback on "felt understood" metric

**Second iteration (Days 6-7)**
- [ ] Prepare updated training dataset
- [ ] Fine-tune model v2 with empathy focus
- [ ] Test new model on empathy scenarios
- [ ] Measure empathy-related annotations
- [ ] Update qualitative log with empathy insights

### Deliverables
- Annotation schema v2
- Model v2 with empathy enhancements
- Empathy evaluation report
- Updated KPI measurements

### KPI targets (Week 4)
- Rapport Quality: ≥ 5.0 (meets target)
- Flexibility: ≥ 4.5
- Concept Synthesis: ≥ 5.5
- Autonomy: ≥ 7.0

---

## Week 5: Data Expansion & Autonomy Testing

### Goals
- Expand training corpus significantly
- Focus on autonomy dimension
- Test balance between guidance and over-direction
- Optimize context retrieval

### Tasks

**Data expansion (Days 1-3)**
- [ ] Process remaining OCR backlog (target: 50+ total pages)
- [ ] Incorporate new handwritten notes
- [ ] Add PHIL 402 lecture notes and reading summaries
- [ ] Expand conversational history
- [ ] Diversify interaction types (Q&A, brainstorming, reflection)
- [ ] Create test set for context recall evaluation

**Autonomy calibration (Days 3-5)**
- [ ] Analyze over-direction vs. under-support patterns
- [ ] Create autonomy test scenarios
- [ ] Adjust system prompts for balance
- [ ] Test response to open-ended vs. directive requests
- [ ] Measure user perception of autonomy
- [ ] Document autonomy guidelines

**Context optimization (Days 6-7)**
- [ ] Implement context retrieval scoring
- [ ] Test context recall on 20 queries
- [ ] Measure appropriate vs. inappropriate context invocation
- [ ] Optimize retrieval thresholds
- [ ] Improve temporal awareness
- [ ] Update evaluation rubric (src/eval.py)

### Deliverables
- Expanded training corpus (50+ pages processed)
- Autonomy testing report
- Context recall evaluation (≥ 80% target)
- Model v3 (if warranted by findings)

### KPI targets (Week 5)
- Rapport Quality: ≥ 5.5
- Flexibility: ≥ 5.0 (meets target)
- Concept Synthesis: ≥ 6.0 (meets target)
- Autonomy: ≥ 7.5

---

## Week 6: Integration & Synthesis Evaluation

### Goals
- Full system integration
- Comprehensive synthesis capability testing
- Cross-domain concept integration
- Prepare for final evaluation

### Tasks

**System integration (Days 1-2)**
- [ ] Integrate all pipeline components
- [ ] End-to-end testing (OCR → retrieval → generation)
- [ ] Performance optimization
- [ ] Error handling and edge case coverage
- [ ] User interface refinement (if applicable)
- [ ] Documentation of complete workflow

**Synthesis testing (Days 3-5)**
- [ ] Create cross-domain test prompts
- [ ] Evaluate concept integration quality
- [ ] Test phenomenological reasoning
- [ ] Assess PHIL 402 content synthesis
- [ ] Measure coherence vs. fragmentation
- [ ] Conduct qualitative depth analysis

**Final tuning (Days 6-7)**
- [ ] Address remaining KPI gaps
- [ ] Final model iteration (v4)
- [ ] Comprehensive evaluation on all metrics
- [ ] Collect rich qualitative examples
- [ ] Update all dashboard files
- [ ] Prepare case study materials

### Deliverables
- Fully integrated system
- Synthesis evaluation report
- Final model version
- Comprehensive KPI dataset
- Case study preliminary materials

### KPI targets (Week 6)
- Rapport Quality: ≥ 6.0
- Flexibility: ≥ 5.5
- Concept Synthesis: ≥ 7.0
- Autonomy: ≥ 8.0 (meets target)

---

## Week 7: Documentation & PHIL 402 Integration

### Goals
- Consolidate results
- Write PHIL 402 case study
- Ethical reflection
- Future iteration planning

### Tasks

**Results consolidation (Days 1-2)**
- [ ] Finalize all KPI measurements
- [ ] Generate visualizations (charts/graphs)
- [ ] Statistical analysis of trends
- [ ] Compile best/worst interaction examples
- [ ] Write technical results summary
- [ ] Archive all data and models

**Case study writing (Days 3-5)**
- [ ] Outline PHIL 402 case study structure
- [ ] Write introduction (project motivation, phenomenological grounding)
- [ ] Write methods section (annotation schema, fine-tuning approach)
- [ ] Write results section (KPIs, qualitative findings)
- [ ] Write discussion (phenomenological insights, relational AI implications)
- [ ] Write conclusion (limitations, future work)

**Ethical reflection (Day 6)**
- [ ] Document parasocial risk observations
- [ ] Reflect on authenticity and transparency
- [ ] Consider boundaries between AI and human relationships
- [ ] Assess academic integrity implications
- [ ] Write ethics appendix for case study

**Future planning (Day 7)**
- [ ] Identify M-Onty v2 priorities
- [ ] Document lessons learned
- [ ] Create handoff documentation
- [ ] Archive project repository
- [ ] Celebration and reflection

### Deliverables
- Complete PHIL 402 case study (8-12 pages)
- Final KPI dashboard with visualizations
- Ethical reflection document
- M-Onty v2 planning notes
- Archived, documented codebase

### KPI targets (Week 7)
- All targets met or documented rationale for gaps
- Qualitative "aha moments" documented

---

## Success Metrics Summary

### Minimum Viable Success (Week 7)
- ✓ All 4 KPIs meet target thresholds
- ✓ ≥ 500 annotated interaction samples
- ✓ Functional OCR → retrieval → generation pipeline
- ✓ 1 publishable case study for PHIL 402

### Aspirational Success
- ✓ Documented "aha moments" of genuine relational attunement
- ✓ Novel phenomenological insights from the process
- ✓ Replicable methodology for personal AI companionship research
- ✓ Clear foundation for M-Onty v2

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| OCR accuracy too low | Medium | High | Manual correction workflow; consider paid API |
| Fine-tuning compute cost | Medium | Medium | Start with smaller models; use open-source options |
| KPI targets not met | Medium | Medium | Focus on qualitative insights; adjust targets if needed |
| Privacy breach | Low | High | Local-only data; rigorous redaction protocol |
| Time overrun | High | Medium | Prioritize core features; defer nice-to-haves |
| Parasocial dependency | Low | Medium | Weekly self-monitoring; transparency practices |

---

## Weekly Rhythm

**Every Monday**: Review previous week, plan current week, update project plan
**Every Wednesday**: Mid-week check-in, adjust course as needed
**Every Friday**: KPI measurement, qualitative log entry, dashboard update
**Every Sunday**: Reflection, prepare for upcoming week

---

## Tools & Resources

**Development**:
- Python 3.x (numpy, pandas, pillow)
- OCR: Tesseract / Google Vision / Azure
- Fine-tuning: OpenAI API / Hugging Face / Local (Ollama, LM Studio)

**Tracking**:
- Git/GitHub for version control
- dashboard/kpi_dashboard.csv for quantitative
- dashboard/qualitative_log.md for qualitative
- Weekly backup to external drive

**PHIL 402 Integration**:
- Course syllabus and readings
- Lecture notes
- Professor office hours for feedback

---

## Contact & Support

**Primary researcher**: Harvey
**Course**: PHIL 402 — Toward a Lived World for AI
**Project repo**: /home/user/m-onty
**Documentation**: See README.md, CONTEXT_MANIFEST.md, TECHNICAL_SPECS.md

---

*This plan is a living document. Adjust as needed based on learnings and constraints.*
