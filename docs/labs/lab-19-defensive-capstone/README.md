---
title: "LAB-19 — Defensive Security Capstone (Multi-Stage)"
layout: default
---

# LAB-19 — Defensive Security Capstone (Multi-Stage)

**Lab ID:** LAB-19 · **Difficulty:** Capstone (Advanced) · **Estimated duration:** 6 hours · **Module:** M19 · **Mode:** Portfolio synthesis over course-provided synthetic datasets + one self-created local artifact

## Scenario

**Elmwood Credit Union** (fictional) has given you its *pre-engagement* package: no systems to touch — only documentation, two exported configurations, and logs from the incident that made them call you. Your job is the full defensive arc a course should build toward: **scope a system → model its threats → audit its controls → detect the intrusion → contain it on paper → present findings to executives** — with every claim traceable to evidence and every recommendation priced in effort. The capstone is deliberately a *paper* engagement: realism without risk (Safety Policy §2), and it forces the skill that matters most — judgment.

## Learning Objectives

1. Integrate Level 1–3 skills into one coherent engagement: scoping, threat modeling, control auditing, detection reasoning, IR planning, and executive communication.
2. Produce a **traceable** analysis: every finding cites its evidence artifact; every recommendation names the control type, effort, and risk retired.
3. Demonstrate intellectual honesty: separate *observed facts* from *assumptions* from *unknowns*, and list what data you would have requested.
4. Author one piece of original defensive automation (a local script) as proof of applied M18 skills.
5. Deliver a board-ready presentation deliverable (executive summary + one-page architecture/trust-zone view) alongside the technical report.

## Prerequisites and Required Skills

- All Level 1–3 modules; **labs LAB-01, LAB-07, LAB-13, LAB-14, LAB-17, LAB-18 strongly recommended first** (their skills and datasets are reused here).
- Skills: reading logs/JSON/YAML, basic Python, risk vocabulary (M02), policy literacy (M03), network fundamentals (M04).
- Mindset prerequisite: you must be willing to say *"insufficient data — here's what I'd ask for"* at least once. That is graded, not penalized.

## Tools, Operating Systems, and Versions

- Provided package: the course datasets (synthetic auth logs from LAB-13, mock cloud configs from LAB-17, malware report from LAB-16) are **referenced from their home labs** to avoid duplication — see Setup for the exact manifest. There is no separate `data/` folder; copy the listed files into a local working folder.
- Python 3.8+ (stdlib only) for Stage 4's script; any editor; a browser for ATT&CK/NIST references.
- Optional: Mermaid-capable renderer (GitHub/GitLab preview or VS Code extension) for diagrams.

**$0.** No accounts, keys, paid tools, or live targets anywhere in this capstone.

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-19/` with subfolders `stages/s1..s5/`.
2. **Dataset manifest** (copy into `data/` or reference in place — record which you did):
   - `syslog-sample.log` ← [LAB-18 data](../lab-18-security-automation/data/syslog-sample.log) (host detection evidence)
   - `auth-attempts.csv`, `admin-actions.jsonl` ← [LAB-13 data](../lab-13-log-analysis/data/index.md) (auth/privilege evidence)
   - `mock_s3_bucket.json`, `mock_iam_policy.json` ← [LAB-17 data](../lab-17-cloud-config-review/data/index.md) (control-audit targets)
   - `sample-analysis-report.json` ← [LAB-16 data](../lab-16-malware-behavior/data/index.md) (sample evidence, reports-only)
   - Course docs: [course-roadmap](../../course-roadmap.md), [learning outcomes](../../learning-outcomes.md), [lab safety policy](../../lab-safety-policy.md).
3. **Authorization statement** (write it first, keep it in the report): *engagement limited to course-provided synthetic artifacts and files I create on my own machine; no third-party systems, no credentials, no network probing; all findings fictional and non-attributable.*
4. Read the client brief (Scenario above) and write your **engagement understanding memo** (half a page): what you were asked, what you were *not* asked, and your first three questions for the client. (Stage 1 evidence.)

## Lab Environment and Starting State

A static evidence bundle (no live services). The fictional incident, already summarized for you but requiring your analysis: *an invoice-themed phishing email led to a workstation compromise; the attacker authenticated with captured credentials, attempted lateral movement, touched the mock cloud bucket config, and deployed a second-stage binary — before alerts fired (late). The company wants to know what was missed and what to fix first.* Starting state: raw artifacts, zero analysis, no deliverables.

## Tasks (Five Stages)

### Stage 1 — Scoping & Asset Framing (≤ 1 page)
Build a **scoped asset/system inventory** (M01's asset-inventory lab, now for a real-shaped client): assets, owners, data classes (PII/financial per M03), and *explicit out-of-scope* list. Draw a **trust-zone diagram** (ASCII or Mermaid): internet → edge → workstations → internal services → cloud bucket, with the incident's likely path annotated. State your assumptions as assumptions.

### Stage 2 — Threat Model & Risk Register (M02 craft)
Apply a simple method (STRIDE-per-element or attack-tree — name which, cite M02/M14) to **three** assets from Stage 1. Produce a risk register table with: ID, threat, existing control (from evidence), gap, likelihood × impact, and treatment (mitigate/transfer/accept) *with one-line justification each*. Score at least one risk using both the 5×5 matrix and a CVSS-style number, then explain why the two rankings differ (the M02 lesson, applied).

### Stage 3 — Control Audit (configs) + Detection Reasoning (logs)
- **3a. Config audit:** review `mock_s3_bucket.json` + `mock_iam_policy.json` against your checklist (condensed from LAB-17's): ≥ 4 findings with evidence lines, exploitability narrative, and fixes — but now justified *against your Stage 2 register* (which gap does each finding close?).
- **3b. Detection:** using `syslog-sample.log` + the LAB-13 files, reconstruct **what happened and when** (timeline: first failure burst → success → privilege action → second-stage indicators). Identify which of your Stage 2 threats were *actually observed* vs merely possible. Name the **detection gap**: which event should have alerted earlier, and where (host/EDR/network/identity per M04/M05 control-placement thinking).
- **3c. Sample intel:** from `sample-analysis-report.json`, extract ≤ 5 IOCs with confidence/robustness ratings (LAB-16 skill) and mark which are *blocking* vs *hunting* candidates.

### Stage 4 — Original Automation (M18 proof)
Write one script that materially helps this engagement (choose): (a) timeline builder merging the three log sources into one ordered `timeline.csv`; (b) an analyzer that flags success-after-failures across sources and emits Stage-3-grade alerts; (c) a register-linter that checks your own risk-register CSV for missing fields (meta-quality tooling). Requirements: stdlib only, deterministic, **test fixture included**, README with one-command run, and a paragraph on what a production version would add (scheduling, state, RBAC on the tool itself).

### Stage 5 — IR Plan & Executive Delivery
- **5a. Containment plan (paper IR):** play the first 60 minutes (M14/LAB-14): detection time, severity call, escalation, containment options *for each foothold you found* (workstation, identity, cloud config) with trade-offs (what breaks if you disable this account now?). Legal/handoff note: what you'd preserve for forensics (M18 chain-of-custody) and why you do **not** collect beyond scope yourself.
- **5b. Prioritized roadmap:** top 5 recommendations, each with: control type (preventive/detective/corrective — M02), effort (S/M/L), risk retired (register ID), and quick-win vs strategic. No recommendation without a register link.
- **5c. Executive summary (≤ 300 words, non-technical):** the five-sentence version a board reads first — exposure, top risk, top fix, cost/effort, ask. Plus a **"what we don't know"** paragraph (unknowns + the data you'd request next).

## Expected Observations

| Stage | Expected |
|---|---|
| 1 | Trust-zone diagram with an annotated likely attack path; out-of-scope list present; assumptions labeled |
| 2 | ≥ 3 threats modeled; register with treatments + justifications; 5×5 vs CVSS divergence explained concretely |
| 3a | ≥ 4 config findings each mapped to a register gap (audit ≠ laundry list) |
| 3b | Coherent timeline from ≥ 3 sources; "detected late" explained as a *specific* gap (e.g., no alert on success-after-burst), not "they needed better security" |
| 3c | ≤ 5 IOCs, robustness-rated, blocking-vs-hunting split stated |
| 4 | Script runs, tests pass, output supports Stage 3 (your timeline/alerts actually appear in later prose) |
| 5 | Containment options per foothold with trade-offs; roadmap fully register-linked; exec summary jargon-free; unknowns disclosed |

## Investigation Questions

1. You found the phishing→compromise chain *after the fact* with logs the client already had. Which single **preventive** control (M02 taxonomy) would have most cheaply broken the chain, and what does your answer cost in user friction? (Trade-off, not slogans.)
2. Two findings compete for the same S/M effort budget: a config fix and a detection improvement. Which do you fund first *for this client* — and how does your Stage 2 register decide it rather than your preference?
3. The identity touched the bucket but the report shows *no evidence of data egress* — state precisely what you can claim, what you cannot, and how that changes severity (evidence-honesty, echoing LAB-16's verdict critique).
4. Where did automation change your *judgment* (not just your speed)? Where did it risk automating a wrong assumption?
5. A reviewer challenges your likelihood scores as "gut feel." What in your write-up defends them (evidence links, method citation, explicit assumptions)?

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Dataset links 404 | LAB-13/16/17/18 folders not present locally | Copy from the course repo paths in the manifest, or open the linked lab pages; record provenance either way |
| Timeline timestamps don't line up across sources | Different formats/timezones | Normalize to one timezone with a documented rule; note the assumption in the timeline header |
| Stage 4 script grows huge | Scope creep (building a SIEM) | One script, one job, ≤ ~150 lines; production gaps go in the README paragraph, not the code |
| Register feels arbitrary | Scores without evidence anchors | Tie each likelihood to an observed event (Stage 3) or a named threat (Stage 2); say when it's an assumption |
| Stuck on "is this the right answer?" | Capstone has no single right answer | Graded on traceability, honesty, and coherence — justify decisions; flag unknowns explicitly |
| Executive summary keeps leaking jargon | Written last-minute from the technical report | Rewrite from scratch for a non-technical reader; have the glossary handy — every term must be plain language |

## Evidence to Collect

- `stages/s1..s5/` folders: scope memo + trust-zone diagram; threat model + risk register; config findings + timeline + IOC table; script + tests + README; IR plan + roadmap + exec summary.
- One **comparison table**: register ID ↔ finding ↔ evidence artifact ↔ recommendation (the traceability spine of the whole capstone).
- Stage 4 test output (passing) and a sample of generated `timeline.csv`/alerts.
- The authorization/scope statement (Task 3) as the report's front matter.
- Safety statement: *all analysis on course-provided synthetic artifacts + files I created; no live targets, no credentials, no network activity; nothing committed or deployed.*

## Deliverable and Report Structure

`portfolio/LAB-19/report.md` (or PDF) in order: **(1)** scope + authorization + assets/trust zones, **(2)** threat model + risk register, **(3)** control audit + incident timeline + IOCs, **(4)** automation appendix (code summary, run instructions, test output), **(5)** IR containment plan, **(6)** prioritized roadmap with the traceability table, **(7)** executive summary + "what we don't know", **(8)** references (course + NIST/ATT&CK) + safety statement. Target 6–10 pages; diagrams where prose gets dense.

## Completion Checklist

- [ ] Scope memo with out-of-scope list + labeled assumptions; trust-zone diagram drawn
- [ ] Threat model (named method) for ≥ 3 assets; register with treatments and justifications
- [ ] 5×5 and CVSS-style scores both present with a divergence explanation
- [ ] ≥ 4 config findings, each linked to a register gap
- [ ] Multi-source timeline; detection gap named precisely (which event, which layer)
- [ ] ≤ 5 robustness-rated IOCs split into blocking vs hunting
- [ ] Original stdlib script with passing test fixture + README; used in the report
- [ ] Containment options per foothold with trade-offs; forensic preservation noted
- [ ] Roadmap: every recommendation linked to a register ID + effort + control type
- [ ] ≤ 300-word executive summary, jargon-free, with a disclosed-unknowns paragraph
- [ ] Traceability comparison table (register ↔ finding ↔ evidence ↔ recommendation)
- [ ] Authorization + safety statements written

## Cleanup and Reset

1. Nothing executed against external systems — there is nothing to stop or roll back; delete only scratch files (`__pycache__/`, temp outputs) if desired.
2. Keep the full portfolio: it is summative evidence. Original course datasets remain untouched (you copied or referenced them).
3. No secrets, keys, or personal data were ever involved — re-confirm by grepping your deliverables for anything that looks like a credential or real PII before sharing.
4. If you generated extra synthetic data (Stage 4 fixtures), label it synthetic inside the file so future-you stays compliant with Safety Policy §5.

## Optional Challenges

- **Red-team reflection (paper only):** write a one-page "what a skilled adversary would do next from the weakest foothold" *purely to prioritize defense* — clearly labeled as defensive planning, no tooling, no target (Safety Policy §2's offensive-technique boundary).
- **Re-score after remediation:** assume your top 3 roadmap items shipped; re-run the register with updated likelihoods and show the before/after risk heat map — the metric story executives love.
- **Portfolio integration:** assemble LAB-01…LAB-19 highlights into a capstone *portfolio index* with reflections (great interview artifact); optionally preview it with your instructor's guidance.

## References and Safety Notes

- NIST SP 800-61 Rev. 2 (*Computer Security Incident Handling Guide*): <https://csrc.nist.gov/pubs/sp/800/61/r2/final>.
- NIST SP 800-30 Rev. 1 (*Guide for Conducting Risk Assessments*): <https://csrc.nist.gov/pubs/sp/800/30/r1/final>.
- NIST CSF 2.0: <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final> · MITRE ATT&CK: <https://attack.mitre.org>.
- Course: [M19](../../modules/module-19-integrated-capstone-project/README.md) · [roadmap](../../course-roadmap.md) · [learning outcomes](../../learning-outcomes.md) · [Lab Safety Policy](../../lab-safety-policy.md) (§1 authorized scope, §2 defensive-only rule, §5 synthetic-data labeling).
- **Safety:** capstone operates exclusively on course-provided **synthetic** artifacts and self-created local files; no live systems, credentials, personal data, or network probing; offensive-flavored thinking stays **on paper** (Stage 5/Challenge 1) and is explicitly scoped to fictional assets. Nothing in this lab is committed, pushed, or deployed.

**Navigation:** · [← Previous: LAB-18](../lab-18-security-automation/README.md) · [Lab index](../README.md)
