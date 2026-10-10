# Information Security — A Self-Study Course from Beginner to Advanced

A complete, free course in information security — **19 modules across 4 progressive levels**, from your very first security concepts to an integrated capstone where you architect, harden, assess, and defend a system. Every module is written for **independent learners**: study on your own schedule, prove your skills through a personal portfolio of evidence, and use only free tools in isolated, safe labs.

**Start in three steps:** check the [Prerequisites](docs/prerequisites.md) · read the [Lab Safety Policy](docs/lab-safety-policy.md) · begin [Module 01](docs/modules/module-01-information-security-foundations/README.md).

---

## Table of Contents

- [What You Will Learn](#what-you-will-learn)
- [Who This Course Is For](#who-this-course-is-for)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Course Contents (All 19 Modules)](#course-contents-all-19-modules)
- [Progression Map](#progression-map)
- [How to Study Each Module](#how-to-study-each-module)
- [Labs and Your Lab Portfolio](#labs-and-your-lab-portfolio)
- [Safety, Authorization, and Responsible Use](#safety-authorization-and-responsible-use)
- [Assessment and Self-Evaluation](#assessment-and-self-evaluation)
- [Free Tools and Learning Resources](#free-tools-and-learning-resources)
- [If You Get Stuck](#if-you-get-stuck)
- [About the Instructor](#about-the-instructor)
- [Educational Use and Attribution](#educational-use-and-attribution)

## What You Will Learn

- **Reason about risk:** the CIA triad, threats vs. vulnerabilities vs. controls, and how to rank and treat risk with recognized frameworks (NIST CSF 2.0, CIS Controls v8.1).
- **Defend systems:** harden Linux and Windows hosts, segment networks with firewall rules, and read intrusion-detection alerts.
- **Use cryptography correctly:** encrypt, sign, verify, and spot common crypto misdesigns (weak hashing, static IVs, hard-coded keys).
- **Control access:** authentication factors, MFA, least privilege, and role-based access — designed against NIST SP 800-63-4 guidance.
- **Break things safely, then fix them:** find web vulnerabilities against local, deliberately vulnerable apps using the OWASP Top 10:2025, and write professional reports.
- **Write secure software:** remediate common weaknesses and run security checks automatically in a delivery pipeline.
- **Think like an architect:** model threats with STRIDE and evaluate designs against zero-trust principles.
- **Detect and respond:** engineer logging and detections mapped to MITRE ATT&CK, triage alerts, run incident response, and reconstruct forensic timelines.
- **Analyze malware defensively** in an isolated sandbox and turn findings into detections.
- **Operate at program level:** cloud/container security, privacy and compliance (DPIA, control mapping), security automation — integrated in a five-stage capstone.

The full, measurable statement of these outcomes — each mapped to the modules that assess it — is in [docs/learning-outcomes.md](docs/learning-outcomes.md).

## Who This Course Is For

- **Self-study learners** with no prior security background: students, career-changers, and early-career IT staff.
- **Working professionals** near security (developers, data engineers, network admins) who want structured depth.
- **Instructors** who wish to adopt the materials for a class.

**Prerequisites (summary — full detail in [docs/prerequisites.md](docs/prerequisites.md)):**

- Comfort with basic computing: installing software, managing files, following English-language technical documentation (B1+ reading).
- No mathematics beyond secondary school; no programming required until Module 10 (basic programming in any language by then — resources listed).
- A computer with 8 GB RAM (16 GB recommended), ~60 GB free disk, and hardware virtualization. **Total course cost: $0.**
- Commitment of 8–12 hours/week for roughly 7–9 months.
- Agreement to follow the [Lab Safety Policy](docs/lab-safety-policy.md).

## Course Learning Outcomes

On completion, you can demonstrate all twelve outcomes (Bloom levels and evidence in [docs/learning-outcomes.md](docs/learning-outcomes.md)):

| ID | Outcome |
|---|---|
| CLO-1 | Explain core security principles — CIA triad, asset/threat vocabulary, and the governance, ethics, and legal frame of security work. |
| CLO-2 | Analyze threats, vulnerabilities, and risk, and select controls using NIST CSF 2.0, CIS Controls v8.1, and CVSS v4.0. |
| CLO-3 | Apply defensive configuration on operating systems and networks — hardening, segmentation, firewall rules, IDS. |
| CLO-4 | Apply cryptography correctly and evaluate designs for misuse. |
| CLO-5 | Design identity and access arrangements (MFA, least privilege, RBAC) consistent with NIST SP 800-63-4. |
| CLO-6 | Assess systems **within authorized scope** using OWASP Top 10:2025, WSTG, and ASVS — and report findings professionally. |
| CLO-7 | Develop secure software: fix common weaknesses and operate SAST/secret/dependency-scanning gates. |
| CLO-8 | Model threats (STRIDE, data-flow diagrams) and evaluate architectures against risk-based and zero-trust principles. |
| CLO-9 | Operate detection and response: ATT&CK-mapped detections, alert triage, incident response, and forensic timelines. |
| CLO-10 | Analyze malware artifacts safely and defensively, converting observations into detections and IOCs. |
| CLO-11 | Evaluate cloud/infrastructure security and privacy obligations, mapping controls across frameworks. |
| CLO-12 | Synthesize everything into an integrated capstone: architect, harden, assess, defend, and document. |

## Course Contents (All 19 Modules)

Complete the modules in this order. Each link opens the module page (outcomes, deliverables, and full specification).

### Level 1 — Information Security Foundations

| # | Module | Est. time |
|---|---|---|
| 01 | [Information Security Foundations and the CIA Triad](docs/modules/module-01-information-security-foundations/README.md) | 8–10 h |
| 02 | [Threats, Vulnerabilities, Risk, and Controls](docs/modules/module-02-threats-vulnerabilities-risk-and-controls/README.md) | 10–12 h |
| 03 | [Security Governance, Policy, Ethics, and Law](docs/modules/module-03-governance-policy-ethics-and-law/README.md) | 8–10 h |
| 04 | [Networking Fundamentals for Security](docs/modules/module-04-networking-fundamentals-for-security/README.md) | 12–14 h |
| 05 | [Operating System and Endpoint Security](docs/modules/module-05-operating-system-and-endpoint-security/README.md) | 12–14 h |

### Level 2 — Core Technical Security Skills

| # | Module | Est. time |
|---|---|---|
| 06 | [Cryptography and Applied Cryptography](docs/modules/module-06-cryptography/README.md) | 14–16 h |
| 07 | [Identity, Authentication, Authorization, and Access Management](docs/modules/module-07-identity-and-access-management/README.md) | 12–14 h |
| 08 | [Network Security: Perimeter, Segmentation, and Secure Protocols](docs/modules/module-08-network-security/README.md) | 14–16 h |
| 09 | [Web Application Security (OWASP Top 10:2025)](docs/modules/module-09-web-application-security/README.md) | 18–20 h |
| 10 | [Secure Programming and Software Security](docs/modules/module-10-secure-programming/README.md) | 18–20 h |
| 11 | [Threat Modeling and Security Architecture](docs/modules/module-11-threat-modeling-and-security-architecture/README.md) | 12–14 h |

### Level 3 — Practical Security Assessment and Defense

| # | Module | Est. time |
|---|---|---|
| 12 | [Vulnerability Assessment and Authorized Security Testing](docs/modules/module-12-vulnerability-assessment-and-security-testing/README.md) | 16–18 h |
| 13 | [Logging, Monitoring, and Security Operations](docs/modules/module-13-logging-monitoring-and-security-operations/README.md) | 16–18 h |
| 14 | [Incident Response and Digital Forensics](docs/modules/module-14-incident-response-and-digital-forensics/README.md) | 18–20 h |
| 15 | [Malware Concepts and Defensive Analysis](docs/modules/module-15-malware-and-defensive-analysis/README.md) | 16–18 h |

### Level 4 — Advanced Security and Capstone

| # | Module | Est. time |
|---|---|---|
| 16 | [Cloud and Infrastructure Security](docs/modules/module-16-cloud-and-infrastructure-security/README.md) | 16–18 h |
| 17 | [Privacy, Data Protection, Risk Management, and Compliance](docs/modules/module-17-privacy-data-protection-and-compliance/README.md) | 12–14 h |
| 18 | [Security Automation and Emerging Challenges](docs/modules/module-18-security-automation-and-emerging-challenges/README.md) | 14–16 h |
| 19 | [**Integrated Capstone Project**](docs/modules/module-19-integrated-capstone-project/README.md) | 30–40 h |

### Course sections

| Section | Purpose |
|---|---|
| [Course Roadmap](docs/course-roadmap.md) | Full curriculum specification (per-module labs, concepts, completion criteria, references) |
| [Learning Outcomes](docs/learning-outcomes.md) | Measurable outcomes and module mapping |
| [Prerequisites](docs/prerequisites.md) | Entry requirements, hardware/software, pacing |
| [**Lab Collection**](docs/labs/README.md) | All hands-on labs by module + portfolio rules |
| [**Assessment Guide**](docs/assessment-guide.md) | Quizzes, scenario exercises, portfolio, investigations, capstone rubric |
| [**Lab Safety Policy**](docs/lab-safety-policy.md) | Authorization, isolation, prohibited activities |
| [Module Index](docs/modules/README.md) | All modules on one page |
| [About the Course](docs/about-the-course.md) | Design principles, standards, and use terms |
| [**Capstone**](docs/modules/module-19-integrated-capstone-project/README.md) | The five-stage final project |

## Progression Map

```text
BEGINNER                    INTERMEDIATE                PRACTITIONER                ADVANCED
Level 1                     Level 2                     Level 3                     Level 4
Foundations        ──▶      Core Technical Skills  ──▶   Assessment & Defense  ──▶   Advanced & Capstone
M01–M05                    M06–M11                      M12–M15                     M16–M19

CIA, risk,          Crypto, IAM, network       Authorized testing,         Cloud, privacy,
governance,         defense, web security,     SOC detection, IR/          automation,
networking,         secure code, threat        forensics, malware          emerging threats,
OS hardening        modeling                   defense                     CAPSTONE (M19)
```

**Rules:** modules run in order; each level gate requires all prior-level modules finished (knowledge check ≥ 80% + deliverables submitted). Full rules in [Progression and course completion](docs/course-roadmap.md#progression-rules-and-course-completion).

## How to Study Each Module

Every module page follows the same self-study loop:

1. **Read the prerequisites** — confirm the previous modules are done.
2. **Read the learning outcomes** — these are what you must be able to *do*.
3. **Study the material** with your own notes (any Markdown editor). Follow "Further reading" references — official documentation first.
4. **Do the labs** in your isolated environment (see next section).
5. **Produce the deliverable(s)** — the portfolio pack listed on each module page.
6. **Take the knowledge check** — self-grade with the answer key; retake until ≥ 80%.
7. **Reflect** — one short paragraph: what changed in your mental model?
8. **Move on** only when the module's completion criteria are met.

Suggested rhythm: one module per 1–2 weeks at 8–12 hours/week. Detailed per-module specifications live in the [Course Roadmap](docs/course-roadmap.md).

## Labs and Your Lab Portfolio

- **Where the labs live:** the [Lab Collection](docs/labs/README.md) lists every lab by module, its environment, and the artifact it produces.
- **Environments:** free, local, and isolated — a host-only VM network, deliberately vulnerable apps you run yourself (Juice Shop, DVWA, WebGoat), your own hardening VMs, and synthetic evidence bundles. Full list in [Prerequisites](docs/prerequisites.md).
- **Portfolio discipline:** keep `portfolio/M01/` … `portfolio/M19/`, each containing the deliverable, annotated evidence (screenshots/logs), and a one-line **safety statement** (targets used + isolation method). How it's graded: [Assessment Guide](docs/assessment-guide.md).
- **The golden rule:** *if it isn't evidenced, it isn't done.* Save commands and outputs as you go — your portfolio becomes your interview artifact after the course.

## Safety, Authorization, and Responsible Use

This course teaches techniques that are powerful and, without authorization, illegal. Non-negotiable rules (full policy: [docs/lab-safety-policy.md](docs/lab-safety-policy.md)):

1. **Authorization first** — test only systems you own or have written permission to test.
2. **Isolate** — offensive labs run on host-only/internal networks, proven with an isolation checklist before each lab.
3. **No public targets** — never scan, probe, or exploit random public systems, neighbors' networks, or services you don't own.
4. **Defensive-only malware handling** — analysis stays in an isolated sandbox; this course never requires real-world malware.
5. **Synthetic data only** — never real personal data in labs or submissions.

Ethical boundaries, responsible disclosure, and the legal frame (including Pakistan's PECA 2016 as amended) are taught in [Module 03](docs/modules/module-03-governance-policy-ethics-and-law/README.md). Any submitted work that violates the safety policy is returned ungraded under the [safety gate](docs/assessment-guide.md).

## Assessment and Self-Evaluation

You assess yourself with clear rubrics; instructors adopting the course can grade the same way. Details in the [Assessment Guide](docs/assessment-guide.md).

| Component | Role | Weight |
|---|---|---|
| Knowledge checks (18 quizzes) | **Practice/gate** — self-graded, retake until ≥ 80% | 0% |
| Scenario exercises (6) | **Graded** — judgment and decision-writing | 20% |
| Lab portfolio (module packs) | **Graded** — evidence of executed skills | 40% |
| Defensive investigations (M13–M15 + integrative) | **Graded** — profession-like reports | 20% |
| Capstone (5 stages) | **Graded** — integrated demonstration | 20% |

**Practice vs. graded:** quiz retakes, worked examples, checklists, and side-exercises are practice — free to fail, never submitted. Items marked *Assessed* (scenarios, portfolio packs, investigations, capstone) carry the weight. Course pass: ≥ 60% in every graded component with the capstone stage standard met, plus full safety compliance. Self-check your standing anytime against the [completion criteria](docs/course-roadmap.md#progression-rules-and-course-completion).

## Free Tools and Learning Resources

All tools are free/open-source and run on your own machine (full table with per-module uses in [docs/prerequisites.md](docs/prerequisites.md)):

| Area | Tools |
|---|---|
| Networking & capture | Wireshark, Nmap (lab IPs only) |
| Virtualization | VirtualBox or VMware Workstation Player (personal use), Ubuntu/Debian ISOs, Microsoft free developer VMs |
| Web testing | OWASP Juice Shop, DVWA, WebGoat, OWASP ZAP, Burp Suite Community Edition |
| Crypto & identity | OpenSSL, GnuPG, CyberChef, Keycloak/Vault (community) |
| Detection & defense | Suricata + ET Open rules, Sigma rules, `journalctl`/`auditd`, Sysmon |
| Forensics & malware | Autopsy, The Sleuth Kit, YARA, Volatility |
| Code & supply-chain | Semgrep Community, Gitleaks, Trivy, `pip-audit`/`npm audit` |
| Containers & IaC | Docker Engine or Podman, Trivy, Checkov |

**Authoritative references (free):** [NIST CSF 2.0 & SP publications](https://csrc.nist.gov) · [OWASP Top 10, ASVS, WSTG, Cheat Sheets](https://owasp.org) · [CISA resources](https://www.cisa.gov) · [MITRE ATT&CK](https://attack.mitre.org) · [CIS Controls](https://www.cisecurity.org/controls) · [FIRST CVSS v4.0](https://www.first.org/cvss) · [NIST NVD](https://nvd.nist.gov). Standards editions used in the course are listed with verification dates in the [Course Roadmap](docs/course-roadmap.md#reference-and-version-policy).

## If You Get Stuck

1. **Re-check the chain** — most dead-ends come from skipping a prerequisite; the module page lists them.
2. **Re-check your lab isolation** — a failing lab is often a network/adapter setting; run the [isolation checklist](docs/lab-safety-policy.md).
3. **Reduce the step** — split the exercise into smaller commands; verify each output against the module's expected evidence.
4. **Use the completion criteria** — they state exactly what "done" looks like; compare your pack against them.
5. **Read the reference first** — every module's "Further reading" points to official docs (Wireshark wiki, Nmap guide, OWASP cheat sheets) that answer most setup issues.
6. **Rest and return** — knowledge checks allow unlimited retakes; if you've been away, redo the last quiz to reactivate context (see [Progression rules](docs/course-roadmap.md#progression-rules-and-course-completion)).

## About the Instructor

**Engr. Dr. Muhammad Nadeem Majeed**
Professor
Department of Data Science (PUCIT)
University of the Punjab, Lahore, Pakistan

## Educational Use and Attribution

Course materials in this repository are © 2026 Engr. Dr. Muhammad Nadeem Majeed, provided **free of charge for personal study and for classroom use with attribution**. When reusing or adapting substantial portions, credit the course title, the instructor's name, and a link to this repository. Selling the materials, removing attribution, or presenting derived content as your own is not permitted without written permission. Code snippets and configuration examples inside the course may be freely reused in your own labs. This is the repository's documented licensing decision until a formal `LICENSE` file is added, which would supersede it — full statement in [About the Course](docs/about-the-course.md).

---

**Quick links:** [Course Roadmap](docs/course-roadmap.md) · [Module Index](docs/modules/README.md) · [Lab Collection](docs/labs/README.md) · [Assessment Guide](docs/assessment-guide.md) · [Lab Safety Policy](docs/lab-safety-policy.md) · [Prerequisites](docs/prerequisites.md) · [Learning Outcomes](docs/learning-outcomes.md)
