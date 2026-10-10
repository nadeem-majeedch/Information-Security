---
title: "LAB-02 — Threat Modeling and Risk Register Preparation"
layout: default
---

# LAB-02 — Threat Modeling and Risk Register Preparation

**Lab ID:** LAB-02 · **Difficulty:** Intermediate · **Estimated duration:** 3 hours · **Modules:** M02, M11 · **Mode:** Analysis + diagramming (no network activity)

## Scenario

**CampusEats** is a 10-person startup running a food-delivery web app for one university: customers order from canteen vendors, riders pick up, payments are settled weekly. Engineering asks you to threat-model the system *before* the next release and to produce the company's first real risk register. You get the architecture description below — no access to their infrastructure (none exists yet; this is a design-time exercise).

> **System description:** A React web app and a mobile app talk over HTTPS to an API server (Linux, cloud VM). The API uses a PostgreSQL database (orders, customers, card tokens). A third-party payment provider is called server-side. Riders get a GPS ping per order and a 6-digit pickup code. An admin panel (same API, staff accounts) manages vendors. Weekly settlement runs as a batch job with a service account.

## Learning Objectives

1. Build a data-flow diagram (DFD) with processes, data stores, data flows, external entities, and **trust boundaries**.
2. Apply STRIDE to every DFD element and elicit ≥ 15 distinct threats.
3. Prioritize threats into a scored risk register (likelihood × impact) with treatments and residual risk.
4. Justify control choices using CSF 2.0 functions and CIS v8.1-style safeguards.

## Prerequisites and Required Skills

- Modules 02 and 11 (risk scoring, STRIDE, DFD basics). Lab 01 recommended.
- Skills: diagramming (draw.io/diagrams.net free, or pen-and-paper photo), table writing.

## Tools, Operating Systems, and Versions

- diagrams.net (free, browser) or paper; any editor. Optional: Mermaid in a Markdown viewer. **$0.**

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-02/`.
2. No systems, accounts, or authorization needed — design-time analysis only.

## Lab Environment and Starting State

Self-contained scenario above + a starter DFD sketch to complete:

```text
 [Customer app] ──HTTPS──►  (1) Web/API     ──► (2) PostgreSQL
                              │  ▲                 (orders, customers,
 [Rider app]   ──HTTPS──►     │  │                   card tokens)
                              │  │
 [Payment provider] ◄─────────┘  │
    (external)          (3) Settlement job ──reads──► (2)
                            (service account)
 [Admin panel] ──HTTPS──► (1)
```

Starting state: unnumbered boundaries, no threats, no register.

## Tasks

1. **Complete the DFD:** redraw with five element types clearly distinguished (external entity = rectangle, process = circle, data store = cylinder, flow = arrow, trust boundary = dashed line). Place at least **three** trust boundaries (internet↔API, API↔DB, settlement job↔DB/service account — justify any you add).
2. **STRIDE pass:** table with columns *DFD element | STRIDE category | Threat (one sentence) | Attacker goal*. Cover every process and store; ≥ 15 rows. Include at least: spoofing a rider, tampering with an order price, repudiating a settlement, information disclosure of card tokens, denial of service on checkout, elevation of privilege in the admin panel.
3. **Score:** add Likelihood (1–5), Impact (1–5), Score, Band (M02 bands) per row; sort descending.
4. **Treat:** for the top 8, choose treatment (mitigate/avoid/transfer/accept), 1–2 concrete controls each (map to a CSF function), and record **residual risk**.
5. **Coverage check:** confirm every STRIDE category appears at least once; note any element you deliberately excluded and why.
6. **Memo:** 10 sentences to CampusEats leadership: top 3 risks, the single control you would fund first, and one *design change* (not a product) that removes a threat entirely — e.g., never storing card data yourself.

## Expected Observations

- Spoofing concentrates on identities (rider/customer/admin/service account); repudiation on the settlement job (no human in the loop); information disclosure on the DB and payment path.
- At least one high-score risk should be **design-level** (card tokens in DB; admin panel sharing the public API) — fixing design beats bolting on controls (a core M11 lesson).
- DoS on checkout scores high-likelihood/high-impact for a delivery app during lunch peak — discussion point about availability investment.
- A control like "MFA for admins" is preventive/administrative; "hash API audit logs" is detective/technical — expect a healthy mix.

## Investigation Questions

1. Which threat disappears completely if payment card handling is fully delegated (tokens only, no PAN stored)? Which new threat appears (provider compromise)?
2. Why is the settlement service account a bigger prize than one admin account? Use least-privilege language.
3. Where does STRIDE *not* fit well (which element drew forced threats)? What does that teach about framework limits?
4. Your top risk and CISA/NVD evidence: would a KEV-listed CVE change its likelihood? (Reason; no lookups required.)
5. Which two threats need the *vendor* (payment provider) rather than CampusEats to fix? How is that documented (contract/SLA — M02 "transfer")?

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| DFD has 20 boxes | Everything drawn as one "system" | Split processes from stores; if you can't name the data it handles, it's a process, not a blob |
| Threats all "hacker attacks website" | No STRIDE discipline | One row per element per category; ask "what would *spoofing this element* mean?" |
| All scores 12–15 | Impact not tied to business | Re-rate through CIA harm to CampusEats (orders, money, trust) |
| Register without residual risk | Stopped at "we'll add a firewall" | Every mitigated row keeps a residual line — controls reduce, never eliminate |

## Evidence to Collect

- `dfd.png` (or photo) — element types visually distinct, boundaries labeled.
- `stride-table.md` — ≥ 15 rows, all six categories covered.
- `risk-register.md` — scored, sorted, top 8 with treatment/controls/residual.
- `memo.md` — leadership summary.
- Safety statement: *no systems touched; design-time analysis.*

## Deliverable and Report Structure

`portfolio/LAB-02/`: DFD → STRIDE table → risk register → memo (in that order), each with a one-line header (system, version, date, author). This mirrors professional threat-model documents; the capstone (M19 Stage A) reuses this exact structure.

## Completion Checklist

- [ ] DFD with all five element types and ≥ 3 justified trust boundaries
- [ ] STRIDE table ≥ 15 threats, all six categories present
- [ ] Risks scored (L×I), banded, sorted
- [ ] Top 8 have treatment + controls (CSF-mapped) + residual risk
- [ ] Leadership memo ≤ 10 sentences with one funded control and one design change
- [ ] Safety statement written

## Cleanup and Reset

1. Nothing executed; no systems to restore.
2. Keep artifacts in `portfolio/LAB-02/`; delete scratch files.
3. If you used diagrams.net local storage, export a PNG into the portfolio so it survives browser cache clears.

## Optional Challenges

- Model the same system a year later: a new "family account" sharing feature appears — what new threats enter the table?
- Add a fourth boundary (corporate VPN→admin panel) and re-run STRIDE on it only.
- Convert your top-3 register rows into M01-style policy clauses (M03 practice).

## References and Safety Notes

- NIST SP 800-154, *Guide to Data-Centric System Threat Modeling*: <https://csrc.nist.gov/pubs/sp/800/154/ipd>.
- Microsoft STRIDE model overview: <https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling>.
- NIST SP 800-207, *Zero Trust Architecture* (for boundary thinking): <https://csrc.nist.gov/pubs/sp/800/207/final>.
- Course: [M02](../../modules/module-02-threats-vulnerabilities-risk-and-controls/README.md) · [M11](../../modules/module-11-threat-modeling-and-security-architecture/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** purely analytical; no CampusEats-like system may be probed — if you later test anything real, it needs written authorization first (Safety Policy §3).

**Navigation:** · [← Previous: LAB-01](../lab-01-cia-case-analysis/README.md) · [Lab index](../README.md) · [Next: LAB-03 →](../lab-03-password-hashes/README.md)
