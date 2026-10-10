---
title: "LAB-12 — Vulnerability Scan Result Interpretation"
layout: default
---

# LAB-12 — Vulnerability Scan Result Interpretation

**Lab ID:** LAB-12 · **Difficulty:** Advanced · **Estimated duration:** 2.5 hours · **Module:** M12 · **Mode:** Report analysis + validation against **your own controlled lab target**

## Scenario

**Riverbend Clinic** (fictional) contracted an automated scan of its *staging* server before go-live. The tool delivered the report below; the vendor now wants $9,000 to "remediate everything urgently." You are the assessor hired to interpret the report honestly: which findings are real *here*, which are tool noise, what each is actually worth in risk, and what order to fix things. You will validate against **your own lab VM** — the only machine you may probe — using manual checks, not re-scanning at the vendor's scale.

## Learning Objectives

1. Parse raw scanner output: extract finding, affected asset, evidence, and claimed severity.
2. Manually validate findings (version checks, config reads, reachability) to classify true positive / false positive / not-applicable.
3. Recompute risk with CVSS v4.0-style reasoning *plus* exposure and asset context — demonstrating CVSS ≠ risk (M02).
4. Prioritize remediation with evidence (KEV status, exploitability, business impact) and write a defensible work order.
5. Produce a client-quality interpretation report with confidence statements and retest plan.

## Prerequisites and Required Skills

- M12 module (assessment methodology, RoE), M02 (CVSS/KEV/risk), M04 isolation proof, M05 baseline knowledge (to judge "expected vs. odd").
- Skills: reading technical reports, Linux config/version checks, careful note-taking.

## Tools, Operating Systems, and Versions

- Provided synthetic scan report (below — no tool needed to receive it).
- Your lab VM ("target") — Ubuntu with a couple of services you control (e.g., the LAB-08 hardened VM works well).
- Optional manual checkers (free, lab-target only): `nmap` (version flags), `openssl s_client`, `curl -I`, direct config reads (`ss`, `systemctl`, package versions).
- References: NVD/CISA KEV (browser, for lookup).

**$0.** No scanner installation required — this lab teaches *interpretation*, the skill tools can't automate.

## Setup (Free) and Required Permissions

1. Isolation proof (M04) for the target VM; snapshot `pre-lab12`.
2. Prepare the target to match the report's assumptions: Ubuntu VM with OpenSSH, `ufw` active, and a local Nginx serving a static page (`sudo apt install nginx`; keep it local). *Alternatively* treat your LAB-08 kiosk VM as the asset.
3. Authorization record: *"Target: 192.168.56.30 (my VM, host-only). Methods: manual version/config inspection and single-target service probes. No scanning tools beyond nmap against this one address."*

## Lab Environment and Starting State

One hardened-ish lab VM + the synthetic report below. Starting state: no validation done; report accepted uncritically by no one.

> ### Provided scan extract (synthetic — `scan-report-excerpt.txt`)
> ```
> Tool: AutoScan Pro 9.1  Target: 192.168.56.30 (lab-staging)  Scanned: 2026-10-01
> F-01 [HIGH]   OpenSSH 7.6p1 — CVE-2018-15473 user enumeration (CVSS 5.3)     Evidence: banner grab :22
> F-02 [CRITICAL] Apache HTTP Server 2.4.49 — CVE-2021-41773 path traversal (CVSS 9.8)  Evidence: GET /cgi-bin/.%2e/ response fingerprint
> F-03 [MEDIUM] Telnet service detected on port 23                            Evidence: TCP open
> F-04 [HIGH]   MySQL 3306/tcp reachable from scanner network                  Evidence: TCP open
> F-05 [LOW]    TLS 1.0 supported on 443                                     Evidence: handshake accepted
> F-06 [MEDIUM] SSH allows password authentication                            Evidence: sshd probe
> F-07 [INFO]   Server header discloses "nginx/1.18.0"                        Evidence: HTTP header
> F-08 [HIGH]   Missing HTTP security headers (CSP, HSTS, X-Frame-Options)   Evidence: header check
> F-09 [MEDIUM] DNS open resolver on 53/udp                                  Evidence: UDP probe
> F-10 [LOW]    ICMP timestamp response enabled                              Evidence: ICMP reply
> ```

## Tasks

1. **Scope & RoE first (discipline check):** before touching anything, write the 3-line RoE: target, methods, exclusions (from Setup step 3). *Then* begin.
2. **Evidence triage table:** for each finding F-01…F-10 record: claimed issue, claimed severity, **how to verify manually** (one command/config read per finding), verdict pending validation.
3. **Validate on your target (commands explained):**
   - Versions: `ssh -V` (prints the client/server version string — compare to F-01's claim); `nginx -v`; `dpkg -l | grep -E 'nginx|openssh'` (lists installed package versions).
   - Services: `ss -tulnp` (which ports actually listen — is 23 open? 3306? 53? F-03/F-04/F-09 testable instantly).
   - HTTP: `curl -I http://127.0.0.1/` (F-02 server header? F-07 disclosure? F-08 missing headers — count them).
   - TLS: `openssl s_client -connect 127.0.0.1:443 </dev/null 2>/dev/null | grep Protocol` — is 443 even up? (If not, F-05 may be *not applicable* to this asset — a distinct verdict from "false".)
   - Remote reachability: **from your tester VM only**, `nmap -sT -Pn -p 22,23,80,443,3306,53 192.168.56.30` (single target, named ports — justification: confirming what the scanner claimed; still inside your written RoE).
4. **Classify every finding** as **True Positive** (confirmed on *this* asset), **False Positive** (scanner wrong — e.g., banner-based guess from a different product), **Not Applicable** (issue real elsewhere but absent here — no such service), or **Informational**. Give the confirming/denying evidence line for each — a verdict without evidence is not accepted.
5. **Risk recomputation:** for each TP, write a risk line using M02's register format (threat/vulnerability/L/I/score/treatment) — demonstrate at least one downgrade (e.g., CVSS 9.8 Apache flaw = *not applicable* here, or a HIGH whose exposure is host-only → lower risk) and one justified keep.
6. **Prioritized work order:** top 5 actions with rationale; explicitly reference KEV-lookup discipline (check CVEs in CISA KEV; note results), patch-gap reasoning, and which items are *configuration* (hours) vs *project* (days).
7. **Confidence & honesty:** write the report section "What we did NOT test" (scope limits: no authenticated testing, no app-layer logic, UDP mostly unchecked…) — professional reports always bound their claims.
8. **Retest plan:** 5-line plan — what to re-run, expected result, who signs off.

## Expected Observations

| Finding | Likely verdict on *your* target (verify, don't copy) | Lesson |
|---|---|---|
| F-01 (old OpenSSH) | **False/NA** — your VM runs the distro's current OpenSSH (banner differs) | Scanners fingerprint banners; versions lie (backports!) |
| F-02 (Apache 2.4.49) | **False positive** — asset runs nginx, not Apache | Product misidentification; a 9.8 "CRITICAL" that doesn't exist here |
| F-03 (telnet) | **False/NA** if `ss` shows no :23 | Open ≠ listening; scanner vs host config |
| F-04 (3306 reachable) | **NA** if no MySQL installed; TP if it listens **and** ufw allows | Exposure needs *both* listener and path |
| F-05 (TLS 1.0) | **NA** if 443 not served; else TP → configure protocols | "Not applicable" ≠ "fine forever" |
| F-06 (password auth) | TP if `sshd_config` says `PasswordAuthentication yes` | Config reading beats probing |
| F-07 (banner) | TP (real, low) — decide: accept or `server_tokens off` | Info disclosure trade-offs |
| F-08 (headers) | TP if `curl -I` lacks them (LAB-11 skills) | Cross-lab reuse |
| F-09/F-10 | Likely NA on a desktop VM | Environment mismatch noise |

Overall: expect **roughly half** the report to be TP-or-NA noise — the core insight: *a scanner generates hypotheses; an assessor produces validated findings.*

## Investigation Questions

1. F-02 scores 9.8 "CRITICAL" but the product doesn't exist on your asset. What score belongs in your *risk register* for it, and why does copying CVSS verbatim mislead management?
2. Ubuntu/OpenSSH version strings include distro backports — how does that break naive version-based detection, and what's the better evidence (config reading, changelog)?
3. F-06 vs F-01: which would an attacker prefer and why? (Password auth enabled invites exactly the brute-force patterns LAB-13 triages.)
4. The vendor proposed remediating all 10 "urgently" for $9k. Using your verdict table, write a 3-sentence reply that saves the client money *and* builds trust.
5. "Not tested" honesty (Task 7): why does listing gaps *increase* credibility, and what liability language does it protect against?

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| No 443 on target | Nothing serving TLS | Expected for a minimal VM → F-05 = Not Applicable; or reuse LAB-11's Nginx TLS vhost |
| `nginx -v` silent | Version prints to stderr | `nginx -v 2>&1` or check `dpkg -l nginx` |
| nmap refused/filtered | ufw working as designed | "Filtered" is *also* a validated answer — record it as exposure evidence |
| Can't decide TP vs NA | TP = present **on this asset**; NA = issue class real but absent here | If unsure, gather one more evidence line — never guess |
| Report ballooning | You're rewriting the scan | Your artifact is the **verdict table + work order**, not a copy of F-01…F-10 |

## Evidence to Collect

- Written RoE (3 lines) dated before validation.
- `verdict-table.md` — all 10 findings: claim / verification method / evidence line / verdict.
- Command outputs proving at least: version check, `ss -tulnp`, `curl -I` header set, nmap single-target result.
- Risk register lines for TPs (M02 format) with at least one demonstrated downgrade.
- `work-order.md` (top 5, with KEV-check notes) + "not tested" section + retest plan.
- Safety statement: *validation limited to my host-only VM 192.168.56.30 per written RoE; no third-party targets; no exploitation attempts.*

## Deliverable and Report Structure

`portfolio/LAB-12/`: (1) RoE, (2) verdict table with evidence per row, (3) risk recomputation notes, (4) prioritized work order + KEV notes, (5) confidence/"not tested" section, (6) retest plan, (7) safety statement. 3 pages max — concision is the skill.

## Completion Checklist

- [ ] RoE written before any target contact
- [ ] All 10 findings validated or classified with an evidence line each
- [ ] ≥ 1 false positive and ≥ 1 not-applicable demonstrated with proof
- [ ] Risk register lines for TPs; ≥ 1 CVSS-vs-risk downgrade shown
- [ ] KEV consulted for applicable CVEs; results noted
- [ ] Top-5 work order with configuration-vs-project distinction
- [ ] "Not tested" honesty section + 5-line retest plan
- [ ] Safety statement written

## Cleanup and Reset

1. Stop any probe sessions; nothing persistent was changed on the target (validation was read-only — if you changed `server_tokens` experimenting, revert or revert the snapshot).
2. Revert `pre-lab12` if in doubt; delete temp outputs outside the portfolio.
3. Keep the verdict table and evidence — this is graded work and capstone reference material.

## Optional Challenges

- Feed the *same* report to a second reviewer (friend/another AI) and diff your verdict tables — discuss evidence quality, not just conclusions.
- Write the Sigma-style detection (M13) that would catch F-06's abuse (password-auth brute force).
- Re-scan your own target with a free scanner (Nmap NSE scripts or OpenVAS on a beefy VM — heavy) and compare *its* raw output to this curated report: what extra noise does real tooling add?

## References and Safety Notes

- NIST SP 800-115, *Technical Guide to Information Security Testing and Assessment*: <https://csrc.nist.gov/pubs/sp/800/115/final>.
- CISA KEV catalog: <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>; NVD: <https://nvd.nist.gov>.
- PTES (methodology reference): <http://www.pentest-standard.org>.
- Course: [M12](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** all validation targets your own host-only VM per written RoE (Safety Policy §3); commands are read-only inspections plus a single-target port list — no exploitation, no brute force, no third-party hosts, no scanning "to see what happens."

**Navigation:** · [← Previous: LAB-11](../lab-11-headers-tls-analysis/README.md) · [Lab index](../README.md) · [Next: LAB-13 →](../lab-13-log-analysis/README.md)
