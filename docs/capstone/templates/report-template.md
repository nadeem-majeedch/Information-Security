---
title: "Capstone Template — Final Project Report"
layout: default
---

# Capstone Template — Final Project Report

**Part of:** [M19 Capstone Project](../README.md) · Copy this into `portfolio/CAPSTONE/report.md` (or `.docx` — same structure). Target length: **15–25 pages** including appendices; exec summary ≤ 300 words. Section guidance in *italics*; delete guidance when filling in. Every section maps to a rubric dimension ([D1–D7](../rubric.md)).

---

**Title:** Security Review & Remediation Plan — *[Scenario org name]*
**Author:** · **Date:** · **Scenario:** A / B · **Version:** 1.0
**Assistance declaration:** *(tools/AI used for what — per [§8](../../assessment-guide.md#8-evidence-integrity-and-academic-honesty); "none" is a valid answer)*

---

## 1. Executive summary *(≤ 300 words · D6)*

*The board/owner reads only this. Five moves: (1) who they are and what you were asked; (2) overall posture in one sentence; (3) top exposure; (4) top fix + effort; (5) the ask (decision or resource). No jargon, no CVE strings, no tool names unless the owner already uses them.*

## 2. Scope, authorization, and method *(D7, D6)*

- Engagement question and in/out-of-scope lists *(from Stage 1 memo — reproduce verbatim)*
- Authorization & safety statement: targets used (provided artifacts + your local lab only), isolation method, no real data / no public systems
- Assumptions (labeled) · Artifact manifest summary (file, source, copied/referenced, SHA-256)
- Method: stages performed, in order, with dates/effort

## 3. Organizational context and asset inventory *(D1, D2)*

- Org context table (from your scenario + your additions)
- Asset inventory ≥ 10 rows: asset · owner · data classes · CIA impact · justification
- DFD with trust boundaries *(link or embed; ≥ 2 boundaries justified in one line each)*

## 4. Threat model summary *(D1, D4)*

- Method used (STRIDE-per-element — name it, cite where you learned it)
- ≥ 15 distinct threats: condensed table (ID · element · STRIDE · L×I · treatment) — full detail in the [threat-model template](threat-model-template.md) appendix
- Attack-path narrative: the 2–3 chains that worry you most, end to end

## 5. Risk register summary *(D4)*

- Top 10 risks with scores/treatments; full register as appendix *(link the [risk-register template](risk-register-template.md) file)*
- Define your scales (what 5/4/3/2/1 likelihood and impact mean *here*)
- At least one paragraph where business context **changes** a technical ranking — and why

## 6. Configuration and control review *(D1, D3)*

- What you reviewed and against what checklist (name it)
- Findings summary table (ID · title · severity · register link) — full findings in the [findings template](findings-remediation-template.md) appendix
- ≥ 1 rejected candidate / false positive and the evidence that rejected it
- Controls that *work* (a review that only lists problems is incomplete — name 3 things doing their job)

## 7. Incident investigation *(D2, D3)*

- Timeline: ≥ 3 artifact classes merged, timezone stated, every entry cited (file + line/field)
- Investigation answers: facts vs inferences labeled; ≥ 1 "insufficient data — what I would request"
- Triage table: ≥ 5 alerts with verdict · severity · action (include an expected-benign with justification)
- Detection gap: which event should have alerted earlier, at which layer, and your draft rule (Sigma-style + ATT&CK ID)

## 8. Response plan (first 60 minutes) *(D2, D5)*

- Ordered actions with trade-offs (what breaks if you disable X now?)
- Evidence preservation: what you would preserve, chain-of-custody handling, what you explicitly would *not* collect and why

## 9. Prioritized remediation roadmap *(D4, D5)*

- Top-5 table: rank · recommendation · register ID · control type · effort S/M/L · risk retired · quick-win/strategic · owner
- Non-recommendations: deferred items with residual statements + revisit trigger
- Privacy/control note: DPIA-lite bullets for the scenario's personal data **or** a CSF 2.0 ↔ CIS v8.1 mini-map (choose one; say why)

## 10. Validation of improvements *(D1, D3, D5)*

For each of ≥ 3 improvements: **claim → change made → evidence (before/after or test-fire) → result → what production would still need** (retest criteria). One sub-section each; screenshots/logs referenced by filename.

## 11. Residual risk and unknowns *(D4, D2)*

- Residual-risk table: what remains after fixes, owner, revisit trigger
- "What we don't know" + the data/questions we would request next

## 12. Reflection *(D6)*

500 words: the decision you got wrong first and why · the evidence that changed your mind · which module's skill saved you most time · what you would do differently with one more week.

## Appendices

- **A.** Full risk register *(from [template](risk-register-template.md))* · **B.** Full threat model *(from [template](threat-model-template.md))* · **C.** All findings *(from [template](findings-remediation-template.md))* · **D.** Evidence index (name · bytes · hash · used-in-section) · **E.** Stage packs S1–S7 with safety statements

---

**Self-score:** copy the scoring sheet from the [rubric](../rubric.md) into `portfolio/CAPSTONE/RUBRIC.md` and complete it before submission.

**Back to:** [Capstone brief](../README.md) · [Checklists](../checklists.md)
