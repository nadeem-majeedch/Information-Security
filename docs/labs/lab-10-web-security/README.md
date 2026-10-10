---
title: "LAB-10 — Web Security on a Local Deliberately Vulnerable Application"
layout: default
---

# LAB-10 — Web Security on a Local Deliberately Vulnerable Application

**Lab ID:** LAB-10 · **Difficulty:** Intermediate · **Estimated duration:** 3 hours · **Module:** M09 · **Mode:** Offensive exercises **against a local app you run, on an isolated machine**

## Scenario

**MaplePay** (fictional demo fintech) is about to demo a customer portal and asks you to sanity-check the "usual web problems" before architects review it. You won't touch MaplePay's real anything — instead you run the industry-standard training target **OWASP Juice Shop** locally (the course's stand-in), discover and document at least six issues spanning different OWASP Top 10:2025 categories, and deliver a vulnerability report in professional format. Every request you send goes to `127.0.0.1` — your machine, your process.

## Learning Objectives

1. Run a deliberately vulnerable web app locally and confirm its exposure boundary (localhost only).
2. Discover ≥ 6 vulnerabilities spanning ≥ 5 OWASP Top 10:2025 categories using browser tools and an intercepting proxy.
3. Capture reproducible evidence (request/response pairs) for each finding.
4. Write findings as professional reports: steps, evidence, impact, remediation, severity (CVSS v4.0-style reasoning).
5. Map each finding to an OWASP ASVS requirement area — verification, not just discovery.

## Prerequisites and Required Skills

- M09 module (Top 10 categories), M04 isolation proof, M03 authorization frame (this lab *is* your authorized target).
- Skills: browser DevTools basics; comfort installing/running a container or downloading a release.

## Tools, Operating Systems, and Versions

| Tool | Purpose | Source |
|---|---|---|
| OWASP Juice Shop (current release) | Training target | Official: `docker run` image `bkimminich/juice-shop` **or** release bundle from `github.com/juice-shop/juice-shop` (free) |
| Docker Engine **or** Node.js 18/20 **or** prebuilt VM image | Runs it | Docker: free (Linux engine); Node: nodejs.org |
| Browser DevTools (built-in) | Inspect/modify requests | any browser |
| OWASP ZAP (current, free) or Burp Suite Community | Intercepting proxy | free downloads |
| Optional second target: DVWA (local) | Practice rotation | `github.com/digininja/DVWA` (free; PHP+MySQL, e.g., via local VM) |

**$0.** If Docker is unavailable: download the Juice Shop release `.zip`/installer and run it with Node — either path works; state which you used.

## Setup (Free) and Required Permissions

1. Isolation recommended: run on your lab VM (host-only) **or** on your own machine with strict localhost binding.
2. Start target (Docker path — note the `127.0.0.1:` binding; it is the safety mechanism):
   ```bash
   docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
   ```
   *What it does:* pulls the official training image, publishes container port 3000 **only on your loopback interface** (`--rm` removes the container on stop), so no other machine can reach it. Verify: open `http://127.0.0.1:3000` — the shop loads; from another device/VM, it must **not** (test if you have a second VM).
3. Authorization record (write in your notes): *"Target: OWASP Juice Shop v<version>, run by me, bound to 127.0.0.1 on my machine, session: this lab. Scope: this app only. No third-party sites, no real payment data (the app's data is fake)."*
4. Configure your proxy (ZAP/Burp) to capture browser traffic via its proxy listener (ZAP: default proxy port 8080; set browser proxy or use ZAP's embedded browser). Certificates: import the proxy's CA so HTTPS is readable **in your browser only**.

## Lab Environment and Starting State

Local Juice Shop at `http://127.0.0.1:3000`, preloaded with its standard fake data (fake users, fake orders, no real data anywhere). Your portfolio folder empty. Starting state: no findings.

## Tasks

1. **Baseline & boundary check:** load the app; confirm via `docker ps` (or `ss -tulnp | grep 3000`) that it listens on `127.0.0.1:3000`, not `0.0.0.0`. Record this — it's part of your safety statement.
2. **Recon through DevTools:** browse with the Network tab open: note API endpoints (`/api/…`), JWT-ish tokens, error behaviors. List 5 endpoints in `recon.md`.
3. **Find six findings across five Top 10 categories.** Use Juice Shop's own challenge hints (its scoreboard at `/#/score-board` lists challenge names — using them is legitimate training), or your proxy. Target spread (examples — verify yourself, document what you actually did):
   - **A01 Broken Access Control:** view another user's order/data by manipulating an ID (IDOR-style).
   - **A02 Cryptographic Failures:** find data exposed because something wasn't encrypted/obscured (e.g., error/debug info, exposed sensitive field).
   - **A03 Injection:** SQL-injection-style login bypass or search injection (through the app's injection challenge).
   - **A05 Security Misconfiguration:** exposed panel/backup/debug feature.
   - **A07 Identification & Authentication Failures:** weak login/recovery behavior (e.g., default/known credentials on a demo account, or JWT weakness).
   - **A04 Insecure Design** (bonus): business-logic flaw — e.g., placing a negative quantity/price order.
4. **Capture evidence per finding:** for each — (a) exact steps (URL/clicks/payload), (b) request/response from the proxy (sanitize: it's fake data, but habit matters), (c) why it works (root cause in one sentence), (d) fix (code/config-level), (e) severity with **CVSS v4.0-style reasoning** (attack vector — network? credentials needed? user interaction?) — compute an approximate vector string or explain the rating qualitatively; (f) ASVS area mapped (e.g., "V5 Validation, Sanitization and Encoding").
5. **False-start reflection:** list one thing you tried that failed and why (proxy didn't intercept, payload filtered) — troubleshooting is part of the craft.
6. **Report** (deliverable below): executive summary (3 sentences), finding table, then findings in full.
7. **DVWA rotation (optional):** if you set up DVWA locally, repeat injection + XSS at LOW and MEDIUM security, then explain what the MEDIUM mitigation fails to stop (filter bypass reasoning).

## Expected Observations

| Expectation | Verification |
|---|---|
| App reachable only at loopback | `ss -tulnp` shows `127.0.0.1:3000`; other devices can't connect |
| ≥ 6 findings across ≥ 5 categories | Your table spans distinct Top 10 IDs — not 6 injection variants |
| Proxy captures API traffic | Request/response pairs in ZAP/Burp history with JSON bodies |
| Each finding reproducible | A classmate could redo it from your numbered steps alone |
| Severity reasoning differs by finding | IDOR (attacker = authenticated user) ≠ RCE-style (unauthenticated) — justify |

## Investigation Questions

1. Finding A01: the app returned *another user's* data to you — state precisely which check was missing (server-side ownership verification) and why "guessable ID" alone isn't the root cause.
2. Category A03 vs A07: your login-bypass finding — which category dominates, and how does the *fix* differ (input handling vs authentication logic)?
3. You used hints from the scoreboard. Does that invalidate the exercise? What would a *no-hints* recon plan look like (endpoint enumeration → parameter mapping → hypothesis list)?
4. Local-only binding: which of your findings would still work if the app were on the internet unchanged? Which would be harder (think rate, discovery)?
5. For one finding, name a *detective* control (what log/alert would reveal exploitation — M13 bridge).

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `docker: command not found` | No Docker | Use the Node release bundle (`npm install` path per official README) or the standalone installer — document which you used |
| Port 3000 refused | Container still starting / wrong port | Juice Shop takes ~10–30 s; `docker ps` shows status; retry |
| Proxy shows nothing | Browser not routed through proxy / HTTPS not decrypted | Set proxy 127.0.0.1:8080; import proxy CA into browser; use ZAP's embedded browser as the easy path |
| "Target closed" / stale session | Container restarted (`--rm`) | Data resets each run — that's fine; re-do the step (evidence is per-session) |
| Challenge not triggering | Newer Juice Shop versions renamed challenges | Use the scoreboard's current names; the *categories* matter, not challenge labels |
| App reachable from LAN | Bound `0.0.0.0` or wrong `-p` flag | Stop it; re-run with `-p 127.0.0.1:3000:3000` exactly |
| Temptation to "try it" on a real bank demo site | Out of scope | **Stop** (Safety Policy §3) — reproduce on Juice Shop; the class of flaw transfers, the target must not |

## Evidence to Collect

- Authorization record + boundary check (`ss`/`docker ps` output showing loopback binding).
- `recon.md` (5 endpoints).
- Six finding records: steps, sanitized request/response, root cause, fix, severity reasoning, ASVS mapping.
- `false-starts.md`.
- Proxy history export (optional, ZAP can save sessions).
- Safety statement: *target = my local Juice Shop on 127.0.0.1 only; no third-party systems contacted; fake data only.*

## Deliverable and Report Structure

`portfolio/LAB-10/`: (1) scope/environment/boundary proof, (2) exec summary + findings table (ID, title, category, severity), (3) six full findings (steps→evidence→root cause→fix→severity→ASVS), (4) false-starts, (5) safety statement. Format mirrors M09's professional report guidance; 3–4 pages.

## Completion Checklist

- [ ] Target runs locally with verified loopback-only binding
- [ ] Written authorization record (self-granted, lab target)
- [ ] ≥ 6 findings across ≥ 5 distinct Top 10:2025 categories
- [ ] Every finding has steps + captured evidence + root cause + fix + severity reasoning + ASVS area
- [ ] At least one proxy-captured request/response pair per finding type
- [ ] False-start reflection written
- [ ] Report assembled in professional structure
- [ ] Safety statement written

## Cleanup and Reset

1. Stop the target: `Ctrl+C` in its terminal (or `docker stop <name>`; `--rm` removes the container automatically). Verify: `ss -tulnp | grep 3000` → empty.
2. Remove the proxy CA from your browser if you imported it (Settings → Certificates) — leaving CAs installed weakens your personal trust store.
3. Clear proxy session files from your machine after exporting evidence.
4. Delete the downloaded image/bundle if you want the space back (`docker rmi bkimminich/juice-shop` / remove the folder).
5. Nothing outside your machine was touched — confirm no stray listeners: `ss -tulnp | grep -E '3000|8080'`.

## Optional Challenges

- Complete three Juice Shop *progression* challenges of your own choosing and document each in report format.
- Write one **Sigma-style detection** (M13 preview) for your IDOR finding: what web-log pattern would reveal enumeration of sequential IDs?
- Redesign one broken feature with a threat-model snippet (STRIDE row) — connecting M09 → M11.
- Set up DVWA and compare how the *same* SQLi payload behaves at LOW vs MEDIUM (patch-vs-design argument).

## References and Safety Notes

- OWASP Juice Shop (official project + setup docs): <https://owasp.org/www-project-juice-shop/>; scoreboard at `/#/score-board`.
- OWASP Top 10:2025: <https://top10.owasp.org/2025/en/>; ASVS 5.0: <https://owasp.org/www-project-application-security-verification-standard/>; WSTG v4.2: <https://wstg.owasp.org>.
- OWASP ZAP (free): <https://www.zaproxy.org>; Burp Community: <https://portswigger.net/burp/communitydownload>.
- Course: [M09](../../modules/module-09-web-application-security/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** only the locally running training app is in scope; it is bound to `127.0.0.1` so no other machine can reach it; its data is fake. Proxies intercept **your own browser's** traffic to **your own** app. Never run these techniques against sites you don't own — authorized, isolated, intentional (Safety Policy §3).

**Navigation:** · [← Previous: LAB-09](../lab-09-secure-coding/README.md) · [Lab index](../README.md) · [Next: LAB-11 →](../lab-11-headers-tls-analysis/README.md)
