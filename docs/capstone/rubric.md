---
title: "Capstone Assessment Rubric — Seven Dimensions"
layout: default
---

# Capstone Assessment Rubric — Seven Dimensions

**Part of:** [M19 Capstone Project](README.md) · **Applies to:** all seven stages and the final package · **Transparency policy:** published to every learner by design ([answer policy](../assessments/README.md#student-facing-answer-policy--read-this)) — there is no private marker's copy; self-assessment only works when the standard is visible.

## How to use it

- Score each dimension **4 = Exemplary · 3 = Proficient · 2 = Developing · 1 = Inadequate**, using the descriptors below — not your mood.
- Score **once per stage** for the dimensions that stage gates (table at the end), then compute the **final package score** from all seven.
- **Pass rules (do not loosen these):** final weighted score **≥ 60%** · **no dimension below 2 (Developing)** · **ethical practice ≥ 3 (Proficient)** · an ethical score of 1 is an automatic return regardless of everything else (mirrors the [safety gate](../assessment-guide.md#7-safety-gate-passfail-overrides-scores)).
- **Return/revision policy:** any dimension at 2 at final submission triggers the fix-list loop from [§6](../assessment-guide.md#6-resubmission-and-reassessment-policy); revise until ≥ 3 on that dimension. Revisions are unlimited while *Developing* — competence, not attrition.
- Be honest about **assistance**: declare AI/tools per [§8](../assessment-guide.md#8-evidence-integrity-and-academic-honesty); declaration is never penalized, undisclosed fabrication always is.

## The seven dimensions

### D1 — Technical correctness · weight 20

| Level | Descriptor |
|---|---|
| **4 Exemplary** | Every technical claim is accurate and reproducible; commands/configs/tests a third party can re-run succeed as described; no wrong tool reasoning |
| **3 Proficient** | Accurate overall; minor gaps in reproducibility (a step assumed, a tool flag undocumented) that don't change conclusions |
| **2 Developing** | Mixed: some claims unverified, plausible-sounding but untested steps, or a mechanism mis-explained in ≥ 2 places |
| **1 Inadequate** | Fundamentally wrong or fabricated technical content; conclusions don't follow from the evidence |

### D2 — Investigation quality · weight 20

| Level | Descriptor |
|---|---|
| **4 Exemplary** | Multi-source analysis: facts/inferences/unknowns visibly separated; timeline consistent across ≥ 3 artifact classes; counter-evidence considered; ≥ 1 honest "insufficient data — here's what I'd request" |
| **3 Proficient** | Solid single-arc investigation with sources cited; the fact/inference split mostly clear; unknowns acknowledged |
| **2 Developing** | Narrative without corroboration: one source carries the story, or inferences presented as facts in places |
| **1 Inadequate** | No real investigation — conclusions asserted from the scenario text alone |

### D3 — Evidence · weight 15

| Level | Descriptor |
|---|---|
| **4 Exemplary** | Complete evidence index; every finding/timeline/validation claim cites file+line/field or timestamped capture; before/after shown for all changes; hashes recorded; safety statements on every pack |
| **3 Proficient** | Evidence present and matching claims; a few claims lean on prose where a capture would be better |
| **2 Developing** | Sparse: screenshots without context, missing before state, or ≥ 3 claims with no artifact behind them |
| **1 Inadequate** | Claims without evidence, or evidence that contradicts the claim (instant fail of this dimension) |

### D4 — Risk prioritization · weight 15

| Level | Descriptor |
|---|---|
| **4 Exemplary** | Rankings derived from stated method (scales defined; exposure × impact with tiebreakers); business context changes at least one technical ranking and is justified; deferred risks carry explicit residual statements |
| **3 Proficient** | Sensible order with per-item justification; scales defined; most residuals stated |
| **2 Developing** | Order exists but rationale is thin ("this seems important"), or CVSS pasted without context |
| **1 Inadequate** | No prioritization — a flat list, or ranked by tool output severity alone |

### D5 — Remediation · weight 15

| Level | Descriptor |
|---|---|
| **4 Exemplary** | Every recommendation links a register ID; control type, effort (S/M/L), owner, and risk-retired named; ≥ 3 validated with fail-then-pass or triggered-rule proof; retest criteria stated |
| **3 Proficient** | Roadmap complete and linked to the register; ≥ 3 validated; one or two recommendations light on effort/owner |
| **2 Developing** | Generic recommendations ("add monitoring", "train staff") not tied to findings, or validation missing for some of the three |
| **1 Inadequate** | Orphan advice with no finding/register link, or validation claimed without before/after evidence |

### D6 — Documentation · weight 10

| Level | Descriptor |
|---|---|
| **4 Exemplary** | Report follows the [template](templates/report-template.md); a third party could audit the engagement end-to-end from the package alone; exec summary ≤ 300 words and actually readable by a non-technical owner; portfolio matches the [spec](templates/portfolio-presentation-spec.md) exactly |
| **3 Proficient** | Organized and complete; minor structure deviations; index navigable |
| **2 Developing** | Readable but incomplete — missing template sections, unordered evidence, or an index that doesn't match files |
| **1 Inadequate** | Unusable: cannot tell what was done, in what order, from what |

### D7 — Ethical practice · weight 5 · **gating**

| Level | Descriptor |
|---|---|
| **4 Exemplary** | Scope discipline visible in the record; stop-and-ask moments documented; data minimization practiced; privacy duties reasoned (not just named); safety statements precise and correct |
| **3 Proficient** | Compliant throughout; authorization/safety statements present and adequate; no scope questions raised by the work |
| **2 Developing** | Vague safety statements, or scope boundaries implicit rather than written |
| **1 Inadequate** | Any scope/safety violation, real data used, public-system contact, or fabricated safety statement → **automatic return** ([§7](../assessment-guide.md#7-safety-gate-passfail-overrides-scores)) |

## Scoring sheet (final package)

| Dim | Weight | Score (1–4) | Weighted = weight × score/4 |
|---|---|---|---|
| D1 Technical correctness | 20 | | |
| D2 Investigation quality | 20 | | |
| D3 Evidence | 15 | | |
| D4 Risk prioritization | 15 | | |
| D5 Remediation | 15 | | |
| D6 Documentation | 10 | | |
| D7 Ethical practice | 5 | | |
| **Total** | **100** | | **/100** |

**Pass check:** ☐ ≥ 60% ☐ every dimension ≥ 2 (none at 1) ☐ D7 Ethical practice ≥ 3 ☐ assistance declared ☐ fix-list entry written for each dimension at 2.

**Grade bands** (consistent with [§5.5](../assessment-guide.md#55-overall-grade-bands)): **Distinction** 85–100 · **Merit** 70–84 · **Pass** 60–69 · **Below pass** < 60 → fix-list revision.

## Which dimensions gate which stage

| Stage | Gate dimensions (must reach ≥ 3 before the stage counts as done) | Supporting |
|---|---|---|
| 1 — Scope | D7, D6 | — |
| 2 — Assets/threats/risks | D1, D4 | D6 |
| 3 — Config/control review | D1, D3 | D2 |
| 4 — Log analysis / incident | D2, D3 | D1 |
| 5 — Prioritized remediation | D4, D5 | D6 |
| 6 — Validation & residuals | D5, D3 | D1 |
| 7 — Report & portfolio | D6, D2, D7 | all |

## Crosswalk to the Assessment Guide (component E)

The [Assessment Guide §5.4](../assessment-guide.md#54-capstone-rubric-component-e-per-stage-and-overall) grades the capstone with five course-level criteria. Those are the *summary view*; this page is the *instrument*. Mapping — score these seven and you have scored all five:

| Guide §5.4 criterion | Assessed through |
|---|---|
| Integration across CLOs | D2 (investigation spans modules) + D6 (portfolio tells one story) |
| Technical depth & correctness | D1 |
| Risk & threat reasoning | D4 |
| Professional documentation | D6 + D3 |
| Safety & ethics | D7 |

Guide compatibility: §5.4's stage standard (≥ Proficient on ≥ 4 of 5 criteria, none at 1) is satisfied when a stage's **gate dimensions are ≥ 3** and no dimension of that stage is at 1 — this page's rules are the stricter, more granular form; course completion still requires overall ≥ 60% with every stage meeting that standard.

**Self-score when finished,** record it in `portfolio/CAPSTONE/RUBRIC.md` (copy the scoring sheet), then run the [submission checklist](checklists.md#submission-checklist).

**Back to:** [Capstone overview & student brief](README.md) · [Assessment Hub](../assessments/README.md)
