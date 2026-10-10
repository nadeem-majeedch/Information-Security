---
title: "Module 14 Quiz — Incident Response and Digital Forensics"
layout: default
---

# Module 14 Quiz — Incident Response and Digital Forensics

**Type:** Formative knowledge check (completion gate) · **Questions:** 14 (9 multiple choice + 5 applied sequencing questions) · **Pass mark:** ≥ 80% (12 of 14) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Sequencing questions: give the **ordered steps** (numbered) — partial order scores partial credit, and each step needs a one-line "why this position."

**Coverage.** Maps to Module 14 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m14--incident-response-and-digital-forensics)): IR plan structure (NIST SP 800-61 Rev. 3), evidence order and chain of custody, timeline reconstruction, tabletop + lessons learned.

**Related:** [Module 14 lesson](../../modules/module-14-incident-response-and-digital-forensics/README.md) · [LAB-15 digital forensics](../../labs/lab-15-digital-forensics/README.md) · [LAB-14 IR tabletop](../../labs/lab-14-ir-tabletop/README.md) · [LAB-13 log analysis](../../labs/lab-13-log-analysis/README.md) · [CS-3 case study](../case-studies/cs-3-detection-to-response.md)

> **Safety reminder:** forensics and IR here use the course's **synthetic evidence bundles and lab VMs only**. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (9)

**Q1.** The NIST SP 800-61 incident-response phases in order are:

- (a) Detect → Prevent → Report → Recover
- (b) Preparation; Detection & Analysis; Containment, Eradication & Recovery; Post-Incident Activity
- (c) Containment → Preparation → Recovery → Detection
- (d) Analysis → Prevention → Escalation → Documentation

**Q2.** The single most important reason to **image** a compromised disk before analysis is:

- (a) Disks are slow
- (b) Analysis on a copy preserves the original's state and hash, keeping evidence defensible and repeatable
- (c) Images compress better
- (d) Courts require a specific file format regardless of context

**Q3.** The **order of volatility** dictates you collect first:

- (a) Backups, then archive, then disk, then memory
- (b) CPU cache/registers → memory → network state → running processes → disk → backups/printouts (most volatile first)
- (c) Disk, then memory, then network
- (d) Whatever is easiest to copy

**Q4.** **Chain of custody** documents:

- (a) Only the case name
- (b) Who held the evidence, when, and what was done to it — from collection through court/disposition, proving no tampering
- (c) The attacker's movements
- (d) The encryption keys used

**Q5.** During containment, the *worst* typical action is:

- (a) Isolating the host from the network while preserving state
- (b) Immediately powering off a live system to "secure it" — losing memory, connections, and running-malware evidence needed for scope and analysis
- (c) Snapshotting before changes
- (d) Notifying the incident owner per plan

**Q6.** A file's `mtime`, `atime`, and `ctime` on Linux mean (respectively):

- (a) Created, modified, deleted
- (b) Content last modified, last accessed, metadata last changed (ctime = inode change, not creation)
- (c) Copied, moved, renamed
- (d) Compressed, encrypted, archived

**Q7.** In a ransomware tabletop, "we'd restore from backup" is only a valid *recovery* answer if you can also show:

- (a) The backup software's logo
- (b) Backups are offline/offsite per 3-2-1, **tested-restorable**, and the restore happens *after* eradication so the ransomware isn't restored with the data
- (c) Backups ran yesterday
- (d) Backups are encrypted with the server's key

**Q8.** A **lessons-learned** report should contain:

- (a) Blame naming and punishment records
- (b) Timeline, what worked, what failed, root cause, and *actionable* improvements with owners and due dates
- (c) Only the final cost
- (d) Marketing-safe language only

**Q9.** Hashing evidence files (SHA-256) at collection serves to:

- (a) Compress them
- (b) Prove integrity — any later alteration changes the hash, and the recorded value proves the analyzed copy matches what was collected
- (c) Encrypt the evidence
- (d) Satisfy a formatting habit

## Part B — Applied sequencing (5)

**Q10.** **Evidence collection order.** A live compromised Linux host in your lab is running suspicious processes with an active network connection. List the collection order for: disk image, memory capture, `netstat`/connection state, running process list, and volatile capture timestamps — with one line of justification per position. (Name the tool for at least two steps.)

**Q11.** **Incident containment sequencing.** Ransomware is actively encrypting file shares. Order these: (a) restore from backup, (b) isolate affected hosts/network segments, (c) identify patient zero and scope, (d) notify stakeholders per plan, (e) eradicate the ransomware/persistence, (f) verify eradication. State what you must *not* do first and why.

**Q12.** **Forensic timeline build.** Given a synthetic evidence bundle (disk image + `auth.log` + web logs), describe your workflow from receiving the bundle to answering "when did the attacker first gain access, and what did they do?" — including hash verification, mounting/imaging discipline, and at least 3 artifact types you'd correlate with timestamps. → [LAB-15](../../labs/lab-15-digital-forensics/README.md)

**Q13.** **IR plan structure.** Outline a 2–3 page IR plan for a 10-person org: list its required sections (aligned to NIST SP 800-61 Rev. 3) and give the escalation table's columns. Which section is most often missing in ad-hoc plans, and why does that omission hurt most?

**Q14.** **Tabletop decision point.** During a ransomware tabletop it's discovered a *second* share began encrypting 5 minutes after the first was isolated. What does that imply about containment (one host vs. scope), and what's your next decision + justification?

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Preparation; Detection & Analysis; Containment, Eradication & Recovery; Post-Incident Activity. Misconceptions: (a) invented phases; (c) containment cannot precede detection; (d) scrambles the canonical order.

**Q2 — (b).** Working on a verified copy preserves the original (write-blocker/imaged copy), makes analysis repeatable and auditable, and lets you re-run new techniques later. Misconceptions: (a) performance is incidental; (c) forensic images are deliberately *not* compressed lossily; (d) format choices matter, but the *reason* is integrity/defensibility, not format ritual.

**Q3 — (b).** Volatility: cache → RAM → network → processes → disk → offline/archives. Misconceptions: (a) backwards; (c) disk before memory destroys live state; (d) convenience ignores that RAM evidence disappears at power-off.

**Q4 — (b).** Custody log: collector, time, hash, transfers, access, purpose — an unbroken accountability record. Misconceptions: (a) too little to prove anything; (c) that's a timeline, not custody; (d) keys are handling details, not custody itself.

**Q5 — (b).** Powering off kills RAM (connections, injected code, keys) and running-state evidence — you can't get it back. Misconceptions: (a) network isolation preserves state *and* cuts attacker control — correct; (c) snapshots before changes are best practice; (d) notification per plan is required.

**Q6 — (b).** `mtime` = content change, `atime` = last read, `ctime` = inode/metadata change (permissions, links — **not** creation time; creation-ish is `crtime`/btime on some filesystems). Misconceptions: (a) common trap — `ctime` ≠ created; (c)/(d) unrelated operations.

**Q7 — (b).** Restorable, isolated (3-2-1 offline), and sequenced after eradication — otherwise you re-infect or discover backups are worthless. Misconceptions: (a) branding proves nothing; (c) recency ≠ usability or isolation; (d) if the *server* key encrypted backups, ransomware with server control owns them too.

**Q8 — (b).** Blameless, factual, improvement-oriented — with owners/dates so lessons become changes. Misconceptions: (a) blame kills reporting; (c) cost alone teaches nothing; (d) sanitizing until nothing critical remains makes the exercise pointless.

**Q9 — (b).** Hash at collection = integrity anchor: re-hash later and compare; mismatch = altered evidence. Misconceptions: (a) hashing doesn't compress; (c) hashing ≠ encryption (no confidentiality); (d) it's evidentiary, not stylistic.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q10.** Because the host is **live with an active connection**, volatile-first: (1) **Timestamp** the start of collection (log UTC start) — establishes the evidentiary baseline everything else references. (2) **Network connection state** — `ss -tunap` / `netstat -tunap` + routing/ARP: the active C2 session is the *most* volatile useful artifact (gone the moment the socket drops) and often defines scope. (3) **Running processes + memory capture** — process list (`ps auxf`, then `/proc/*/exe` links) followed by memory dump (`pmem`/AVML, `LiME`): RAM holds injected code, loaded modules, keys, and process-network mapping; dump memory *before* anything that shifts paging. (4) **Disk image** (forensic clone, hashed) — least volatile of these; a live-image or post-isolation clone captures files/artifacts while (2)/(3) would have rotted. (5) **Hash everything + record** (SHA-256 into the chain-of-custody form with times and collector). One-line logic: *anything that vanishes on reboot/packet-close comes first; anything re-readable later comes last* — and you never power off to "make disk easier," because step 3 dies with the power.

**Q11.** **Order:** (b) **isolate** affected hosts/segments first — network cut stops encryption spread immediately while preserving live state for analysis; then (d) **notify stakeholders per plan** (legal/comms paths have lead times and are time-critical); then (c) **identify patient zero + scope** — which shares/hosts/users, how it arrived (needed to know what eradication must remove); then (e) **eradicate** (remove persistence, the dropper, close the initial vector); then (f) **verify eradication** (scan + confirm no re-encryption capability, monitor); only then (a) **restore from backup** (known-good, offline, tested) and validate data integrity. **Must NOT do first:** (a) restore — you'd restore into a still-compromised environment and watch the fresh copies get encrypted (worse: ransomware often watches for restored files), and you'd also destroy the evidence needed to find the vector. *Containment protects both data and evidence; recovery must follow eradication.* → [LAB-14](../../labs/lab-14-ir-tabletop/README.md)

**Q12.** **Workflow:** (1) **Receive + document:** log receipt time/source, place the bundle in read-only/working-copy discipline, and **verify provided SHA-256 hashes first** — mismatch stops the analysis (integrity before curiosity). (2) **Work only on copies:** mount the disk image read-only (`mount -o loop,ro`, or mount a working copy; never the original), create your own working copy for carving. (3) **Extract timeline artifacts:** filesystem timestamps (mtime/ctime/atime, directory entries), `auth.log`/`secure` (SSH success/fail, source IPs, users), web server access/error logs (URIs, status codes, source IPs), plus shell history, cron/systemd units, and (if present) Prefetch/journal equivalents. (4) **Normalize:** unify timezones (convert to UTC, note offsets), convert epoch times, and build a single chronological table. (5) **Correlate:** first *successful* auth after a failure burst = likely initial access; chain: first access → privilege steps (sudo, new SUID) → persistence (cron/systemd/authorized_keys) → actions (file changes, data staging). (6) **Answer with citations:** state "first access at T, source IP X, evidence lines A/B/C," and re-hash any file you export as evidence. **3+ artifact classes correlated:** auth logs, filesystem timestamps, cron/persistence artifacts — add web logs and shell history where available. → [LAB-15](../../labs/lab-15-digital-forensics/README.md)

**Q13.** **Sections (NIST SP 800-61-aligned):** (1) Purpose/scope + how to detect an incident; (2) Roles & responsibilities (incident handler, IT, comms, decision authority); (3) **Detection & analysis** (triage, severity definitions, classification); (4) **Containment/eradication/recovery** strategies per incident type; (5) **Communication plan** — internal escalation + external (customers/regulators/law enforcement) triggers; (6) Evidence handling & chain of custody; (7) Post-incident activity (lessons learned); (8) Appendices: contact list, asset inventory, tooling. **Escalation table columns:** contact/role · channel (and backup channel) · when to contact (trigger/threshold) · decision authority (what they can approve) · max response time. **Most-missing section: the communication plan** — ad-hoc responders focus on tech and improvise notifications; the omission hurts most because notification deadlines (regulatory, contractual, customer) have clocks that start at *discovery*, not when you finish fixing — late notification converts a technical incident into a legal/PR one.

**Q14.** **Implication:** the first isolation was **incomplete scope** — either other hosts were already compromised (shared credentials/persistence), the share itself was reached via a different path (a second machine with share access), or lateral movement continued because containment covered one node while the *vector* (e.g., domain admin creds, a management tool) remained live. One-host containment ≠ incident containment: you contained a *symptom*, not the scope. **Next decision:** treat as multi-host: widen scope identification *while* maintaining network-level containment (segment/shut the share access, block lateral paths, disable suspect shared credentials), then re-run scope with the broader lens — which hosts share creds/tools/paths, were backups affected — and only proceed to eradication once no active encryption path remains. **Justification:** re-encryption in a *second* location proves an active, ongoing mechanism; eradicating or restoring before you've stopped that mechanism repeats the loss and burns the backups. → [Module 14 lesson](../../modules/module-14-incident-response-and-digital-forensics/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **IR plan (professional writing).** A 2–3 page plan for a 10-user org covering preparation → post-incident with the escalation table — M14 deliverable.
2. **Forensic timeline (investigation).** Receive the synthetic bundle, hash → image → carve → timeline → answer 5 investigation questions with artifact citations — M14 deliverable. (LAB-15)
3. **Tabletop run (scenario).** Run the ransomware-in-lab tabletop solo or with peers: document decisions at each phase, containment trade-offs, recovery validation, then a lessons-learned report with owners/dates. (LAB-14)
4. **Risk prioritization.** Your IR plan can pre-authorize three containment actions and must get approval for everything else. Choose the three pre-authorized ones (and justify why *those*), and name the approval path for destructive actions like reimaging.

*Review guidance:* sequencing questions are where professionals separate from amateurs — the graders look for *volatile-first* and *contain-before-recover* instincts plus a stated reason at each step, not just a correct-looking list.

**Next:** [M15 quiz](./quiz-m15.md) · **Previous:** [M13 quiz](./quiz-m13.md) · **Hub:** [Assessment Hub](../README.md)
