---
title: "Module 05 Quiz — Operating System and Endpoint Security"
layout: default
---

# Module 05 Quiz — Operating System and Endpoint Security

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 short answer) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Short answers: 2–5 sentences. Where a command is asked for, give it and say in one line what it does and how you would read the result.

**Coverage.** Maps to Module 05 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m05--operating-system-and-endpoint-security)).

**Related:** [Module 05 lesson](../../modules/module-05-operating-system-and-endpoint-security/README.md) · [LAB-04](../../labs/lab-04-permissions-hardening/README.md) · [CS-1 case study](../case-studies/cs-1-breach-at-meridian.md)

> **Safety reminder:** all hardening and hunting happens on a VM you own, isolated from your real LAN. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** The principle of **least privilege** means a user/process should have:

- (a) Every permission they might ever need, to avoid friction
- (b) Only the permissions required to perform their task, and no more
- (c) Full admin rights if they are trusted
- (d) The same rights as their team lead

**Q2.** On Linux, what does the `sudo` mechanism primarily provide?

- (a) Faster command execution
- (b) Controlled, auditable elevation of specific commands for authorized users
- (c) Encryption of the user's home directory
- (d) Automatic patching

**Q3.** The **3-2-1 backup rule** means:

- (a) 3 hours RTO, 2 zones, 1 alert
- (b) 3 copies, 2 different media types, 1 copy offsite
- (c) 3 admins, 2 servers, 1 network
- (d) 3 encryption keys, 2 certificates, 1 password

**Q4.** Full-disk encryption (BitLocker/LUKS) primarily protects data when:

- (a) The powered-on, logged-in device is in use
- (b) The device is powered off or the disk is removed and viewed offline
- (c) The data is backed up to the cloud
- (d) The network is compromised

**Q5.** **Application allowlisting** differs from antivirus in that it:

- (a) Tries to detect all known malware signatures
- (b) Permits only explicitly approved applications to run, blocking everything else
- (c) Scans files after execution
- (d) Relies on cloud heuristics

**Q6.** A **persistence** mechanism is:

- (a) A way for malware to survive reboots and stay resident
- (b) A backup strategy
- (c) A firewall rule
- (d) A type of encryption

**Q7.** Which is the *strongest* sign of possible endpoint compromise among these?

- (a) A scheduled backup job running nightly
- (b) A new autorun/startup entry pointing to an unknown executable in a temp folder
- (c) A Windows update installing
- (d) A user logging in during business hours

**Q8.** Patch management is primarily a control of which type?

- (a) Detective only
- (b) Preventive (removing a known weakness before it is exploited)
- (c) Corrective only
- (d) Physical

## Part B — Short answer (4)

**Q9.** State the Linux command to list file permissions for `/etc/passwd`, and explain in one line what the output tells you and why an owner/group/other distinction matters for least privilege.

**Q10.** You suspect a Linux host is compromised. Name two persistence locations or artifacts you would check and one command that reveals each.

**Q11.** Explain why "the firewall is on and the antivirus is updated" is *not* sufficient endpoint hygiene. Name two missing layers and justify.

**Q12.** Describe the difference between *detection* (what EDR/AV notices) and *recovery* (what you do after), using a ransomware example with one concrete control from each.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Only the permissions required for the task, nothing more — excess rights expand blast radius if an account or process is compromised. *Misconception:* (a) is convenience, not a principle; (c) confuses trust with entitlement — even trusted admins should hold only task-needed rights.

**Q2 — (b).** Controlled, auditable elevation of *specific* commands for authorized users — not blanket root access; every `sudo` use is logged. *Misconception:* (a) is a performance myth; (c)/(d) describe unrelated features — sudo's defining traits are scoped commands *and* a trail, neither of which plain root has.

**Q3 — (b).** 3 copies, 2 different media types, 1 offsite — defending against local failure, media failure, and site loss (fire/theft). *Misconception:* the digits are not hours or zones — the rule's point is *three independent failure modes*, so variations that reuse one medium or keep everything on-site fail it.

**Q4 — (b).** It protects data at rest on a powered-off device or a removed disk. *Misconception:* (a) is exactly what full-disk encryption **cannot** do — once the owner is logged in the keys are in memory; (c)/(d) concern data *in transit*, a different layer entirely.

**Q5 — (b).** Allowlisting permits only explicitly approved applications and blocks everything else — a preventive, default-deny posture. *Misconception:* (a)/(c) describe *detection*, which must already know the bad file; allowlisting inverts the model: unknown = denied, no signature knowledge required.

**Q6 — (a).** Persistence = the techniques that keep malware resident across reboots/sessions (autorun keys, services, cron, shells). *Misconception:* (c) a firewall rule is a *preventive network* control — it says nothing about surviving a restart; that temporal survival is the defining feature.

**Q7 — (b).** An unknown autorun/startup entry pointing at a temp-folder executable is a classic persistence indicator. *Misconception:* scheduled backups, OS updates, and business-hours logins are all *expected* behavior — severity comes from the anomaly (unknown target, odd location), not from merely existing.

**Q8 — (b).** Preventive — patching removes a known weakness *before* exploitation. *Misconception:* (a) *detective only* would mean noticing the weakness without fixing it — patching eliminates it; (c) corrective applies to the *aftermath* of an exploited or failed patch, not the patch itself.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** `ls -l /etc/passwd` (or `stat /etc/passwd`). Output shows permissions as `rwxr-xr-x`-style triples for **owner / group / other**, plus the owning user and group. The distinction matters for least privilege because it lets you grant a specific group exactly the access it needs (e.g., read-only for a service account) without opening the file to everyone. → [LAB-04](../../labs/lab-04-permissions-hardening/README.md)

**Q10.** *(a)* **Startup/autorun** — on Linux check cron (`crontab -l`, `/etc/cron.*`) and systemd units (`systemctl list-unit-files --state=enabled`); on Windows, Run keys / Startup folder. *(b)* **SSH authorized_keys** — `cat ~/.ssh/authorized_keys` (an unexpected key = silent backdoor). Each reveals a mechanism that re-launches the attacker after reboot or grants re-entry.

**Q11.** Firewall + up-to-date AV cover only the *network* and *known-signature* layers. Missing: **least privilege / account control** (a compromised admin account bypasses both) and **patching/known-vulnerability management** (AV cannot stop exploitation of a legit, unpatched app). Also missing: tested **backups** (recovery) and **logging/EDR visibility** (detection). Defense in depth requires independent layers.

**Q12.** *Detection:* EDR/AV notices ransomware behaviour (mass file renames, shadow-copy deletion) and raises an alert. *Recovery:* you restore encrypted files from an **offline/offsite 3-2-1 backup** and rebuild the host. One preventive control: application allowlisting to stop the unknown encryptor running. One detective control: EDR alert on mass-file-modification. Detection without backups still loses data; backups without detection lose time.

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Harden a VM.** Take a fresh Ubuntu Server VM through a 15-point hardening checklist (accounts, sudo, firewall, updates, SSH config). Verify each change with a command and a before/after screenshot.
2. **Windows baseline.** Apply 10 hardening settings on a Windows VM (Microsoft free dev VM), recording before/after evidence.
3. **Compromise hunt (simulated).** In a provided benign exercise set, find and document 5 planted indicators (odd startup entry, rogue service, unexpected open port).
4. **Audit scoring.** Run `lynis audit system /` on your Linux lab VM and write a half-page on the top three recommendations and which control type each is.

*Review guidance:* 1–3 are the portfolio evidence for M05. If your hardening proof shows a *command* but not the *before/after state change*, it is not evidence yet — that is the same discipline the capstone demands.

**Next:** [Level 1 case study CS-1](../case-studies/cs-1-breach-at-meridian.md) · [Previous: M04](./quiz-m04.md) · [Assessment Hub](../README.md)
