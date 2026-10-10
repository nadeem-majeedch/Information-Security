---
title: "Module 05 — Operating System and Endpoint Security"
layout: default
---

# Module 05 — Operating System and Endpoint Security

> **Level 1 · Foundations · Beginner · Estimated study time: 12–14 hours**
> **Prerequisites:** [Module 04](../module-04-networking-fundamentals-for-security/README.md) (recommended), Module 01.

## Why This Module Matters

Everything you protect — files, credentials, keys, the network traffic itself — lives and runs on endpoints. Attackers know it: intrusions that begin with a phishing email *land* on an endpoint, and ransomware's entire business model is encrypting yours. This module turns a fresh Linux VM and a Windows machine into a documented, hardened baseline: right accounts, minimal services, updates flowing, firewall on, backups that actually restore. It also teaches the inverse skill — recognizing when a machine *has* been compromised — which is the seed of Level 3's detection work (M13) and forensics (M14). Every later lab runs on the machines you harden here.

## Prerequisites and Estimated Study Time

- **Prerequisites:** [Module 04](../module-04-networking-fundamentals-for-security/README.md) recommended (isolation proof, basic terminal); Module 01 required.
- **Estimated study time:** 12–14 hours — ~3 h reading, ~7 h labs (two hardening runs + hunt), ~2 h knowledge check.
- **Tools:** VirtualBox/VMware (free), Ubuntu/Debian ISO (free), Windows: your own machine's VM or Microsoft's free developer VM images (evaluation images expire — rebuild when they do), `lynis` (free Linux audit tool). **$0.**

## Learning Outcomes

By the end of this module, you can:

1. Apply OS hardening baseline steps on Linux (user accounts, sudo, firewall, updates, SSH config) and Windows (accounts, UAC, BitLocker awareness, firewall, updates). *(Apply)*
2. Explain malware protection layers: antivirus/EDR behavior, application control, patching, and least privilege. *(Understand)*
3. Configure and verify basic endpoint hygiene: disk encryption awareness, secure backup (3-2-1 rule), and browser security settings. *(Apply)*
4. Detect basic signs of endpoint compromise (unexpected processes, persistence locations, unexpected outbound connections). *(Analyze)*

---

## Core Concepts

### 1. How an OS is organized (the map for everything below)

**Plain language.** An operating system is a referee: applications ask it for everything — files, network sockets, more memory — and it decides who gets what.

**Technical detail.**

- **Kernel vs. user space.** The *kernel* is the trusted core managing hardware, memory, processes, and permissions; your apps run in *user space* and must request resources through system calls. Malware wants **kernel-level** access — that's total control.
- **Users, groups, permissions.** Linux permissions are per-file triples (`rwx` — read/write/execute) for **owner, group, others**, plus special bits (SUID — *set user ID*, runs a program as its file owner, often root: a classic privilege-escalation plant). Windows uses Access Control Lists (ACLs) per file with user/group entries. **Principle of least privilege:** every account gets *only* the rights needed — no daily-driving as administrator/root.
- **Processes & services.** Running programs (*processes*) and auto-started background programs (*services/daemons* in Linux; *services* in Windows) form your **attack surface** — every listening service is a door. Minimize doors.
- **Configuration lives in files (Linux) vs. stores (Windows).** Text configs under `/etc/` (e.g. `/etc/ssh/sshd_config`) vs. the Windows Registry plus Settings — same concepts, different address labels.

### 2. Least privilege, in practice

**Plain language.** The intern shouldn't have the master key. Rights are handed out like keys: minimum set, checked in, logged.

**Technical detail.** Concrete forms: use a **standard user account** for daily work and elevate only when installing (Windows UAC prompt; Linux `sudo` — note: `sudo` is *controlled* root-use, not a different user — beware `sudo` habit loops). Group-based rights (`sudo`/`Administrators` membership reviewed). File permissions set to minimum (`chmod 750` not `chmod 777` — world-writable = anyone/anything can modify). Separation of duties (one person deploys, another approves — full treatment in M07). Least privilege is the single control that most shrinks malware impact: *a process can only do what its user can do.*

### 3. Patch management: the process, not the reflex

**Plain language.** Updates fix known holes. The organizational question isn't *whether* to patch — it's *who, how fast, and how do we know it worked.*

**Technical detail.** The lifecycle: **inventory** (what do we run?) → **prioritize** (KEV-listed and internet-facing first; then CVSS bands — Module 02 method) → **test** (updates on non-critical machines first in organizations) → **deploy** (automatic where possible) → **verify** (confirm versions/uptime) → **record**. On Ubuntu: `sudo apt update && sudo apt upgrade` (apt = Debian/Ubuntu package manager); on Windows: Settings → Windows Update, with active-hours scheduling. Auto-updates are the correct default for endpoints — the "patch gap" you studied in M02 starts here, at *not clicking*. Emergency patches (actively exploited) get 24–72h treatment; routine updates flow weekly.

### 4. Malware protection layers

**Plain language.** No single product stops everything — you stack layers: prevention that blocks, detection that watches, and design that limits blast radius.

**Technical detail.**

| Layer | What it does | Notes |
|---|---|---|
| **AV (antivirus)** | Matches known-bad file *signatures* | Still common baseline; weak vs. novel files |
| **EDR (endpoint detection & response)** | AV + behavioral monitoring + telemetry + investigation/response console | Sees *behavior* (e.g., a document spawning a shell), not just hashes |
| **Application allowlisting** | Only *approved* programs run; everything else blocked | Strongest prevention; managed via Windows Defender Application Control/AppLocker on Windows, or package/whitelist policies on Linux |
| **Patching** | Removes the known vulnerability being abused | The cheapest high-yield control (§3) |
| **Least privilege** | Caps what a successful exploit can do | §2 |
| **Browser hardening** | Blocks the #1 initial-access path (web) | §6 below |
| **Firewall** | Controls inbound/outbound connections per rule | On by default on modern Windows/Linux — never disable to "make it work" |

*Signature vs. behavior:* AV asks "is this file bad?" (reliable for known, blind to new); EDR asks "is this *process* acting bad?" (catches more, needs tuning — M13). Defense in depth means both, plus privilege limits so a caught exploit still fails.

```text
   What the user does          What stops a bad outcome
   ─────────────────────────────────────────────────────
   Clicks a link      ──►   Browser hardening + updates
   Runs a file        ──►   AV signature  /  application allowlisting
   Exploit behaves    ──►   EDR behavioral detection ──► alert (M13)
   Exploit succeeds   ──►   Least privilege caps blast radius
   Persistence attempt──►   Startup inventory vs. baseline (Procedure B)
   Data at rest       ──►   Disk encryption (stolen-device case)
   Everything lost    ──►   Tested 3-2-1 backups (recoverability)
```

### 5. Disk encryption and backups — recoverability as a control

**Plain language.** Encryption makes a stolen laptop unreadable without the key. Backups make *any* disaster survivable.

**Technical detail.**

- **Disk encryption:** BitLocker (Windows Pro/Enterprise/Education; consumer Windows Home lacks it — FileVault on macOS; LUKS on Linux). Modern systems bind keys to the **TPM** chip (hardware key storage). It protects data on a *powered-off, lost/stolen device* — it does nothing against malware running while you're logged in. Record your recovery key somewhere off-device (cloud key escrow or printed) — an encrypted disk with a lost key is your own ransomware.
- **The 3-2-1 backup rule:** **3** copies of your data, on **2** different kinds of media, with **1** copy offsite (cloud counts). Add two modern amendments: backups must be **tested by restoring**, and one copy should be **immutable/air-gapped** (offline or write-once — ransomware can't encrypt what it can't reach). A sync folder is *not* a backup — deletions sync everywhere (M01's logistics example).

### 6. Browsers and everyday hygiene

**Plain language.** The browser is the most-attacked app you own — it's a program that fetches and runs other people's code.

**Technical detail.** Baseline: keep the browser auto-updating; use a **password manager** with unique passwords instead of the browser's remember-box for your *main* accounts (a shared/family computer can expose browser-stored passwords; a manager with a strong master + MFA resists better); install **few, trusted extensions** (every extension is code with broad page access); prefer a standard tracker-blocker; enable HTTPS-Only/Always-Use-HTTPS mode; treat download-and-run prompts as the danger zone. Also: **screen lock** within 1–2 minutes of idle; **automatic OS updates**; device **full-disk encryption** where available; **MFA** on email (ties to M07).

### 7. Persistence: how attackers stay after reboot

**Plain language.** Sneaky programs survive restarts by registering themselves where the OS automatically runs things — those places are your hunting ground.

**Technical detail.** Standard persistence locations (**safe to *inspect*; never add entries you don't recognize**):

- **Linux:** cron jobs (`crontab -l` for your user; `/etc/cron.*`), systemd units (`systemctl list-unit-files --state=enabled`), shell startup files (`~/.bashrc`, `~/.profile`), service files in `/etc/systemd/system/`.
- **Windows:** Run/RunOnce registry keys (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and `HKLM\…`), the Startup folder, Scheduled Tasks, Windows Services.
- **Everywhere:** unexpected outbound connections (`ss -tulnp` on Linux; `netstat -ano` or Resource Monitor on Windows), unknown users/groups, unknown listening ports.

You'll exploit exactly these in the lab hunt — they're also what M13's detections learn to watch.

---

## Worked Example: Hardening a Fresh Ubuntu VM (with commands)

**Scenario.** You just created an Ubuntu Server VM. Walk the baseline end-to-end — every command is safe to run on *your own* lab VM (run inside your isolated lab; no scanning involved):

| # | Goal | Command / action | How you verify |
|---|---|---|---|
| 1 | Fully patched | `sudo apt update && sudo apt upgrade -y` | Re-run: 0 to upgrade |
| 2 | Non-root daily use + controlled elevation | Use a normal account; `sudo -l` shows your rights | `whoami` ≠ root for daily work |
| 3 | Host firewall on, default deny incoming | `sudo ufw default deny incoming` then `sudo ufw allow 22/tcp` (SSH — lab only) and `sudo ufw enable` | `sudo ufw status verbose` → active, scoring |
| 4 | Minimal listening doors | `ss -tulnp` | Every listed port has a known purpose; anything else → investigate/remove |
| 5 | SSH hardened (if enabled) | Edit `/etc/ssh/sshd_config`: `PermitRootLogin no`; prefer key auth (`PasswordAuthentication no` *only after* keys work) | `sudo sshd -t` (config valid) → `sudo systemctl reload sshd` |
| 6 | Services minimized | `systemctl list-unit-files --state=enabled` | Disable what you don't use: `sudo systemctl disable --now <unit>` |
| 7 | Accounts reviewed | `cat /etc/passwd` (users with real shells), `groups` on yours | Only expected accounts with `/bin/bash`-style shells |
| 8 | Automatic security updates | Ubuntu: `sudo apt install unattended-upgrades` then `sudo dpkg-reconfigure unattended-upgrades` | `systemctl status unattended-upgrades` |
| 9 | Audit score recorded | `sudo apt install lynis && sudo lynis audit system` | Save the "Hardening" index; re-run at end and compare |
| 10 | Snapshot the clean state | VirtualBox/VMware: take snapshot `baseline-clean` | Rollback works: restore test |

**Windows baseline (equivalent run, on your own machine or an eval VM):** Settings → Windows Update → on with automatic restarts; **Firewall: on for all profiles**; use a **standard account** daily (admin only for installs — UAC never disabled); **BitLocker** enabled where the edition provides it (recovery key saved off-device); **screen lock ≤ 2 min**; check *Startup apps* and `services.msc` for unknowns; optional: *Windows Security → Virus & threat protection → Cloud-delivered protection* on. Settings names drift between Windows versions — judge by *function* (is the control on?), not the exact label.

**Read the design:** steps 1–2 = attack surface and blast radius (M02's controls); 3–4 = doors (M08 will make them intelligent); 5 = remote-access hygiene; 6–7 = inventory & minimization (*Identify* in CSF terms); 8 = shrinking the patch gap; 9–10 = measurability + recovery. **Apply:** run steps 1–4 on your own VM now (they're safe and reversible) and *write one sentence per step* explaining which risk it treats. **Self-check:** if you cannot explain why step 5's `PasswordAuthentication no` is dangerous *before keys are installed* (answer: you'd lock yourself out of your own VM — the classic first-day mistake), redo step 5's note.

---

## Step-by-Step Procedures

### Procedure A — Endpoint hardening with evidence

1. Create the VM (or use your lab machine); record OS version (`lsb_release -a` / `winver`).
2. Work the Worked Example table **in order**; after *each* step, capture evidence: command + output (or settings screenshot). Evidence per step beats a final screenshot — you can't reconstruct history later.
3. Run `lynis audit system` **before** changes (baseline score) and **after** (improvement) — save both reports.
4. Fill `hardening-checklist.md`: step, action taken, verification, risk treated (M01/M02 vocabulary).
5. Enable/verify disk encryption path (LUKS on Linux installs with encryption; BitLocker where available) and record where your recovery key is stored *off-device*.
6. Configure backup: one synced copy + one **separate** weekly copy (different location/service) of one important folder; **restore a test file** from the second copy and screenshot it.
7. Browser pass: update, HTTPS-only mode, password manager installed with unique logins for 3 accounts, extension list reduced to trusted ones.
8. Snapshot: `baseline-clean` — the safe point you roll back to before every future experiment.

### Procedure B — Endpoint compromise hunt (five planted indicators)

*Run only inside your lab VM. Course exercise uses benign planted artifacts; the same commands are your real triage toolkit later.*

1. **Unexpected accounts:** `cat /etc/passwd | cut -d: -f1,7` — flag any user with a login shell you didn't create.
2. **Persistence in cron:** `crontab -l` (yours) and `ls -la /etc/cron.*` — flag unknown entries (comments starting with `#` are fine; look for commands you don't recognize).
3. **Auto-start creep:** `systemctl list-unit-files --state=enabled` — flag unfamiliar units.
4. **Listening ports:** `ss -tulnp` — compare against your step-4 baseline from Procedure A; a new LISTEN entry is a new door.
5. **Outbound connections:** `ss -tnp` while idle — established connections to unfamiliar IPs deserve a question (DNS and your own SSH are expected).
6. For each finding: describe *what*, *where* (path/port/unit), *why suspicious*, and *first response* (isolate VM → snapshot → investigate — previewing M14's incident flow).

---

## Common Mistakes, Misconceptions, and Troubleshooting

| Mistake / misconception | Why it is wrong | Correction |
|---|---|---|
| Disabling the firewall/antivirus "to make it work" | Removes the control entirely instead of adding a rule | Add a specific allow rule; keep the layer on |
| Daily driving as root/administrator | One click or script = full compromise | Standard account + elevation only when needed |
| `chmod 777` as the fix for permission errors | World-writable = any process can modify | Diagnose owner/group; grant the *minimum* (`750`/`640`) |
| "I have sync, so I have backups" | Sync mirrors deletions and ransomware in real time | 3-2-1: independent copies + tested restores + offline/immutable copy |
| Encryption as malware protection | It protects *data at rest* on lost/stolen devices — useless against a logged-in session | Pair with patching, EDR/AV, least privilege |
| Fear-driven update avoidance ("they break things") | Unpatched = open door; rollbacks via snapshot handle breakage | Auto-update + snapshot before big upgrades |
| AV = full security | Signature-only detection misses new/behavioral attacks | Layered table in §4; behavior + privilege limits |
| "Hardening done" without verification | Unverified claims fail audits and hunts | Every step gets a verification artifact (Procedure A) |
| Reboot-needed patches sitting for weeks | Reboots postponed = patch gap in hours | Schedule maintenance windows; count days-to-patch |

**Troubleshooting:** *`ufw enable` killed my SSH* → you filtered port 22 before allowing it; use the VM console (not SSH) to `ufw allow 22/tcp`. *Keys-required SSH locked me out* → restore via VM snapshot; never set `PasswordAuthentication no` before a working key is verified. *`lynis` won't install* → it's in Ubuntu's universe repo (`sudo apt install lynis`); on minimal images enable universe first. *Windows BitLocker missing* → edition limitation (Home) — note it in your checklist as "encryption unavailable, mitigated by device tracking + backups" (an honest residual-risk entry, not a failure). *Restore test failed* → the backup never worked — fix the schedule/format **now**, that's the lab's whole point.

---

## Lab 5 — Hardened Workstation Evidence Pack and Planted-Indicator Hunt

*Active lab, isolated VM only. Overview: [Lab Collection](../../labs/README.md); rules: [Lab Safety Policy](../../lab-safety-policy.md).*

**Dedicated lab worksheet:** [LAB-04 — File Permissions and Endpoint Hardening](../../labs/lab-04-permissions-hardening/README.md) · [Full lab collection](../../labs/README.md).

**Objective:** a fully evidenced hardening pack (Linux required, Windows optional-but-claimed) + a five-indicator hunt.

**Steps:**

1. Create `portfolio/M05/`.
2. Run **Procedure A** on a fresh Ubuntu VM: all 10 table steps + before/after `lynis` scores + `hardening-checklist.md` (step → action → verification → risk treated).
3. Windows pass (own machine, eval VM, or VM you own): apply the listed baseline; screenshot each control's state. *(If a control is unavailable by edition, record it honestly as a residual-risk note.)*
4. **Backup test:** second copy of a folder in a *different* location + a successful restore screenshot. No credit for "backup configured" without a restore.
5. **Recovery-key check:** state where your disk-encryption recovery key is stored off-device (or why not applicable).
6. Run **Procedure B** — you need five findings. If your clean VM is *too* clean to find five, use the course's benign plant list: add a test user with a shell, a `@reboot` cron line running `echo test`, enable one extra service, open one listener (`python3 -m http.server 8000 &` **in the lab**), start one idle outbound connection — then hunt and document all five as if unknown.
7. Browser hygiene screenshot + the three accounts moved to a password manager (passwords themselves never appear in evidence).
8. Safety statement: targets used = *own lab VMs on host-only network*; isolation = *Procedure B proof attached (M04) — re-run if new VMs*.

**Completion check:** all 10 hardening steps evidenced with verifications; lynis before/after; restore test works; 5/5 hunt findings with what/where/why/first-response; browser pass done.

---

## Knowledge Check

*Formative — self-graded; retake until ≥ 80% (10 of 12).*

**Extend your practice:** [Module 05 quiz — more questions, worked answers, and outcome mapping](../../assessments/level-1/quiz-m05.md) · module-end review exercises are on the same page · [Assessment Hub](../../assessments/README.md)

**Multiple choice (8):**

1. "Every account gets only the rights needed for its job" describes:
   - (a) Defense in depth  (b) Least privilege  (c) Non-repudiation  (d) The patch gap
2. Which correctly pairs protection with what it does *not* do?
   - (a) BitLocker stops malware running in your session  (b) Disk encryption protects a lost powered-off device, not a logged-in session  (c) A sync folder protects against ransomware deletion  (d) AV guarantees detection of new malware
3. The 3-2-1 rule means:
   - (a) 3 devices, 2 networks, 1 firewall  (b) 3 copies, 2 media types, 1 offsite  (c) 3 admins, 2 passwords, 1 key  (d) 3 patches, 2 reboots, 1 snapshot
4. Which is a **persistence** location on Linux?
   - (a) `/etc/hosts`  (b) a `@reboot` cron entry  (c) the DNS resolver cache  (d) the firewall ruleset
5. EDR improves on classic antivirus mainly by:
   - (a) Scanning faster  (b) Monitoring behavior/telemetry and supporting response  (c) Replacing patching  (d) Encrypting disks
6. `chmod 777 file` is wrong because it:
   - (a) Makes the file executable only by root  (b) Grants read/write/execute to *everyone*  (c) Disables backups  (d) Corrupts the inode
7. Setting SSH `PasswordAuthentication no` before installing keys will:
   - (a) Improve speed  (b) Lock you out of your own VM  (c) Enable Telnet  (d) Rotate keys automatically
8. Why is a documented, verified baseline essential before a compromise hunt?
   - (a) It impresses auditors only  (b) "Unexpected" requires knowing "expected" — deviation needs a baseline  (c) It removes the need for EDR  (d) It patches automatically

**Short answer (4):**

9. Explain why "we have backups" can be false even when backup software reports success daily.
10. Describe the patch lifecycle in order and state where prioritization (KEV/CVSS) enters.
11. Give one example each of a Linux and a Windows hardening action that reduces *blast radius* (impact if compromised), and explain the mechanism.
12. Your `ss -tulnp` shows a new LISTEN entry you don't recall opening. Write your first four response steps in order.

<details>
<summary><b>Answer key</b> — attempt the questions first</summary>

1. **(b)** — least privilege (M01/M02's blast-radius control; full design in M07).
2. **(b)** — encryption is data-at-rest protection; a session with malware already runs as you. Sync mirrors deletions; AV is signature-limited (novel files slip).
3. **(b)** — and modern additions: tested restores + one immutable/offline copy.
4. **(b)** — cron (incl. `@reboot`), systemd units, shell rc files are auto-execution points; hosts/DNS/rules are not execution.
5. **(b)** — behavioral telemetry + investigation/response; scanning speed isn't the differentiator.
6. **(b)** — world-writable + executable: any user/process can modify — permission errors need minimal targeted grants (`750`/`640`).
7. **(b)** — the classic lockout; verify keys first, snapshot before changing sshd (Procedure A step 5).
8. **(b)** — anomaly detection is comparison against normal; without the baseline you have signals, not findings (this is why Procedure A step 4 lists every port's purpose).
9. *Model:* success messages can mask wrong targets (synced/encrypted backups that ransomware also reached), untested restores (nobody proved the files open), or single-location copies (disk dies with the original). Hence: independent copies, restore *tests*, offline/immutable copy.
10. Inventory → prioritize (KEV/exploited-in-wild first, then CVSS bands + exposure — Module 02) → test → deploy (auto where possible) → verify versions → record. Prioritization enters at step 2, before effort is spent.
11. *Linux:* run daily from a standard account with `sudo` only as needed — a compromised process inherits *user* rights, so it cannot install system-wide malware or alter other users' files. *Windows:* standard account + UAC — same mechanism: exploit lands with limited token, cannot reach admin-only resources; (alternatives: non-admin service accounts, `ufw` limiting which service an intruder can reach.)
12. (1) Identify what the process is (`ss -tulnp` shows PID/program; `ps -fp <pid>`), (2) decide expected vs. unknown against your baseline — don't kill yet (preserve evidence), (3) isolate: disconnect lab network / stop the VM (safety first, per policy), (4) snapshot for analysis, then document and trace how it started (cron/systemd/Run-key review) — the M14 flow in miniature.

</details>

## Scenario Exercises (Practice)

1. **Risk-to-control mapping.** Take four M02-style risks for a student laptop — stolen device, ransomware, unpatched browser drive-by, nosy sibling — and for each name: the endpoint control from this module, its type (preventive/detective/corrective) and nature (technical/administrative/physical).
2. **Backup design review.** A friend backs up their thesis daily to an external SSD kept plugged into the same laptop. Using 3-2-1 + immutability + restore-testing, critique the setup and redesign it on a $0 budget.
3. **Hunt write-up.** Turn one Procedure B finding into a mini incident note: what/where/why suspicious/first response/what log you'd want next — practicing M13/M14 language now.

## Key Takeaways

1. **Endpoints hold everything worth protecting** — hardening them is the highest-yield defensive work there is.
2. **Least privilege caps blast radius:** standard accounts, `sudo`/UAC elevation, minimal file permissions (`750` not `777`).
3. **Patching is a lifecycle, not a click:** inventory → prioritize (KEV/CVSS) → deploy → verify; auto-update is the right default.
4. **Protection is layered:** AV/behavioral EDR, application allowlisting, firewall, encryption, browsers — each covers a gap in the others; **disk encryption protects lost devices, not infected sessions.**
5. **Backups must obey 3-2-1 — plus tested restores and one offline/immutable copy.** Sync is not backup.
6. **Persistence lives in known places** (cron/systemd/rc files; Run keys/Startup/Tasks/services) — and knowing them turns "something feels off" into a repeatable hunt.
7. **A verified baseline is what makes detection possible** — every listener, account, and enabled service documented before you hunt.

## Self-Assessment Checklist

- [ ] I applied all 10 Ubuntu hardening steps with per-step verification evidence (Linux).
- [ ] I applied the Windows baseline steps (or recorded honest edition limitations as residual risk).
- [ ] `lynis` before/after scores are saved and the delta explained.
- [ ] My firewall is active with default-deny and only intended allows.
- [ ] A backup restore test succeeded from an independent copy (screenshot).
- [ ] I know where my disk-encryption recovery key is stored off-device.
- [ ] Browser pass done: auto-update, HTTPS-only, password manager, minimal extensions.
- [ ] I found and documented all 5 planted/persistence indicators (what/where/why/first response).
- [ ] `baseline-clean` snapshot taken and rollback verified.
- [ ] Scored ≥ 80% on the knowledge check.

*Level 1 complete when all boxes are checked → celebrate, then read the Level 2 gate in the [Course Roadmap](../../course-roadmap.md#progression-rules-and-course-completion) before Module 06.*

## Further Reading

Verified as of 2026-10-09.

- **CIS Benchmarks** (free registration) — vendor-specific hardening guides: <https://www.cisecurity.org/cis-benchmarks>.
- **NIST SP 800-123, *Guide to General Server Security*** (2008): <https://csrc.nist.gov/pubs/sp/800/123/final>.
- **Microsoft security baselines** — official recommended settings: <https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines>.
- **Ubuntu Security documentation** (updates, AppArmor, ufw): <https://documentation.ubuntu.com/security/>.
- **Lynis documentation** — auditing and hardening tool: <https://cisofy.com/documentation/>.
- **NIST SP 800-88 Rev. 1, *Guidelines for Media Sanitization*** (2014) — for end-of-life disks: <https://csrc.nist.gov/pubs/sp/800/88/r1/final>.
- **CISA #StopRansomware Guide** — backup/IR practices against ransomware: <https://www.cisa.gov/stopransomware>.

---

**Navigation:** [← Previous: Module 04](../module-04-networking-fundamentals-for-security/README.md) · [Module index](../README.md) · [Lab collection](../../labs/README.md) · [Reference Library](../../reference/README.md)
