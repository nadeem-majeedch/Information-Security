---
title: "LAB-14 — Incident Response Tabletop Exercise"
layout: default
---

# LAB-14 — Incident Response Tabletop Exercise

**Lab ID:** LAB-14 · **Difficulty:** Advanced · **Estimated duration:** 2 hours · **Module:** M14 · **Mode:** Written discussion exercise (no systems touched)

## Scenario

**Delta Manufacturing** (fictional, 220 staff, one IT manager, one MSP) starts a normal Monday. At 07:40, the warehouse reports "shared drives asking for a key." By 08:10 the IT manager confirms: files renamed with an unfamiliar extension, ransom notes on three PCs, and email *still working*. You are running (and playing) this **tabletop exercise**: a structured rehearsal where the "players" make decisions under time pressure, and you capture the decision log — the artifact that later becomes the real playbook. Solo players rotate roles; with a group, assign them.

## Learning Objectives

1. Execute the NIST SP 800-61r3 response phases against a scripted incident: preparation gaps, detection/analysis, containment, eradication, recovery, post-incident.
2. Make and justify containment decisions under competing pressures (production, evidence, payroll deadline).
3. Maintain a decision log with options considered, decision, owner, and rationale — the professional artifact.
4. Distinguish facts from assumptions at each inject (intelligence discipline).
5. Extract actionable improvements: update one IR-plan section and one control with each round.

## Prerequisites and Required Skills

- M14 module (IR lifecycle, roles, evidence handling), M13 (log/alert vocabulary), M02 (risk framing).
- Skills: structured writing, timekeeping, decision logging. **No technical tools.**

## Tools, Operating Systems, and Versions

- A timer (phone/clock), any editor. Optional role cards if playing with others (roles below).
- Reference: NIST SP 800-61r3 phase model; your M14 IR-plan draft (reused if present).

**$0.**

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-14/` with `decision-log.md`, `inject-notes.md`, `improvements.md`.
2. Read the **org profile** below; timebox: 2 hours total (~15 min orientation, ~90 min injects, ~15 min wash-up).
3. Nothing is executed — no authorization needed. This exercise must stay *written*: imagining containment, not performing it.

## Lab Environment and Starting State

**Org profile (pre-read):** 220 staff; Windows domain (single site); 2 file servers; nightly tape-less backups to an NAS *on the same VLAN* (last verified restore: 8 months ago — "successful"); email via Microsoft 365 (cloud); one IT manager, one part-time helper, MSP for after-hours; flat network (warehouse, office, finance all one VLAN); no EDR — antivirus on servers only; no documented IR plan (that's partly why you're here); cyber-insurance policy exists (notification in 72h of "confirmed" incident). **Roles:** IT Manager (decision owner), MSP engineer (technical), Finance manager (payroll at risk Friday), CEO/comms (reputation + regulator contact), You = IR lead (facilitator).

> **Inject timeline (reveal one at a time; never read ahead — discipline is the exercise):**
>
> **I1 (T+00:10):** Warehouse: 12 PCs and both file servers encrypted; ransom note demands crypto payment in 72h; a screenshot arrives. *Decision needed: first three actions, and who is notified in the first 30 minutes?*
>
> **I2 (T+00:25):** Email still works. Finance says an invoice payment ran normally 40 minutes ago. Someone recalls "a weird login alert on Saturday" nobody triaged. *Decision: is this *only* ransomware, or possibly hands-on-keyboard + data theft? What evidence settles it?*
>
> **I3 (T+00:40):** MSP confirms the NAS backup share is reachable from the infected VLAN and its snapshots were *also* encrypted for September. The "successful restore" from 8 months ago was of a *different* share. *Decision: recovery path now? (Pay? Restore-from-scratch feasibility? Manual reconstruction?)* Justify against the 72h clock.
>
> **I4 (T+00:55):** Legal asks: is this notifiable? (Fictional jurisdiction; insurance says "confirmed incident" triggers the 72h clock; personal-data files were among the encrypted.) *Decision: notification posture and who owns it; what you can state factually today.*
>
> **I5 (T+01:10):** Pressure: Friday payroll must run; Finance proposes re-enabling one infected PC "just for payroll." The note's IP has been "DDoS-ing" the website (low-volume noise). *Decision: payroll continuity plan that doesn't launder malware; evidence-preservation stance.*
>
> **I6 (T+01:25):** Post-mortem request from the CEO 3 weeks later. You hold: decision log, ransom note, NAS state photos, MSP's network diagram, the Saturday alert (now retrieved). *Deliverable: 3 root causes, 5 improvements with owners/dates, one plan-section update.*

## Tasks

1. **Preparation gap review (10 min):** from the org profile, list 5 gaps *before* any inject (no IR plan, untested backups, flat network, no EDR, alert nobody triaged). This is your "what preparation should have caught" baseline.
2. **Play the injects (90 min):** for each, log: *situation* → *options considered (min 2)* → *decision* → *owner* → *rationale* → *evidence/assumption flag*. Enforce the fact/assumption split explicitly ("fact: note demands X; assumption: attackers still have access").
3. **Phase mapping:** after the session, tag each decision with its NIST phase (Preparation / Detection & Analysis / Containment / Eradication / Recovery / Post-incident — noting r3's risk-managed framing). Any decision with no home = process gap you invented during play.
4. **Evidence discipline check:** list what you would **not** do (pay immediately without analysis; wipe servers before imaging; reconnect before scoping) and why — each tied to a concept (chain of custody, scope-before-eradication).
5. **Improvements (the point of tabletops):** produce 5 improvements, each: *gap → change → owner → due date → how verified*. At least one must update an **IR-plan section** (write the 10-line section) and one a **control** (e.g., immutable off-VLAN backups; EDR; alert triage SLA).
6. **Retrospective:** 150 words on what the exercise revealed about *process* (who decided what; where time was lost) — the tabletop's real product.

## Expected Observations

- I2 forces the "ransomware vs. intrusion" distinction: encryption can be a *cover* for theft (extortion double-pressure) — log-scope answers (mailbox rules? mass download? weekend alert content) come before assumptions.
- I3 is the classic untested-backup collapse: "we had backups" fails the first real restore test — directly M05's 3-2-1 + tested-restore lesson.
- I5 tempts an unsafe shortcut: the correct posture is a *clean* rebuild of a segregated payroll path, never re-enabling an infected host.
- I4 shows why "confirmed" is a legal/insurance hinge; facts-first language protects everyone.
- Players who pay without scoping learn the cost in the retrospective: payment doesn't restore data guarantees and can't precede containment.

## Investigation Questions

1. Which inject first *changed your incident classification*, and what evidence (not intuition) justified the change?
2. Containment option matrix: network isolation vs targeted blocking vs "monitor only" — for *this* org, costs and benefits of each (production impact matters).
3. The Saturday alert: name the process fix that would have changed this incident's trajectory, typed as preventive/detective/corrective (M02).
4. Backup architecture: draw the minimal "ransomware-survivable" backup for Delta (3-2-1 + immutability + tested restores) in ≤ 6 lines.
5. Post-incident: which single metric would you add to Delta's monthly IT review to keep improvements alive (e.g., days-to-patch on internet-facing assets; restore-test recency) — and why that metric, not another?

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Reading all injects first | Impatience | The surprise *is* the exercise; fold discipline into the report |
| Decisions logged without options | Skipping analysis | Minimum two options per decision — one must be the tempting-bad one |
| Timeline collapsing | No timekeeping | Use the T+ markers; record decision *times* — recovery-vs-72h reasoning needs them |
| Everything labeled "fact" | Intelligence sloppiness | Force the Fact/Assumption tag; untagged lines are invalid in grading |
| Solo play feels fake | No team | Rotate hats explicitly (30 s in-role speech per role) or invite one friend; solo is acceptable with written role-switch notes |

## Evidence to Collect

- `decision-log.md` — all 6 injects, full option/decision/owner/rationale/fact-flag fields, with times.
- `phase-mapping.md` — decisions → NIST phases + gaps.
- `improvements.md` — 5 improvements with owners/dates/verification; the 10-line IR-plan section; the control change.
- `preparation-gaps.md` (Task 1).
- `retrospective.md` (150 words).
- Safety statement: *entirely written exercise; no systems contacted; ransom payment deliberately not part of any lab action.*

## Deliverable and Report Structure

`portfolio/LAB-14/`: org profile summary → preparation gaps → decision log → phase mapping → improvements (with the embedded plan section) → retrospective → safety statement. 3–4 pages.

## Completion Checklist

- [ ] 5 preparation gaps listed before injects
- [ ] All 6 injects played in order with timed decision logs (options ≥ 2 each, fact/assumption tags)
- [ ] Phase mapping complete; ≥ 1 self-identified process gap
- [ ] "Would not do" list with concept-backed justifications
- [ ] 5 improvements with owners/dates/verification; includes 1 IR-plan section + 1 control change
- [ ] 150-word retrospective
- [ ] Safety statement written

## Cleanup and Reset

1. Nothing was executed — no systems, no payments, no law-enforcement contact needed (all fictional).
2. Consolidate into `portfolio/LAB-14/`.
3. Keep the IR-plan section — M19's capstone Stage D reuses it.

## Optional Challenges

- Run it with a team of 3–4 (roles pre-assigned) and diff decision logs — where did the team outperform you solo?
- Write inject I7: "a journalist emails asking about the ransom note" — practice comms discipline.
- Convert your improvements into a 90-day roadmap with effort estimates (management practice).
- Map the same injects onto the CSF 2.0 functions — Respond/Recover coverage check.

## References and Safety Notes

- NIST SP 800-61r3 (Apr 2025), *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*: <https://csrc.nist.gov/pubs/sp/800/61/r3/final>.
- CISA Incident Response Playbook templates: <https://www.cisa.gov/resources-tools/services/incident-response-services>; #StopRansomware Guide: <https://www.cisa.gov/stopransomware>.
- Course: [M14](../../modules/module-14-incident-response-and-digital-forensics/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** this is a written rehearsal — no malware is generated, no systems touched, and no payments/ransoms are ever made or simulated as *recommended actions*. Fictional org, synthetic injects; personal data never appears.

**Navigation:** · [← Previous: LAB-13](../lab-13-log-analysis/README.md) · [Lab index](../README.md) · [Next: LAB-15 →](../lab-15-digital-forensics/README.md)
