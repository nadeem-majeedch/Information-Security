---
title: "Capstone Scenarios — A: Copperfield Books · B: Larkspur Labs"
layout: default
---

# Capstone Scenarios — Choose One

**Part of:** [M19 Capstone Project](README.md) · Both scenarios run the same [seven stages](README.md#6-staged-project-workflow-with-milestones) against the same [rubric](rubric.md). Pick the emphasis you learn best in.

**Rules common to both (from the [brief §4](README.md#4-scope-assumptions-constraints-and-explicit-exclusions)):** fictional organizations · provided synthetic artifacts only · your own local lab for anything hands-on · **$0** · no public systems, no university systems, no real data, no live malware.

After choosing, copy the scenario's manifest into `portfolio/CAPSTONE/data/MANIFEST.md` recording whether you **copied** each file or **referenced it in place** (both are fine — unrecorded is not).

---

## Scenario A — Copperfield Books: small-business security review

### Organizational context

**Copperfield Books** is a 12-person independent bookshop in a market town: a physical shop, a small warehouse, and an online store that ships nationally. It has no IT staff. "IT" is split between the **owner** (orders the hosting, knows the password for everything) and a **part-time weekend assistant** who once fixed a printer and is now "the computer person."

| | |
|---|---|
| **Systems** | One Debian server (`shop01`, local VM in your lab) hosting the storefront, till backend, and staff webmail; office router/firewall (consumer box); 11 staff laptops/workstations; NAS with nightly backups; a cloud-sync bucket for scanned stock lists |
| **Data** | Customer names/emails/addresses (synthetic), order history, stock lists, staff rota. Card payments run through a third-party terminal (**never in scope**) |
| **Money/time** | Budget: **$0**. Downtime costs real revenue; the owner wants "the top five things to fix, in order, with reasons" |
| **People** | Shared logins are an open secret ("we all use `shop` for the POS"); the owner reuses one password "for convenience"; the weekend assistant has admin rights "so he can fix things" |
| **Current posture** | Storefront behind a hosting provider (patching *probably* automatic); firewall "has something enabled"; NAS backups nightly — *tested twice last year, maybe*; no one reads logs |

### Background — why they called you (the simulated incident)

Three weeks ago the bookkeeper noticed two invoice PDFs in the shared stock folder had been **altered**, and a month of shipping logs was **missing**. The owner shrugged it off until a customer emailed to say their address-change confirmation went to someone else's email. The shop's insurance provider now requires an independent **security review with a prioritized remediation plan** — that is your engagement.

What actually happened (you must establish this from evidence, not from this paragraph): an attacker brute-forced an internet-facing service from a single source, landed on a service account, escalated, altered/removed files, and used an internal no-login upload page — while firewall logs sat unread. The organization does not know any of this; *your report is how they find out.*

### Provided artifact manifest

| Artifact | Source | Your use |
|---|---|---|
| `auth.log`, `auth-attempts.csv`, `admin-actions.jsonl` | [LAB-13 data](../labs/lab-13-log-analysis/data/index.md) | The shop server's authentication and admin logs — Stage 4 timeline, triage, detection gaps |
| `syslog-sample.log` | [LAB-18 data](../labs/lab-18-security-automation/data/syslog-sample.log) | Host-level service/cron events for cross-source correlation |
| `mock_s3_bucket.json`, `mock_iam_policy.json` | [LAB-17 data](../labs/lab-17-cloud-config-review/data/index.md) | The cloud-sync bucket + access policy your Stage 3 audits |
| `sample-analysis-report.json` | [LAB-16 data](../labs/lab-16-malware-behavior/data/sample-analysis-report.json) | A *report* (not a binary) on a suspicious file the assistant received — IOC extraction only |
| Course docs | [Roadmap](../course-roadmap.md) · [Safety policy](../lab-safety-policy.md) | Scoping and control references |

**Optional extra evidence (free):** build the shop as 2–3 local VMs (server + workstation + router VM) so Stage 6 improvements are validated hands-on.

### Deliverable emphasis
Network/endpoint posture · identity and shared-login remediation · backup and recovery validation · cloud-config audit · log pipeline and detections · privacy note for customer data · executive summary a non-technical owner can act on.

### Scenario-specific preparation
[LAB-13](../labs/lab-13-log-analysis/README.md), [LAB-04](../labs/lab-04-permissions-hardening/README.md), [LAB-08](../labs/lab-08-firewall-config-audit/README.md), [LAB-17](../labs/lab-17-cloud-config-review/README.md) · refresher: [M02](../modules/module-02-threats-vulnerabilities-risk-and-controls/README.md), [M05](../modules/module-05-operating-system-and-endpoint-security/README.md), [M13](../modules/module-13-logging-monitoring-and-security-operations/README.md).

---

## Scenario B — Larkspur Labs: simulated web-application defense

### Organizational context

**Larkspur Labs** is a 15-person startup selling **Beacon**, a CRM web app for small teams (their fictional flagship — the scenario's "web application + internal network" from the [roadmap](../course-roadmap.md#m19--integrated-capstone-project)). Four developers, one designer, two sales, one founder-CTO, five others. The product is the company; a bad week of the product is an existential week.

| | |
|---|---|
| **Systems** | Beacon web app + REST API (locally hosted — a course lab app such as Juice Shop/DVWA *is* Beacon in your lab); PostgreSQL on an app-tier host; Redis session store; staff internal wiki; developer laptops; a CI pipeline (local); cloud-style object storage for exports (mock configs) |
| **Data** | Trial-user accounts (names/emails — synthetic), CRM records *their* customers put in (treated as personal data), API tokens, export files |
| **Money/time** | Budget: **$0**. Next release in ~3 weeks; the CTO wants a **fix-first list** the team can actually ship |
| **People** | Two founders still hold deploy rights "for speed"; secrets live in a `.env` "just for now"; the newest developer has production database read access "to help with support" |
| **Current posture** | No automated security checks in CI; headers "added by someone once"; login has no rate limiting; nobody has written a threat model |

### Background — why they called you (the simulated incident)

A design-partner company reported that changing a record ID in Beacon's web app returned **another tenant's records**. Separately, their monitoring showed a burst of path-scanning against the API at 04:00 one morning, and a developer noticed an unexpected `helpers.js` file in the build output after a dependency update. Larkspur has no security function; they have engaged you (with written scope) to **review the application's security posture, investigate the provided logs and artifacts, and deliver a prioritized, validated fix plan** before the release.

The IDOR is confirmed and reproducible **only in your local lab copy**; the 04:00 scan and the timeline of what followed are yours to reconstruct from evidence.

### Provided artifact manifest

| Artifact | Source | Your use |
|---|---|---|
| Forensic bundle: `timeline.csv`, `bash_history.txt`, `crontab.txt` | [LAB-15 data](../labs/lab-15-digital-forensics/data/index.md) | Server compromise evidence — Stage 4 timeline, persistence, investigation answers |
| `auth.log`, `auth-attempts.csv`, `admin-actions.jsonl` | [LAB-13 data](../labs/lab-13-log-analysis/data/index.md) | Beacon's authentication/admin API logs — brute-force, session, privilege analysis |
| `mock_s3_bucket.json`, `mock_iam_policy.json` | [LAB-17 data](../labs/lab-17-cloud-config-review/data/index.md) | The export-bucket and access policy for Stage 3's cloud-config audit |
| Local lab app (you deploy) | [LAB-10](../labs/lab-10-web-security/README.md) / [LAB-09 app](../labs/lab-09-secure-coding/data/vulnerable_app.py) | Reproduce the IDOR/XSS-class findings **only against your local copy**; Stage 6 fix validation |
| `syslog-sample.log` | [LAB-18 data](../labs/lab-18-security-automation/data/syslog-sample.log) | Host events for the app tier |

**Rule of the scenario:** every web request you send goes to `localhost` or a host-only VM you started. "Reproduce the finding" never means "check the public internet."

### Deliverable emphasis
OWASP-class findings with professional reports · access-control and session fixes · security headers/TLS posture · threat model of an app + API (STRIDE) · secure-SDLC/CI gate design · detections for web/auth signals · privacy note for CRM data · a fix-first list a four-dev team can ship.

### Scenario-specific preparation
[LAB-10](../labs/lab-10-web-security/README.md), [LAB-11](../labs/lab-11-headers-tls-analysis/README.md), [LAB-09](../labs/lab-09-secure-coding/README.md), [LAB-15](../labs/lab-15-digital-forensics/README.md) · refresher: [M07](../modules/module-07-identity-and-access-management/README.md), [M09](../modules/module-09-web-application-security/README.md), [M10](../modules/module-10-secure-programming/README.md), [M11](../modules/module-11-threat-modeling-and-security-architecture/README.md).

---

## After you choose

1. Read your scenario twice; write the Stage 1 [scoping memo](README.md#6-staged-project-workflow-with-milestones) the same day (memory of the brief fades fast).
2. Copy the manifest into `portfolio/CAPSTONE/data/MANIFEST.md`.
3. Open the templates: [report](templates/report-template.md) · [risk register](templates/risk-register-template.md) · [threat model](templates/threat-model-template.md) · [findings & remediation](templates/findings-remediation-template.md) · [portfolio & presentation](templates/portfolio-presentation-spec.md).
4. Work the stages; gate each with the [checklists](checklists.md).

**Back to:** [Capstone overview & student brief](README.md)
