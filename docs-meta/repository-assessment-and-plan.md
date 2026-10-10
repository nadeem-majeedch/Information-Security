# Repository Assessment & Implementation Plan
**Repository:** `nadeem-majeedch/Information-Security`
**Instructor:** Engr. Dr. Muhammad Nadeem Majeed, Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore
**Date:** 2026-10-09 · **Phase:** 1 of 5 (assessment & planning only — no content generation, no commits, no deploys)

---

## 1. Current repository state (verified)

| Item | Finding |
|---|---|
| Local workspace | `C:\Users\Nadeem\Documents\Information Security` contains **only** `.freebuff/` (app metadata). It is **not** a Git working copy — no `.git`, no source files. |
| Remote repository | **Public, completely empty.** Created 2026-10-09; `git ls-remote` returns no refs; API reports `isEmpty: true` and no default branch. |
| GitHub Pages | **Not enabled** (Pages API returns 404 — no Pages site exists yet). |
| Existing course content | **None in this repo** — nothing to preserve and nothing at risk of being overwritten. |
| Existing tests / CI | **None.** |
| Existing docs / config | **None.** |
| Tooling available locally | Git 2.54, GitHub CLI authenticated as `nadeem-majeedch`, Python available. |

**Conclusion:** this is a greenfield repository. The "preserve existing work" rules are trivially satisfied today, but the plan below deliberately avoids patterns that would create overwrite hazards later.

## 2. Relevant prior art in the instructor's other repositories

These were inspected read-only to reuse what works and avoid what doesn't:

- **`Cyber-Security-Course`** — Jekyll site built by a GitHub Actions workflow from a `website/` tree; root-level `lectures/`, `labs/`, `case-studies/`, `assessments/{student,instructor-only}/`; `docs-meta/` for planning; a CI guard that fails the build if instructor-only material reaches the publish tree.
  - ⚠️ **Weakness observed:** course Markdown exists **twice** (root `lectures/` = 41 files, `website/lectures/` = 40 files, currently byte-identical copies). Two copies of the same content drift over time — one file is already out of sync.
- **`Network-Security-Course`** — MkDocs Material with a dedicated `site-src/` publish tree; canonical student Markdown is *copied* into `site-src/` by `docs-meta/build_site_content.py` before `mkdocs build`; instructor trees sit outside `docs_dir` so they are never in the build input.
  - ⚠️ Same duplication concern, mitigated by a generator script, at the cost of a Python/MkDocs toolchain dependency.
- Other assets: `agent-security-labs`, `Network-Protocol-Visual-Lab` (hands-on lab patterns reusable later).

## 3. Risks & constraints

| # | Risk | Mitigation |
|---|---|---|
| R1 | No local clone yet — edits would have nowhere to be committed by the instructor. | Phase 1 step: clone the repo locally (or `git init` + remote). Instructor keeps sole commit/push control. |
| R2 | Content duplication (`content/` vs `website/`) as seen in sibling repos. | **Single source of truth:** one Markdown tree that is *simultaneously* the GitHub-browsable course and the Pages build input. |
| R3 | Scope overlap with `Cyber-Security-Course` and `Network-Security-Course`. | Define a distinct syllabus for *Information Security* (foundations + breadth, beginner→advanced) and cross-link rather than copy. |
| R4 | Enabling Pages / changing repo settings is outside the agent's allowed actions. | Instructor enables **Settings → Pages → Source: GitHub Actions** after the first push. |
| R5 | Any future instructor-only material (answer keys, exam papers) must never reach the public site. | Keep instructor trees **outside** the site source directory (structural exclusion, same safety property as `Network-Security-Course`); optionally add a CI guard. |
| R6 | Windows paths containing spaces in the workspace path. | All local scripts/commands quote paths; validation tooling kept path-safe. |
| R7 | No verification exists today; a pushed site could silently break. | Local Markdown structure/link checker (Python stdlib only) + the Pages workflow as the authoritative build. Only claim checks that were actually run. |

## 4. Recommended architecture

**Approach: Markdown-first, single tree, GitHub Pages (native Jekyll) via Actions workflow, stock theme.**

Why this over the alternatives:

- **vs. MkDocs Material (Network-Security-Course pattern):** needs a Python toolchain, a copy/generation step, and a second tree. The stated requirement is *minimal dependencies* and *plain Markdown usable on GitHub*.
- **vs. `website/` copy tree (Cyber-Security-Course pattern):** hand-maintained duplication that has already drifted.
- **vs. no-CI "deploy from branch":** works, but a workflow gives us an explicit build, an instructor-content guard, and consistency with the instructor's other repos.

```text
/                                   ← repo root (Git-browsable course)
├── README.md                       landing page: course title, instructor, how to study
├── .gitignore
├── LICENSE                         (instructor's choice, see §7)
├── docs-meta/                      planning & governance — NEVER published
│   └── repository-assessment-and-plan.md
├── tools/
│   └── validate_content.py         stdlib-only link/front-matter checker (local + CI)
├── .github/workflows/pages.yml     Pages build/deploy + publish-tree guard
└── docs/                           ★ canonical course content = GitHub Pages source
    ├── _config.yml                 theme, title, baseurl; excludes tuned
    ├── index.md                    course home (published)
    ├── syllabus.md                 weekly plan, CLOs, assessment scheme
    ├── modules/                    module-01-… → module-NN (beginner → advanced)
    │   └── module-NN-<name>/
    │       ├── README.md           module overview + outcomes
    │       └── lesson-NN.md        one file per lecture/lesson
    ├── labs/                       practical worksheets + safe starter code
    ├── case-studies/               real-world incidents, exercises
    ├── quizzes/                    practice questions (student-facing only)
    ├── resources/                  readings, cheat sheets, further study
    └── assets/images/              diagrams
```

Key properties:

1. **One copy of every Markdown file.** Students read it on GitHub; GitHub Pages builds the *same* `docs/` tree. Changing a theme later changes only `_config.yml` — content never moves.
2. **Structural safety:** anything outside `docs/` (planning, tools, future `instructor-only/`) is outside the build input — it cannot leak to the site.
3. **Zero content dependencies:** plain GitHub-Flavored Markdown + light YAML front matter (`title`, `layout`, `nav_order`). No npm, no Python packages for the site itself.
4. **CI:** `pages.yml` mirrors the proven pattern — checkout → content guard → `actions/jekyll-build-pages` with `source: ./docs` → deploy. Stock Jekyll theme (e.g. `jekyll-theme-cayman`/`minimal`) needs no `remote_theme` plugin.

## 5. Proposed course shape (to be confirmed in Phase 2 — not written yet)

Beginner → advanced, ~10–11 modules, one directory per module, one Markdown file per lesson:

1. Foundations of Information Security (CIA triad, threats, risk, security models)
2. Ethics, Law & Governance (incl. Pakistan PECA 2016 context; GDPR-style regimes)
3. Cryptography (symmetric, asymmetric, hashing, PKI, common misuses)
4. Authentication, Identity & Access Control
5. Operating System & Endpoint Security
6. Network Security (firewalls, IDS/IPS, secure protocols)
7. Web & Application Security (OWASP Top 10, secure SDLC)
8. Malware, Social Engineering & the Human Factor
9. Defensive Operations: monitoring, incident response, digital forensics
10. Cloud, Mobile & IoT Security; Privacy & Data Protection
11. Modern frontiers: Zero Trust, AI/ML security — plus a capstone project

Each lesson: learning outcomes → concepts with diagrams → worked examples → hands-on activity → practice questions → summary → references. Full syllabus, CLO mapping, and assessment plan are a Phase 2 deliverable requiring instructor approval.

## 6. Implementation sequence

| Phase | Deliverable | Checkpoint |
|---|---|---|
| **0 (done)** | This assessment & plan | Instructor review ✅ |
| **1 — Bootstrap** | Clone repo locally; scaffold `README.md`, `docs/_config.yml`, `docs/index.md`, `.github/workflows/pages.yml`, `.gitignore`, `tools/validate_content.py`; run the validator | Instructor commits & pushes; enables Pages (Settings → Pages → Source: GitHub Actions); site goes live |
| **2 — Blueprint** | `docs/syllabus.md`: module map, weekly plan, CLOs, assessment scheme | Instructor approves outline **before** any mass content generation |
| **3 — Content** | Modules generated one at a time (beginner → advanced), validator run after each | Per-module review; instructor pushes each batch |
| **4 — Site polish** | Home page, navigation, images, cross-links; full link check; observe the real Pages build succeed | Live site verified in browser (console/network clean, correct URLs) |
| **5 — Maintenance** | Content-inventory report, periodic link checks, optional instructor-content CI guard | Ongoing |

**Validation honesty policy:** locally we can run only the Markdown structure/link checker and static inspection (no Ruby/Jekyll assumed locally). The authoritative Jekyll build runs in GitHub Pages CI after the instructor's push — its result will be reported only after it actually runs.

## 7. Decisions needed from the instructor

1. **Site theme** — stock Jekyll theme: Cayman (bold header), Minimal (clean reading), or Slate (fixed header). Default proposal: **Minimal**.
2. **License** — MIT (most permissive) vs CC BY 4.0 (content-friendly) vs no license.
3. **Course format** — 32×2-hour lectures / 16 weeks (consistent with sibling courses) or self-paced modules?
4. **Instructor-only material** — will answer keys/exam papers be added? (Determines whether we add `instructor-only/` trees now and the CI guard.)
5. **Scope differentiation** — confirm this course targets *foundations + breadth* distinct from `Cyber-Security-Course`.

## 8. Rules of engagement (restated)

- The instructor commits and pushes manually; the agent never runs `commit`, `push`, `pull`, `merge`, `rebase`, or any remote-state-modifying command.
- No deployment, no Pages enabling, no GitHub settings/permissions/visibility changes by the agent.
- No destructive changes; inspect before touching anything.
- No build/test result is ever reported as passing unless it was actually executed.
