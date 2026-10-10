---
title: "LAB-11 — Security Header and TLS Configuration Analysis"
layout: default
---

# LAB-11 — Security Header and TLS Configuration Analysis

**Lab ID:** LAB-11 · **Difficulty:** Intermediate · **Estimated duration:** 2 hours · **Modules:** M09, M06 · **Mode:** Local service you host + browser-only observation of sites you own

## Scenario

**CityNews** (fictional local news site) got a "security audit quote" that looks like a bill for magic. The editor asks you for a second opinion: what do response headers and TLS settings *actually* prove, and what can she check herself for free? You will stand up your own small web service locally, measure it **before** hardening, apply a header baseline and a proper TLS setup, then re-measure — producing a repeatable checklist the newsroom can run against *their own* site (and only their own).

## Learning Objectives

1. Inspect HTTP response headers with `curl` and DevTools; explain the security purpose of: CSP, HSTS, `X-Content-Type-Options`, `X-Frame-Options`/`frame-ancestors`, `Referrer-Policy`, `Permissions-Policy`.
2. Explain what each header does **and does not** protect (no magic claims).
3. Set up TLS locally with a self-signed certificate; inspect the chain and negotiation with `openssl s_client`/`curl -vk`; articulate why browsers rightly distrust self-signed certs (trust anchors — M06).
4. Compare before/after header sets and justify each addition with a threat it mitigates.
5. Apply scope discipline: deeper third-party analysis only for domains you control, using browser tools only otherwise.

## Prerequisites and Required Skills

- M06 (certificates/TLS basics), M09 (misconfiguration category), M04 (handshake familiarity).
- Skills: terminal, basic HTTP understanding, editing a small server config.

## Tools, Operating Systems, and Versions

| Tool | Purpose | Source |
|---|---|---|
| `curl` (7.x, current) | Request + header inspection (`-I` = HEAD only) | preinstalled on Linux/macOS; bundled or via curl.se on Windows |
| Python 3 `http.server` (baseline) or Nginx (config exercise) | Your local service | preinstalled / `sudo apt install nginx` (free) |
| OpenSSL 3.x | Cert creation + handshake inspection | preinstalled |
| Browser DevTools → Security tab | Certificate view | any |
| Optional: testssl.sh | Richer local TLS scan | free, GitHub `testssl/testssl.sh` (run **against your own local service only**) |

**$0.** No third-party scanning services are used.

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-11/`.
2. Service scope: **your own machine**. Two options — (a) plain Python for the baseline, (b) Nginx local VM for the full exercise (recommended, isolated VM per M04 proof).
3. Domain scope statement: *"Header/TLS measurements performed on my local service (127.0.0.1 / lab VM IP). Any public-site comparison limited to sites I own or ordinary browser viewing (Security tab) — no scanners directed at third parties."*

## Lab Environment and Starting State

A local web service reachable at `http://127.0.0.1:8080` (Python baseline) and Nginx on your lab VM at `http://192.168.56.x:80` (host-only). Starting state: **zero** security headers, plain HTTP. Your portfolio folder empty.

## Tasks

1. **Baseline measurement:**
   ```bash
   python3 -m http.server 8080          # serves CWD over HTTP on loopback
   curl -I http://127.0.0.1:8080        # -I sends HEAD and prints the RESPONSE HEADERS only
   ```
   Record the full header block. Expected: essentially `Server:` + `Content-Type` — **no security headers at all**. Explain in notes what an attacker gains with this header set (nothing stops clickjacking, MIME sniffing, referrer leaks, etc.).
2. **Header theory → checklist:** build a table: *header / example value / threat mitigated / limitation*. Required entries:
   - `Content-Security-Policy: default-src 'self'` — blocks injected scripts & many XSS *if* policy fits the site; limitation: complex sites break; doesn't stop all XSS forms.
   - `Strict-Transport-Security: max-age=31536000; includeSubDomains` — forces HTTPS after first visit; limitation: needs real HTTPS first; useless on plain HTTP (and dangerous if mis-set on HTTP-only — discuss).
   - `X-Content-Type-Options: nosniff` — kills MIME sniffing; limitation: none meaningful — just set it.
   - `X-Frame-Options: DENY` / `frame-ancestors 'none'` (in CSP) — stops clickjacking framing; note modern CSP directive supersedes the old header.
   - `Referrer-Policy: no-referrer` (or `strict-origin-when-cross-origin`) — stops URL/path leakage via referer.
   - `Permissions-Policy: camera=(), microphone=(), geolocation=()` — disables powerful APIs the page never uses.
   - Mention: `X-XSS-Protection` is deprecated/removed in modern browsers (don't recommend it — accuracy check!).
3. **Implement on Nginx (local VM):** edit the server block (via `sudo nano /etc/nginx/sites-available/default` or your own conf) to add all six headers; `sudo nginx -t` (**tests config syntax before reload — never reload blind**), then `sudo systemctl reload nginx`. `curl -I http://<vm-ip>/` → all headers present. Save before/after outputs.
4. **TLS setup (local):**
   ```bash
   mkdir -p ~/tls-lab && cd ~/tls-lab
   openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 30 -subj "/CN=lab.local"
   ```
   *What it does:* creates a self-signed certificate + private key (RSA-2048, valid 30 days, Common Name `lab.local`) — **lab-only trust**. Serve HTTPS with it (Nginx `listen 443 ssl ssl_certificate…` or Python: wrap socket — Nginx path documented). Then inspect:
   ```bash
   openssl s_client -connect 127.0.0.1:443 -servername lab.local </dev/null 2>/dev/null | openssl x509 -noout -subject -dates -issuer
   curl -vk https://127.0.0.1/ 2>&1 | grep -E "subject|SSL certificate|TLS|issuer"
   ```
   *What they do:* print the presented certificate's fields/validity/issuer; `curl -v` shows the handshake **and `-k` explicitly skips verification** — explain why `-k` is a lab convenience and a bad habit in production scripts. Browser check: open `https://127.0.0.1` (or VM IP) → expect a **privacy warning** ("not privately verified") — screenshot it and explain: the *encryption works*, the *identity is unproven* (no trusted CA signed it — trust anchor story from M06).
5. **Negotiation reading:** `openssl s_client … | grep -E "Protocol|Cipher"` (or DevTools → Security → Connection) — record negotiated protocol (expect TLS 1.3 or 1.2) and cipher. State the rule: TLS 1.0/1.1 must not be offered (RFC 8996) and what you'd configure (`ssl_protocols TLSv1.2 TLSv1.3;`).
6. **(Optional) testssl.sh on your own local HTTPS service only:** `./testssl.sh https://<your-lab-vm-ip>` — summarize graded results. **Never point it (or any TLS scanner) at a site you don't own.**
7. **Newsroom checklist** (deliverable): one page — 8 checks (6 headers + protocol policy + certificate validity) with exact commands, pass criteria, and the one-line "why" each; plus a scope note: *"Run against citynews.example only with the team's authorization; browser Security tab is fine anywhere you're a normal user."*

## Expected Observations

| Step | Expected |
|---|---|
| Baseline headers | No CSP/HSTS/frame options; only `Server`/`Content-Type`-class headers |
| After Nginx edit | `nginx -t` = syntax ok; `curl -I` lists all six headers |
| Self-signed TLS | Handshake succeeds; browser shows cert warning; issuer = your CN |
| `-k` behavior | `curl` works with `-k` but **without** it you get "self-signed certificate" **exit code error** — show both |
| Negotiation | TLS 1.2/1.3 + modern AEAD cipher; no SSLv3/TLS1.0 |

## Investigation Questions

1. HSTS set on a plain-HTTP response: what happens (browsers ignore it — it's only honored over HTTPS)? Why would setting it wrongly brick a service (preloaded HSTS on a domain you can't serve HTTPS for)?
2. CSP `default-src 'self'` on a site using a CDN script: what breaks, and what's the correct fix (allowlist vs self-host)? Trade-off reasoning.
3. Clickjacking with `frame-ancestors` vs `X-Frame-Options`: which is honored where, and why both appear during transition?
4. Your self-signed cert: name the exact properties a CA-validated cert adds (identity proof via validation) and one free legitimate option for a real domain (Let's Encrypt — automated validation). Which one applies when you have **no** domain (internal TLS → explicit trust distribution; M06).
5. Headers are *defense-in-depth on the response* — name two attacks they don't touch (e.g., server-side injection, stolen credentials) and where those are handled (M09/M07).

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `curl: command not found` (Windows) | Not bundled | Use WSL, or curl for Windows (curl.se/windows) — free |
| Headers not appearing in browser | Caching old response | `curl -I` is ground truth; hard-refresh browser; check *which* server block your request hits |
| `nginx -t` fails | Semicolon/bracket typo | The error line tells you where — fix and re-test **before** reload (that's why `-t` exists) |
| HTTPS refuses connection | Cert paths wrong / not listening 443 | Check `listen 443 ssl` + file paths + `ss -tulnp \| grep 443` |
| Browser warning absent | You visited HTTP not HTTPS, or previously clicked through and it's cached | Use a private-window; never permanently exception a cert in a real browser profile |
| `s_client` shows no Protocol line | Pipe closed early | Use the `</dev/null` form, or add `-brief` variant and grep accordingly |
| Tempted to run an online SSL checker on a random site | Scope violation | Only domains you own (or own *on behalf of* the org that asked) |

## Evidence to Collect

- Baseline `curl -I` output (no security headers).
- Header checklist table (six headers: value / threat / limitation).
- Nginx config snippet + `nginx -t` output + hardened `curl -I` output.
- TLS: cert fields (`x509 -noout` output), browser warning screenshot, `curl` with vs without `-k` (success + error), negotiated protocol/cipher.
- `newsroom-checklist.md` (Task 7).
- Safety statement: *all measurements on my own local service; no third-party scanners; browser viewing only elsewhere.*

## Deliverable and Report Structure

`portfolio/LAB-11/`: (1) scope statement, (2) baseline vs hardened header comparison, (3) header theory table, (4) TLS evidence set, (5) newsroom checklist, (6) safety statement. 2 pages.

## Completion Checklist

- [ ] Baseline headers captured (none present — documented)
- [ ] Six-header theory table with threats *and* limitations; deprecated `X-XSS-Protection` called out as not-recommended
- [ ] Nginx hardened: `nginx -t` before reload, all headers verified via `curl -I`
- [ ] Self-signed TLS stood up; cert fields recorded; browser warning explained (encryption vs identity)
- [ ] `-k` shown as success **and** failure modes; protocol/cipher recorded (no TLS ≤1.1)
- [ ] Newsroom checklist written (8 checks + commands + pass criteria + scope note)
- [ ] Safety statement written

## Cleanup and Reset

1. Stop Python server (`Ctrl+C`); stop/disable lab Nginx site if desired (`sudo systemctl stop nginx` or revert config to backup you made — **make that backup before editing**).
2. Delete lab key material: `rm -rf ~/tls-lab` (your own folder; keys were self-signed lab-only — but keys shouldn't linger anyway).
3. Nothing external changed; no certificates were requested from real CAs; no third parties scanned.
4. Portfolio keeps outputs only, **not** the private key.

## Optional Challenges

- Add a CSP that actually works for a small static site with one inline script — document `'unsafe-inline'` risk and the nonce/hash alternative.
- Enable HSTS on the local HTTPS vhost with a tiny `max-age`, explain browser-side behavior, then remove it (know how to undo).
- Compare your local `curl -I` results with DevTools' Security tab on a site **you own** (or the browser's ordinary view anywhere) — note tool-vs-tool differences in header coverage.
- Write a tiny `check-headers.sh` that curls a URL and exits non-zero if a required header is missing — seed for LAB-18.

## References and Safety Notes

- MDN Web Docs — HTTP security response headers: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#security>.
- OWASP *Secure Headers Project* / Cheat Sheet: <https://owasp.org/www-project-secure-headers/> · <https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html>.
- RFC 8996 (TLS 1.0/1.1 deprecated), RFC 8446 (TLS 1.3); Mozilla SSL Configuration Generator (free): <https://ssl-config.mozilla.org>.
- Let's Encrypt (free certificates for real domains): <https://letsencrypt.org>.
- Course: [M06](../../modules/module-06-cryptography/README.md) · [M09](../../modules/module-09-web-application-security/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** scanners and header probes are directed only at services you run yourself; ordinary browser viewing of public sites is fine, but no automated scanning of third-party hosts (Safety Policy §3/§5). Self-signed keys stay lab-local and are deleted in cleanup.

**Navigation:** · [← Previous: LAB-10](../lab-10-web-security/README.md) · [Lab index](../README.md) · [Next: LAB-12 →](../lab-12-vuln-scan-interpretation/README.md)
