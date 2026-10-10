---
title: "Capstone Template — Threat Model (DFD + STRIDE)"
layout: default
---

# Capstone Template — Threat Model (DFD + STRIDE)

**Part of:** [M19 Capstone Project](../README.md) · Copy into `portfolio/CAPSTONE/S2/threat-model.md`. Gate ([G2](../checklists.md#g2--after-stage-2-assets-threats-risks)): DFD with all four element types and **≥ 2 justified trust boundaries**; **≥ 15 distinct STRIDE threats** each with L×I, treatment, mitigation. Method taught in [M11](../../modules/module-11-threat-modeling-and-security-architecture/README.md) ([LAB-02](../../labs/lab-02-threat-model-risk-register/README.md)).

## Part 1 — Data-flow diagram

**Diagram:** draw with draw.io/pen-and-paper-photo/Mermaid. Use exactly these symbols and say so in a legend:

| Symbol | Element type | Examples in your scenario |
|---|---|---|
| Rectangle | **Process** | storefront web app, API, backup job, CI pipeline |
| Parallel lines / cylinder | **Data store** | orders DB, backup share, export bucket, log store |
| Rounded box / circle | **External entity** | customer browser, payment terminal (out of scope), cloud provider |
| Arrow | **Data flow** | HTTPS session, SQL query, nightly rsync, log ship |
| Dashed line/box | **Trust boundary** | internet↔LAN, workstation↔server zone, app↔DB, org↔cloud provider |

**Trust boundaries (≥ 2 — justify each in one line):**

| # | Boundary | Why it's a boundary (privilege/ownership/network change) |
|---|---|---|
| TB1 | e.g. internet → DMZ/web tier | untrusted public input crosses into systems you operate |
| TB2 | | |

## Part 2 — STRIDE-per-element grid

Walk **every element and every boundary**; append rows until you reach **≥ 15 threats**. Keep threats *distinct* — different element or different path, not different wording.

| # | Element / boundary | STRIDE category | Threat (one sentence: actor → action → consequence) | L×I (from register) | Mitigation (control, named) | Register ID |
|---|---|---|---|---|---|---|
| T-01 | | S/T/R/I/D/E | | | | R- |
| … | | | | | | |

**Coverage checklist:** each of the six STRIDE categories appears ≥ 2× · every trust boundary has ≥ 2 threats · every process and data store appears at least once · external entities considered.

## Part 3 — Attack-path narratives (2–3 chains)

*Threat tables are static; attacks are sequences.* For each chain: `entry → pivot → objective`, naming the elements crossed and the boundary violated, and which register risks it realizes.

> *Example shape:* "Internet → storefront login (no rate limit, T1110) → valid customer session (S) → IDOR on record API (E) → cross-tenant data read (I) — realizes R-07, R-11."

## Part 4 — Zero-trust check (short)

Three lines: (1) how each request is authenticated/authorized today; (2) where least privilege fails; (3) what "assume breach" changes about your monitoring plan. *(M11's three tenets — one sentence each.)*

## Part 5 — Abuse cases (≥ 3 for auth-adjacent flows)

| # | Abuse case (attacker goal + trick) | Design change it forces | Where implemented/validated |
|---|---|---|---|
| AC-1 | | | |

## Quality bar (G2)

- [ ] All four element types present; ≥ 2 boundaries justified (not just drawn)
- [ ] ≥ 15 distinct threats, every row complete, each linked to a register ID
- [ ] All six STRIDE categories covered ≥ 2×; facts/inferences honest (unknowns marked)
- [ ] ≥ 2 attack-path narratives; ≥ 3 abuse cases; zero-trust check present
- [ ] L×I values match the [risk register](risk-register-template.md) exactly (one source of truth)

**Back to:** [Capstone brief](../README.md) · [Risk-register template](risk-register-template.md)
