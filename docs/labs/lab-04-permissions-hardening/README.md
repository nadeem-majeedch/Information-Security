---
title: "LAB-04 — File Permissions and Endpoint Hardening"
layout: default
---

# LAB-04 — File Permissions and Endpoint Hardening

**Lab ID:** LAB-04 · **Difficulty:** Introductory · **Estimated duration:** 2.5 hours · **Modules:** M05, M07 · **Mode:** Hands-on in **your own Linux VM (isolated)**

## Scenario

**Northside Clinic** (fictional, 8 staff) runs one Linux box holding patient-adjacent admin files. A junior admin once made a shared folder "just work" by running `chmod -R 777 /data` — and three years later, an audit finds every file world-writable and a rogue script hiding among them. You are hired to (a) demonstrate *why* permission bits matter with a safe sandbox, and (b) deliver a hardened permissions baseline for the clinic's box — using your own VM, not theirs.

## Learning Objectives

1. Read and explain `ls -l` permission strings (owner/group/other, rwx) and translate them into risk statements.
2. Apply `chmod` (symbolic and octal), `chown`, and `umask` deliberately, with recovery planning.
3. Detect common permission-based weaknesses: world-writable files, misplaced SUID bits, open home directories, permissive sudoers.
4. Produce a before/after audit (optionally with `lynis`) as evidence of hardening.

## Prerequisites and Required Skills

- Module 05 (hardening baseline) started; M04 (isolation proof) **required** before any VM work.
- Skills: Linux terminal basics — directory navigation, editing a file, running commands with `sudo`.

## Tools, Operating Systems, and Versions

- Ubuntu/Debian LTS ISO (free) in VirtualBox/VMware (free) — or any Linux VM you own.
- `lynis` (free, community edition): `sudo apt install lynis`.
- Standard coreutils (`ls`, `chmod`, `chown`, `find`, `umask`, `visudo`) — preinstalled.

## Setup (Free) and Required Permissions

1. Complete M04's **isolation proof** (host-only adapter; ping to public IP must fail).
2. Create a disposable VM snapshot named `pre-lab04`.
3. Work in a **scratch directory** (`~/perm-lab/`) for all destructive practice — never in `/etc` or your home root.
4. Permission scope: your VM only. `sudo` allowed **inside the VM only**; never run lab commands on your host OS.

## Lab Environment and Starting State

One Linux VM, freshly snapshotted, with a scratch tree you create in Task 1. Starting state: default Ubuntu permissions, `lynis` baseline recorded, no changes made.

## Tasks

1. **Build the sandbox:**
   ```bash
   mkdir -p ~/perm-lab/{shared,private,scripts}
   echo "salary data" > ~/perm-lab/shared/budget.txt
   echo "#!/bin/sh\necho hello" > ~/perm-lab/scripts/deploy.sh && chmod +x ~/perm-lab/scripts/deploy.sh
   ls -l ~/perm-lab
   ```
   *What it does:* creates three folders, two files, and marks the script executable. `ls -l` shows the permission string (e.g. `-rw-r--r--` = owner rw, group r, other r).
2. **Decode:** write the meaning of each of your three files' permission strings in words (Task output → `permissions-decoded.md`).
3. **Permission surgery (all inside `~/perm-lab`):**
   - `chmod 600 shared/budget.txt` (octal: owner rw, everyone else nothing — *sensitive file pattern*).
   - `chmod g+w shared/budget.txt`? No — first `chgrp` a group you belong to (`groups` lists yours), then `chmod g+w` — demonstrate group collaboration safely.
   - `chmod 777 scripts/` then observe `ls -l` (world-writable directory) — then `chmod 755 scripts/` to restore. **Recovery note:** every change here is one command away from reversible; that's why we practice in scratch space.
   - `umask` — run `umask` before/after `umask 077`, create a file, observe the default permissions change (077 ⇒ new files are owner-only).
4. **Find weaknesses (clinic-style audit):**
   ```bash
   sudo find / -xdev -perm -0002 -type f 2>/dev/null | head -20   # world-writable files
   sudo find / -xdev -perm -4000 -type f 2>/dev/null              # SUID files
   ls -ld /home/*                                                  # home dirs should be 750-ish, not 777
   ```
   *What they do:* `find` scans one filesystem (`-xdev`), matching files with *any* write bit for others (`-perm -0002`) or the SUID bit (`-perm -4000` — a file that runs with its **owner's** privileges, a classic escalation plant when writable by non-owners). Explain each hit: expected (e.g. `/usr/bin/sudo` is legitimately SUID) vs suspicious.
5. **Sudoers (read-only + one safe change):** run `sudo visudo -c` (checks syntax without editing). Read `/etc/sudoers` via `sudo grep -E '^(root|%sudo)' /etc/sudoers`. **Never edit with a normal editor** — a syntax error can lock you out; `visudo` validates before saving (that's its whole purpose; recovery: VM snapshot).
6. **Harden + measure:** apply clinic baseline — fix any scratch world-writable files you created, ensure your user's home is `chmod 700`, document sudo policy as found. Run `sudo lynis audit system` **before** (Task 1... actually at start) and **after**; save both reports and note the Hardening Index delta.
7. **Report** (deliverable below).

## Expected Observations

- `chmod 600` output shows `rw-------`; group write requires shared group membership (or the write silently affects only your own group).
- World-writable scan on a fresh Ubuntu returns few/no hits (good baseline) — clinic's `777 -R` would return thousands; state this contrast.
- SUID list includes standard binaries (`/usr/bin/passwd`, `sudo`, `mount`) — the skill is *reviewing* the list, not fearing it.
- `umask 077` makes new files `rw-------` — visible immediately in `ls -l`.
- `lynis` Hardening Index typically rises several points after even this small pass (exact numbers vary by version — record *yours*).

## Investigation Questions

1. `budget.txt` after `chmod 600`: can the clinic's *backup service account* still read it? What permission model problem does this expose (services need group rights — link to M07 least privilege)?
2. Why is world-writable + SUID together catastrophic? Sketch the three-step abuse path.
3. `visudo` exists because of which failure mode? What is your documented recovery path if sudo is ever broken (snapshot!)? 
4. Does `chmod 700 ~` protect data if the disk is stolen? (No — that's encryption's job; M05 §5.) Which control answers theft?
5. Is "everyone in `sudo` group" (default Ubuntu) least privilege for a 6-person clinic? Propose a better split (admins vs users) in two sentences.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `chgrp: permission denied` | Group not yours / target not owned | Use `groups` to pick your group; operate only inside `~/perm-lab` |
| `find` hits nothing | Expected on clean system, or wrong `-perm` syntax | `-perm -0002` (any-write) not `-perm 777` (exact); run the SUID variant too |
| sudoers scare / sudo broken | Edited outside `visudo` or wrong permissions | Roll back to `pre-lab04` snapshot — this is why it exists |
| `lynis` not found | Package name/repo | `sudo apt update && sudo apt install lynis` |
| Permission denied after `chmod 600` on *your own* file | Expected — you removed your read? (600 keeps owner rw; check who you're logged in as) | `whoami`; owner still has access under 600 |

## Evidence to Collect

- `permissions-decoded.md` (Task 2) + before/after `ls -l` outputs for every Task 3 change.
- Audit outputs: world-writable and SUID scan results with your expected/suspicious annotations.
- `lynis` before/after reports + Hardening Index delta.
- Sudoers review notes (read-only findings + recovery plan).
- Safety statement: *all changes confined to my snapshot-lab VM; scratch directory only; no host or network changes.*

## Deliverable and Report Structure

`portfolio/LAB-04/`: (1) sandbox description + isolation proof reference (M04), (2) decoded permissions, (3) surgery log (command → purpose → before/after), (4) clinic audit findings table (finding / risk / recommended fix), (5) lynis delta, (6) safety statement. 2 pages max.

## Completion Checklist

- [ ] Isolation proof attached (or referenced from M04, re-run if VM changed)
- [ ] Scratch tree created; all six permission experiments evidenced
- [ ] `umask` change demonstrated with before/after files
- [ ] World-writable + SUID scans run and annotated (expected vs suspicious)
- [ ] `visudo -c` and sudoers read-only review completed; recovery path documented
- [ ] lynis before/after with recorded delta
- [ ] Safety statement written

## Cleanup and Reset

1. Remove the scratch tree: `rm -rf ~/perm-lab` (deletes only what Task 1 created — check the path before pressing Enter; **this is the one destructive command in the lab**, scoped to your own scratch folder).
2. Undo any home permission change you made (`chmod 755 ~` if you set 700 and prefer default).
3. Revert VM to `pre-lab04` snapshot if you want a pristine machine for the next lab — **or** keep it and re-run M05's `baseline-clean` flow.
4. Delete lynis reports from the VM after copying them to your portfolio.

## Optional Challenges

- Demonstrate the SUID abuse path *safely*: copy `/bin/bash` to `~/perm-lab/`, `chmod 4755` your *copy* (it runs as you — no privilege gained), then explain why the same bit on a root-owned binary matters.
- Write the clinic's `/data` permissions policy: owner/group/umask rules in 5 clauses (M03 practice).
- Repeat the audit on Windows (your own machine): compare NTFS ACLs vs POSIX modes in a half-page table.

## References and Safety Notes

- `chmod(7)`, `sudoers(5)`, `find(1)` man pages (installed: `man chmod`).
- CIS Benchmarks (free) — Linux file-permission recommendations: <https://www.cisecurity.org/cis-benchmarks>.
- Lynis documentation: <https://cisofy.com/documentation/>.
- Course: [M05](../../modules/module-05-operating-system-and-endpoint-security/README.md) · [M07](../../modules/module-07-identity-and-access-management/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** `sudo` only inside your lab VM; destructive commands only against `~/perm-lab` with the path echoed first; no scanning, no network targets, no host-OS changes. Snapshot before starting = your recovery guarantee.

**Navigation:** · [← Previous: LAB-03](../lab-03-password-hashes/README.md) · [Lab index](../README.md) · [Next: LAB-05 →](../lab-05-hashing-integrity-signatures/README.md)
