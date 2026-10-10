---
title: "LAB-08 — Firewall Rule Analysis and Host Configuration Audit"
layout: default
---

# LAB-08 — Firewall Rule Analysis and Host Configuration Audit

**Lab ID:** LAB-08 · **Difficulty:** Intermediate · **Estimated duration:** 2.5 hours · **Modules:** M08, M05 · **Mode:** Hands-on in **your own isolated lab network (two VMs)**

## Scenario

**Harborview Library** (fictional) runs a public-access kiosk Linux box in the lobby. A consultant left behind a ruleset described as "temporary": SSH open to everyone, HTTP allowed from anywhere, and a mystery rule nobody remembers. Management wants you to (1) analyze the firewall rules for meaning and risk, (2) verify actual exposure from *inside* the lab network — where you're authorized, (3) audit host configuration against the listening ports, and (4) deliver a tightened ruleset with before/after evidence. Scope: your two lab VMs only.

## Learning Objectives

1. Read and explain `ufw`/`iptables`-style rules: direction, source, destination, action, order sensitivity.
2. Verify firewall behavior empirically with **authorized** probes against a lab peer (port open vs filtered).
3. Reconcile *listening sockets* (`ss`) against *permitted traffic* (firewall) — identify gaps in both directions.
4. Audit host configuration (services, accounts, updates) against a documented baseline and rate findings.
5. Produce a least-privilege ruleset with justification per rule and confirm with before/after tests.

## Prerequisites and Required Skills

- M04 **isolation proof** (mandatory — this lab scans lab IPs), M05 hardening, M08 module (firewalls/IDS concepts).
- Skills: Linux terminal, reading rule tables, running `nmap` against listed lab targets only.

## Tools, Operating Systems, and Versions

- Two Ubuntu VMs (free) on a host-only network: **kiosk** (`192.168.56.30`) and **tester** (`192.168.56.31`) — IPs you assign; any host-only range works.
- `ufw` (preinstalled on Ubuntu; `sudo ufw status verbose`), `ss`/`netstat`, `nmap` (free; `sudo apt install nmap`), `lynis` (free, optional).
- All probes target `192.168.56.30` **only** — a machine you built, listed in your scope statement.

## Setup (Free) and Required Permissions

1. Re-run isolation proof: from *both* VMs, public ping must **fail**; peer ping must **succeed**. Screenshot it.
2. Snapshot both VMs: `pre-lab08`.
3. Scope/authorization statement (write it): *"Targets: 192.168.56.30 and .31, my own VMs on host-only network, dates: this lab session. Methods: local service tests + TCP connect scans from .31 to .30. Out of scope: everything else."* (Template from M03 — this is your authorization record.)
4. On **kiosk**: start two test services you control: `python3 -m http.server 8000` (web demo) and keep SSH available if you enabled it. Do not install anything else.

## Lab Environment and Starting State

Two VMs, host-only, isolated. Kiosk firewall begins in a deliberately flawed state you create to match the consultant's story:

```bash
sudo ufw reset            # y to reset — resets ONLY ufw rules on this lab VM (reversible: you are re-adding them below)
sudo ufw default allow incoming     # the "temporary" mistake: default-open
sudo ufw allow 22/tcp      # SSH from anywhere
sudo ufw allow 8000/tcp    # demo web server from anywhere
sudo ufw enable            # ufw is inactive until enabled; this applies rules
sudo ufw status numbered   # list with order numbers
```

*What these do:* `ufw` (Uncomplicated Firewall) is Ubuntu's iptables front-end; **rule order matters** (first match wins); `default allow incoming` means anything not explicitly mentioned is **open** — the exact flaw you'll fix. **Safety note before `enable`:** if you manage these VMs over SSH, allow SSH *before* enabling, or your session may drop — recovery = VM console (not SSH) + `ufw allow 22/tcp`, or revert the snapshot. Never run these on your host or any non-lab machine.

## Tasks

1. **Read the starting ruleset:** `sudo ufw status numbered verbose` — decode every column into English sentences (direction, action, source, port). Record in `rules-decoded.md`. Flag each rule as *justified / excessive* for a lobby kiosk (who legitimately needs SSH? From where?).
2. **Measure actual exposure (authorized probes):** from **tester** run:
   ```bash
   nmap -sT -Pn 192.168.56.30        # TCP connect scan of your lab target: which ports appear open?
   nmap -sT -Pn -p 22,8000,3306 192.168.56.30
   ```
   *What `-sT` does:* full TCP handshakes (the polite, standard detection — exactly what a real connection attempt looks like); `-Pn` skips host discovery; `-p` limits to named ports. **Interpret:** port 8000 open + SSH open = matches the loose ruleset; a port you never opened but appears open (e.g., 3306) = host listening *and* allowed by "default allow" — your first finding. Record output.
3. **Reconcile listeners vs rules:** on kiosk: `ss -tulnp` — list every LISTEN socket with owning process. Build a two-column table: *listening service* × *reachable from tester (yes/no per nmap)*. Both directions of mismatch matter: (a) listening + reachable but shouldn't be; (b) allowed by firewall but nothing listening (dead rule — remove).
4. **Harden the ruleset (least privilege):**
   ```bash
   sudo ufw default deny incoming     # flip the consultant's mistake
   sudo ufw default allow outgoing    # kiosk needs updates/DNS out
   sudo ufw delete <n>                # delete excessive rules by number (shown by status numbered) — double-check the number!
   sudo ufw allow from 192.168.56.31 to any port 22 proto tcp   # SSH only from your tester (lab-scoped admin)
   sudo ufw allow 8000/tcp            # demo service (consider restricting source too)
   sudo ufw status numbered           # verify final order
   ```
   *Explain each rule you keep* — direction, source, port, purpose. Order: specific allows before any catch-all; deny by default.
5. **Re-test (before/after proof):** repeat Task 2's nmap commands. Expected change: ports that were open only due to "default allow" now show **filtered/closed**; 8000 and 22 (from .31) still work. Save both outputs side by side.
6. **Host audit beyond firewall:** on kiosk run `ss -tulnp`, `systemctl list-unit-files --state=enabled`, and (optional) `sudo lynis audit system --quick`. Findings to rate (baseline = M05 checklist): unnecessary listening services, services enabled without need, weak points a firewall *cannot* fix (unpatched package, shared account). Produce an audit table: *finding / evidence / risk / fix / owner*.
7. **Report** with recommended final ruleset (Task 4) + audit table + a one-paragraph "what the firewall does NOT protect" section (from Task 6 findings).

## Expected Observations

| Phase | Expected |
|---|---|
| Starting ruleset | `default allow incoming`; port 8000 + 22 allowed; `status` shows "Anywhere" sources (excessive for a kiosk) |
| nmap before | 8000 open; plus any other listening port (e.g., 3306 if a DB listens) also **open** — proof "default allow" exposes everything |
| After hardening | Previously-open unexpected ports now `filtered`; 8000 still open; 22 open **from .31 only** |
| Reconciliation table | Every open port traceable to a service *and* a deliberate rule — no orphans either way |
| Audit | ≥ 1 real finding firewall can't fix (patch level, account hygiene, or enabled-but-unused unit) |

## Investigation Questions

1. Rule order: with rules `[1] allow 22 from .31` and `[2] deny 22` (hypothetical), what happens for .31? Why does `status numbered` order matter when editing?
2. You deleted a rule by number *after* another deletion — what happened to the numbering? (ufw renumbers on each change — re-check before every delete. This is why Task 4 tells you to re-run `status numbered`.)
3. nmap shows 8000 "open" even though a rule allows it — would nmap from the *internet* reach it? (No: host-only network is unreachable — isolation beats rules here; defense in depth.) Which layer did that protection come from?
4. The kiosk's SSH rule is source-limited to `.31`. List two more controls that would harden SSH even further (key-only auth from M05; fail2ban-style rate limiting — M13 detection tie-in).
5. Audit finding: a world-writable directory under the web root — would any firewall rule have prevented exploitation? What control class is missing?

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Lost SSH after `ufw enable` | Default policies + your source not allowed | Open VM **console** (not SSH): `ufw allow 22/tcp`, or revert `pre-lab08` |
| nmap shows all ports open | Rules never applied (ufw inactive) or default allow still on | `sudo ufw status verbose` — "inactive" ⇒ `sudo ufw enable` |
| Peer ping fails | Isolation/adapter mis-set | Re-check host-only on both VMs; positive/negative isolation tests (M04 §4.3) — if public ping succeeds you are **not isolated**: stop and fix |
| `nmap: command not found` | Package missing | `sudo apt install nmap` (in the tester VM) |
| Port 8000 "closed" though allowed | Server not running / bound only to localhost | Re-run `python3 -m http.server 8000` in kiosk; check `ss -tulnp` shows `0.0.0.0:8000` not `127.0.0.1:8000` |
| `ufw delete` removed wrong rule | Number shifted after previous delete | Always re-run `sudo ufw status numbered` immediately before deleting |

## Evidence to Collect

- Scope/authorization statement (Task setup).
- Isolation proof (both VMs) + VM labels/IPs.
- `rules-decoded.md`; nmap **before** and **after** outputs; `ss -tulnp` snapshot.
- Reconciliation table; final ruleset (`ufw status numbered` output); host-audit table with risk ratings.
- Safety statement: *probes only 192.168.56.30/.31 (own VMs, host-only, isolated); no external targets.*

## Deliverable and Report Structure

`portfolio/LAB-08/`: (1) scope + isolation, (2) initial ruleset decoded + verdicts, (3) before/after exposure evidence, (4) listener-vs-rule reconciliation, (5) recommended ruleset with per-rule justification, (6) host audit table + "what firewalls can't fix" note, (7) safety statement. 2–3 pages.

## Completion Checklist

- [ ] Isolation proof (positive + negative tests) for both VMs
- [ ] Written scope/authorization statement with IPs and methods
- [ ] Starting ruleset decoded; excessive rules flagged
- [ ] Authorized nmap before/after with interpretation
- [ ] Listener ↔ rule reconciliation table (both mismatch types addressed)
- [ ] Hardened ruleset applied, ordered, per-rule justified
- [ ] Host audit table ≥ 4 findings with risk/fix/owner
- [ ] Safety statement written

## Cleanup and Reset

1. Stop test services (`Ctrl+C` the http.server).
2. Reset firewall to your M05 baseline on the kiosk: `sudo ufw reset` → re-apply just SSH + needed allows (or revert `pre-lab08` snapshot — cleanest).
3. Optionally uninstall nmap (`sudo apt remove nmap`) — not required.
4. Delete the scope statement's temp files only after the portfolio copy exists.
5. Confirm both VMs still fail public pings (isolation intact for the next lab).

## Optional Challenges

- Add a second service (e.g., `nc -l 9999` **in the lab**) and write the allow/deny matrix for three sources (.31, other lab IP, "Anywhere") before testing it.
- Capture the nmap scan from the *kiosk's* perspective in Wireshark (LAB-07 skill): see the SYN sequence and your firewall's refusal — annotate RST/no-response behavior.
- Translate your final ruleset into a 5-clause firewall policy for Harborview (M03 practice).

## References and Safety Notes

- Ubuntu firewall docs (`ufw`): <https://documentation.ubuntu.com/server/how-to/security/firewalls/>.
- NIST SP 800-41 Rev. 1, *Guidelines on Firewalls and Firewall Policy*: <https://csrc.nist.gov/pubs/sp/800/41/r1/final>.
- Nmap book/guide (official): <https://nmap.org/book/man.html>.
- Course: [M08](../../modules/module-08-network-security/README.md) · [M05](../../modules/module-05-operating-system-and-endpoint-security/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** scanning is limited to the two VMs you own on an isolated host-only network, per your written scope (Safety Policy §3). `ufw`/`nmap` never pointed at any other address — including your home router, LAN devices, or public hosts. Destructive-ish commands (`ufw reset`, `enable`) explained with console/snapshot recovery paths.

**Navigation:** · [← Previous: LAB-07](../lab-07-packet-analysis/README.md) · [Lab index](../README.md) · [Next: LAB-09 →](../lab-09-secure-coding/README.md)
