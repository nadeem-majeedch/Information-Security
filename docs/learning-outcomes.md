---
title: "Learning Outcomes"
layout: default
---

# Information Security — Learning Outcomes

**Course:** Information Security: A Self-Study Course from Beginner to Advanced
**Instructor:** Engr. Dr. Muhammad Nadeem Majeed — Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore, Pakistan
**Status:** DRAFT for instructor review · **Version:** 0.1 · **Last verified:** 2026-10-09
**Companion documents:** [Course Roadmap](./course-roadmap.md) · [Prerequisites](./prerequisites.md) · [Assessment Guide](./assessment-guide.md) · [Lab Safety Policy](./lab-safety-policy.md)

---

## 1. Purpose

This document defines what a learner can **demonstrate** after completing the course. Outcomes are written to be measurable (observable verbs, stated conditions where useful) and are mapped to Bloom's revised taxonomy levels. They drive the assessments in the [Assessment Guide](./assessment-guide.md) and are evidenced by the module deliverables in the [Course Roadmap](./course-roadmap.md).

## 2. Course-level learning outcomes (CLOs)

Upon successful completion of this course, a learner can:

| ID | Learning outcome | Bloom level | Main evidence |
|---|---|---|---|
| **CLO-1** | Explain core information security principles — the CIA triad, asset and threat vocabulary, and the governance/policy/ethics/legal frame that constrains security work. | Understand | M01–M03 quizzes, policy set, ethics case analyses |
| **CLO-2** | Analyze threats, vulnerabilities, and risk, and select appropriate controls using recognized frameworks (NIST CSF 2.0, CIS Controls v8.1, CVSS v4.0). | Analyze / Evaluate | M02 risk register, M17 control mapping |
| **CLO-3** | Apply defensive configuration skills on operating systems and networks — hardening, segmentation, firewall rules, IDS deployment — in an isolated lab. | Apply | M05, M08 lab evidence packs |
| **CLO-4** | Apply cryptography correctly and evaluate cryptographic designs for misuse (weak hashing, ECB/static IVs, key handling failures). | Apply / Evaluate | M06 crypto notebook, misuse analysis |
| **CLO-5** | Design identity and access arrangements (authentication factors, MFA, least privilege, RBAC) consistent with NIST SP 800-63-4 guidance. | Apply / Design | M07 IAM design note + lab |
| **CLO-6** | Assess web applications and other systems **within authorized scope** using OWASP Top 10:2025, WSTG methodology, and ASVS verification, and report findings professionally. | Apply / Analyze | M09 report, M12 engagement report |
| **CLO-7** | Develop secure software: find and fix common weaknesses (CWE classes), and operate SAST/SCA/secret-scanning gates in a delivery pipeline. | Apply | M10 patch set + pipeline evidence |
| **CLO-8** | Model threats (STRIDE, data-flow diagrams) and evaluate security architectures against risk-based and zero-trust principles. | Analyze / Evaluate | M11 threat model, capstone Stage A |
| **CLO-9** | Operate detection and response: engineer logging and detections mapped to MITRE ATT&CK, triage alerts, and execute incident response and forensic timeline analysis per NIST SP 800-61r3. | Apply / Analyze | M13 detection pack, M14 IR plan + forensic report |
| **CLO-10** | Analyze malware artifacts **defensively and safely** in an isolated environment, and convert observations into detections and IOCs. | Analyze | M15 triage reports, YARA/Sigma rules |
| **CLO-11** | Evaluate cloud/infrastructure security and privacy obligations, mapping controls across frameworks and completing a DPIA-style assessment. | Evaluate | M16 audits, M17 DPIA + mapping |
| **CLO-12** | Synthesize the full pathway into an integrated capstone: architect, harden, assess, defend, and document a small-system security program, and reflect on professional and ethical responsibilities. | Create / Evaluate | M19 capstone portfolio |

## 3. Level-level outcomes

Shorter statements summarizing what each level establishes. All are prerequisites for the next level.

### Level 1 — Information Security Foundations
By the end of Level 1, the learner can:
1. Use security vocabulary (threat, vulnerability, risk, control, asset, CIA) precisely and consistently.
2. Reason about risk at a basic level (5×5 matrix, control selection, risk treatment).
3. Articulate governance, ethics, and legal boundaries — including authorization — and draft simple security policies.
4. Read network traffic and protocol exchanges with Wireshark on an isolated lab network.
5. Harden a Linux and a Windows endpoint to a documented baseline.

### Level 2 — Core Technical Security Skills
By the end of Level 2, the learner can:
1. Use cryptographic tools correctly and identify common cryptographic misdesigns.
2. Apply authentication, MFA, and least-privilege authorization in a working system.
3. Build segmented networks with firewall rules and read IDS alerts.
4. Identify, exploit **in-lab only**, and professionally report OWASP Top 10:2025 classes.
5. Remediate seeded code weaknesses and enforce security gates in a pipeline.
6. Produce a STRIDE threat model with risk-ranked mitigations.

### Level 3 — Practical Security Assessment and Defense
By the end of Level 3, the learner can:
1. Run an authorized assessment end-to-end with rules of engagement, validated findings, and a client-quality report.
2. Engineer detections (Sigma-style) mapped to MITRE ATT&CK and triage alerts against a playbook.
3. Write an IR plan and reconstruct incident timelines from forensic artifacts with chain-of-custody discipline.
4. Triage malware samples safely (static + dynamic) and hand results to detection engineering.

### Level 4 — Advanced Security and Capstone
By the end of Level 4, the learner can:
1. Harden container/IaC workloads and review cloud architectures against shared-responsibility and CIS-derived controls.
2. Complete a DPIA-style privacy assessment and map controls across CSF 2.0 / CIS v8.1 / ISO 27001:2022.
3. Automate security tasks and pipelines, and evaluate automation failure modes.
4. Analyze an emerging challenge (AI/ML security, supply chain, ransomware trends) with credible sources.
5. Integrate everything into a documented, reproducible, safely conducted capstone.

## 4. CLO → module map

Legend: **●** primary evidence · **○** supporting coverage.

| CLO | M01 | M02 | M03 | M04 | M05 | M06 | M07 | M08 | M09 | M10 | M11 | M12 | M13 | M14 | M15 | M16 | M17 | M18 | M19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLO-1 | ● | ○ | ● | | | | | | | | | | | | | | ○ | | ○ |
| CLO-2 | ○ | ● | ○ | | | | | | | | | | | | | | ● | | ○ |
| CLO-3 | | | | ○ | ● | | | ● | | | | | | | | ○ | | | ● |
| CLO-4 | | | | | | ● | ○ | | ○ | | | | | | ○ | | | | ○ |
| CLO-5 | | | | | | | ● | | ○ | | | | | | | | | | ● |
| CLO-6 | | | | | | | | ○ | ● | | | ● | | | | | | | ● |
| CLO-7 | | | | | | | | | ○ | ● | | | | | | | | ● | ● |
| CLO-8 | | | | | | | | | | | ● | | | | | ○ | | | ● |
| CLO-9 | | | | | ○ | | | | | | | | ● | ● | ○ | | | ○ | ● |
| CLO-10 | | | | | ○ | | | | | | | | | ○ | ● | | | | ● |
| CLO-11 | | | | | | | | | | | | | | | | ● | ● | | ● |
| CLO-12 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |

## 5. Progression and scaffolding logic

1. **Vocabulary before technique** (M01–M03): misapplied skill without authorization or risk framing is the primary harm mode in security education.
2. **Transport before defense, defense before offense** (M04 → M08/M09 → M12): learners must understand how systems communicate before testing them.
3. **Defend before assess** (M13–M14 before M12 is *not* required, but M13/M14 build on M05–M08): detection and response follow the same network/OS foundations; M12 (assessment) precedes M13 to keep the offensive track supervised by rules-of-engagement discipline before learners start watching their own lab firewalls.
4. **Secure code after seeing broken code** (M09 → M10): vulnerability classes are learned experientially first, then remediation patterns.
5. **Design last in Level 2** (M11): threat modeling draws on every prior technical module.
6. **Integration at the top** (M19): the capstone is deliberately impossible without all four levels.

## 6. Measuring and maintaining outcomes

- Graded scenario items cite the CLO(s) they measure (see the scenario table in the [Assessment Guide](./assessment-guide.md)), and every module quiz cites the module learning outcomes it measures; CLO-level coverage is then asserted by the module map above — no CLO is assessed by a single item only (each CLO has ≥ 2 evidence points, marked ● and ○). *(Wording corrected 2026-10-10 during quality audit: quizzes reference module outcomes, not CLO labels directly.)*
- **Version maintenance:** outcomes are reviewed whenever a cited standard changes edition (see the version table in the [Course Roadmap](./course-roadmap.md)). Last reference check: 2026-10-09.
- **Accessibility:** outcomes avoid institutional jargon; each is demonstrated through an artifact a self-study learner can produce without lab partners or paid tooling.

## 7. References

- NIST CSF 2.0, NIST CSWP 29 (Feb 2024) — function structure informing CLO-2/CLO-12.
- NIST SP 800-61 Rev. 3 (Apr 2025) — CLO-9.
- NIST SP 800-63-4 (Jul 2025) — CLO-5.
- CIS Controls v8.1 (Jun 2024) — CLO-2/CLO-11.
- OWASP Top 10:2025; OWASP ASVS 5.0.0 (May 2025); OWASP WSTG v4.2 — CLO-6/CLO-7.
- MITRE ATT&CK v19.x (2026) — CLO-9/CLO-10.
