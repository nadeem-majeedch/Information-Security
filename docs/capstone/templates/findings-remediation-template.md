---
title: "Capstone Template — Findings and Remediation"
layout: default
---

# Capstone Template — Findings and Remediation

**Part of:** [M19 Capstone Project](../README.md) · Copy into `portfolio/CAPSTONE/S3/findings.md` (one record per finding) and keep a one-row-per-finding tracker at the top. Gate ([G3](../checklists.md#g3--after-stage-3-configuration--control-review)): ≥ 6 findings, each with an evidence line, control-type classification, severity **+** business context, and a register link. Reporting discipline taught in [M12](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md) and [M09](../../modules/module-09-web-application-security/README.md); formats practiced in [LAB-12](../../labs/lab-12-vuln-scan-interpretation/README.md)/[LAB-10](../../labs/lab-10-web-security/README.md).

## Tracker (one row per finding)

| ID | Title | Asset | Severity | Register ID | Status | Recommendation ID |
|---|---|---|---|---|---|---|
| F-01 | | | | R- | open / fixed / accepted | REC- |

## Finding record (copy per finding)

### F-__ — *title in plain language*

- **Asset & location:** which system/element (Stage 3 inventory ID) and where (file path, endpoint, config key)
- **Category:** OWASP Top 10:2025 (if app) · CWE (if code/config) · control family (CIS/CSF) — name the taxonomy you're filing it under
- **Description:** what is wrong, in ≤ 4 sentences — factual, no adjectives
- **Evidence:** artifact + line/field or timestamped capture — e.g. `mock_s3_bucket.json → "PublicAccess": true (line 14)` · `S3-finding-01-before.png`. **Required:** this is what makes it a finding and not an opinion.
- **Validation:** exactly what you did to confirm it (command/inspection steps) — and what you did *not* do (no exploitation beyond local lab, no production contact)
- **Impact:** *technical* (what an attacker gains, from where) and *business* (data, revenue, trust, compliance — scenario-specific)
- **Severity:** score (CVSS v4.0 vector where applicable, or L×I against your register scale) **+ one line of business context** — and a note if context moves the number up or down from the raw technical score
- **Likelihood in this scenario:** is it exposed/reachable *here*? (evidence-based, not theoretical)
- **Existing controls that blunt it:** what already helps, if anything
- **Recommendation → REC-__:** concrete fix (parameterize, deny-by-default, rotate, MFA, segment, alert…) — named mechanism, not "harden"
- **Retest criteria:** what proves it fixed (exact check/command/test) and its expected result
- **Register link:** `R-__` (the gap this finding evidences)

## Recommendation record (Stage 5 tracker — one per prioritized fix)

| Field | Content |
|---|---|
| `REC-ID` | REC-01 … |
| **Recommendation** | The fix, one sentence, mechanism named |
| **Addresses findings** | F-__ , F-__ |
| **Register / risk retired** | R-__ with post-fix residual score |
| **Control type** | preventive / detective / corrective *(M02)* |
| **Effort** | S (< 2 h) / M (< 1 day) / L (multi-day) — with the one assumption the estimate rests on |
| **Priority & class** | rank 1–5 · quick-win / strategic |
| **Owner (fictional)** | role in the scenario org |
| **Validation** | how Stage 6 will prove it (before/after, test-fire, blocked-flow, fail-then-pass) |

## Rejected candidates (≥ 1 — the false-positive discipline)

| Candidate | Why it looked like a finding | Evidence that rejected it |
|---|---|---|
| | | |

## Quality bar (G3 + D3)

- [ ] ≥ 6 findings across ≥ 3 control domains; every record complete; **zero** scanner-copy findings (validation steps written out)
- [ ] Every finding links a `R-__`; every `REC-__` links findings *and* register (no orphans either direction)
- [ ] Severity = technical + business context, stated separately; ≥ 1 case where they disagree, explained
- [ ] ≥ 1 rejected candidate with deciding evidence
- [ ] All evidence references resolve from the portfolio index (paths as written)

**Back to:** [Capstone brief](../README.md) · [Report template](report-template.md) · [Risk register](risk-register-template.md)
