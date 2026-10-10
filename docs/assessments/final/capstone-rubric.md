---
title: "Capstone Assessment Rubric — M19 Integrated Capstone Project"
layout: default
---

# Capstone Assessment Rubric — M19 Integrated Capstone Project

**Type:** Capstone assessment rubric (standalone, self-assessed) · **Applies to:** [M19 Integrated Capstone Project](../../modules/module-19-integrated-capstone-project/README.md) · **Companion to:** [Assessment Guide §5.4](../../assessment-guide.md#54-capstone-rubric-component-e-per-stage-and-overall) (this page is the expanded, stage-by-stage scoring instrument — the guide holds the summary; weights in §4 of the guide are unchanged)

**Project package:** the full capstone brief — alternative scenarios, the seven-stage workflow with milestone gates, report/register/threat-model/findings templates, and the seven-dimension scoring instrument — is the [M19 Capstone Project](../../capstone/README.md); its [rubric page](../../capstone/rubric.md) crosswalks those seven dimensions to the five criteria used below.

**How to use this rubric.** The capstone is graded **per stage (A–E) and overall**, exactly as the [Assessment Guide](../../assessment-guide.md) defines. This page makes self-assessment concrete: for every criterion and stage it states what *Exemplary / Proficient / Developing / Inadequate* looks like **for that specific stage**, so you can score your own work without guessing. There is no hidden marker's copy — by [policy](../README.md#student-facing-answer-policy--read-this), the standards are published because self-assessment only works when the standard is visible.

**Scoring rules (from the guide — do not loosen these):**
- Five criteria per stage, each scored **4 (Exemplary) / 3 (Proficient) / 2 (Developing) / 1 (Inadequate)**.
- **Stage passes** with ≥ 3 (Proficient) on **at least 4 of 5** criteria, and **no criterion at 1**.
- **Safety & ethics at 1 = automatic stage return** (safety gate overrides scores — [§7](../../assessment-guide.md#7-safety-gate-passfail-overrides-scores)).
- **Overall course capstone mark:** weighted average of the five stages; **≥ 60% overall, no stage below Developing**, to pass component E ([§5.5](../../assessment-guide.md#55-overall-grade-bands)).
- Revisions: a stage returned while Developing/Inadequate may be revised any number of times ([§6](../../assessment-guide.md#6-resubmission-and-reassessment-policy)) — the goal is competence, not attrition.

**The five criteria (every stage):**
1. **Integration across CLOs** — draws on multiple prior modules, not isolated tricks.
2. **Technical depth & correctness** — works, verified, reproducible.
3. **Risk & threat reasoning** — explicit and framework-linked (CSF 2.0 / CIS v8.1 / ATT&CK / STRIDE).
4. **Professional documentation** — a third party could re-run or review it from your submission alone.
5. **Safety & ethics** — isolation, authorization, data rules, evidence handling correct.

---

## Stage A — Design and threat model

*Deliverables (M19):* architecture documentation for the scenario (15-person startup, $0 budget), DFD with trust boundaries, STRIDE threat model (≥ 15 threats), control selection mapped to CSF 2.0 / CIS v8.1.

| Criterion | 4 — Exemplary | 3 — Proficient | 2 — Developing | 1 — Inadequate |
|---|---|---|---|---|
| Integration | Design explicitly cites M01–M11 decisions (identity, network zones, web surface) and reconciles them | Uses 3+ prior modules with most linkages stated | Design mostly module-silo; links implicit | Isolated diagram, no cross-module reasoning |
| Technical depth | DFD complete (4 element types, every boundary justified); threats are distinct and element-specific | DFD + ≥ 15 threats, boundaries present; a few threats generic | Boundaries thin or threats padded/duplicated | DFD missing elements/boundaries |
| Risk reasoning | Every threat: likelihood×impact with **defined scales**, treatment + rationale; residual risk stated | Most threats rated + treated; residual risk mentioned | Ratings present, treatments thin or unexplained | No prioritization method |
| Documentation | Third party could redraw the model from your docs alone; control map complete with owners | Readable, mostly complete; mapping present | Understandable but gaps (no owners/rationale) | Unusable or missing |
| Safety & ethics | Scenario stays fictional/lab; privacy implications of scenario data considered (links M17) | Compliant; safety statement present and specific | Minor omission (vague statement) | Violation → automatic return |

**Common Stage-A failure:** 15 *rephrasings* of one threat. Distinctness across elements and boundaries is the skill being scored.

---

## Stage B — Implement baseline hardening

*Deliverables:* reproducible host + network + access-control hardening in the lab, with before/after evidence.

| Criterion | 4 — Exemplary | 3 — Proficient | 2 — Developing | 1 — Inadequate |
|---|---|---|---|---|
| Integration | Hardening ties to Stage-A threats and to least-privilege/RBAC decisions (M05/M07/M08) | Most changes trace to a threat or baseline | Generic hardening checklist, weak traceability | Changes unexplained |
| Technical depth | Every control verified with a state-change test; blocked-flow evidence for firewall; no broken services | Most controls verified; blocked + allowed flow tests present | Commands shown but before/after state missing for some | Claims without evidence |
| Risk reasoning | Residual risks after hardening named with treatment decisions | Residual risks listed with rough ratings | Residual risk hand-waved | Ignored |
| Documentation | Rebuildable from your runbook alone (order, commands, expected outputs) | Runbook mostly complete | Steps readable but incomplete | Not reproducible |
| Safety & ethics | Isolation proven; authorization statement correct and specific; no real data | Compliant, statement present | Vague statement | Violation → automatic return |

---

## Stage C — Authorized assessment

*Deliverables:* RoE, professional assessment report of the Stage-B environment, findings with evidence, remediation roadmap, retest plan.

| Criterion | 4 — Exemplary | 3 — Proficient | 2 — Developing | 1 — Inadequate |
|---|---|---|---|---|
| Integration | Uses M12 method + M09 reporting discipline; findings reference ASVS/CWE where apt | Phases followed; reports in professional structure | Report written but method loose | Scan dump, no validation |
| Technical depth | All findings manually validated (incl. documented FP handling); severity = CVSS vector **+** business context | Findings validated; severity mostly justified | Some scanner-only findings slip through | Unvalidated "criticals" |
| Risk reasoning | Roadmap prioritized by exposure × impact with retest criteria per finding | Roadmap ordered with rationale | Flat list of fixes | No roadmap |
| Documentation | Client-ready: exec summary, methodology, evidence, appendices; third-party retestable | Complete with minor gaps | Readable, incomplete | Unusable |
| Safety & ethics | RoE with stop conditions *before* testing; scope never exceeded; data minimization observed | RoE present; scope respected | RoE thin | Scope violation → automatic return |

---

## Stage D — Detect, triage, respond

*Deliverables:* monitoring deployed, **≥ 4 detections**, simulated incident with triage → response, forensic evidence and timeline.

| Criterion | 4 — Exemplary | 3 — Proficient | 2 — Developing | 1 — Inadequate |
|---|---|---|---|---|
| Integration | Full M13→M14→M15 loop; detections informed by the threat model and malware/IOC work | Detections + IR executed; most linkage stated | Pieces present, loop incomplete | Detections never fired |
| Technical depth | Detections **tested by triggering** with evidence; triage worksheet complete; volatile-first evidence order documented | Tests + worksheet + reasonable evidence order | Rules written but untested | Fabricated or missing evidence |
| Risk reasoning | Triage verdicts use asset value + context; response order justified (contain-before-recover) | Verdicts with action; order mostly right | Verdicts lack reasoning | No triage |
| Documentation | Timeline with artifact citations; chain-of-custody form; detections versioned with FP notes | Timeline + citations present | Timeline with gaps | Unusable |
| Safety & ethics | Simulated incident fully in-lab; sandbox discipline for any sample analysis | Compliant | Minor omission | Violation → automatic return |

*This stage also feeds component D ([Investigation rubric §5.3](../../assessment-guide.md#53-investigation-rubric-component-d-per-report-100-points)): the written investigation must reach ≥ 60/100.*

---

## Stage E — Final package and lessons learned

*Deliverables:* architecture docs + threat model (A), hardening evidence (B), assessment report (C), detection/IR evidence (D), **privacy/compliance note**, and a lessons-learned report — assembled as one coherent package with an index.

| Criterion | 4 — Exemplary | 3 — Proficient | 2 — Developing | 1 — Inadequate |
|---|---|---|---|---|
| Integration | Package reads as one story; privacy note (M17) and automation notes (M18, if used) woven through | All five artifacts present and cross-referenced | Artifacts present, weakly connected | Loose files |
| Technical depth | Every claim in the package backed by an artifact you can point to | Most claims evidenced | Some unsupported claims | Contradictions/fabrication |
| Risk reasoning | Privacy/compliance note classifies data and states retention/controls; final risk posture honest (residuals included) | Note present with classifications | Thin note | Missing |
| Documentation | Index navigable; third party can audit end-to-end; versioning clean | Organized with minor gaps | Usable but messy | Unusable |
| Safety & ethics | Safety statements on every pack; data rules followed throughout | Statements present | Some vague | Violation → automatic return |

---

## Self-assessment worksheet (print or copy)

| Stage | Integ. (1–4) | Tech (1–4) | Risk (1–4) | Doc. (1–4) | Safety (1–4) | Stage pass? (≥3 on 4/5, none at 1) | Fix list for returned criteria |
|---|---|---|---|---|---|---|---|
| A — Design & threat model | | | | | | | |
| B — Hardening | | | | | | | |
| C — Assessment | | | | | | | |
| D — Detect & respond | | | | | | | |
| E — Final package | | | | | | | |

**Overall:** average of stage percentages (each stage = 20 points of criteria) → map to [grade bands](../../assessment-guide.md#55-overall-grade-bands). Then complete one line per returned criterion: *the specific gap, the fix, the evidence you'll add.*

**Integrity note:** your submission may use AI or other assistants as *learning support* — declare them in a "Sources & assistance" line; fabrication or undisclosed ghost-work is what fails honesty, not assistance itself ([§8](../../assessment-guide.md#8-evidence-integrity-and-academic-honesty)).

---

**Related:** [CAP-ADV — Advanced Final Assessment](advanced-final.md) · [Lab Challenges](lab-challenges.md) · [M19 module](../../modules/module-19-integrated-capstone-project/README.md) · [Assessment Guide](../../assessment-guide.md) · **Hub:** [Assessment Hub](../README.md)
