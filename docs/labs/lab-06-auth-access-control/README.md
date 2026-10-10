---
title: "LAB-06 — Authentication, Access Control, and Least Privilege"
layout: default
---

# LAB-06 — Authentication, Access Control, and Least Privilege

**Lab ID:** LAB-06 · **Difficulty:** Intermediate · **Estimated duration:** 2.5 hours · **Module:** M07 · **Mode:** Hands-on in **your own Linux VM (isolated)**

## Scenario

**Bright Books** (fictional accounting firm, 12 staff) is migrating from a shared login ("everyone uses `accountant`") to per-person access after a dispute over who changed a client file. As the incoming security analyst you must prove — on a sandbox — how role-based access control (RBAC) and least privilege work in practice: who can read client data, who can modify it, who administers the box, and how you'd *verify* each rule and detect a violation. All identities are synthetic.

## Learning Objectives

1. Create users/groups and implement an RBAC permission matrix with standard Linux tools.
2. Demonstrate the difference between authentication ("who are you") and authorization ("what may you do") using concrete access tests.
3. Apply least privilege: grant, verify, then *revoke and show the denial* — evidence in both directions.
4. Evaluate shared-account risks and design an MFA recommendation consistent with NIST SP 800-63-4.
5. Audit privilege assignment (sudo membership, SUID, writable-by-others files) and justify each finding.

## Prerequisites and Required Skills

- M04 isolation proof; M05 hardening baseline; M07 module concepts (IAAA, RBAC, least privilege).
- Skills: Linux terminal (users, groups, files), editing with `sudoedit`/`visudo`.

## Tools, Operating Systems, and Versions

- Ubuntu/Debian VM (free) in VirtualBox/VMware (free). Core tools: `adduser`/`useradd`, `groupadd`, `chgrp`, `chmod`, `getfacl`/`setfacl` (package `acl` — `sudo apt install acl`), `sudo`, `id`, `su`.
- Optional: KeePassXC (free) to demonstrate password-manager-based unique credentials.

## Setup (Free) and Required Permissions

1. Isolation proof from M04 re-run for this VM (or reuse `baseline-clean` snapshot); take snapshot `pre-lab06`.
2. Create scratch scope: only users/groups/directories you name below — **your lab VM only**.
3. `sudo` inside the VM only. No network targets; no scanning of anything.

## Lab Environment and Starting State

One Linux VM with three synthetic people and one client-data folder you create in Task 1. Starting state: no extra users, no project directory, no RBAC.

**Actors (synthetic):** `alice` (partner — full client read/write), `bob` (junior — read-only clients), `carol` (IT admin — system management, *no* client data by default).

## Tasks

1. **Provision (authN scaffolding):**
   ```bash
   sudo groupadd clients        # group for client-data access
   sudo adduser alice --disabled-password   # account exists, no usable password (key/console auth)
   sudo adduser bob   --disabled-password
   sudo adduser carol --disabled-password
   sudo usermod -aG clients alice           # -a = append, -G = supplementary group
   ```
   *What each does:* creates the access group and three named identities. `id alice` shows uid/group membership — the **identity record** everything else keys off.
2. **Data + matrix:**
   ```bash
   sudo mkdir -p /srv/clients && echo "CLIENT: Alpha Ltd — fee 5000" | sudo tee /srv/clients/alpha.txt
   sudo chown -R root:clients /srv/clients && sudo chmod -R 750 /srv/clients
   ```
   *What it does:* creates client data owned by group `clients` with 750 (owner rw+x, group r+x, others nothing) — the DAC encoding of your matrix. **Matrix to implement:** alice: rwx on `/srv/clients`; bob: rx (read, cannot modify); carol: *no* access to `/srv/clients`, full admin rights elsewhere.
3. **Authorization tests (authZ proof — both directions):**
   - `sudo -u alice cat /srv/clients/alpha.txt` → **works** (runs as alice).
   - `sudo -u bob sh -c 'echo hack >> /srv/clients/alpha.txt'` → **denied** (group has r+x, not w) — the denial is your evidence.
   - `sudo -u carol cat /srv/clients/alpha.txt` → **denied** (carol not in `clients`).
   Record every command + output. This is *authorization failing/succeeding for an authenticated identity* — the IAAA distinction made visible.
4. **Fine-grained with ACLs (optional but recommended):** `sudo apt install acl; sudo setfacl -m u:bob:r /srv/clients/alpha.txt; getfacl /srv/clients/alpha.txt` — grant per-user rights *without* group reshuffling; explain when ACLs beat group membership (temporary contractor!).
5. **Shared-account teardown:** contrast the new model vs Bright Books' old shared login: list 4 concrete forensic/authorization failures of shared accounts (no attribution — who changed the file? no revocation when someone leaves; no MFA possible per-person; audit logs meaningless). Draft the replacement rule in one policy sentence (M03 style).
6. **MFA recommendation:** for alice/bob/carol accounts, recommend an authenticator approach per NIST SP 800-63-4 thinking: phishing-resistant options (passkeys/FIDO2) preferred for admins (carol), TOTP acceptable for others, SMS discouraged; include account-recovery story (who approves recovery, with what ID check). One paragraph — no real MFA deployment required.
7. **Privilege audit:**
   ```bash
   getent group sudo                       # who can administer?
   sudo find /srv -perm -0002 2>/dev/null  # anything world-writable in scope?
   sudo grep -R "NOPASSWD" /etc/sudoers.d/ 2> | head
   ```
   *What they do:* enumerate admin rights, find open write paths, and list passwordless sudo entries. For each result: justified or excessive? (Least-privilege review.)
8. **Revoke + re-test:** `sudo gpasswd -d alice clients` (remove alice from group) → re-run her cat test → **denied**. Restore with `usermod -aG clients alice`. *Both states documented* = provisioning **and** de-provisioning evidence (the "leaver" workflow).

## Expected Observations

| Test | Expected |
|---|---|
| alice reads client file | Success (group `clients`, 750) |
| bob appends to client file | `Permission denied` (no group write) |
| carol reads client file | `Permission denied` (not in group) — even though she is a sudo admin |
| ACL grant on one file | `getfacl` shows named-user entry; group model untouched |
| After `gpasswd -d` | alice denied; after re-add, allowed |
| Audit | `clients` group = exactly alice (+bob); NOPASSWD entries minimal/none |

**Key insight to record:** carol can `sudo` her way to anything — that's *why* admin accounts shouldn't casually join data groups, and why her day-to-day should still avoid root where possible (separation of duties preview).

## Investigation Questions

1. carol is in `sudo` yet "denied" — explain in IAAA terms why that is correct behavior and what single command would break the design (and why she shouldn't use it casually).
2. Bright Books' shared account: which of your Task-3 tests would be *impossible* to run there? What does that mean for incident response (M14 preview)?
3. Bob's rights changed from r to rw "for one week" — design the change: who approves, what command, how you verify, when it reverts. (Process, not just command!)
4. NIST 800-63-4 framing: why is "password + SMS code" weaker than a passkey for alice? Name the attack each resists.
5. Which is worse for least privilege: too many group members, or NOPASSWD sudo? Defend with blast-radius reasoning (M05).

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `adduser: user already exists` | Leftover from a retry | `sudo deluser alice` (only your synthetic user) and recreate — or revert `pre-lab06` |
| bob *can* write — test failed | Directory default perms, or you're in group yourself | Check `ls -ld /srv/clients` (need 750 + group `clients`); confirm `groups` of the *test user*, not yours |
| `sudo -u alice` asks password | You used `--password` creation | Accounts were created `--disabled-password`; `sudo` from root doesn't need their password |
| `getfacl: command not found` | acl package missing | `sudo apt install acl` |
| Permission denied editing sudoers | By design | Use `sudo visudo` (never a plain editor) |
| VM lost network after group changes | Unrelated — adapter setting | Check host-only adapter in VM settings; isolation must still hold (ping public must fail) |

## Evidence to Collect

- `rbac-matrix.md` — intended matrix + implemented command per cell.
- `authz-tests.md` — all test commands with outputs, **including denials** (marked ✅/❌ with meaning).
- ACL demo output (`getfacl` before/after).
- Shared-account risk list + policy sentence; MFA recommendation paragraph.
- Audit outputs (sudo group, world-writable, NOPASSWD) with verdicts.
- Revocation cycle evidence (Task 8).
- Safety statement: *synthetic users on my isolated lab VM only; no real accounts, no network services touched.*

## Deliverable and Report Structure

`portfolio/LAB-06/`: (1) design (matrix + reasoning), (2) implementation (commands), (3) verification (test log both directions), (4) shared-account analysis + MFA policy paragraph, (5) privilege audit with verdicts, (6) safety statement. 2–3 pages.

## Completion Checklist

- [ ] Three synthetic users + `clients` group created; ownership/mode set as specified
- [ ] All six authorization tests recorded with expected allow/deny outcomes
- [ ] ACL per-user grant demonstrated with `getfacl` output
- [ ] Four shared-account failures documented + one policy sentence
- [ ] MFA recommendation per SP 800-63-4 (passkey for admin, TOTP ok, SMS discouraged) with recovery story
- [ ] Privilege audit run with justified/excessive verdicts
- [ ] Revoke → deny → restore → allow cycle evidenced
- [ ] Safety statement written

## Cleanup and Reset

1. Remove synthetic identities: `sudo deluser alice; sudo deluser bob; sudo deluser carol; sudo delgroup clients; sudo rm -rf /srv/clients` — **only** the exact names you created (echo them first). *Purpose: leave the VM as `baseline-clean`-like state for the next lab.*
2. Remove the `acl` package only if you want the pristine base (`sudo apt remove acl` — optional).
3. Best option: revert to `pre-lab06` snapshot after copying evidence to your portfolio.
4. Confirm no real credentials exist anywhere in evidence (synthetic names only).

## Optional Challenges

- Implement a deny-by-default firewall rule for a "client service" port and show bob/alice/carol connectivity differences from a second lab VM (ties to LAB-08).
- Draw the provisioning/de-provisioning lifecycle (joiner/mover/leaver) as a 6-box diagram for Bright Books.
- Script the RBAC setup as an idempotent shell script (`setup_rbac.sh`) — seed for LAB-18.

## References and Safety Notes

- NIST SP 800-63-4 (Jul 2025) — Digital Identity Guidelines: <https://pages.nist.gov/800-63-4/>.
- `useradd(8)`, `usermod(8)`, `sudoers(5)`, `setfacl(1)` man pages.
- OWASP *Authorization Cheat Sheet*: <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>.
- Course: [M07](../../modules/module-07-identity-and-access-management/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** synthetic identities only, on your isolated VM; no real accounts created or touched; no password spraying, no network logins to third parties; `deluser`/`rm -rf` targets echoed and scoped to your own lab names.

**Navigation:** · [← Previous: LAB-05](../lab-05-hashing-integrity-signatures/README.md) · [Lab index](../README.md) · [Next: LAB-07 →](../lab-07-packet-analysis/README.md)
