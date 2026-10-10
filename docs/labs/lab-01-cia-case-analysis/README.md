---
title: "LAB-01 — CIA Triad Analysis of Organization Case Studies"
layout: default
---

# LAB-01 — CIA Triad Analysis of Organization Case Studies

**Lab ID:** LAB-01 · **Difficulty:** Introductory · **Estimated duration:** 1.5–2 hours · **Module:** M01 · **Mode:** Analysis (no tools, no network activity)

## Scenario

You are a newly hired security analyst at **GreenField Logistics**, a 60-person delivery company. After three incidents in one quarter, management asks you to classify what actually went wrong *before* anyone buys technology. You will analyze three provided cases (below) using the CIA triad vocabulary from Module 01 and produce a one-page prioritization memo. Context: mixed office/warehouse IT, a small public website, customer addresses in a CRM, and a warehouse barcode system.

## Learning Objectives

1. Classify incident impacts as confidentiality, integrity, or availability failures — including cases where more than one pillar fails.
2. Separate the *threat*, *vulnerability*, *risk*, and *control* elements inside a narrative.
3. Rate impact (Low/Moderate/High) per pillar with justification tied to business harm.
4. Recommend one preventive and one detective control per case and justify the ordering.
5. Communicate findings as a professional one-page memo.

## Prerequisites and Required Skills

- Module 01 completed (CIA vocabulary, threat/vulnerability/risk/control).
- Skills: careful reading, table writing in any editor. No technical tooling.

## Tools, Operating Systems, and Versions

- Any text/Markdown editor (VS Code, Notepad++, or paper). No version requirements; zero cost.

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-01/` in your course folder.
2. No systems are touched — no authorization, accounts, or network access needed.
3. Permission needed: only your own time. (Safety statement for this lab: *no targets, analysis only*.)

## Lab Environment and Starting State

A clean portfolio folder plus the three synthetic case files below (inlined here so the lab is self-contained). Starting state: no analysis performed.

> **Case A — "The Open Bucket":** The marketing intern uploads campaign files to cloud storage using a shared account. One folder holding the customer CRM export (names, phones, addresses of 12,000 customers) has permissions set to "public on the internet." Unknown parties download it. The company learns of it from a journalist, not from its own tools.
>
> **Case B — "The Tampered Invoice":** A warehouse PC is infected with commodity malware. attackers do not steal data; they modify three delivery invoices in the accounting system from $1,400 to $14,000, routed to a supplier-looking bank account. Two payments go out before anyone compares invoices to delivery records.
>
> **Case C — "Friday Blackout":** The warehouse barcode system dies at 04:00 on Black Friday. Cause: the single server ran an unpatched database for 19 months; an automatic data-import job consumed all disk. No backup had been *restored* in two years; restore attempts fail. Shipping stops for 26 hours; penalties and lost contracts follow.

## Tasks

1. **Per case, fill a CIA matrix:** rows = Confidentiality / Integrity / Availability; columns = *Failed? (Y/N)*, *Evidence from the narrative*, *Impact rating (L/M/H)*, *Business harm in one sentence*.
2. **Element extraction:** for each case, list one threat, one vulnerability, the resulting risk (one sentence), and one control that was missing.
3. **Detection gap:** for each case, state why the organization learned of the problem late (Case A: journalist; Case B: reconciliation; Case C: crash). Name the detective control that would have shortened detection.
4. **Prioritization:** rank the three cases by residual business risk to GreenField *as described* (not by technical severity) and write a 4–6 sentence memo to management: what to fix first, why, and which pillar dominates each.
5. **Control pairing:** for your top-priority case, recommend exactly one preventive and one detective control, each tagged technical/administrative/physical (Module 02 vocabulary preview).

## Expected Observations

- **Case A:** Confidentiality **and** availability-adjacent governance failure; detection came from outside (no monitoring). *Key insight: no malware was needed — a permissions/process gap sufficed.*
- **Case B:** Primarily **integrity** (data altered) with a fraud outcome; confidentiality unaffected. *Key insight: "nothing was stolen" does not mean "no breach of trust."*
- **Case C:** **Availability** dominant, with integrity secondary (unverified restore) and confidentiality unaffected. *Key insight: the vulnerability was a missing process (patching + tested backups), not an exotic exploit.*
- Most learners initially mark only one pillar per case; Cases A and C each legitimately touch two.

## Investigation Questions

1. Which case would you report to GreenField's board first, and how does your answer change if the company has cyber insurance (transfer treatment)? Defend with impact reasoning.
2. In Case A, why is "the intern made a mistake" an incomplete vulnerability statement? What systemic control prevents the *next* intern's mistake?
3. Case C's backup "existed but failed." Which M01/Module 05 concept was missing, and what single sentence in the policy would have caught it during review?
4. Where does authenticity/non-repudiation appear in Case B? What evidence would prove *who* approved the payment?
5. For one case of your choice, identify a control that would have *prevented* vs one that would have *detected* — and why detective controls alone are insufficient for Case B.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| "All three cases are all three pillars" | Rating everything = prioritizing nothing | Only mark a pillar **failed** if the narrative shows loss/breach/outage of *that* property; justify with a quote |
| Impact ratings all "High" | Rating worst-possible, not worst-*realistic* | Use the M01 CIA procedure: what actually follows for this business? |
| Memo keeps growing past a page | You're writing analysis, not decisions | Lead with the ranking; details go in the matrices |

## Evidence to Collect

- `cia-matrix.md` — three matrices (one per case), fully filled.
- `elements.md` — threat/vulnerability/risk/control extraction per case.
- `memo.md` — the one-page prioritization memo (ranking + rationale + control picks).
- Safety statement line: *targets = none; analysis only.*

## Deliverable and Report Structure

`portfolio/LAB-01/` containing: (1) title line + course/module/date, (2) executive summary ≤ 6 sentences, (3) three CIA matrices, (4) element table, (5) prioritized recommendations with pillar tags, (6) safety statement. Length target: 1–2 pages.

## Completion Checklist

- [ ] Three CIA matrices complete with evidence quotes and L/M/H ratings
- [ ] Threat/vulnerability/risk/control extracted for each case
- [ ] Detection gap identified for each case with a named detective control
- [ ] Cases ranked with business (not technical) justification
- [ ] One preventive + one detective control for the top case, typed (technical/administrative/physical)
- [ ] Safety statement written

## Cleanup and Reset

1. Nothing was executed — no systems changed.
2. Keep `portfolio/LAB-01/` (it is graded evidence); delete any scratch drafts.
3. If you copied the case text into extra files, consolidate into the portfolio folder.

## Optional Challenges

- Re-analyze Case A assuming the CRM export contained health data: how do impact ratings change?
- Find one **public** post-mortem (organization's own report or a regulator's summary) and run the same five tasks on it. Cite it properly; never reproduce private data.
- Draft the GreenField "acceptable use of shared cloud accounts" policy clause (M03 practice).

## References and Safety Notes

- NIST CSF 2.0 (Feb 2024) — Respond/Recover functions frame Cases B and C: <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final>.
- NIST SP 800-12 Rev. 1 (2017), *An Introduction to Information Security*: <https://csrc.nist.gov/pubs/sp/800/12/r1/final>.
- Course: [M01 module](../../modules/module-01-information-security-foundations/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** this lab touches no systems. Cases are synthetic composites; any real-world case you add for the challenge must come from published, public reports and be analyzed read-only.

**Navigation:** · [Lab index](../README.md) · [Next: LAB-02 →](../lab-02-threat-model-risk-register/README.md)
