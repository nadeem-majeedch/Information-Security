---
title: "Lab Collection"
layout: default
---

# Lab Collection — 19 Practical Labs

Every lab is written to be **independently understandable and reproducible**: full scenario, environment, tasks, expected observations, evidence, deliverable, cleanup, and references — no lecture required. Labs run on **free tools**, in **isolated labs you own**, with **synthetic data only**.

> **Before any lab:** read the [Lab Safety Policy](../lab-safety-policy.md) and complete the isolation checklist (§4.3). Test only systems you own or have written authorization to test — never public hosts. Offensive labs (LAB-08, LAB-10, LAB-12) stay inside your host-only network.

## Labs by module

| Lab ID | Title | Module(s) | Difficulty | Duration | Mode |
|---|---|---|---|---|---|
| [LAB-01](./lab-01-cia-case-analysis/README.md) | [CIA Triad Analysis of Organization Case Studies](./lab-01-cia-case-analysis/README.md) | M01 | Introductory | 1.5–2 h | Analysis, no tools |
| [LAB-02](./lab-02-threat-model-risk-register/README.md) | [Threat Modeling and Risk Register Preparation](./lab-02-threat-model-risk-register/README.md) | M02, M11 | Intermediate | 3 h | Analysis + diagramming |
| [LAB-03](./lab-03-password-hashes/README.md) | [Password Security and Offline Hash Demonstrations](./lab-03-password-hashes/README.md) | M06, M07 | Intermediate | 2–2.5 h | Offline, synthetic hashes |
| [LAB-04](./lab-04-permissions-hardening/README.md) | [File Permissions and Endpoint Hardening](./lab-04-permissions-hardening/README.md) | M05, M07 | Introductory | 2.5 h | Own VM (Linux) |
| [LAB-05](./lab-05-hashing-integrity-signatures/README.md) | [Cryptographic Hashing, Integrity, and Digital Signatures](./lab-05-hashing-integrity-signatures/README.md) | M06 | Intermediate | 2 h | Own machine |
| [LAB-06](./lab-06-auth-access-control/README.md) | [Authentication, Access Control, and Least Privilege](./lab-06-auth-access-control/README.md) | M07 | Intermediate | 2.5 h | Own VM (Linux) |
| [LAB-07](./lab-07-packet-analysis/README.md) | [Packet Analysis of Authorized Local Traffic](./lab-07-packet-analysis/README.md) | M04 | Introductory | 2.5 h | Isolated network capture |
| [LAB-08](./lab-08-firewall-config-audit/README.md) | [Firewall Rule Analysis and Host Configuration Audit](./lab-08-firewall-config-audit/README.md) | M08, M05 | Intermediate | 2.5 h | Own VM (isolated) |
| [LAB-09](./lab-09-secure-coding/README.md) | [Secure Coding and Input-Validation Testing](./lab-09-secure-coding/README.md) | M10 | Intermediate | 3 h | Local code review |
| [LAB-10](./lab-10-web-security/README.md) | [Web Security on a Local Deliberately Vulnerable App](./lab-10-web-security/README.md) | M09 | Intermediate | 3 h | Local Juice Shop/DVWA |
| [LAB-11](./lab-11-headers-tls-analysis/README.md) | [Security Header and TLS Configuration Analysis](./lab-11-headers-tls-analysis/README.md) | M09, M06 | Intermediate | 2 h | Local/authorized service |
| [LAB-12](./lab-12-vuln-scan-interpretation/README.md) | [Vulnerability Scan Result Interpretation](./lab-12-vuln-scan-interpretation/README.md) | M12 | Advanced | 2.5 h | Controlled lab target |
| [LAB-13](./lab-13-log-analysis/README.md) | [Log Analysis, Authentication Anomalies, and Alert Triage](./lab-13-log-analysis/README.md) | M13 | Intermediate | 2.5 h | Synthetic dataset |
| [LAB-14](./lab-14-ir-tabletop/README.md) | [Incident Response Tabletop Exercise](./lab-14-ir-tabletop/README.md) | M14, M03 | Advanced | 2 h | Written exercise |
| [LAB-15](./lab-15-digital-forensics/README.md) | [Digital Forensics on a Synthetic Evidence Bundle](./lab-15-digital-forensics/README.md) | M14 | Advanced | 3 h | Synthetic artifacts |
| [LAB-16](./lab-16-malware-behavior/README.md) | [Malware Behavior Analysis from Pre-Generated Reports](./lab-16-malware-behavior/README.md) | M15 | Advanced | 2.5 h | Non-executable reports |
| [LAB-17](./lab-17-cloud-config-review/README.md) | [Cloud Security Configuration Review (Mock Configs)](./lab-17-cloud-config-review/README.md) | M16 | Intermediate | 2 h | Static JSON review |
| [LAB-18](./lab-18-security-automation/README.md) | [Security Automation on Synthetic Logs](./lab-18-security-automation/README.md) | M18 | Intermediate | 2.5 h | Local scripting |
| [LAB-19](./lab-19-defensive-capstone/README.md) | [Multi-Stage Defensive Security Capstone](./lab-19-defensive-capstone/README.md) | M01–M19 | Capstone | 6 h | Integrated lab |

## By difficulty

| Tier | Labs | What changes |
|---|---|---|
| **Introductory** (L1) | LAB-01, LAB-04, LAB-07 | Fewer tools, more guidance; one VM or none; safe commands explained in full |
| **Intermediate** (L2) | LAB-02, 03, 05, 06, 08, 09, 10, 11, 13, 17, 18 | Multi-step tasks; some freedom in tool choice; interpretation-heavy questions |
| **Advanced** (L3) | LAB-12, 14, 15, 16, 19 | Open-ended analysis, professional report formats, cross-module synthesis |

## Provided datasets (synthetic, legally reusable)

| Path | Used by | Contents |
|---|---|---|
| `lab-03-…/data/users-hashes.csv` | LAB-03 | 16 synthetic accounts with MD5/SHA-1/SHA-256 hashes (training passwords) |
| `lab-03-…/data/wordlist-small.txt` | LAB-03 | 40-word training wordlist (lightweight alternative to large public lists) |
| `lab-03-…/data/ANSWERS-hashes.txt` | LAB-03 | Self-check answers (open only after attempting) |
| `lab-09-…/data/vulnerable_app.py` | LAB-09 | Deliberately insecure app with 7 seeded weaknesses (local use only) |
| `lab-13-…/data/auth.log` | LAB-13, LAB-18 | Synthetic SSH brute-force-then-success log |
| `lab-15-…/data/timeline.csv`, `bash_history.txt`, `crontab.txt` | LAB-15 | Synthetic incident timeline + artifacts |
| `lab-16-…/data/sample-analysis-report.json` | LAB-16 | Pre-generated behavior report (no executable) |
| `lab-17-…/data/mock_s3_bucket.json`, `mock_iam_policy.json` | LAB-17 | Mock cloud configs with seeded issues |
| `lab-18-…/data/syslog-sample.log` | LAB-18 | Synthetic syslog with detectable patterns |

**Large-data alternative:** labs that could use big public sets (e.g., password lists, PCAP corpora) ship a lightweight built-in dataset first; documented optional sources (Wireshark SampleCaptures, SecLists) are listed inside those labs.

## Evidence and portfolio

Each lab's *Evidence to Collect* and *Deliverable* sections define your portfolio pack (`portfolio/LAB-XX/`), including the mandatory **safety statement** (targets used, isolation method). Grading rubric: [Assessment Guide](../assessment-guide.md).

---

**Course navigation:** [Course home](../index.md) · [Module index](../modules/README.md) · [Prerequisites](../prerequisites.md) · [Assessment Guide](../assessment-guide.md) · [Lab Safety Policy](../lab-safety-policy.md)
