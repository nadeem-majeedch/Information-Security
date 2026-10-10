---
title: "Course Completion Matrix"
layout: default
---

# Course Completion Matrix

**Date:** 2026-10-10 · **Purpose:** maps every planned module and course learning outcome to its lesson, labs, assessments, and references, with honest completion status. Companion to the [Quality Audit](./quality-audit.md).

**Legend:** ✅ full lesson published · 🟩 specification published (measurable outcomes, core concepts, completion criteria in the [Course Roadmap](./course-roadmap.md)) with an **outline lesson page** — the lesson-prose gap is audit finding F-01 · **Q-n** = module quiz with n questions (pass ≥ 80%, worked answers, unlimited retakes).

---

## Table A — Modules (M01–M19)

| # | Module (level) | Lesson | Labs | Assessments | Key references (roadmap "further reading" + reference library) |
|---|---|---|---|---|---|
| M01 | Foundations & CIA Triad (L1) | ✅ full | LAB-01 (primary) | Q-12 · CS-1 | NIST CSF 2.0; SP 800-12r1 |
| M02 | Threats, Vulnerabilities, Risk & Controls (L1) | ✅ full | LAB-02 (also M11) | Q-12 · CS-1 | CVSS v4.0 spec; SP 800-30r1; CISA KEV |
| M03 | Governance, Policy, Ethics & Law (L1) | ✅ full | LAB-14 (supporting) | Q-10 · CS-1 | PECA 2016 (as amended); GDPR text; (ISC)² ethics; OWASP disclosure |
| M04 | Networking Fundamentals for Security (L1) | ✅ full | LAB-07 | Q-12 | RFC 1122/793; Wireshark docs; SP 800-41r1; Cloudflare Learning |
| M05 | OS & Endpoint Security (L1) | ✅ full | LAB-04 (also M07); LAB-08 (also M08) | Q-12 | CIS Benchmarks; SP 800-123; Microsoft security baselines |
| M06 | Cryptography (L2) | 🟩 outline | LAB-05 (primary); LAB-03 (also M07); LAB-11 (supporting) | Q-14 · CS-2 | OWASP Crypto/Password cheat sheets; SP 800-57; FIPS 203/204/205 |
| M07 | Identity, AuthN/AuthZ & Access Mgmt (L2) | 🟩 outline | LAB-06 (primary); LAB-03, LAB-04 (supporting) | Q-12 · CS-2 | SP 800-63-4 (final, Jul 2025); OWASP AuthN/AuthZ cheat sheets; OAuth.net |
| M08 | Network Security (L2) | 🟩 outline | LAB-08 (primary) | Q-12 | SP 800-41r1; Suricata docs; ATT&CK for Network |
| M09 | Web Application Security (L2) | 🟩 outline | LAB-10 (primary); LAB-11 (supporting) | Q-14 · CS-2 | OWASP Top 10:2025; ASVS 5.0; WSTG v4.2 |
| M10 | Secure Programming (L2) | 🟩 outline | LAB-09 (primary) | Q-12 | CWE Top 25; OWASP SAMM; supply-chain cheat sheets; SLSA |
| M11 | Threat Modeling & Architecture (L2) | 🟩 outline | LAB-02 (supporting) | Q-10 · CS-2 (S4) | SP 800-154 (draft — flagged); Microsoft STRIDE; SP 800-207 |
| M12 | Vulnerability Assessment & Authorized Testing (L3) | 🟩 outline | LAB-12 (primary) | Q-12 | SP 800-115; WSTG v4.2; PTES; CVSS v4.0 |
| M13 | Logging, Monitoring & SecOps (L3) | 🟩 outline | LAB-13 (primary); LAB-18 (supporting) | Q-12 · CS-3 (S5) | SP 800-92; MITRE ATT&CK; SigmaHQ; CISA detection playbooks |
| M14 | Incident Response & Forensics (L3) | 🟩 outline | LAB-14 (primary); LAB-15 (supporting) | Q-14 · CS-3 | SP 800-61r3 (Apr 2025); SP 800-86; SP 800-101; CISA IR playbooks |
| M15 | Malware & Defensive Analysis (L3) | 🟩 outline | LAB-16 (primary) | Q-12 · CS-3 | ATT&CK malware behavior pages; YARA docs; CISA #StopRansomware |
| M16 | Cloud & Infrastructure Security (L4) | 🟩 outline | LAB-17 (primary) | Q-12 · CS-4 | Cloud providers' shared-responsibility docs; CIS Docker/K8s benchmarks; SP 800-204 |
| M17 | Privacy, Data Protection & Compliance (L4) | 🟩 outline | *(no dedicated lab — DPIA-style deliverable; CS-4 covers)* | Q-12 · CS-4 | NIST Privacy Framework 1.0; ICO DPIA guidance; ISO/IEC 27001:2022; GDPR text |
| M18 | Security Automation & Emerging Challenges (L4) | 🟩 outline | LAB-18 (primary) | Q-12 · CS-4 (S6) | OWASP Top 10 for LLM Apps; NIST AI RMF 1.0 |
| M19 | Integrated Capstone (L4) | 🟩 outline | LAB-19 (integrates LAB-13/15/16/17 datasets) | Capstone rubric + stage checklists ([capstone](./capstone/README.md)) · CAP-ADV | SP 800-61r3 + CSF 2.0 integration; CIS v8.1 IG1; public post-mortems |

**Level totals:** L1 5 modules · L2 6 · L3 4 · L4 4. Every module has ≥ 1 lab, a quiz (or the capstone rubric), and a further-reading set; all labs and assessments are machine-validated (see [quality audit](./quality-audit.md)).

## Table B — Course learning outcomes (CLO-1 … CLO-12)

Mapping per [learning-outcomes.md](./learning-outcomes.md) §4 (● primary evidence · ○ supporting).

| CLO | Outcome (abridged) | ● Primary modules | ○ Supporting | Evidence instruments | Standards |
|---|---|---|---|---|---|
| CLO-1 | Explain CIA triad, assets/threats, governance/policy/ethics frame | M01, M03 | M02, M17, M19 | Q-01/02/03, policy set, ethics cases | CSF 2.0 |
| CLO-2 | Analyze threats/vulnerabilities/risk; select controls (CSF, CIS, CVSS) | M02, M17 | M01, M03, M19 | Risk register, control mapping, Q-02 | CSF 2.0, CIS v8.1, CVSS v4.0, SP 800-30 |
| CLO-3 | Apply OS/network defensive configuration in an isolated lab | M05, M08 | M04, M16, M19 | Hardening packs, firewall rules, Q-05/08 | CIS Benchmarks, SP 800-41/123 |
| CLO-4 | Apply cryptography correctly; evaluate for misuse | M06 | M07, M09, M15, M19 | Crypto notebook, misuse analysis, Q-06 | FIPS 203-205, OWASP crypto sheets |
| CLO-5 | Design IAM arrangements (MFA, least privilege, RBAC) | M07 | M09, M19 | IAM design note + lab, Q-07 | SP 800-63-4 |
| CLO-6 | Assess systems within authorized scope; report professionally | M09, M12 | M07, M19 | Web report, engagement report, Q-09/12 | Top 10:2025, WSTG, ASVS |
| CLO-7 | Develop secure software; run SAST/SCA/secret gates | M10 | M09, M18, M19 | Patch set + pipeline evidence, Q-10/18 | CWE Top 25, SAMM |
| CLO-8 | Model threats (STRIDE, DFDs); evaluate architecture | M11 | M14, M19 | Threat model, capstone Stage A, Q-11 | SP 800-154, SP 800-207 |
| CLO-9 | Operate detection & response (ATT&CK-mapped), triage, IR, forensics | M13, M14 | M12, M16, M18, M19 | Detection pack, IR plan, timelines, Q-13/14 | ATT&CK v19, SP 800-61r3, SP 800-92/86 |
| CLO-10 | Analyze malware defensively; convert to detections/IOCs | M15 | M13, M18, M19 | Triage reports, YARA/Sigma rules, Q-15 | ATT&CK, YARA docs |
| CLO-11 | Evaluate cloud security & privacy obligations; DPIA-style work | M16, M17 | M18, M19 | Cloud audits, DPIA + mapping, Q-16/17 | CIS v8.1, Privacy Framework, ISO 27001:2022 |
| CLO-12 | Synthesize the pathway in the capstone; professional reflection | M19 | all (M01–M18 as ○) | Capstone portfolio, CAP-ADV (S6) | CSF 2.0, CIS v8.1 IG1 |

## Supporting instruments (cross-module)

| Instrument | Spans | Role |
|---|---|---|
| CS-1 … CS-4 case studies | M01–05 · M06–11 · M12–15 · M16–18 | Integrative graded scenarios (rubric §5.2), mapped to CLOs S1–S6 in the Assessment Guide |
| CAP-ADV (advanced final) | Level 3–4 | Capstone-preparatory written assessment |
| Lab challenges | per lab | Optional depth extensions inside each lab |
| Capstone rubric + checklists | M19 | Stage-gated evaluation (5 stages / gates G1–G7 in the [capstone package](./capstone/README.md)) |

## Honest status summary

- **Fully student-ready today:** Level 1 (M01–M05) — full lessons + labs + quizzes.
- **Specification-ready, lesson-in-progress:** Levels 2–4 (M06–M19) — complete outcomes, labs, datasets, quizzes with worked answers, and curated references; authored lesson prose is pending (audit F-01, owner decision).
- **Everything machine-checkable is green:** labs (17-point format), assessments (counts/answers/links), references (66 entries + URL manifest), site build and 1399 internal links, accessibility (0 axe violations on audited pages).
