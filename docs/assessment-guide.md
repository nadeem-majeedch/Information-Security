---
title: "Assessment Guide"
layout: default
---

# Information Security — Assessment Guide

**Course:** Information Security: A Self-Study Course from Beginner to Advanced
**Instructor:** Engr. Dr. Muhammad Nadeem Majeed — Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore, Pakistan
**Status:** DRAFT for instructor review · **Version:** 0.1 · **Last verified:** 2026-10-09
**Companion documents:** [Course Roadmap](./course-roadmap.md) · [Learning Outcomes](./learning-outcomes.md) · [Prerequisites](./prerequisites.md) · [Lab Safety Policy](./lab-safety-policy.md)

---

## 1. Assessment philosophy

This is a **self-study course**: assessment exists to make progress visible and verifiable, not to rank learners. The design follows three principles:

1. **Balanced evidence.** No single instrument decides competence — quizzes check recall and understanding, scenario exercises check judgment, lab portfolios check execution, investigations check analysis, and the capstone checks integration.
2. **Practice is separated from graded work.** Learners must be free to fail privately while practicing; only designated, clearly marked items carry weight.
3. **Safety is a gate, not a score.** Any work that violates the [Lab Safety Policy](./lab-safety-policy.md) is not graded — it is returned for correction (see §7).

All components are completable with **$0** of tools and no live proctoring.

## 2. Component overview

| # | Component | Type | Weight | Count | Pass mark |
|---|---|---|---|---|---|
| A | Module knowledge checks (quizzes) | Formative → gate | 0% (completion gate) | 18 (M01–M18) | ≥ 80% each (unlimited retakes) |
| B | Scenario-based exercises | **Graded** | 20% | 6 (one per level checkpoint + 2 mid-level) | ≥ 60% each |
| C | Lab portfolio (module deliverables) | **Graded** | 40% | 19 module evidence packs | Rubric ≥ "Developing" each; 17/19 required |
| D | Defensive investigations (monitoring, IR, forensics, malware) | **Graded** | 20% | 4 (M13, M14, M15, + one integrative) | ≥ 60% each |
| E | Capstone project | **Graded** | 20% | 1 (M19, staged A–E) | ≥ 60% overall **and** §5.4 stage standard met, no stage below "Developing" |
| — | Professional practice & safety compliance | **Gate** (pass/fail) | — | continuous | Full compliance (§7) |
| | **Total graded** | | **100%** | | |

**Distinction — practice vs. graded:**
- **Practice (ungraded):** quiz retakes after first attempt, "Try it" side-boxes, example walkthroughs, discussion prompts, flashcards, self-check checklists, and any item explicitly labeled *Practice*. Practice work never lowers a grade and is never submitted.
- **Graded:** items explicitly labeled *Assessed* — the six scenario exercises (B), portfolio packs (C), investigations (D), and the capstone (E). First-attempt quiz scores (component A) are recorded as the completion gate but carry no weight in the final percentage.

## 3. Component details

### A — Module knowledge checks (formative, completion gate)
- **Format:** 10–14 questions per module (mix of MCQ and short answer; scenario questions in higher modules), with an answer key released after first attempt.
- **Rule:** ≥ 80% to unlock the next module; unlimited retakes with re-study prompts between attempts. First-attempt result is logged for the learner's own tracking.
- **Instruments:** one quiz per module (M01–M18) in the [Assessment Hub](./assessments/README.md), each with worked answers, outcome mapping, and module-end review exercises.
- **Purpose:** recall, comprehension, and safe-judgment checks (including scope/ethics questions from M03 onward).
- **CLOs covered:** all (see module → CLO map in [learning-outcomes.md](./learning-outcomes.md)).

### B — Scenario-based exercises (graded, 20%)
Six written scenarios, each 45–90 minutes: a short realistic situation + 4–6 structured questions (decide, justify, prioritize). Delivered at level checkpoints:

| ID | Placed after | Focus | CLOs |
|---|---|---|---|
| S1 | M03 (Level 1 checkpoint) | Risk + governance + ethics in a small-org situation | CLO-1, CLO-2 |
| S2 | M06 | Crypto and identity choices for a product launch | CLO-4, CLO-5 |
| S3 | M09 | Web-app risk judgment (findings triage, what to fix first) | CLO-6 |
| S4 | M11 (Level 2 checkpoint) | Threat model critique — spot design flaws | CLO-8 |
| S5 | M13 | Detection/triage decisions from alert data | CLO-9 |
| S6 | M18 (Level 3/4 checkpoint) | Automation risk + emerging-threat analysis | CLO-7, CLO-12 |

- **Format:** self-graded against a model answer + 4-point rubric (accuracy, justification, safety/ethics, clarity). Peer or instructor review optional if available.
- **Pass:** ≥ 60% per scenario; one reassessment allowed.

### C — Lab portfolio (graded, 40%)
- The evidence packs defined per module in the [Course Roadmap](./course-roadmap.md) ("Evidence / deliverables"), collected in a `portfolio/` folder with an index.
- **Graded per pack** with the Lab Portfolio Rubric (§5). 17 of 19 packs required (M01 and M17 may be substituted by any two others with prior notice — but the capstone stages cannot be substituted).
- **Integrity:** every pack includes a "safety statement" line (targets used, isolation method) per the safety policy.
- Portfolio is the course's primary skill evidence: scans, captures, configurations, reports, rules, and patches.

### D — Defensive investigations (graded, 20%)
Four investigation reports produced in Level 3 (with the integrative one in M18/capstone prep):

1. **Detection engineering report** (M13): rules, ATT&CK mapping, test evidence, false-positive analysis.
2. **Incident response + forensic timeline report** (M14): chain of custody, artifacts, timeline answers.
3. **Malware triage report** (M15): static/dynamic analysis, YARA, IOC handoff.
4. **Integrative investigation** (capstone Stage D or, if taking capstone separately, an M18-based mini-incident): detect → triage → respond across the whole toolchain.

- **Pass:** ≥ 60% each against the Investigation Rubric (§5). These reports are graded more strictly than portfolio packs because they represent professional deliverables.

### E — Capstone project (graded, 20%)
- Five stages (A–E) as defined in M19 of the roadmap; each stage separately assessed with the Capstone Rubric (§5); **no stage below "Developing."**
- Recommended pacing: ≥ 4 weeks, one stage per week minimum.
- **Project package:** the capstone is delivered via the [M19 Capstone Project brief](./capstone/README.md) — two alternative scenarios, a seven-stage workflow (rolling up to stages A–E), templates, and a seven-dimension rubric crosswalked to §5.4.

## 4. Weighting rationale

| Component | Weight | Why |
|---|---|---|
| Lab portfolio | 40% | Security is a practice discipline — demonstrated execution is the strongest evidence |
| Scenario exercises | 20% | Judgment and prioritization can't be shown by labs alone |
| Defensive investigations | 20% | Detection/response/forensics are the most profession-like outputs and need stricter calibration |
| Capstone | 20% | Integration across all CLOs; large but weighted so failure on one weak day doesn't erase a course |
| Knowledge checks | 0% (gate) | Recall is necessary but not sufficient — gating without weight encourages honest retake-and-learn behavior |

## 5. Rubrics

### 5.1 Lab portfolio rubric (applies to each pack in component C)

| Criterion | Exemplary (4) | Proficient (3) | Developing (2) | Inadequate (1) |
|---|---|---|---|---|
| Technical correctness | All steps work; outputs verified | Works with minor issues | Partially works | Non-functional or fabricated |
| Evidence quality | Complete, annotated, reproducible | Mostly complete screenshots/logs | Sparse evidence | No evidence |
| Safety compliance | Isolation + authorization statement correct and specific | Statement present, adequate detail | Vague statement | Missing or unsafe |
| Reflection/justification | Explains *why*, not just *what* | Some rationale | Mostly descriptive | None |
| **Pack standard** | | **≥ 3 = pass for that pack** | | |

### 5.2 Scenario exercise rubric (component B, per scenario, 20 points)

| Criterion | Max |
|---|---|
| Technical accuracy | 8 |
| Justification quality (reasoned, references where relevant) | 6 |
| Safety/ethics reasoning (scope, authorization, privacy considered) | 4 |
| Clarity and structure | 2 |
| **Pass = ≥ 12/20** | |

### 5.3 Investigation rubric (component D, per report, 100 points)

| Criterion | Max |
|---|---|
| Method correctness (correct tool use, reproducible steps) | 30 |
| Analysis quality (findings accurate, false positives handled, timeline/artifacts cited) | 30 |
| Defensive translation (detections/playbook updates/IOC quality) | 20 |
| Professional structure (executive summary, evidence hygiene, remediation) | 10 |
| Safety & evidence handling (chain of custody, isolation, data rules) | 10 |
| **Pass = ≥ 60/100** | |

### 5.4 Capstone rubric (component E, per stage and overall)

| Criterion | Exemplary (4) | Proficient (3) | Developing (2) | Inadequate (1) |
|---|---|---|---|---|
| Integration across CLOs | Draws on ≥ 4 prior modules seamlessly | Uses 3 prior modules | Uses 1–2 | Isolated actions |
| Technical depth & correctness | Flawless execution with verification | Minor gaps | Notable gaps | Broken |
| Risk & threat reasoning | Explicit, framework-linked (CSF/CIS/ATT&CK/STRIDE) | Framework named, partial linkage | Informal reasoning | Absent |
| Professional documentation | Client-ready, reproducible by a third party | Good, minor gaps | Readable but incomplete | Unusable |
| Safety & ethics | Full compliance, statements correct | Compliant | Minor omission | Violation (automatic stage return) |
| **Stage standard** | | **≥ 3 on at least 4 of 5 criteria = stage passes** | | |

### 5.5 Overall grade bands

| Band | Percentage | Meaning |
|---|---|---|
| Distinction | 85–100% | Exemplary portfolio + investigations + capstone |
| Merit | 70–84% | Consistently proficient |
| Pass | 60–69% | Meets all completion criteria |
| Below pass | < 60% | Resubmit failed components (§6) |

**Course completion** (in addition to ≥ 60% overall): all 18 knowledge-check gates passed, ≥ 17/19 portfolio packs, all four investigations ≥ 60%, capstone ≥ 60% overall with every stage meeting the §5.4 stage standard (≥ Proficient on 4 of 5 criteria) and no stage below Developing, and full safety-policy compliance. See "Progression rules" in the [Course Roadmap](./course-roadmap.md).

## 6. Resubmission and reassessment policy

- **Knowledge checks:** unlimited retakes; system suggests review sections after each attempt.
- **Scenarios / investigations / portfolio packs:** one reassessment per item after completing a targeted "fix list" (the marker's specific gaps). Second reassessment requires addressing the fix list in full.
- **Capstone stages:** may be returned for revision any number of times while "Developing/Inadequate"; the goal is competence, not attrition.
- **Level gates:** a learner who fails a gate repeats the level's scenario exercises after review; no content is skipped.

## 7. Safety gate (pass/fail, overrides scores)

Any submitted work that violates the [Lab Safety Policy](./lab-safety-policy.md) is **not scored**; it is returned with required corrections. Examples: missing safety statement, targets outside the authorized list, evidence showing scanning of non-lab systems, real personal data in submissions, live malware outside the sandbox VM.

- First occurrence: return for correction + mandatory re-read of the policy section.
- Second occurrence: portfolio component (C) paused until a written re-acknowledgment is filed; repeated or willful violations end participation (self-study integrity depends on self-discipline).

## 8. Evidence, integrity, and academic honesty

- **Honesty expectations:** submitted work is your own; where generative AI or other assistants are used for learning support, declare it in a "Sources & assistance" line in the pack (declaration is not penalized; undisclosed fabrication is).
- **Evidence hygiene:** screenshots/logs must match claimed commands; fabrication invalidates the pack regardless of grade.
- **Data rules:** only synthetic or course-provided data may appear in submissions (per safety policy §Data handling).
- **Portfolio retention:** keep your `portfolio/` folder even after completion — it is your interview artifact.

## 9. For instructors adopting this course

Each graded component cites CLOs (see component tables above and the CLO map in [learning-outcomes.md](./learning-outcomes.md)); model answers and marker notes for quizzes/exercises follow the module pages. Weighting can be adjusted (e.g., investigations 15% / portfolio 45%) provided all CLOs retain ≥ 2 graded evidence points.

## 10. References

- NIST CSF 2.0 (Feb 2024) and CIS Controls v8.1 (Jun 2024) — framework linkage in rubrics.
- OWASP Top 10:2025, ASVS 5.0, WSTG v4.2 — assessment-method references for M09/M12 work.
- MITRE ATT&CK v19.x (2026) — detection/investigation mapping.
- NIST SP 800-61r3 (Apr 2025) — investigation report structure for component D.
