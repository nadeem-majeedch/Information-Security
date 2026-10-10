---
title: "Practical Lab Challenges (LC-1 – LC-4)"
layout: default
---

# Practical Lab Challenges (LC-1 – LC-4)

**Type:** Practical lab challenges with defined deliverables · **Tools:** free/lab-only · **Grading:** each challenge scored with the published [Lab Portfolio Rubric](../../assessment-guide.md#51-lab-portfolio-rubric-applies-to-each-pack-in-component-c) (≥ 3 = pass) unless noted

These four challenges sit at the end of each level. They are *integrations* of the level's labs — bigger than any single lab pack, but built entirely from skills you already practiced. Each states **deliverables** (what you hand yourself to grade) and **evaluation criteria** (how you decide it passed).

> **Safety gate:** every challenge inherits the [Lab Safety Policy](../../lab-safety-policy.md). Isolated lab systems only, synthetic data only, written authorization for your own scope. Work missing its safety statement is not gradeable — same rule as the rest of the course.

---

## LC-1 — Endpoint to Perimeter (L1)

**Spans:** M01–M05 · **Ties to:** [LAB-01](../../labs/lab-01-cia-case-analysis/README.md) · [LAB-04](../../labs/lab-04-permissions-hardening/README.md) · [LAB-08](../../labs/lab-08-firewall-config-audit/README.md)

**The challenge.** Take one fresh VM (Linux or Windows) from *default install* to a defensible baseline, then prove your perimeter logic with connectivity tests — and defend every decision in writing as if to a skeptical manager.

**Deliverables:**
1. **CIA asset inventory** for the host: 10+ assets/services classified with CIA impact ratings and one-line justifications.
2. **Hardening log:** ≥ 15 hardening steps (accounts, sudo/admin rights, firewall, updates, unused services, SSH/server config), each with **before → command → after** evidence.
3. **Firewall rule table** (host-based): rules with a justification column, deny-by-default, plus **blocked-flow and allowed-flow test evidence** for at least three flows.
4. **Risk note (1 page):** the three residual risks you accepted after hardening, each with likelihood × impact and treatment (mitigate/accept/transfer).
5. **Safety statement:** targets, isolation method, dates.

**Evaluation criteria:**
- Every hardening entry shows a *state change*, not just a command (screenshot or log proving before ≠ after).
- Firewall includes demonstrated **blocked** flows — an allow-only test set scores "Developing."
- Justifications reference control types (preventive/detective/corrective) correctly.
- Rubric ≥ 3 on all four criteria (technical correctness, evidence, safety, reflection).

---

## LC-2 — Identity and Web (L2)

**Spans:** M06–M11 · **Ties to:** [LAB-06](../../labs/lab-06-auth-access-control/README.md) · [LAB-09](../../labs/lab-09-secure-coding/README.md) · [LAB-10](../../labs/lab-10-web-security/README.md) · [LAB-11](../../labs/lab-11-headers-tls-analysis/README.md)

**The challenge.** Ship a small internal web service that is *correctly identified, correctly authorized, and honestly tested* — then break your own work on purpose and document what it took.

**Deliverables:**
1. **IAM design note:** roles/permission matrix for a 5-person team, least-privilege rationale, MFA policy with recovery-path risk, one separation-of-duties rule.
2. **Working service:** a locally hosted app with login, per-role authorization (server-side, deny-by-default), TLS (locally-generated cert acceptable), and security headers — with config evidence.
3. **Crypto/credential evidence:** password storage with a memory-hard hash + salt (commands/output), and one signed or encrypted artifact from your lab notebook (OpenSSL/GnuPG).
4. **Self-assessment report:** ≥ 5 findings against your own service (different OWASP categories), each with steps, evidence, impact, severity attempt, fix — plus one IDOR/access-control test that *fails closed*.
5. **CI gate:** the M10 pipeline (SAST + secrets + dependency audit) wired to your service repo, with **red log → fix → green log** evidence.
6. **Threat model excerpt:** DFD with ≥ 2 trust boundaries + 10 threats with mitigations (scaled from M11's 15 — the capstone demands 15).
7. **Safety statement.**

**Evaluation criteria:**
- Authorization is proven by a *denied* request (per role), not only by allowed ones.
- Findings are your own captured evidence — scanner-only lines score "Developing."
- The pipeline genuinely fails on a planted issue (log shows the rule/line).
- Rubric ≥ 3 on all four criteria.

---

## LC-3 — Detect and Respond (L3)

**Spans:** M12–M15 · **Ties to:** [LAB-12](../../labs/lab-12-vuln-scan-interpretation/README.md) · [LAB-13](../../labs/lab-13-log-analysis/README.md) · [LAB-14](../../labs/lab-14-ir-tabletop/README.md) · [LAB-15](../../labs/lab-15-digital-forensics/README.md) · [LAB-16](../../labs/lab-16-malware-behavior/README.md)

**The challenge.** Run the full defensive loop on your isolated lab: **assess → detect → triage → respond → document** — as one continuous engagement with one continuous paper trail.

**Deliverables:**
1. **Rules of engagement** for your lab scope (targets, window, exclusions, **stop conditions**).
2. **Assessment report:** ≥ 6 validated findings (scanner + manual validation evidence), severity with CVSS vector + business context, remediation roadmap, retest plan. Include one documented false positive *and* its validation proof.
3. **Detection pack:** ≥ 6 rules (Sigma-style) mapped to ATT&CK, each **triggered in-lab** with captured alert evidence.
4. **Triage worksheet:** ≥ 5 alerts with verdict/severity/action — including at least one "expected-benign by context" justified from your RoE.
5. **IR + forensic timeline:** from the synthetic evidence bundle: hash verification, collection order documented, a chronological timeline answering 5 investigation questions with artifact citations, and a chain-of-custody form.
6. **Malware triage (benign training binaries only):** static + dynamic analysis, 3 YARA rules with FP test results, IOC package (CSV or STIX-lite) handed into your detection pack.
7. **One-paragraph incident summary** written for a non-technical owner (M14 comms practice).
8. **Safety statement** (sandbox isolation details required for this challenge).

**Evaluation criteria:**
- Traceability: every finding/alert line cites a recorded artifact.
- Volatile-first collection order is documented and followed.
- YARA/Sigma rules include tested false-positive behavior (with the test output).
- Investigation rubric ≥ 60/100 applies to the report portion ([§5.3](../../assessment-guide.md#53-investigation-rubric-component-d-per-report-100-points)); portfolio rubric ≥ 3 for the rest.

---

## LC-4 — Secure the Stack (L4)

**Spans:** M16–M18 · **Ties to:** [LAB-17](../../labs/lab-17-cloud-config-review/README.md) · [LAB-18](../../labs/lab-18-security-automation/README.md) · [LAB-19](../../labs/lab-19-defensive-capstone/README.md)

**The challenge.** Harden a cloud-style stack (provider free tier **you own**, or local emulation), decide a real privacy question in writing, and automate your hygiene *without building a bot that can hurt you*.

**Deliverables:**
1. **Container hardening evidence:** vulnerable image → hardened derivative (non-root, no baked secrets, no privileged, limits, read-only where feasible) with **Trivy before/after** reports.
2. **IaC audit:** the provided Compose/Terraform config reviewed — 8 issues identified, fixed, rescanned (tool output as evidence), prioritized by risk with one-line justifications.
3. **Shared-responsibility worksheet:** 10 scenarios assigned provider/customer/shared with the customer-side control named.
4. **DPIA or control-mapping artifact:** full DPIA for a provided scenario *or* 15 controls mapped CSF 2.0 ↔ CIS v8.1 with gaps flagged (one of the two; both for distinction).
5. **Automation bot:** the M18 hygiene bot end-to-end — script, schedule, report, alert — **plus failure-path evidence**: killed-run heartbeat fires, transient-failure retry/backoff behaves, exit codes correct.
6. **Automation guardrail note (1 page):** for your bot, the auto-vs-human action split, exclusions policy (owner + expiry), and the failure mode you most need to watch.
7. **Emerging-threat brief:** 600–800 words, ≥ 3 credible sources, small-org implications, 3 layered controls.
8. **Safety statement** (including: no real tenant/PII data, key handling for any free-tier account).

**Evaluation criteria:**
- Scan evidence shows *improvement*, not just a scan having run.
- The bot's failure handling is demonstrated live (heartbeat/retry/exit-code), not described.
- The brief is source-backed and non-hype; recommendations are executable by a ≤15-person org.
- Rubric ≥ 3 on all four criteria.

---

## How to grade your own challenge

1. Read the **evaluation criteria** before you start — they are the acceptance tests.
2. Assemble deliverables in your `portfolio/` folder under `LC-1/` … `LC-4/` with an index.
3. Score each against the [Lab Portfolio Rubric](../../assessment-guide.md#51-lab-portfolio-rubric-applies-to-each-pack-in-component-c) (technical correctness · evidence quality · safety compliance · reflection). ≥ 3 on all four = pass; below, use the fix-list loop from [§6](../../assessment-guide.md#6-resubmission-and-reassessment-policy).
4. LC-3's report component additionally meets the [Investigation Rubric](../../assessment-guide.md#53-investigation-rubric-component-d-per-report-100-points) ≥ 60/100.

**Next:** [CAP-ADV — Advanced Final Assessment](advanced-final.md) · **Back to:** [Assessment Hub](../README.md)
