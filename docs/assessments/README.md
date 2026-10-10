---
title: "Assessment Hub"
layout: default
---

# Assessment Hub

**Course:** Information Security: A Self-Study Course from Beginner to Advanced
**Companion documents:** [Assessment Guide](../assessment-guide.md) (weights, rubrics, policy) · [Learning Outcomes](../learning-outcomes.md) · [Course Roadmap](../course-roadmap.md) · [Lab Safety Policy](../lab-safety-policy.md)

This hub holds every self-check and graded instrument in the course. Because this is a **self-study** course, every assessment is designed so you can run it, mark it, and improve **without an instructor**. Nothing here needs a proctor, a paid tool, or a lab partner.

---

## How assessment works here

1. **Practice first, always.** Quizzes and review exercises are *formative*: attempt them openly, mark them against the worked answers, retake until you clear the gate. They never penalise a wrong first try.
2. **Gates, not grades, for recall.** Each module quiz is a completion gate (typically ≥ 80%) that unlocks the next module. It carries no weight in a final percentage — that weight lives in labs, scenarios, investigations, and the capstone (see the [Assessment Guide](../assessment-guide.md)).
3. **Judgment is graded separately.** Scenario exercises, the capstone, and investigation challenges test *decisions*, which a quiz cannot. They use published rubrics.
4. **Safety is a gate, not a score.** Any work that breaks the [Lab Safety Policy](../lab-safety-policy.md) is returned for correction, not graded.

## Student-facing answer policy — read this

**Every worked answer, model response, and rubric in this course is published to students, openly and by design.**

- Answers live inside collapsible `<details>` blocks on the same page as the questions, or on the same page as the exercise. They are real page content — not hidden behind JavaScript tricks, obfuscated markup, or secret filenames.
- This is **honest transparency, not "security through obscurity."** In a self-study course there is no private instructor key to protect; withholding answers would only make honest self-assessment impossible.
- The educational sequence is always: **attempt → then reveal.** The collapsible blocks exist to support that sequence, not to conceal anything. If you reveal an answer before trying, that is a study-habit choice, not a security boundary.
- If you are an **instructor** adopting this course and want genuinely private marking material, keep it in a separate private repository or local folder outside the published site — do not rely on hiding it inside these pages. The [Assessment Guide §9](../assessment-guide.md) explains how to adapt weighting.

## Question-quality standard

Every quiz in this hub follows the same rules:

- Clear instructions and an unambiguous pass mark.
- Plausible distractors for multiple-choice — each wrong option maps to a real misconception, and the key explains *why* it is wrong.
- Every question mapped to a learning outcome and linked back to the lesson that teaches it.
- Worked answers that state the correct response **and** the reasoning.
- A difficulty progression from recall → comprehension → application → judgment, with no two questions testing the same fact.

## What's here

### Module quizzes (formative completion gates)

Ten to fourteen questions each, matching the format published in the [Course Roadmap](../course-roadmap.md). Self-graded, unlimited retakes, ≥ 80% to progress.

| Level | Module quizzes |
|---|---|
| **1 · Foundations** | [M01](./level-1/quiz-m01.md) · [M02](./level-1/quiz-m02.md) · [M03](./level-1/quiz-m03.md) · [M04](./level-1/quiz-m04.md) · [M05](./level-1/quiz-m05.md) |
| **2 · Core Technical** | [M06](./level-2/quiz-m06.md) · [M07](./level-2/quiz-m07.md) · [M08](./level-2/quiz-m08.md) · [M09](./level-2/quiz-m09.md) · [M10](./level-2/quiz-m10.md) · [M11](./level-2/quiz-m11.md) |
| **3 · Assessment & Defense** | [M12](./level-3/quiz-m12.md) · [M13](./level-3/quiz-m13.md) · [M14](./level-3/quiz-m14.md) · [M15](./level-3/quiz-m15.md) |
| **4 · Advanced & Capstone** | [M16](./level-4/quiz-m16.md) · [M17](./level-4/quiz-m17.md) · [M18](./level-4/quiz-m18.md) |

### Module-end review exercises

After each quiz, a short set of harder *ungraded* exercises that pull the whole module together — configuration analysis, log interpretation, risk prioritization, and practical investigation. These sit right after the quiz on each quiz page.

### Cross-module case studies (integrative, scenario-based)

Multi-concept situations that deliberately span several modules, with model answers and the same published rubric used for graded scenarios.

| ID | Spans | Focus |
|---|---|---|
| [CS-1](./case-studies/cs-1-breach-at-meridian.md) | M01–M05 | A small-org breach: triad, risk, governance, network, and endpoint reasoning |
| [CS-2](./case-studies/cs-2-product-launch-crypto-identity.md) | M06–M11 | Crypto, identity, network defense, web, and threat-model decisions for a launch |
| [CS-3](./case-studies/cs-3-detection-to-response.md) | M12–M15 | From scoped testing through detection, IR, forensics, and malware triage |
| [CS-4](./case-studies/cs-4-cloud-privacy-automation.md) | M16–M18 | Cloud config, privacy obligations, and automation risk |

### Practical lab challenges

Hands-on, deliverable-driven challenges tied to the [Lab Collection](../labs/README.md). Each names its deliverables and evaluation criteria.

| ID | Tied to | Deliverable focus |
|---|---|---|
| [LC-1](./final/lab-challenges.md#lc-1--endpoint-to-perimeter-l1) | M01–M05 | Harden an endpoint, prove isolation, defend the configuration |
| [LC-2](./final/lab-challenges.md#lc-2--identity-and-web-l2) | M06–M11 | Design IAM, secure a local app, ship a security gate |
| [LC-3](./final/lab-challenges.md#lc-3--detect-and-respond-l3) | M12–M15 | Scoped assessment → detection → IR → forensic timeline |
| [LC-4](./final/lab-challenges.md#lc-4--secure-the-stack-l4) | M16–M18 | Harden cloud/IaC, complete a DPIA, automate a control |

### Advanced final assessment

- **[CAP-ADV — Advanced Final Assessment](./final/advanced-final.md)** — a proctored-free, open-book, time-boxed exam spanning all four levels. The hardest written instrument in the course; recommended after M18, before or alongside the capstone.

### Capstone rubric

- **[Capstone Assessment Rubric](./final/capstone-rubric.md)** — the standalone, expanded scoring rubric for the M19 Integrated Capstone Project (stages A–E), self-assessed against five criteria. The full **[M19 Capstone Project](../capstone/README.md)** package — scenario briefs, seven-stage workflow, templates, seven-dimension rubric, checklists — lives beside this hub.

---

## Suggested sequence

```text
Module lesson ──▶ Module quiz (gate ≥ 80%) ──▶ Review exercises
       │                                            │
       └──▶ Lab (portfolio pack)                    │
                                                    ▼
                              Level checkpoint: case study / scenario
                                                    │
                                                    ▼
                    CAP-ADV (advanced final)  +  M19 Capstone (rubric)
```

Start at [Module 01](../modules/module-01-information-security-foundations/README.md) · return to the [Course home](../index.md).
