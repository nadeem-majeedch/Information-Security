---
title: "M19 Capstone Project — Overview and Student Brief"
layout: default
---

# M19 Capstone Project — Overview and Student Brief

**Module:** [M19 — Integrated Capstone Project](../modules/module-19-integrated-capstone-project/README.md) · **Level:** 4 · **Estimated effort:** 30–40 hours over ≥ 4 weeks (7 stages) · **Cost:** **$0** · **Assessment:** [capstone rubric](rubric.md) (self-assessed; optional peer review) · **Course weight:** component E, 20% per the [Assessment Guide](../assessment-guide.md)

**Companion pages:** [Scenarios](scenarios.md) · [Rubric](rubric.md) · [Completion & submission checklists](checklists.md) · Templates: [report](templates/report-template.md) · [risk register](templates/risk-register-template.md) · [threat model](templates/threat-model-template.md) · [findings & remediation](templates/findings-remediation-template.md) · [portfolio & presentation spec](templates/portfolio-presentation-spec.md)

---

## 1. Overview and student brief

This is the course's final project: you play the security practitioner for a small organization, end to end. You will **understand the organization → model its risks → review its configurations and controls → investigate a simulated incident from provided logs → recommend prioritized remediation → validate improvements in your lab → report and reflect.**

Three things distinguish it from everything before it:

1. **It is evidence-based, not tool-based.** Every claim in your report must point to an artifact you produced or were given — a log line, a config field, a before/after diff, a test result. "We should add monitoring" is not an answer; "*alert on success-after-burst would have caught the 03:19 event — here is the rule and its test fire*" is.
2. **It integrates.** No stage uses only one module. Stage 2 needs M01+M02+M11; Stage 4 needs M04+M05+M13+M14; Stage 5 needs M02+M12+M17. The [skills provenance table](#7-skills-provenance-every-requirement-was-taught-first) proves every required skill was taught earlier — the capstone *tests* judgment, it does not *teach* new techniques.
3. **It is safe by construction.** You choose one of two fictional scenarios, work with provided **synthetic** artifacts and your **own local lab**, and never touch a real organization's systems. See [§4](#4-scope-assumptions-constraints-and-explicit-exclusions).

**How to work:** read the [scenario briefs](scenarios.md), pick A or B, copy the templates into your `portfolio/CAPSTONE/` folder, and work the stages in order. Each stage ends with a **milestone gate** (in the checklists) — do not advance until it passes; later stages inherit quality from earlier ones. Self-assess honestly with the [rubric](rubric.md) before marking the project complete.

> **Safety first:** engagement is limited to course-provided synthetic artifacts and files you create on your own machine. This brief is your written authorization *scope* — anything outside it requires nothing short of stopping. See the [Lab Safety Policy](../lab-safety-policy.md).

---

## 2. Project objectives and measurable outcomes

Each objective states a measurable bar. All map to the synthesis outcomes in the [Course Roadmap §M19](../course-roadmap.md#m19--integrated-capstone-project) and to the CLOs in [Learning Outcomes](../learning-outcomes.md).

| # | Objective | Measurable outcome (the bar) |
|---|---|---|
| O1 | Understand and scope an engagement | ≥ 1-page scoping memo: engagement question, **explicit out-of-scope list**, assumptions labeled as assumptions, ≥ 3 questions you would ask the client |
| O2 | Inventory and classify assets | ≥ 10 assets/systems with owner, data classes (incl. any personal data), CIA impact ratings, one-line justification each |
| O3 | Threat-model the chosen system | DFD with all four element types, **≥ 2 justified trust boundaries**; **≥ 15 distinct STRIDE threats**, each with likelihood × impact (defined scales), treatment, and mitigation |
| O4 | Audit configurations and controls | ≥ 6 validated findings against the provided configs/system state — each with evidence line, control-type classification, and the register gap it closes (no unvalidated scanner-style claims) |
| O5 | Analyze logs and investigate | A chronological timeline built from **≥ 3 provided artifacts**, answering ≥ 5 investigation questions with artifact citations; verdict/severity/action for ≥ 5 alerts |
| O6 | Prioritize remediation | Top-5 recommendations, each linked to a register ID, with control type, effort (S/M/L), risk retired, and one-line justification — no orphan recommendations |
| O7 | Validate improvements | **≥ 3 implemented defensive improvements** in your local lab with before → change → after evidence and a fail-then-pass test (or a triggered detection rule with captured alert) |
| O8 | Document residual risk | Residual-risk statements for every accepted/deferred risk, plus a "what we don't know / what we would request" section |
| O9 | Communicate professionally | Report built on the [report template](templates/report-template.md) with exec summary ≤ 300 words; presentation/portfolio per the [portfolio spec](templates/portfolio-presentation-spec.md) |
| O10 | Practice ethically | Safety/authorization statement in every stage pack; zero scope violations; honesty declaration for any assistance used |

---

## 3. Choosing your scenario

Two complete alternative scenarios are provided — pick **one**. Both are fully supported by provided synthetic artifacts and both exercise the same seven stages; they differ in emphasis (network/endpoint/backup posture vs. web application/API posture). Full backgrounds, org context, artifact manifests, and starting states: **[Scenarios](scenarios.md)**.

| | **Scenario A — Copperfield Books** | **Scenario B — Larkspur Labs** |
|---|---|---|
| Emphasis | Small-business security review: network, endpoint, identity, backups, cloud-sync config | Simulated web-application defense: OWASP-class findings, app hardening, app+auth logs, secure code |
| Org | 12-person independent bookshop + online store; one Linux server, office Wi-Fi, NAS, cloud-sync bucket | 15-person SaaS startup (CRM product); web app + API + internal network; local staging app |
| Primary datasets | LAB-13 auth logs, LAB-18 syslog sample, LAB-17 mock configs, LAB-16 sample report | LAB-15 forensic bundle, LAB-13 auth/admin logs, LAB-17 mock configs, optional local Juice Shop/DVWA |
| Best for | Learners who enjoyed M04/M05/M08/M13/M17 | Learners who enjoyed M06/M07/M09/M10/M11 |

Both scenarios are fictional; no system you touch belongs to anyone else; all personal data in the artifacts is synthetic.

---

## 4. Scope, assumptions, constraints, and explicit exclusions

### In scope (for both scenarios)
- Analysis of the **provided synthetic artifacts** listed in your scenario manifest.
- A **local lab replica** on your own machine (VMs, containers, local apps) that you create, own, and may tear down.
- Writing: memos, diagrams, registers, findings, detections, the report, and the presentation deliverable.
- One piece of **original local automation** (stdlib-level scripting) — Stage 4 or 6.

### Assumptions (state yours explicitly in the scoping memo)
- You have completed M01–M18 and own the machine you work on.
- Provided datasets are complete enough for the required analyses; where they are not, you say so and list what you would request (this is *graded*, not penalized).
- "Improvements" are validated on your local replica, not on the fictional organization's live systems.

### Constraints
- **Budget = $0.** Free/open tools only (the same toolset as prior modules: Linux/Windows VMs, Wireshark, nmap *lab-only*, Suricata, Sigma/YARA CLIs, OpenSSL, Semgrep, Gitleaks, Trivy, Python stdlib, Juice Shop/DVWA/WebGoat, draw.io/pen-and-paper).
- **Timebox:** 30–40 hours; work staged over ≥ 4 weeks.
- **Environment:** your own machine or an isolated lab network (host-only/NAT-isolated). Datasets are copied/referenced from their home labs — record which you did.
- **Evidence:** synthetic or course-provided data only, per [Lab Safety Policy](../lab-safety-policy.md) §Data handling.

### Explicit exclusions — the capstone must NOT require any of these
1. **No attacking, scanning, or probing public or third-party systems.** All network activity is against VMs/containers you started on your own machine. (If a scenario step seems to need the internet beyond *reading* documentation, it does not — re-read the step.)
2. **No purchasing software or services.** No paid tools, licenses, cloud tiers, or hardware. No credit card anywhere.
3. **No accessing university/employer systems.** Do not use campus infrastructure, work systems, or shared lab machines as your environment.
4. **No real organizational or personal data.** Organizations are fictional; datasets are synthetic; if you recognize real-looking personal data, stop and report it as a dataset defect instead of using it.
5. **No live malware.** Sample analysis uses the provided *report* artifact and, at most, benign binaries you compile yourself inside an isolated VM ([LAB-16](../labs/lab-16-malware-behavior/README.md) discipline).
6. **No credentials, accounts, or keys** outside ones you create locally. No real payment flows, no real patient/customer records.
7. **No out-of-scope "quick checks."** The scenario's systems are the systems — improvising extra targets is a scope violation even on your own network (this mirrors Stage 1's RoE discipline).

Anything excluded here is excluded **by the rubric too**: a submission that needed an exclusion to complete is returned under [ethical practice](rubric.md).

---

## 5. Prerequisites and recommended preparation

**Required before starting:**
- **Modules:** all of M01–M18, with knowledge-check gates passed (≥ 80% each — see the [Assessment Hub](../assessments/README.md)).
- **Portfolio:** ≥ 17 of 19 module packs in your `portfolio/` folder with index (per [Assessment Guide §C](../assessment-guide.md)); your capstone packs extend it.
- **Investigations:** the four Level-3 investigation reports at ≥ 60% each ([§D](../assessment-guide.md)) — Stage 4 assumes you can already triage and build a forensic timeline.
- **Safety:** [Lab Safety Policy](../lab-safety-policy.md) read and acknowledged.

**Recommended preparation (strongly advised, not gating):**
- [CAP-ADV — Advanced Final](../assessments/final/advanced-final.md) — the best readiness check for the written load (≥ 70% suggested).
- The four [case studies](../assessments/README.md#cross-module-case-studies-integrative-scenario-based) (CS-1…CS-4) and your level's [lab challenge](../assessments/final/lab-challenges.md) — same evidence-discipline, smaller scope.
- [LAB-19 — Defensive Security Capstone](../labs/lab-19-defensive-capstone/README.md) — a 6-hour *paper rehearsal* of the same arc on course datasets; doing it first is the single best predictor of a smooth capstone.
- Per-scenario refreshers (listed in [scenarios.md](scenarios.md#scenario-specific-preparation)).

---

## 6. Staged project workflow with milestones

Seven stages, ~40 hours. Work them **in order** — each stage's outputs are inputs to the next. Every stage ends with a gate; the [checklists](checklists.md) are the gate definitions. The mapping column ties each workflow stage to the five graded deliverable stages (A–E) used by the [Assessment Guide](../assessment-guide.md#54-capstone-rubric-component-e-per-stage-and-overall).

| Stage | Goal | Core deliverables | ~h | Maps to |
|---|---|---|---|---|
| **1. Understand the organization and define scope** | Know what you were asked, what you may touch, and what you won't | Scoping memo (O1), engagement/authorization statement, artifact manifest, first-3-questions list, draft schedule | 3 | A (prep) |
| **2. Identify assets, threats, vulnerabilities, and risks** | Turn understanding into a model and a ranked register | Asset inventory (O2), DFD with trust boundaries (O3), STRIDE threat table ≥ 15, risk register with treatments + residuals (O3) | 7 | **A** |
| **3. Review system configurations and security controls (controlled environment)** | Find what's actually wrong, with evidence | Config/control audit ≥ 6 findings (O4) against provided artifacts + local replica baseline; control-type classification; findings in the [findings template](templates/findings-remediation-template.md) | 6 | **B** (baseline) + **C** |
| **4. Analyze provided security logs and investigate the simulated incident** | Reconstruct what happened; show the detection/IR reasoning | Multi-source timeline ≥ 3 artifacts, ≥ 5 investigation answers with citations, ≥ 5 alert triage verdicts, first-60-minutes IR plan, detection-gap analysis (O5) | 7 | **D** |
| **5. Recommend prioritized remediation and justify the decisions** | Decide what gets fixed first, and why | Prioritized top-5 roadmap linked to register IDs (O6), effort/risk-retired/quick-win-vs-strategic columns, deferred-risk notes, privacy/control-mapping note (O8) | 4 | **C** (roadmap) + **E** |
| **6. Validate selected defensive improvements and document residual risks** | Prove ≥ 3 fixes actually work | ≥ 3 improvements implemented on the local replica with before→after + fail-then-pass or rule-trigger evidence (O7); retest notes; updated residual-risk statements (O8) | 7 | **B** + **C** (retest) |
| **7. Produce the final report and reflective portfolio** | Package everything so a third party can audit it | Report per [template](templates/report-template.md) (O9), evidence index, portfolio + presentation per [portfolio spec](templates/portfolio-presentation-spec.md), 500-word reflection, self-scored [rubric](rubric.md), [submission checklist](checklists.md#submission-checklist) | 6 | **E** |

**Milestone gates (detail in [checklists](checklists.md)):** G1 after Stage 1 (scope + authorization complete) · G2 after Stage 2 (register reviewed for distinctness and scoring) · G3 after Stage 3 (every finding has an evidence line) · G4 after Stage 4 (timeline is artifact-cited, triage complete) · G5 after Stage 5 (no orphan recommendations) · G6 after Stage 6 (before/after proof for all three) · G7 at submission (portfolio + self-score).

**Pacing advice:** one stage per week fits 30–40 h over 6–7 weeks; Stages 3+4 are the heaviest — do not start them the week you start the project. Re-entry after a break: re-read your Stage 1 memo first.

---

## 6a. Required technical investigations and defensive decisions

"Evidence-based reasoning, not tool descriptions" is the graded difference. Stage by stage, you must *do* and *decide*:

**Investigations (technical work):**
- **Config/control audit (Stage 3):** manual review of the provided JSON configs and local-replica settings — public exposure, identity/permissions, encryption flags, logging — with each candidate *validated* (does the field really say that? does it matter here?) before it becomes a finding. No scanner output as findings.
- **Multi-source log timeline (Stage 4):** parse auth/admin/syslog/forensic-bundle artifacts; normalize timezones; order events; distinguish *observed* from *inferred*; answer investigation questions with exact artifact+line citations.
- **Alert triage (Stage 4):** ≥ 5 alerts each scored verdict (TP/FP-by-context) · severity · next action, using asset value and scenario context — including at least one "expected-benign" justified from your own scope.
- **Detection-gap analysis (Stage 4):** identify which event *should* have alerted earlier, at which layer (identity/host/network/web), and name the rule you would add (Sigma-style, ATT&CK-mapped).
- **Validation testing (Stage 6):** implement ≥ 3 improvements on the local replica — e.g., firewall/segmentation rules with blocked-flow tests, RBAC matrix with denied-request proof, hardening baseline with before/after scan, a detection rule **fired in-lab** with captured alert, an app/code fix with a fail-then-pass test.

**Defensive decisions (judgment work):**
- Scoping: what is out of scope and *why* (Stage 1).
- Treatment: mitigate / transfer / accept / avoid per register entry, with justification (Stage 2).
- Severity: CVSS-style vector **plus** business context — and say when they disagree (Stage 3).
- Prioritization: rank by exposure × impact under a $0/timebox constraint; quick-win vs strategic; what you defensibly *don't* fix (Stage 5).
- Detection: tune vs. disable — how to add a rule without drowning the analyst (Stage 4/5).
- Residual risk: what remains after your fixes, who owns it, when to revisit (Stage 6/7).
- Ethics: stop-and-ask triggers; what data you would refuse to collect (all stages).

---

## 6b. Evidence collection requirements

Evidence is what makes claims auditable. Requirements apply **per stage pack**:

| Requirement | Standard |
|---|---|
| **Coverage** | Every finding, timeline entry, and validation claim cites at least one artifact (file + line/field, or screenshot with timestamp) |
| **Before/after** | Any change you made shows state *before*, the change made, state *after* — commands and outputs, not prose alone |
| **Test fires** | Detections include the synthetic event that triggered them and the resulting alert; fixes include the test that fails before and passes after |
| **Integrity** | Record file names, sizes, and (for bundles you copy) SHA-256 sums in the evidence index; never edit provided artifacts — analyze copies |
| **Timestamps** | Your own captures carry date/time; log-derived claims state the timezone used |
| **Safety statement** | Every stage pack ends with: targets used (none beyond local/provided), isolation method, and confirmation of no real data |
| **Honesty** | Separate **observed facts** / **assumptions** / **unknowns** visibly; assistance declaration per [§8](../assessment-guide.md#8-evidence-integrity-and-academic-honesty) |
| **Naming** | `S<stage>-<type>-<nn>-<desc>` e.g. `S3-finding-01-bucket-public-before.png` — full scheme in the [portfolio spec](templates/portfolio-presentation-spec.md) |

Where a stage says "≥ N artifacts," they must be distinct sources — three screenshots of one file count once.

---

## 7. Skills provenance: every requirement was taught first

No capstone technique is introduced here that the course did not teach. Required skill → where it was introduced:

| Capstone requirement | Taught in |
|---|---|
| Asset inventory, CIA classification | M01 · [LAB-01](../labs/lab-01-cia-case-analysis/README.md) |
| Risk vocabulary, 5×5 scoring, treatments | M02 · [LAB-02](../labs/lab-02-threat-model-risk-register/README.md) |
| Scope, authorization, RoE, ethics, privacy duties | M03 · [Lab Safety Policy](../lab-safety-policy.md) |
| Network reading, ports/protocols, packet basics | M04 · [LAB-07](../labs/lab-07-packet-analysis/README.md) |
| Host hardening, permissions, persistence locations | M05 · [LAB-04](../labs/lab-04-permissions-hardening/README.md) |
| Password hashing, TLS/certificates, crypto-misuse review | M06 · [LAB-05](../labs/lab-05-hashing-integrity-signatures/README.md) · [LAB-03](../labs/lab-03-password-hashes/README.md) |
| IAM: RBAC, least privilege, MFA, session/OAuth flaws | M07 · [LAB-06](../labs/lab-06-auth-access-control/README.md) |
| Segmentation, firewall rule review, IDS alert reading | M08 · [LAB-08](../labs/lab-08-firewall-config-audit/README.md) |
| Web vulnerabilities, OWASP categories, vuln reports, ASVS/CVSS | M09 · [LAB-10](../labs/lab-10-web-security/README.md) · [LAB-11](../labs/lab-11-headers-tls-analysis/README.md) |
| Code review/fixes, SAST/secrets/dep scanning, fail-then-pass | M10 · [LAB-09](../labs/lab-09-secure-coding/README.md) |
| DFD + STRIDE, threat elicitation, zero-trust review | M11 · [LAB-02](../labs/lab-02-threat-model-risk-register/README.md) |
| Assessment phases, RoE, false-positive validation, report writing | M12 · [LAB-12](../labs/lab-12-vuln-scan-interpretation/README.md) |
| Log pipeline, Sigma/ATT&CK detections, triage, MTTD/MTTR | M13 · [LAB-13](../labs/lab-13-log-analysis/README.md) · [LAB-18](../labs/lab-18-security-automation/README.md) |
| IR plan, evidence order, chain of custody, forensic timelines | M14 · [LAB-14](../labs/lab-14-ir-tabletop/README.md) · [LAB-15](../labs/lab-15-digital-forensics/README.md) |
| Malware classification, static triage, YARA/IOC handoff | M15 · [LAB-16](../labs/lab-16-malware-behavior/README.md) |
| Shared responsibility, container/IaC review | M16 · [LAB-17](../labs/lab-17-cloud-config-review/README.md) |
| Data classification, DPIA-style notes, control mapping | M17 |
| Automation, pipelines, failure modes, emerging-threat briefs | M18 · [LAB-18](../labs/lab-18-security-automation/README.md) |
| Professional reporting, evidence hygiene, self-assessment | [Assessment Guide](../assessment-guide.md) · CS-1…CS-4 · [LAB-19](../labs/lab-19-defensive-capstone/README.md) |

If you hit a step whose *technique* you cannot trace to a row above, that is a bug in this brief — cite it in your reflection; do not silently teach yourself a new tool and claim it as course work.

---

## 8. Optional extensions for advanced learners

Any two of these move a submission from Proficient toward Exemplary in the relevant dimension — but only after the core checklist is complete. All remain $0 and lab-only.

1. **Purple-team the detections:** after Stage 6, run a small authorized exercise (own lab) where each of your ≥ 4 detections is attacked *and* evaded; record which survived and tune them.
2. **Containerize the replica** (Docker/Compose), then harden and re-run Stage 3/6 evidence against the containerized version — plus a Trivy before/after.
3. **Full DPIA** for the scenario's personal data (M17 worksheet), not just the lite note — with retention schedule and control mapping across CSF 2.0 ↔ CIS v8.1.
4. **Automate the retest:** turn your Stage 6 validations into a scheduled local bot with heartbeat and degraded-mode handling (M18 failure discipline), evidence included.
5. **Peer review:** exchange Stage 5 roadmaps with another learner; review against the [rubric](rubric.md) and attach both the review you gave and the one you received.
6. **Board deck:** extend the presentation deliverable into a 10-slide executive deck with a one-page risk heat map — practice for the [portfolio spec](templates/portfolio-presentation-spec.md) audience test.
7. **Assume-breach drill:** add a mini Stage-4 annex where a *second*, undetected foothold is planted in your own replica; write the detection you would need and prove it fires.
8. **Reproducibility audit:** give your entire portfolio to a fresh folder on another machine (or a classmate) and have it rebuilt from your docs alone; log every place instructions were insufficient — then fix them.

---

## 9. Completion in one line

All seven stages' gates pass in [checklists.md](checklists.md) · rubric self-score ≥ 60% with no dimension below *Developing* and ethical practice ≥ *Proficient* ([rubric.md](rubric.md)) · portfolio matches the [portfolio spec](templates/portfolio-presentation-spec.md) · safety statements present everywhere · nothing committed anywhere except your own portfolio folder.

**Start here:** pick your scenario → [Scenarios](scenarios.md) · **Templates:** [report](templates/report-template.md) · [risk register](templates/risk-register-template.md) · [threat model](templates/threat-model-template.md) · [findings & remediation](templates/findings-remediation-template.md) · [portfolio & presentation](templates/portfolio-presentation-spec.md) · **Grade with:** [rubric](rubric.md) · **Course navigation:** [Course home](../index.md) · [M19 module](../modules/module-19-integrated-capstone-project/README.md) · [Assessment Hub](../assessments/README.md)
