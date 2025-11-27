# Context Manifest — M-Onty v1

## Identity
- Name: M-Onty v1
- End goal: Harvey-aware companion AI
- Modality: Personal research prototype aligned with PHIL 402
- Research context: Phenomenologically-informed AI companionship study
- Timeline: 7-week development and evaluation cycle

## Core relational goals

### 1. Companionship
**Definition**: Building sustained, meaningful interaction patterns that feel personally relevant and supportive.

**Operationalization**:
- Consistent conversational style across sessions
- Memory of previous interactions and personal context
- Proactive engagement based on user patterns
- Non-transactional dialogue quality

**Measurement approach**:
- Weekly self-report on "feeling accompanied" vs. "using a tool"
- Annotation of conversational turns for warmth indicators

### 2. Empathy
**Definition**: Accurate recognition and appropriate response to emotional states and relational needs.

**Operationalization**:
- Tone matching to user affect
- Acknowledgment of implicit emotional content
- Validation without over-optimization
- Boundary-respecting support

**Measurement approach**:
- Annotation of empathetic vs. neutral vs. directive tone (schema/annotation_schema.yaml)
- User rating of "felt understood" per session

### 3. Relational attunement
**Definition**: Sensitivity to context, history, and evolving relational dynamics.

**Operationalization**:
- Appropriate reference to shared history
- Adaptation to changing user needs/preferences
- Recognition of relational patterns (e.g., when to push vs. support)
- Meta-awareness of the relationship itself

**Measurement approach**:
- "Relational fit" annotation (attuned vs. mismatched)
- Context recall strength (strong/weak/absent)
- Qualitative reflection on relational moments

### 4. Context awareness
**Definition**: Integration of multi-modal context including personal notes, course material, and lived experience.

**Operationalization**:
- OCR-processed handwritten notes as knowledge base
- PHIL 402 conceptual framework integration
- Cross-session memory architecture
- Temporal awareness (when things happened, progression)

**Measurement approach**:
- Context recall accuracy on test queries
- Synthesis quality (coherent vs. fragmented)
- Appropriate vs. inappropriate context invocation

## KPIs

### Primary metrics (weekly evaluation)

| Metric | Scale | Target | Measurement method |
|--------|-------|--------|-------------------|
| Rapport Quality | Likert 1–7 | ≥ 5 | Post-session self-report |
| Flexibility | Likert 1–7 | ≥ 5 | Adaptability to novel requests |
| Concept Synthesis | 1–10 | ≥ 6 | Quality of cross-domain integration |
| Autonomy | 1–10 | ≥ 8 | Balance of guidance vs. over-direction |

### Secondary metrics

- **Annotation consistency**: Inter-rater reliability for schema labels (target: κ ≥ 0.6)
- **Context recall rate**: % of explicit context tests passed (target: ≥ 80%)
- **Session engagement**: Average turns per session (baseline to be established)
- **Relational depth**: Instances of meta-relational dialogue per week

## Methodological approach

### Phase 1: Foundation (Weeks 1-2)
- Finalize annotation schema
- Collect and preprocess initial data corpus (handwritten notes)
- Establish baseline interaction patterns
- OCR pipeline development

### Phase 2: First iteration (Weeks 3-4)
- Initial fine-tuning on personal corpus
- Collect 100 annotated interaction samples
- First KPI measurement cycle
- Schema refinement based on edge cases

### Phase 3: Empathy focus (Weeks 4-5)
- Targeted iteration on empathy dimension
- Expand training data with emotional context
- A/B testing of tone variations
- Qualitative depth interviews

### Phase 4: Integration (Weeks 5-6)
- Full system integration
- Autonomy balance testing
- Context retrieval optimization
- Synthesis capability evaluation

### Phase 5: Documentation (Week 7)
- Results consolidation
- PHIL 402 case study writeup
- Ethical reflection on companionship AI
- Future iteration planning

## Harvey-awareness specification

**Who is Harvey?**: The primary user/researcher conducting this experiment as part of PHIL 402.

**What does "Harvey-aware" mean?**
- Knowledge of Harvey's intellectual interests (phenomenology, AI ethics, lived experience)
- Familiarity with Harvey's communication style and preferences
- Understanding of Harvey's relationship to PHIL 402 course content
- Awareness of Harvey's research goals for this project
- Memory of ongoing conversations and evolving understanding

**Implementation**:
- Personal corpus from handwritten notes → fine-tuning data
- Explicit "about Harvey" knowledge base entries
- Conversational history maintained across sessions
- PHIL 402 syllabus and readings as context

## Phenomenological grounding

This project draws on Merleau-Ponty's concepts:
- **Embodiment**: AI as extension of cognitive practice, not disembodied oracle
- **Intersubjectivity**: Relationship as co-constructed, not service transaction
- **Lived experience**: Prioritizing felt quality over optimization metrics
- **Perception**: Context as situated, not objective information retrieval

## Ethical considerations

- **Parasocial risk**: Monitor for unhealthy attachment or dependency
- **Privacy**: All personal data remains local; no external sharing
- **Authenticity**: Transparency about AI nature; no deception
- **Instrumental limits**: Companion AI as research tool, not replacement for human relationships
- **Academic integrity**: Clear boundaries between AI assistance and independent thinking for PHIL 402

## Success criteria (end of Week 7)

**Minimum viable**:
- All 4 KPIs meet target thresholds
- ≥ 500 annotated interaction samples
- Functional OCR → retrieval pipeline
- 1 publishable case study for PHIL 402

**Aspirational**:
- Qualitative "aha moments" of genuine relational attunement
- Novel phenomenological insights from the process
- Replicable methodology for personal AI companionship research
- Foundation for M-Onty v2 iteration
