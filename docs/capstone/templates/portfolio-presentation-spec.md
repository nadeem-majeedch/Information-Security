---
title: "Capstone Template — Portfolio and Presentation Specification"
layout: default
---

# Capstone Template — Portfolio and Presentation Specification

**Part of:** [M19 Capstone Project](../README.md) · Gate ([G7](../checklists.md#g7--final-package-before-submission)). The portfolio is the *product*; the report is its main document. A reviewer who has never met you must be able to audit the engagement from this folder alone (rubric **D6**).

## 1. Folder structure

```text
portfolio/CAPSTONE/
├── README.md                 # index: what's here, O1–O10 → file mapping, links resolve
├── data/
│   └── MANIFEST.md           # file · source · copied-or-referenced · SHA-256
├── S1/ … S7/                 # one folder per stage; each ends with its safety statement
│   ├── notes.md              # stage memo/working notes
│   └── evidence/             # that stage's captures (see naming below)
├── report.md                 # from the report template
├── RUBRIC.md                 # completed scoring sheet (rubric.md)
├── presentation/
│   ├── slides.md             # deck source (Markdown/Mermaid) or exported PDF
│   └── demo-script.md        # 5-minute demo runbook (commands, in order)
└── evidence-index.md         # every artifact: name · bytes · SHA-256 · used-in section
```

**File naming:** `S<stage>-<type>-<nn>-<short-desc>` — types: `finding`, `timeline`, `before`, `after`, `test`, `alert`, `diagram`, `log`.
Example: `S6-test-02-rbacs-denied-403.png`. Lowercase-with-hyphens; no spaces; no `final-final2`.

**Rules:** provided artifacts are never edited (analyze copies — manifest says `copied`); your own captures carry real timestamps; evidence-index.md lists *everything* including things the report doesn't cite (uncited ≠ worthless; missing ≠ existed).

## 2. Final presentation specification

**Format (choose one, both are free):**
- **A — Recorded or live walkthrough (8–10 min):** screen-share the portfolio + one live demo; or
- **B — Written deck (10–12 slides) + demo-script.md** — the default if presenting to no one.

**Slide outline (adapt freely, keep the arc):**

| # | Slide | Must show |
|---|---|---|
| 1 | Title + one-line engagement question | scenario chosen, your name, date |
| 2 | The organization | 5 sentences: who, systems, data, constraints |
| 3 | Scope & safety | in/out of scope + the safety statement (30 seconds, non-negotiable) |
| 4 | Threat picture | the DFD with trust boundaries — narrate 1 attack path |
| 5 | Top risks | heat-map or ranked top 5 — with scales visible |
| 6 | What the evidence showed | one investigation highlight: timeline excerpt + one cited artifact |
| 7 | Findings that mattered | 3 findings, each: evidence → severity+context → register link |
| 8 | The plan | top-5 roadmap: effort vs risk-retired, quick wins marked |
| 9 | Proof it works | live or recorded Stage 6 validation: **before → change → after** (choose your strongest) |
| 10 | Residual risk & unknowns | honest "what we don't know" + owners |
| 11 | Reflection | one decision you'd change and why |
| 12 | Appendix | tools, artifact manifest, self-score |

**Demo rules (both formats):** local lab only · demo-script.md must let a reviewer repeat it · show **real evidence, live** — if the live demo fails, the recorded capture in the portfolio stands in (say so honestly; do not stage fake output). No public-system touches, ever, even "just to show."

**Audience test:** slide 2 + 8 must be understandable by the fictional owner with no security background — one non-technical reader is the bar (report §1 shares this constraint).

## 3. Reflection (500 words, in the report §12)

Prompts: a decision you got wrong first and why · evidence that changed your mind · the module skill that saved you most time · what one more week would change.

## 4. Self-assessment packet

- `RUBRIC.md`: scoring sheet completed with **file-path evidence for each score** ("D3 = 4 because S3-evidence/…") — a score without a pointer is a guess.
- Assistance declaration attached ([§8](../../assessment-guide.md#8-evidence-integrity-and-academic-honesty)).
- Submission checklist from [checklists.md](../checklists.md#submission-checklist) ticked and stored in the root.

## 5. Optional extensions in the portfolio

Mark attempted extensions with a top-level `EXTENSIONS.md` (which, status, evidence). Extensions never replace core gates — core first ([brief §8](../README.md#8-optional-extensions-for-advanced-learners)).

**Back to:** [Capstone brief](../README.md) · [Checklists](../checklists.md) · [Rubric](../rubric.md)
