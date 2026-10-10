---
title: "LAB-17 — Cloud Security Configuration Review (Mock Configs)"
layout: default
---

# LAB-17 — Cloud Security Configuration Review (Mock Configs)

**Lab ID:** LAB-17 · **Difficulty:** Intermediate · **Estimated duration:** 2 hours · **Module:** M16 · **Mode:** Static review of mock configurations (**no cloud account required**)

## Scenario

**Sunrise Media** (fictional) moved its asset archive to "the cloud" and asks you for a configuration review before the marketing push. There is no live account to touch — instead, their architect has exported the **two configurations** below (object-storage bucket + identity policy), each with seeded issues. You will review them like a professional: checklist-driven findings, severity, exploitability narrative (how an attacker would actually use each flaw), fixes, and a re-review pass — exactly the workflow of cloud configuration assessment, minus the vendor.

## Learning Objectives

1. Map mock object-storage and identity-policy configurations against a CIS-derived hardening checklist.
2. Identify ≥ 8 seeded misconfigurations and rate each by exploitability and impact.
3. Write findings in professional form: evidence (config line), attack narrative, remediation, priority.
4. Distinguish *preventive* configuration fixes from *detective* monitoring gaps (M02 types).
5. Perform a re-review (before/after) with a corrected configuration — proving remediation.

## Prerequisites and Required Skills

- M16 module (shared responsibility, container/config security, CIS concepts), M02 (risk language).
- Skills: reading JSON; conceptual understanding of object storage and IAM-style policies. No provider account or CLI needed.

## Tools, Operating Systems, and Versions

- Provided configs: [`data/mock_s3_bucket.json`](./data/mock_s3_bucket.json) and [`data/mock_iam_policy.json`](./data/mock_iam_policy.json) (synthetic; not attached to any real account).
- Any editor; `python3 -m json.tool <file>` to validate your *fixed* JSON (what it does: parses and pretty-prints — syntax errors block your remediation, so check it).
- Optional reference: CIS Benchmarks (free with registration) for a real benchmark to cite beyond the course checklist.

**$0.** No cloud sign-up, no CLI keys, no API calls.

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-17/`; copy the two JSON files (originals untouched — work on `*-fixed.json` copies).
2. No accounts, credentials, or network access required. Scope statement: *static analysis of course-provided mock configurations on my machine.*
3. Review checklist (course-provided, CIS-derived — use it as your backbone):

   ```
   Object storage:  public access fully blocked (all four block settings true) · no public ACL grants
                    · versioning on for prod · server-side encryption on · access logging to a
                    separate location · MFA-delete for prod buckets · least-privilege bucket policy
   Identity:        no wildcard Action+Resource · no permissions granted without MFA condition for
                    sensitive ops · no long-lived keys without justification · named statements
                    scoped per team/function · explicit Deny guards where relevant
   ```

## Lab Environment and Starting State

Two JSON files with seeded issues (bucket: public exposure, suspended versioning, no encryption, no logging, no MFA-delete; policy: full-wildcard statement, contractor over-permission, an MFA condition used *backwards*). Starting state: no findings, no fixes.

## Tasks

1. **Line-by-line review:** annotate both files (line-numbered notes in `review-annotations.md`): every setting = *OK / Issue / Question for the architect*. "Question" is legitimate output (missing information is a finding class of its own).
2. **Findings report:** produce ≥ 8 findings, each: *ID, title, config evidence (quote + line), attack narrative (2 sentences: who exploits, how, what they get), impact (CIA + business), remediation (exact config change), priority (P1/P2/P3) + rationale*. At minimum, cover:
   - F1: Public ACL grant + all four `block_*` flags false = **world-readable bucket** (narrative: anonymous listing/download of "corp-documents-archive" — think contracts).
   - F2: Logging disabled = undetectable access (detective gap — M02 type).
   - F3: Encryption off = plaintext at rest; contrast: encryption ≠ access control (don't oversell the fix).
   - F4: Versioning suspended + no MFA-delete = ransomware/deletion fragility (availability + tamper recovery).
   - F5: `LegacyFullAccess` statement (`Action: *`, `Resource: *`) = total compromise of the identity — the highest-priority policy flaw.
   - F6: Contractor statement over-broad (`DeleteObject` for a read-mostly role? scope + business justification questions).
   - F7: `AdminsWithoutMFA` statement — the condition `MultiFactorAuthPresent: false` *grants* the permission when MFA is absent (read conditions carefully; this is the "logic inversion" trap).
   - F8: Missing safeguards not present in config at all (no key-rotation statement, no region restriction) — *absent-control* findings.
3. **Exploitability ordering:** rank all findings by "how an attacker gets value" (wildcard identity + public bucket = trivially chained) — then explain why CVSS-style scoring doesn't translate directly to cloud config (M02's CVSS-vs-risk lesson, new domain).
4. **Remediate:** produce `mock_s3_bucket-fixed.json` and `mock_iam_policy-fixed.json`: every finding addressed (or explicitly accepted with justification comment). Validate both with `python3 -m json.tool`.
5. **Re-review pass:** re-run your checklist against the *fixed* files; write the before/after verdict table (finding → status Fixed/Accepted) — the deliverable's proof section.
6. **Monitoring gap note:** the configs say nothing about *alerting* (e.g., "alert on public-access changes" or "on any `*` policy"). Write the 5-line detective-control addendum the architect needs — separating configuration (preventive) from monitoring (detective).
7. **Executive summary:** 5 sentences a non-technical manager would act on (money/risk language, top fix, effort estimate).

## Expected Observations

| Seeded issue | Expected verdict |
|---|---|
| Public ACL + four false `block_*` flags | **P1** — anonymous read of production archives; trivially exploitable, total confidentiality impact for the bucket's contents |
| `Action: *` / `Resource: *` statement | **P1** — full identity takeover path; the single worst line in either file |
| MFA condition "false" | **P1/P2** — condition logic *permits* the op precisely when MFA is off; catching this separates careful reviewers |
| No logging | **P2** — no detection or forensic trail; cheap to fix, expensive to miss |
| Encryption off | **P2** — meaningful for stolen-media scenarios; pair with access fix (encryption doesn't stop a public GET) |
| Suspended versioning + no MFA-delete | **P2** — recovery/deletion-resilience gap (ransomware-adjacent, M05 lesson ported to cloud) |
| Over-broad contractor actions | **P3** — least-privilege violation; needs business question, not just a config edit |
| Absent controls (rotation/region) | documented as **absent-control** findings with recommendations |

Chaining insight to state explicitly: *public bucket + wildcard identity* converts "bad config" into "company-wide breach in two API calls."

## Investigation Questions

1. Shared responsibility: which of your findings live on the *customer* side of the model for IaaS object storage, and what does the provider guarantee instead? (One paragraph — M16 core concept.)
2. The bucket holds "archives" — versioning-on + MFA-delete changes what cost? Is it justified for prod? (Business trade-off reasoning.)
3. Encryption-at-rest disabled: construct the *realistic* threat it exposes (provider media disposal, stolen snapshot) versus the threat it doesn't (a public GET today) — precise control-to-threat mapping.
4. The contractor statement: what three questions do you ask the business *before* trimming it (data volume? break-glass need? audit requirement?) — process before config.
5. If you could add exactly one **detective** control to this account, which and why? (Defend against the wildcard identity's blast radius.)

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| "Fixed" JSON won't parse | Trailing commas / quote slips | `python3 -m json.tool file` names the error line — fix, re-validate |
| Finding count < 8 | Stopping at obvious ones | Absent-control findings (what *should* exist and doesn't) count — re-read the checklist line by line |
| Tempted to spin up a real free-tier account to "see it live" | Scope creep + key handling risk | Unnecessary — this lab is deliberately accountless; do the optional challenge in LAB-19 instead |
| Unsure if a finding is real (mock vs provider behavior) | Mocks simplify | Your "Question for the architect" category exists for this — mark it and reason conditionally |
| MFA-condition finding missed | Skimmed the `Condition` block | Re-read Task 2 F7 — conditions invert intent when copy-pasted badly; verify semantics carefully |

## Evidence to Collect

- `review-annotations.md` (line-level notes incl. "Question" items).
- `findings-report.md` (≥ 8 findings, all fields, with quoted config evidence).
- `*-fixed.json` (validated) + re-review verdict table.
- `monitoring-addendum.md` (5 lines) + `executive-summary.md` (5 sentences).
- Safety statement: *static review of synthetic configs; no cloud account, keys, or API calls involved.*

## Deliverable and Report Structure

`portfolio/LAB-17/`: (1) scope + checklist used, (2) findings report, (3) exploitability ordering + risk-language note, (4) fixed configs + validation output, (5) before/after verdict table, (6) monitoring addendum, (7) executive summary, (8) safety statement. 2–3 pages.

## Completion Checklist

- [ ] Both configs annotated line-by-line (OK/Issue/Question)
- [ ] ≥ 8 findings; every seeded issue caught (incl. the inverted MFA condition)
- [ ] Each finding has quoted evidence, attack narrative, impact, exact fix, priority
- [ ] Findings ranked by exploitability with the chaining insight stated
- [ ] Fixed JSONs parse cleanly (`python3 -m json.tool`)
- [ ] Re-review verdict table (Fixed/Accepted per finding)
- [ ] Detective-control addendum + 5-sentence executive summary
- [ ] Safety statement written

## Cleanup and Reset

1. Nothing executed — no cloud resources exist to delete; no keys were ever handled.
2. Consolidate into `portfolio/LAB-17/`; keep fixed configs as portfolio evidence.
3. If you *chose* the optional free-tier challenge later (LAB-19), remember its separate safety notes: never paste real keys into files or commits (LAB-18's secret scanning covers this).

## Optional Challenges

- Find a third-party free config linter (e.g., Checkov/TFLint — free, local) and run it on your *fixed* files where format allows; compare its findings to yours (tool-vs-human, echoing LAB-09).
- Convert the wildcard statement into least-privilege: enumerate the 5 actions the legacy app *actually needs* and write the narrowed statement.
- Write the S3-bucket policy snippet (as JSON) that would *deny* any non-TLS access — then explain which threat it adds to your defenses (in-transit protection).

## References and Safety Notes

- CIS Benchmarks (free registration): <https://www.cisecurity.org/cis-benchmarks> — cloud foundations benchmarks exist for major providers; the course checklist is a portable subset.
- NIST SP 800-207 (*Zero Trust Architecture*) for identity-first reasoning: <https://csrc.nist.gov/pubs/sp/800/207/final>.
- NIST CSF 2.0 (Identify/Protect functions): <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final>.
- Course: [M16](../../modules/module-16-cloud-and-infrastructure-security/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** mock configurations only — no provider account, no credentials, no API traffic; nothing in this lab can affect a real cloud resource (Safety Policy §2/§5). If you later practice on your *own* free-tier account, treat real keys as secrets: never in files, screenshots, or commits.

**Navigation:** · [← Previous: LAB-16](../lab-16-malware-behavior/README.md) · [Lab index](../README.md) · [Next: LAB-18 →](../lab-18-security-automation/README.md)
