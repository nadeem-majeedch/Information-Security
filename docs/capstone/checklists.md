---
title: "Capstone Completion and Submission Checklists"
layout: default
---

# Capstone Completion and Submission Checklists

**Part of:** [M19 Capstone Project](README.md) · Print or copy these into `portfolio/CAPSTONE/`. A gate that isn't ticked isn't done — the next stage inherits its quality.

## Completion checklist (per-stage gates)

### G1 — after Stage 1: understand & scope
- [ ] Scoping memo ≥ 1 page: engagement question, in-scope list, **explicit out-of-scope list**, assumptions labeled, ≥ 3 questions for the client
- [ ] Authorization/safety statement written (local + provided artifacts only) and saved in the stage pack
- [ ] Artifact manifest recorded (`data/MANIFEST.md`: file, source, copied-or-referenced, SHA-256)
- [ ] Stage schedule written (which week, which stage)

### G2 — after Stage 2: assets, threats, risks
- [ ] Asset inventory ≥ 10 entries with owner, data class, CIA impact, justification
- [ ] DFD with all four element types and ≥ 2 justified trust boundaries
- [ ] ≥ 15 **distinct** STRIDE threats (no rephrasings), each with likelihood × impact using **defined scales**, treatment, mitigation
- [ ] Risk register complete per [template](templates/risk-register-template.md): no empty treatment/rationale cells; ≥ 1 residual-risk statement
- [ ] Gate dimensions D1/D4 ≥ 3 in the [rubric](rubric.md)

### G3 — after Stage 3: configuration & control review
- [ ] ≥ 6 findings, each with: evidence line (file+field/line), control-type classification, severity **+** business context, link to a register gap
- [ ] Every candidate validated before becoming a finding; ≥ 1 documented false positive or rejected candidate with the evidence that rejected it
- [ ] Findings written in the [findings template](templates/findings-remediation-template.md)
- [ ] Provided artifacts unmodified (analysis done on copies)
- [ ] Gate dimensions D1/D3 ≥ 3

### G4 — after Stage 4: logs & simulated incident
- [ ] Timeline built from ≥ 3 distinct artifact classes, timezone stated, artifact+line cited per entry
- [ ] ≥ 5 investigation questions answered from evidence (facts vs inferences labeled)
- [ ] ≥ 5 alerts triaged with verdict + severity + action (≥ 1 expected-benign justified from your scope)
- [ ] Detection gap named (which event, which layer) + Sigma-style rule drafted with ATT&CK mapping
- [ ] First-60-minutes IR plan: sequence + trade-offs + what you would preserve and why
- [ ] Gate dimensions D2/D3 ≥ 3

### G5 — after Stage 5: prioritized remediation
- [ ] Top-5 recommendations, each linked to a register ID — **zero orphans**
- [ ] Each row has control type, effort (S/M/L), risk retired, one-line justification, quick-win-vs-strategic tag
- [ ] Deferred/accepted items carry residual statements; privacy or control-mapping note included (DPIA-lite or CSF↔CIS mini-map)
- [ ] Executive summary draft ≤ 300 words, non-technical, readable by the owner/founder
- [ ] Gate dimensions D4/D5 ≥ 3

### G6 — after Stage 6: validation & residual risk
- [ ] ≥ 3 improvements **implemented on your local replica** with before → change → after evidence
- [ ] Each improvement has a test: fail-then-pass (code/config) **or** blocked-flow/403 proof (network/RBAC) **or** rule triggered with captured alert (detection)
- [ ] Retest notes: what re-test would confirm this in production (stated, not performed)
- [ ] Residual-risk register updated: every accepted/deferred risk now has owner + revisit trigger
- [ ] Gate dimensions D5/D3 ≥ 3

### G7 — final package (before submission)
- [ ] Report complete per [report template](templates/report-template.md), incl. "what we don't know" section
- [ ] Portfolio + presentation per [portfolio spec](templates/portfolio-presentation-spec.md) (index, naming, demo rules, 500-word reflection)
- [ ] Evidence index lists every artifact with size + hash where applicable
- [ ] Self-scored [rubric](rubric.md): sheet filled, pass rules checked, fix-list for any dimension at 2
- [ ] Safety/authorization statement present in **every** stage pack
- [ ] Assistance declaration written ([§8](../assessment-guide.md#8-evidence-integrity-and-academic-honesty))

## Submission checklist

Verify against the package root (`portfolio/CAPSTONE/`) before declaring done:

**Structure**
- [ ] `README.md` (index) matches actual files — every link in it resolves
- [ ] `data/MANIFEST.md` present; no provided artifact modified
- [ ] Stages S1–S7 folders each contain their deliverables + safety statement
- [ ] Templates used where required: report, risk register, threat model, findings — sections not deleted (empty where N/A is fine; missing is not)

**Content**
- [ ] All 10 measurable outcomes from the [brief §2](README.md#2-project-objectives-and-measurable-outcomes) demonstrably met — write the O1–O10 → file-path mapping in the index
- [ ] Every finding/timeline/validation claim has a resolvable artifact reference
- [ ] ≥ 15 distinct threats · ≥ 6 validated findings · ≥ 5 triage verdicts · ≥ 3 validated improvements · ≥ 4 detections considered (≥ 1 fired)
- [ ] No orphan recommendations; no unvalidated "criticals"; no real data anywhere

**Safety & honesty**
- [ ] Zero contact with public/third-party/university systems (state it affirmatively in the index)
- [ ] No paid tools, no accounts, no keys outside your machine
- [ ] Assistance declared; own work vs. provided artifacts distinguished
- [ ] Would you be comfortable if the *fictional* client read every page? If not, fix before submitting

**Grade-ready**
- [ ] `RUBRIC.md` self-score complete; ≥ 60%, all dimensions ≥ 2, ethical ≥ 3
- [ ] Executive summary and reflection present
- [ ] Optional extensions attempted (if any) are marked as such — core vs. extra is unambiguous

**Done means:** G1–G7 all ticked + submission checklist ticked + rubric pass rules met. Then stop — and keep the portfolio: it is your interview artifact ([§8](../assessment-guide.md#8-evidence-integrity-and-academic-honesty)).

**Back to:** [Capstone overview & student brief](README.md) · [Rubric](rubric.md)
