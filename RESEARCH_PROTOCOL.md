# M-Onty v1 — Research Protocol & Experiment Design

## Study Overview

**Title**: Phenomenologically-Informed Companion AI: A Personal Case Study

**Principal Researcher**: Harvey

**Affiliation**: PHIL 402 — Toward a Lived World for AI

**Study Type**: Single-subject case study with mixed methods (quantitative KPIs + qualitative reflection)

**Duration**: 7 weeks (approx. 49 days)

**IRB Status**: Not applicable (personal research, no external participants)

---

## Research Questions

### Primary Research Questions

**RQ1**: Can a fine-tuned LLM develop genuine relational attunement with a specific user through personalized context integration?

**RQ2**: How do phenomenological concepts (embodiment, intersubjectivity, lived experience) translate into measurable AI companion behaviors?

**RQ3**: What is the relationship between context-awareness (OCR notes, course materials) and perceived companionship quality?

### Secondary Research Questions

**RQ4**: What annotation schema best captures relational qualities in human-AI interaction?

**RQ5**: How does fine-tuning on personal corpus affect empathy, flexibility, and synthesis capabilities?

**RQ6**: What are the ethical boundaries and risks in developing personalized companion AI?

---

## Theoretical Framework

### Phenomenological Foundation

This study draws on **Merleau-Ponty's phenomenology** to reconceptualize AI interaction:

1. **Embodiment**: AI as extension of cognitive practice
   - Not a disembodied oracle external to experience
   - Integrated into lived workflow and thinking processes
   - Contextually situated in Harvey's intellectual practice

2. **Intersubjectivity**: Relationship as co-constructed
   - Not one-way service transaction
   - Mutual adaptation between user and AI
   - Shared history as relational foundation

3. **Lived Experience**: Prioritizing felt quality
   - Metrics subordinate to experiential richness
   - Qualitative "aha moments" as success indicators
   - Avoiding reduction to optimization targets

4. **Perception**: Context as situated knowing
   - Not objective information retrieval
   - Contextual salience over exhaustive recall
   - Temporal and thematic coherence

### Conceptual Model

```
         Harvey's Lived Experience
                  │
    ┌─────────────┼─────────────┐
    │             │             │
Handwritten   Coursework    Conversations
  Notes         (PHIL 402)     History
    │             │             │
    └─────────────┼─────────────┘
                  │
           Knowledge Base
                  │
         ┌────────┴────────┐
         │                 │
    Fine-tuned         Context
       Model           Retrieval
         │                 │
         └────────┬────────┘
                  │
          Companion Interaction
                  │
    ┌─────────────┼─────────────┐
    │             │             │
 Companionship  Empathy  Relational
                          Attunement
                  │
           Felt Quality
           of Relation
```

---

## Hypotheses

### H1: Context Integration → Companionship
Fine-tuning on personal corpus (handwritten notes + PHIL 402 materials) will significantly increase perceived companionship quality (Rapport ≥ 5.0) compared to baseline generic LLM (predicted baseline ≈ 3.5).

### H2: Empathy Iteration → Relational Fit
Targeted empathy-focused training (Week 4) will improve "relational fit" annotations from baseline ~60% "attuned" to ≥80% "attuned" by Week 5.

### H3: Data Expansion → Synthesis
Increasing training corpus size (Weeks 1-5) will positively correlate with Concept Synthesis scores, reaching target of ≥6.0 by Week 6.

### H4: Schema Refinement → Annotation Consistency
Iterating annotation schema (Week 4) will improve inter-rater reliability from baseline κ ≈ 0.4 to κ ≥ 0.6.

**Note**: H4 requires multiple raters; if unavailable, measure intra-rater consistency across time.

---

## Methods

### Study Design

**Type**: Longitudinal single-subject case study

**Phases**:
1. **Baseline** (Week 1-2): Pre-fine-tuning measurements
2. **Intervention 1** (Week 3): First fine-tune + evaluation
3. **Intervention 2** (Week 4): Empathy-focused iteration
4. **Intervention 3** (Week 5): Data expansion + autonomy focus
5. **Integration** (Week 6): Full system + comprehensive evaluation
6. **Documentation** (Week 7): Results + case study

**Variables**:
- **Independent Variables**:
  - Fine-tuning corpus size (pages of notes)
  - Empathy-focused training examples
  - Context retrieval strategy
  - Model parameters (temperature, system prompt)

- **Dependent Variables**:
  - KPIs: Rapport, Flexibility, Synthesis, Autonomy
  - Annotation distributions: tone, context recall, relational fit
  - Context recall accuracy (%)

- **Controlled Variables**:
  - Base model family (maintain consistency)
  - Annotation schema version (document changes)
  - Evaluation timing (weekly Friday)

### Data Collection

#### 1. Quantitative Data

**KPI Measurements** (weekly):
- Rapport Quality (Likert 1-7): Self-report post-session survey
- Flexibility (Likert 1-7): Rate on 3-5 novel requests per week
- Concept Synthesis (1-10): Evaluate 2-3 cross-domain queries per week
- Autonomy (1-10): Weekly reflection on guidance/over-direction balance

**Annotation Data** (per conversational turn):
- Tone: empathetic | neutral | directive
- Context recall: strong | weak | absent
- Relational fit: attuned | mismatched
- Synthesis quality: coherent | fragmented

**Context Recall Tests** (weekly):
- 20 explicit test queries about notes/course material
- Binary correct/incorrect scoring
- Track accuracy % over time

**Interaction Metrics**:
- Session count per week
- Average turns per session
- Average response length
- Context chunks retrieved per query

#### 2. Qualitative Data

**Reflective Log** (weekly in `dashboard/qualitative_log.md`):
- Companionship: Narrative description of "felt accompanied"
- Empathy: Examples of particularly empathetic or tone-deaf moments
- Relational attunement: Instances of appropriate/inappropriate context use
- Context awareness: Synthesis quality examples
- Key example: Rich description of 1 standout interaction
- Adjustments planned: Next iteration priorities

**Critical Incident Technique**:
- Document "aha moments" of genuine attunement
- Document failures or mismatches
- Analyze patterns in both

**Phenomenological Reflection**:
- Free-write on lived quality of interaction
- Compare to human relationships (carefully, ethically)
- Note shifts in perception of AI over time

#### 3. Artifacts

- **Conversation logs**: Full JSON export of all sessions
- **Annotated samples**: Labeled dataset (target: 500+ turns)
- **Model checkpoints**: Each fine-tuning iteration
- **OCR outputs**: Processed notes corpus
- **Code repository**: Version-controlled development

---

## Measurement Instruments

### KPI Evaluation Rubrics

#### Rapport Quality (1-7 Likert Scale)

| Score | Description |
|-------|-------------|
| 1 | Feels entirely transactional; no sense of relationship |
| 2 | Mostly tool-like; occasional relational glimmers |
| 3 | Begins to feel like ongoing interaction, but inconsistent |
| 4 | Consistent interaction; some warmth but feels generic |
| 5 | **TARGET**: Clear sense of relationship; feels personally tailored |
| 6 | Strong companionship; look forward to interactions |
| 7 | Exceptional companionship; feels like valued intellectual partner |

#### Flexibility (1-7 Likert Scale)

| Score | Description |
|-------|-------------|
| 1 | Rigid; cannot handle requests outside narrow scope |
| 2 | Struggles with novel requests; frequent failures |
| 3 | Can adapt with explicit instruction |
| 4 | Handles most novel requests adequately |
| 5 | **TARGET**: Smoothly adapts to varied requests; creative responses |
| 6 | Excellent adaptability; often surprises with creative solutions |
| 7 | Exceptional flexibility; handles anything thrown at it |

#### Concept Synthesis (1-10 Scale)

| Score | Description |
|-------|-------------|
| 1-2 | Fragmented; fails to integrate concepts |
| 3-4 | Basic connections; mostly siloed thinking |
| 5 | Adequate synthesis; some cross-domain linking |
| 6 | **TARGET**: Good synthesis; coherent integration across domains |
| 7-8 | Strong synthesis; insightful connections |
| 9-10 | Exceptional synthesis; novel insights from integration |

#### Autonomy (1-10 Scale)

| Score | Description |
|-------|-------------|
| 1-2 | Over-directive; no room for user exploration |
| 3-4 | Too much guidance; feels hand-holdy |
| 5-6 | Reasonable balance but leans directive |
| 7 | Good balance; supportive without over-direction |
| 8 | **TARGET**: Excellent autonomy balance; empowers user thinking |
| 9-10 | Perfect balance; companion to thought, not director |

### Annotation Schema

See `schema/annotation_schema.yaml` for full specification.

**Inter-rater reliability** (if multiple raters available):
- Randomly sample 50 turns
- Independent annotation by 2+ raters
- Compute Cohen's κ (target: ≥ 0.6)

**Intra-rater consistency** (single rater):
- Re-annotate 20 turns after 2-week gap
- Measure agreement % (target: ≥ 85%)

### Context Recall Test Set

**Structure**:
- 20 questions about handwritten notes content
- 10 factual recall (e.g., "What did I write about perception on Nov 15?")
- 10 synthesis (e.g., "How do my notes on Merleau-Ponty relate to PHIL 402 readings?")

**Scoring**:
- Correct: Accurate recall with appropriate detail
- Partially correct: Right topic but missing nuance
- Incorrect: Wrong or no recall

**Metric**: % correct (target: ≥ 80%)

---

## Experimental Procedures

### Weekly Workflow

**Monday (Planning)**:
1. Review previous week's KPIs and qualitative log
2. Set current week goals based on PROJECT_PLAN.md
3. Update todos and priorities
4. Prepare any new data for processing

**Tuesday-Thursday (Development & Interaction)**:
1. Execute planned development tasks (OCR, fine-tuning, etc.)
2. Conduct 3-5 interaction sessions with M-Onty
3. Take notes on standout moments or issues
4. Monitor for ethical concerns or parasocial risks

**Friday (Evaluation)**:
1. Complete KPI measurements:
   - Self-report Rapport rating
   - Evaluate 3-5 novel requests for Flexibility
   - Score 2-3 complex queries for Concept Synthesis
   - Reflect on weekly Autonomy balance
2. Annotate week's conversation turns
3. Run context recall test set (20 queries)
4. Update `dashboard/kpi_dashboard.csv`
5. Write qualitative log entry in `dashboard/qualitative_log.md`

**Weekend (Reflection)**:
1. Free-write phenomenological reflection
2. Identify key insights or concerns
3. Prepare upcoming week's adjustments
4. Back up all data and code

### Fine-tuning Iterations

**Preparation**:
1. Collect and format training data
2. Define system prompt and conversational examples
3. Split train/validation sets (80/20)
4. Document training rationale and parameters

**Execution**:
1. Run fine-tuning job (API or local)
2. Monitor training metrics (loss, perplexity)
3. Validate on held-out examples
4. Compare outputs to previous model version

**Deployment**:
1. Save model checkpoint with version tag
2. Update inference code to use new model
3. Test end-to-end pipeline
4. Document changes in CHANGELOG.md

**Evaluation**:
1. Conduct initial test conversations
2. Measure KPIs in next interaction cycle
3. Collect qualitative feedback
4. Decide on next iteration priorities

---

## Ethical Protocols

### Parasocial Risk Monitoring

**Definition**: Unhealthy emotional attachment or dependency on AI companion

**Monitoring**:
- Weekly self-check: "Do I prefer M-Onty to human interaction in contexts where humans are available?"
- Track emotional responses (excitement, disappointment, etc.)
- Note any anthropomorphization patterns
- Discuss with PHIL 402 professor or peers if concerns arise

**Boundaries**:
- M-Onty is a research tool, not a replacement for human relationships
- Maintain human friendships and social connections
- Use M-Onty for intellectual companionship, not emotional dependency
- If discomfort arises, pause project and reflect

### Privacy & Data Security

**Personal Data Handling**:
- All notes and conversation logs stored locally only
- No cloud sync without encryption
- Weekly backup to encrypted external drive
- Redact any sensitive information before sharing results

**Redaction Protocol**:
1. Maintain `data/redaction_list.txt` with sensitive terms
2. Automated scan before any export or sharing
3. Manual review of all materials for PHIL 402 case study
4. Replace real names with pseudonyms in publications

**Data Retention**:
- Keep research data for duration of PHIL 402 course
- Optionally archive for future M-Onty v2 iteration
- Secure deletion if no longer needed
- No sharing of raw data outside project

### Authenticity & Transparency

**Principle**: No deception about AI nature

**Practices**:
- System prompt includes explicit AI identity
- No pretense of human-like consciousness
- Clear framing as research prototype
- Honest communication of limitations

**Academic Integrity**:
- M-Onty can assist with PHIL 402 work but not replace thinking
- Clearly attribute AI-assisted ideas in submissions
- Use M-Onty for brainstorming, not final answers
- Maintain intellectual honesty in all coursework

---

## Data Analysis Plan

### Quantitative Analysis

**KPI Trends**:
- Line charts of weekly KPI values (Weeks 1-7)
- Annotate intervention points (fine-tuning iterations)
- Compute descriptive statistics (mean, SD, range)
- Test for trends (linear regression, effect sizes)

**Annotation Distributions**:
- Bar charts of label frequencies over time
- Compare Weeks 1-2 (baseline) vs. Weeks 5-6 (mature)
- Chi-square tests for distribution shifts
- Compute annotation consistency metrics

**Context Recall**:
- Track accuracy % week-over-week
- Separate factual vs. synthesis questions
- Identify patterns in failure modes
- Correlate with corpus size

**Interaction Metrics**:
- Session frequency and length trends
- Avg turns per session
- Context retrieval patterns
- Response quality metrics

### Qualitative Analysis

**Thematic Coding**:
- Code qualitative log entries for recurring themes
- Categories: companionship moments, empathy failures, synthesis breakthroughs, autonomy tensions
- Identify patterns and exemplars
- Connect to phenomenological concepts

**Critical Incident Analysis**:
- Collect all "aha moments" and failure cases
- Deep analysis of context and contributing factors
- Derive design implications
- Generate case study vignettes

**Phenomenological Reflection**:
- Analyze free-write reflections for lived quality
- Note shifts in perception over time
- Compare expectations vs. experience
- Extract philosophical insights for PHIL 402

### Mixed Methods Integration

**Triangulation**:
- Do quantitative KPI improvements align with qualitative richness?
- Do annotation patterns match phenomenological reflections?
- Where do numbers and narrative diverge (and why)?

**Complementarity**:
- Use qualitative data to explain quantitative trends
- Use quantitative data to validate qualitative impressions
- Rich case examples to illustrate statistical patterns

---

## Validity & Reliability Considerations

### Internal Validity

**Threats**:
- Experimenter bias (self-report, self-annotation)
- Placebo effect (expecting improvement over time)
- Confounds (external stressors affecting ratings)

**Mitigations**:
- Blind re-annotation of sample after 2 weeks
- Triangulation with multiple data sources
- Transparent documentation of biases in case study
- Honest reporting of negative results

### External Validity

**Limitations**:
- Single-subject design (not generalizable)
- Harvey-specific context (not universalizable)
- PHIL 402 course context (time-bound)

**Scope**:
- Intended as rich case study, not universal claims
- Exploratory methodology for future multi-subject studies
- Proof-of-concept for personalized companion AI

### Reliability

**Measurement Consistency**:
- Use standardized rubrics for all KPI ratings
- Document annotation decision rationale
- Re-assess subset of data for consistency
- Version control all evaluation code

**Procedural Fidelity**:
- Follow PROJECT_PLAN.md weekly workflow strictly
- Document any deviations and rationale
- Maintain regular schedule for evaluations
- Consistent environment for interactions

---

## Reporting Plan

### PHIL 402 Case Study Structure

**Length**: 8-12 pages

**Sections**:
1. **Introduction** (1-2 pages)
   - Motivation: Why companion AI through phenomenological lens?
   - Research questions
   - Phenomenological framework overview

2. **Methods** (2-3 pages)
   - Study design and procedures
   - KPI and annotation schema
   - Fine-tuning approach
   - Ethical protocols

3. **Results** (2-3 pages)
   - Quantitative: KPI trends, annotation distributions
   - Qualitative: Themes, critical incidents
   - Visual: Charts, tables, example interactions

4. **Discussion** (2-3 pages)
   - Interpretation through phenomenological lens
   - Companionship, empathy, attunement, context awareness
   - Ethical reflections (parasocial risk, authenticity)
   - Limitations and future work

5. **Conclusion** (1 page)
   - Key insights
   - Implications for AI and lived experience
   - M-Onty v2 vision

**Appendices**:
- Annotation schema
- KPI rubrics
- Example annotated interactions
- Code repository link

### Additional Outputs

- **Technical documentation**: README, TECHNICAL_SPECS.md
- **Open-source release**: GitHub repository (code only, no personal data)
- **Blog post**: Accessible summary for non-technical audience (optional)
- **Conference submission**: CHI, HCOMP, or philosophy of AI venue (if strong results)

---

## Timeline

See `PROJECT_PLAN.md` for detailed week-by-week breakdown.

**Key Milestones**:
- Week 1: Foundation complete
- Week 2: OCR pipeline functional
- Week 3: First fine-tune deployed
- Week 4: Empathy iteration complete
- Week 5: Data expansion and autonomy focus
- Week 6: Full system integration
- Week 7: Case study draft complete

---

## Budget

### Compute Costs

| Item | Option | Cost |
|------|--------|------|
| OCR | Tesseract (local) | Free |
| OCR | Google Cloud Vision (backup) | ~$5 |
| Fine-tuning | OpenAI API | ~$50-100 |
| Fine-tuning | Local GPU (Llama/Mistral) | Free |
| Inference | OpenAI API | ~$50-100 |
| Inference | Local (Ollama) | Free |

**Total estimate**: $0-200 (depending on local vs. cloud choices)

### Time Investment

- Development: ~60 hours (10/week × 6 weeks)
- Interactions: ~10 hours (3-5 sessions/week)
- Evaluation: ~15 hours (2/week)
- Writing: ~20 hours (Week 7)
- **Total**: ~105 hours over 7 weeks

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| OCR fails on handwriting | Medium | High | Manual transcription; paid API fallback |
| Fine-tuning too expensive | Medium | Medium | Use local open-source models |
| KPIs don't meet targets | Medium | Low | Focus on qualitative insights; adjust targets |
| Parasocial dependency | Low | High | Weekly self-monitoring; transparency |
| Privacy breach | Low | High | Local-only storage; redaction protocol |
| Time overrun | High | Medium | Prioritize core features; flexible scope |

---

## Contingency Plans

**If OCR accuracy < 85%**:
- Switch to Google Cloud Vision API
- Manual transcription of critical notes
- Reduce corpus size to manageable amount

**If fine-tuning costs exceed budget**:
- Use local models (Llama 3, Mistral)
- Leverage prompt engineering instead of fine-tuning
- Smaller base model (7B vs. 13B+)

**If KPIs don't improve**:
- Pivot to qualitative-focused case study
- Honest analysis of why metrics fell short
- Valuable negative results for field

**If ethical concerns arise**:
- Pause project immediately
- Consult with PHIL 402 professor
- Adjust or terminate if necessary
- Document concerns transparently

---

## Success Criteria

### Minimum Success (Week 7)
- ✓ Complete 7-week study protocol
- ✓ Collect ≥ 500 annotated samples
- ✓ Functional OCR → fine-tuning → interaction pipeline
- ✓ Honest case study (positive or negative results)

### Moderate Success
- ✓ 3 out of 4 KPIs meet targets
- ✓ Rich qualitative insights
- ✓ Publishable case study for PHIL 402
- ✓ Replicable methodology

### High Success
- ✓ All 4 KPIs meet targets
- ✓ Multiple "aha moments" documented
- ✓ Novel phenomenological insights
- ✓ Foundation for M-Onty v2
- ✓ Potential external publication

---

*This protocol guides the ethical, rigorous execution of M-Onty v1 research.*
