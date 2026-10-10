---
title: "Capstone Template — Risk Register"
layout: default
---

# Capstone Template — Risk Register

**Part of:** [M19 Capstone Project](../README.md) · Copy into `portfolio/CAPSTONE/S2/risk-register.csv` (working file) and paste the summary into the [report §5](report-template.md). A register entry with an empty treatment or rationale is an unfinished entry — the gate at [G2](../checklists.md#g2--after-stage-2-assets-threats-risks) fails.

## Columns

| # | Column | What goes in it |
|---|---|---|
| 1 | `risk_id` | `R-01`, `R-02`, … — stable; findings and recommendations reference this |
| 2 | `asset` | The Stage 3 inventory asset this risk lands on |
| 3 | `threat_scenario` | One sentence: *who/what, acting on which vulnerability, producing which consequence* (a threat, a vuln, and an impact — all three, or it's not a risk) |
| 4 | `stride` | S / T / R / I / D / E (primary category; M11 taught the mapping) |
| 5 | `existing_controls` | What already mitigates it (from evidence — cite the artifact) or `none observed` |
| 6 | `likelihood` | 1–5 against your **defined scale** (write the scale below the table) |
| 7 | `impact` | 1–5 against your defined scale |
| 8 | `score` | L × I (state if you use a different formula) |
| 9 | `treatment` | `mitigate` / `transfer` / `accept` / `avoid` |
| 10 | `rationale` | One line: *why this treatment* — including why not the alternatives |
| 11 | `planned_controls` | The specific controls (or `none` for accept/avoid) — link to recommendation IDs in Stage 5 |
| 12 | `residual` | Post-treatment L×I **or** `n/a` if fully eliminated; one-line residual statement for every accepted/deferred risk (owner + revisit trigger) |
| 13 | `evidence_ref` | Artifact + line/field backing entries 3 and 5 |

## Scale definition (required — paste yours here)

*Likelihood (L): 5 = … 4 = … 3 = … 2 = … 1 = …*
*Impact (I): 5 = … 4 = … 3 = … 2 = … 1 = …*
*(M02 taught scales; they must be written down or the numbers are decoration.)*

## Worked example row (synthetic — replace with your own)

| risk_id | asset | threat_scenario | stride | existing_controls | L | I | score | treatment | rationale | planned_controls | residual | evidence_ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-04 | `shop01` backup share | An attacker with a single valid credential reads and encrypts the nightly backups, destroying recovery options | I (integrity/availability) | NAS on internal LAN; nightly job runs (schedule observed) | 4 | 5 | 20 | mitigate | Can't avoid (backups are required) or transfer meaningfully; cheap fix exists | R-02: offline/immutable second copy + quarterly restore test | L3×I5=15 until first successful restore test (owner: *you*, revisit: test date) | `syslog-sample.log` lines showing nightly job; NAS config screenshot `S3-finding-03-*` |

## Quality bar (G2)

- [ ] ≥ 12 rows for a scenario (15+ threats modeled; related ones may share a row only if the *scenario sentence* is genuinely the same)
- [ ] No two rows are rephrasings of one another — distinct elements or distinct paths
- [ ] Every row: all 13 columns filled (use `none observed`/`n/a` deliberately, never blank)
- [ ] Scales defined; at least one row where business context changes the naive technical ranking (say so in the rationale)
- [ ] Accepted risks have residual statements with owner + revisit trigger
- [ ] `risk_id` cross-referenced from [findings](findings-remediation-template.md) and the [roadmap §9](report-template.md)

**Back to:** [Capstone brief](../README.md) · [Threat-model template](threat-model-template.md)
