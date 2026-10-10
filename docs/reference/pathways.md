---
title: "Learning Pathways — Beginner and Advanced"
layout: default
---

# Learning Pathways — Beginner and Advanced

**Part of:** [Reference Library](README.md) · Sequenced routes through the resources, so nobody faces 70 links without an order. Every step names **why it's next**, its **checkpoint**, and its **cost (always $0 for the core path)**.

**Required vs optional:** steps marked **[Core]** are the course itself (required); steps marked **[+]** are optional extensions that deepen the same skill. Paid options are never load-bearing — where a platform has a paid tier, the free tier (or a free substitute) is what the pathway uses.

---

## Pathway 1 — Beginner: from zero to course-ready (≈ 4–6 weeks, part-time)

For learners with basic computer fluency but no security background. Designed so you enter [Module 01](../modules/module-01-information-security-foundations/README.md) *already* able to follow the labs.

| # | Step | Resource (all free) | Why this, now | Checkpoint |
|---|---|---|---|---|
| 1 | Terminal fluency | [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) levels 0–15 | The course assumes you can navigate a shell, edit files, read output — Bandit builds exactly that with immediate feedback | You completed Bandit 10+ without a walkthrough |
| 2 | How the web talks | [MDN Web Docs: HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) ([O], Free) | M04/M09 assume you know what a request, header, and status code are | You can explain a GET and a POST, and find a header in dev tools |
| 3 | Security vocabulary + mindset | [Module 01](../modules/module-01-information-security-foundations/README.md) + this [Glossary](glossary.md) | CIA triad and risk language are the course's grammar | Quiz M01 ≥ 80% ([Assessment Hub](../assessments/README.md)) |
| 4 | Crypto without the math | [Crypto101](https://www.crypto101.io/) ch. 1–5 (skim) *after* [Module 06](../modules/module-06-cryptography/README.md) tools work | Do the tools first (course style), then the "why" where curiosity bites | You can say what a nonce is for without notes |
| 5 | First hands-on security labs | Course [LAB-01](../labs/lab-01-cia-case-analysis/README.md) → [LAB-03](../labs/lab-03-password-hashes/README.md) → [LAB-04](../labs/lab-04-permissions-hardening/README.md) | Early wins on your own machine; each takes < 3 h | Portfolio packs saved with safety statements |
| 6 | Beginner challenge practice | [picoCTF](https://picoctf.org/) (archived) or [PortSwigger Academy](https://portswigger.net/web-security) — *intro topics only* | Quiz-style reasoning under mild time pressure, safely, on *their* infra | 10 solved challenges / 3 academy labs |
| 7 | Breadth reading (pick one) | [Security Engineering](https://www.rossanderson.com/security-engineering.htm) ch. 1–3 | The best free antidote to "security is a checklist" | 1-page notes in your study journal |
| 8 | Enter the course proper | [Course roadmap](../course-roadmap.md), Level 1 | You now have shell, web, vocabulary, and lab hygiene | Schedule: 8–12 h/week for 4–6 months |

**Beginner rules:** (1) never skip the labs because a quiz feels easy — the quiz is recall, the lab is the skill; (2) keep one `notes/` file per module; (3) if a step feels too hard, the [study guide](study-guide.md) says which earlier module to revisit.

---

## Pathway 2 — Advanced: four tracks after the core course

Pick a track by what you want to *be doing* in a year. All tracks assume: course complete (gates ≥ 80%, portfolio ≥ 17/19, investigations ≥ 60%) and the capstone done or in flight. **[Core]** = course component; **[+]** = free extension.

### 2A — Security operations (SOC / detection engineering)

| Stage | Activity | Resource | Free status |
|---|---|---|---|
| 1 **[Core]** | Detection pack + triage worksheet | [LAB-13](../labs/lab-13-log-analysis/README.md), [LAB-18](../labs/lab-18-security-automation/README.md), [M13](../modules/module-13-logging-monitoring-and-security-operations/README.md) | Free |
| 2 **[Core]** | Run a real pipeline: Wazuh (Tier-a) or scripted (Tier-b) with your 6+ Sigma rules | [Wazuh docs](https://documentation.wazuh.com/) · [Sigma](https://github.com/SigmaHQ/sigma) | Free |
| 3 **[+]** | ATT&CK coverage map of your rules: mark covered tactics, find your gaps | [ATT&CK](https://attack.mitre.org/) + [version history](https://attack.mitre.org/resources/versions/) | Free |
| 4 **[+]** | Blue-team scenario practice | [CyberDefenders](https://cyberdefenders.org/) or [LetsDefend](https://letsdefend.io/) (free tier) | Free tier; **paid tiers optional** |
| 5 **[+]** | Network-level visibility | Add [Zeek](https://docs.zeek.org/) or Suricata full-tap on the lab segment; triage what it adds | Free |
| 6 **Checkpoint** | Portfolio: detection rules with ATT&CK IDs, FP analysis, one write-up of an investigated scenario at ≥ 60% against the [Investigation rubric](../assessment-guide.md#53-investigation-rubric-component-d-per-report-100-points) | — | — |

### 2B — Application security (AppSec)

| Stage | Activity | Resource | Free status |
|---|---|---|---|
| 1 **[Core]** | Course web arc: M09 → [LAB-10](../labs/lab-10-web-security/README.md) → 6+ findings with reports | [OWASP Top 10:2025](https://top10.owasp.org/) | Free |
| 2 **[Core]** | Methodology discipline: work the [WSTG](https://owasp.org/www-project-web-security-testing-guide/) checklist against your local app | [WSTG](https://owasp.org/www-project-web-security-testing-guide/) (verify current stable) | Free |
| 3 **[+]** | Depth labs per vulnerability class | [PortSwigger Web Security Academy](https://portswigger.net/web-security) — one topic per week (SQLi, authz, XSS, SSRF, access control) | Free (no account needed) |
| 4 **[+]** | Verification standard fluency: audit your own app to [ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/) L1, then L2 | ASVS 5.0.0 | Free |
| 5 **[+]** | Fix and prove: remediate 8 seeded weaknesses with fail-then-pass tests, gate it in CI ([LAB-09](../labs/lab-09-secure-coding/README.md)) | [Semgrep](https://semgrep.dev/docs/) · [Gitleaks](https://github.com/gitleaks/gitleaks) | Free |
| 6 **Checkpoint** | A defensible mini-engagement write-up on a system *you own*: RoE → findings → ASVS mapping → fixed-and-retested code | — | — |

### 2C — Incident response and forensics

| Stage | Activity | Resource | Free status |
|---|---|---|---|
| 1 **[Core]** | IR plan + tabletop + forensic timeline | [LAB-14](../labs/lab-14-ir-tabletop/README.md), [LAB-15](../labs/lab-15-digital-forensics/README.md), [M14](../modules/module-14-incident-response-and-digital-forensics/README.md) | Free |
| 2 **[Core]** | Read the standard your plan cites | [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (Apr 2025) | Free |
| 3 **[+]** | Professional playbooks to structure yours against | [CISA Incident & Vulnerability Response Playbooks](https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks) | Free (PDF) |
| 4 **[+]** | Tool depth: Autopsy + Volatility 3 on a *self-created* image (create the incident yourself in a VM, then investigate it) | [autopsy.com](https://www.autopsy.com/) · [volatility3 docs](https://volatility3.readthedocs.io/) | Free |
| 5 **[+]** | Ransomware readiness: walk [#StopRansomware](https://www.cisa.gov/stopransomware) against your own backup design; test a restore | CISA guide + your 3-2-1 evidence | Free |
| 6 **Checkpoint** | Full incident package in portfolio: plan, timeline with chain of custody, detections that fired, lessons-learned — scored with the [Investigation rubric](../assessment-guide.md#53-investigation-rubric-component-d-per-report-100-points) | — | — |

### 2D — Security engineering / architecture

| Stage | Activity | Resource | Free status |
|---|---|---|---|
| 1 **[Core]** | Capstone stages 1–6 done well (architecture, threat model, hardening, validation) | [M19 capstone](../capstone/README.md) | Free |
| 2 **[Core]** | Framework fluency: CSF 2.0 Functions ↔ CIS v8.1 mapping exercise | [CSF 2.0](https://www.nist.gov/cyberframework) · [CIS Controls v8.1](https://www.cisecurity.org/controls) | Free / registration for PDF |
| 3 **[+]** | Zero trust deep-read + architecture critique | [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) + your Stage-2 DFD re-drawn as ZTA | Free |
| 4 **[+]** | Control-catalog precision: select controls for a scenario from [SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/final) families and justify each | SP 800-53r5 | Free |
| 5 **[+]** | Infrastructure as code + posture: harden a Compose/Terraform stack, scan with Checkov/Trivy, prove before/after | [LAB-17](../labs/lab-17-cloud-config-review/README.md) + [Checkov](https://github.com/bridgecrewio/checkov) | Free |
| 6 **Checkpoint** | An architecture dossier: DFD, threat model ≥ 15, control mapping, residual-risk statement, validation evidence — the [capstone rubric](../capstone/rubric.md) at *Exemplary* on D1/D4/D5 | — | — |

### Cross-track professional development (any track)

- **[+] Read primary sources, not summaries** — when a blog and a standard disagree, the standard wins; cite versions ([library §how-to-read](README.md#how-to-read-an-entry)).
- **[+] Write publicly** — turning your investigation notes into a clean public write-up (no client/real data — your labs qualify) is the highest-value free career move.
- **[+] Certifications are optional and paid** — see the [paid table](README.md#paid-resources-reference-only--never-required); nothing in any pathway above requires them.

**Next:** [Troubleshooting & independent study](study-guide.md) · [Reference library](README.md) · [Tools directory](tools.md)
