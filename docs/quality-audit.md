---
title: "Quality Audit — Pre-Commit Review"
layout: default
---

# Quality Audit — Pre-Commit Review

**Date:** 2026-10-10 · **Scope:** entire repository (curriculum, lessons, labs, assessments, references, website, hygiene) · **Method:** automated validators + targeted manual review + live URL verification (202 URLs checked) + browser-based accessibility testing (axe-core 4.10.2, WCAG 2.0/2.1 A+AA).

Findings are marked **[Verified]** (confirmed with evidence) or **[Manual review]** (owner judgment required). Remediation status: **FIXED** (corrected during this audit, re-verified) or **OPEN** (needs the owner's decision — nothing was silently changed).

---

## Summary of automated checks (final state, exit codes preserved)

| Check | Result |
|---|---|
| `python scripts/validate-assessments.py` | **PASS (exit 0)** — 18 quizzes, question/answer consistency, coverage, 875 links |
| `python scripts/validate-labs.py` | **PASS (exit 0)** — 19 labs × 17 required elements, 178 links |
| `python scripts/validate-references.py` | **PASS (exit 0)** — 66 curated entries, 110-URL manifest parity, 19 cross-links |
| `jekyll build -s docs -d _site` (github-pages toolchain, Jekyll 3.10) | **PASS (exit 0)** — 93 pages |
| `python scripts/check-site-links.py _site` | **PASS (exit 0)** — 1399 internal links, 0 broken, 0 unrewritten `.md`, 0 maintainer leaks |
| axe-core (homepage, LAB-13, quiz M09, quiz M01) | **0 violations** after F-05 fixes (see below) |
| External URL sweep (202 unique URLs) | 172 OK · 11 bot-blocked · 19 pedagogical placeholders · **10 real dead links → FIXED** |
| Secrets/credentials pattern scan (AKIA/ghp_/sk-/xox/AIza/private keys) | **0 hits** |
| Repeated-word, placeholder (TBD/TODO), odd-code-fence, duplicate-navigation scans | **0 hits** |

---

## Findings

### HIGH

**F-01 — Lesson prose exists only for Modules 01–05; Modules 06–19 are specification-complete but lesson-incomplete. [Verified — OPEN, owner decision]**
- *Evidence:* M01–M05 READMEs are 301–344 lines of full lesson content. M06–M19 READMEs are 30–39 lines and carry the banner `> **Status:** Outline ready — full lesson content coming soon.` (14 modules). The [Course Roadmap](./course-roadmap.md) holds a full *specification* per module (measurable outcomes with Bloom levels, core-concept lists, lab scenarios, completion criteria, further reading) — but not explanatory lesson text.
- *What still works for M06–M19:* real labs with instructions and datasets, worked-answer quizzes, deliverable specs, and curated references — a motivated learner can study from primary sources, but the "lesson" layer is missing.
- *Remediation options (owner's call):* (a) author full lessons for M06–M19 before announcing the course as complete; (b) formally adopt the roadmap as the lesson layer, remove the "coming soon" banners, and describe M06–M19 as source-plus-lab guided modules; (c) publish as-is with the banners (current state — honest, but the gap is visible to students).
- *Related note:* site-level pages (homepage, at-a-glance table) do not summarize this status; only the per-module banners disclose it.

### MEDIUM

**F-02 — Ten real external citations were dead (404). [Verified — FIXED]**
- *Evidence (old → replacement, each replacement verified HTTP 200 or rendered-fetch 200 on 2026-10-10):*
  - `attack.mitre.org/detection/` → `attack.mitre.org/techniques/` — [lab-18](./labs/lab-18-security-automation/README.md)
  - `csrc.nist.gov/pubs/sp/800/154/final` (page never existed; draft-only publication) → `.../154/ipd` — [lab-02](./labs/lab-02-threat-model-risk-register/README.md)
  - `cwe.mitre.org/top25.html` → `cwe.mitre.org/top25` — [lab-09](./labs/lab-09-secure-coding/README.md)
  - `learn.microsoft.com/.../security-baselines` → `.../windows-security-baselines` — [module-05](./modules/module-05-operating-system-and-endpoint-security/README.md)
  - `learn.microsoft.com/.../security-threat-modeling` (section retired) → `microsoft.com/en-us/securityengineering/sdl/threatmodeling` — [lab-02](./labs/lab-02-threat-model-risk-register/README.md)
  - `portswigger.net/burp/communityedition` → `portswigger.net/burp/communitydownload` — [lab-10](./labs/lab-10-web-security/README.md)
  - `wiki.wireshark.org/SampleCaptures` (missing trailing slash) → `.../SampleCaptures/` — [lab-07](./labs/lab-07-packet-analysis/README.md) (2 places)
  - `enisa.europa.eu/publications/enisa-threat-landscape` → `.../topics/cyber-threats/threat-landscape` — [module-01](./modules/module-01-information-security-foundations/README.md)
  - `isc2.org/About-Us/Code-of-Ethics` → `isc2.org/ethics` — [module-03](./modules/module-03-governance-policy-ethics-and-law/README.md)
  - `sleuthkit.org/sleuthkit/doc/` → `sleuthkit.org/` (docs link from home page) — [lab-15](./labs/lab-15-digital-forensics/README.md)
- *Remediation:* applied; full suite re-run green after each batch.

**F-03 — Learning-outcomes document made a claim the repository did not meet. [Verified — FIXED]**
- *Evidence:* [learning-outcomes.md](./learning-outcomes.md) §6 stated "Every knowledge check and graded item … cites the CLO(s) it measures." Actual state: 0 of 18 quiz files reference CLO labels (they cite *module* learning outcomes — e.g. quiz-m13's coverage line); the Assessment Guide maps the six scenario items to CLOs.
- *Remediation:* wording corrected to describe reality (dated note added); no content deleted.

**F-04 — No `.gitignore`; generated artifacts and workspace metadata would be committed. [Verified — FIXED]**
- *Evidence:* repository root contained `_site/` (2.5 MB build output), `.sass-cache/` (128 KB), and `.freebuff/` (agent workspace, single `project-id` file) with no ignore rules.
- *Remediation:* `.gitignore` created at the repository root (Jekyll artifacts, vendor/bundle, `.freebuff/`, OS noise). No files were deleted.

**F-05 — Accessibility violations on content-rich pages. [Verified — FIXED]**
- *Evidence:* axe-core on LAB-13 flagged `color-contrast` ×22 (Rouge "github" syntax tokens — `.nb` #0086b3 = 3.9:1, `.c` #999988 = 2.7:1 on the #f8f8f8 code background), `label` ×9 (GFM task-list checkboxes rendered without accessible names), `scrollable-region-focusable` ×2 (overflowing `<pre>` blocks not keyboard-reachable, WCAG 2.1.1).
- *Remediation:* darkened the failing token families in [style.scss](./assets/css/style.scss) (#0f5499 / #59636e / #006666 — all ≥ 5.6:1); added `docs/_includes/head-custom.html` (the theme's supported hook) with a small progressive script that labels task-list checkboxes from their item text and makes overflowing tables/code blocks focusable regions. Re-verified: **0 violations, 26 passes** on LAB-13; homepage 0/12; quiz-m09 0/14.

### LOW

**F-06 — Favicon finding was partly an artifact; now correctly wired. [Verified — FIXED]**
- *Evidence:* an earlier site check reported 86 "broken favicon links" — they came from the theme's *commented-out* favicon line inside `_includes/head-custom.html` (Liquid renders the URL even inside HTML comments) being counted by our checker's raw regex. Meanwhile no *real* favicon link existed in any page, though `docs/favicon.ico` was added earlier.
- *Remediation:* real `<link rel="icon">` now emitted via head-custom; `scripts/check-site-links.py` hardened to ignore HTML comments; link count restored to 1370 at that checkpoint (1399 after this audit's own pages were added) with the favicon resolving to the actual 1150-byte file.

**F-07 — No `LICENSE` file. [Manual review]**
- README and About page carry a consistent custom terms statement ("© 2026 … free of charge for personal study and classroom use with attribution … until a formal LICENSE file is added"). Adding a formal license (e.g. CC BY-NC-SA 4.0 for content) is the owner's legal decision.

**F-08 — Site-level disclosure of lesson-stage modules. [Manual review]**
- Only per-module banners disclose F-01. Consider one honest sentence on the homepage/at-a-glance table.

**F-09 — SP 800-53 presentation differs between documents. [Manual review]**
- Roadmap version table: "Release 5.2.0 (Aug 2025)"; [reference library](./reference/README.md): "Rev. 5, September 2020 (minor updates since)". Both are consistent with NIST's release scheme, but the audit did not independently re-verify the 5.2.0 release date.

**F-10 — Quiz distractors occasionally humorous. [Verified — OK, style note]**
- e.g. quiz-m13's "Analysts need more caffeine". Pedagogically harmless; strict item-writing style prefers only plausible distractors. Owner may keep or normalize.

**F-11 — Bot-blocked domains remain unverifiable by script. [Manual review]**
- 11 URLs returned 403/429 to scripted clients (cisa.gov ×5, microsoft.com SDL, cloudflare learning, etc.). Sampled ones render correctly in a browser (verified via rendered fetch). Re-check periodically; already listed in the reference library's flagged table.

### INFORMATIONAL (verified clean — recorded so absence of findings is explicit)

- **F-12:** Destructive-looking commands in labs are *teaching context*, not instructions: lab-04 narrates the `chmod -R 777` anti-pattern; lab-06 cleanup removes only names the student created; lab-15's `rm -rf` line is attacker history in a forensic artifact.
- **F-13:** Dataset integrity: 84 backticked data-file references in lab READMEs — every *provided input* exists; the 68 initially-unmatched names are student-created outputs (`detect.py`, `alerts.json`, `*-fixed.json`, …) or documented cross-lab references (LAB-18/LAB-19 reuse LAB-13/15/16/17 files via links); lab-12's "provided scan extract" is intentionally inline.
- **F-14:** Secrets/PII: no credential patterns anywhere in `docs/`, `scripts/`, README, or MAINTENANCE; only fictional contact data (`itoffice.lab@example.edu`); `docs-meta/` planning document contains no sensitive content; `.freebuff/` holds only a workspace id (now gitignored).
- **F-15:** Root README: all 13 TOC anchors and every relative link resolve on GitHub; contains no deployment/build/maintenance instructions (those live in MAINTENANCE.md); instructor attribution present and consistent with the About page.
- **F-16:** Malformed-Markdown scan: no odd code-fence counts, no duplicate `Navigation` footers, no images (0 — diagrams are text blocks, which is the accessibility fallback), no repeated-word typos, no TBD/TODO/placeholder text outside the intentional "coming soon" banners (F-01).
- **F-17:** Standards versions are internally consistent across all documents: CSF 2.0 (×48), SP 800-63-4 (×31, the single 800-63-3 mention is an explicit "supersedes" note), Top 10:2025 (×28), CVSS v4.0 (×27), CIS v8.1 (×12), ATT&CK v19 (×3), with a dated version policy table in the roadmap (checked 2026-10-09).
- **F-18:** Git: the working copy has **no `.git` directory** — `git status` before/after was impossible; no commit/stash/reset was performed by the auditor. All changes are plain file edits for the owner's review.

---

## Audit 1 — Curriculum

- **Progression:** four ordered levels (M01–05 → M06–11 → M12–15 → M16–19) with explicit prerequisites on every module page and in the roadmap; scaffolding logic documented in learning-outcomes.md §5 (vocabulary → networking → defense → offense → design → integration). Verified consistent.
- **Dependencies:** every roadmap module section declares prerequisites (e.g. M07: "M05, M06"); no forward dependencies detected in samples.
- **Measurable outcomes:** 12 CLOs with observable verbs, Bloom levels, evidence columns, and a CLO→module map (●/○) with a ≥2-evidence-points guarantee; per-module outcomes carry Bloom labels. One claim was inaccurate and is corrected (F-03).
- **Coverage:** every module has labs, an assessment, and further reading — see [course-completion-matrix.md](./course-completion-matrix.md).
- **Gaps/duplicates:** the material gap is F-01; M03 and M17 have no *dedicated* lab by design (policy-set and DPIA deliverables; LAB-14/CS-4 provide practical coverage). No duplicated lesson content detected (M01–M05 lessons vs roadmap specs are complementary, not copies).

## Audit 2 — Educational quality

- M01–M05 lessons contain real explanations, worked command examples, case exercises with model guidance, and completion checklists (line counts + sampled reads).
- Quizzes carry instructions, coverage statements, safety reminders, worked answers in collapsed blocks, and unlimited formative retakes — self-study without an instructor is structurally supported (roadmap pacing, study guide, glossary, troubleshooting guide).
- Honest limitation: F-01 means Levels 2–4 currently teach via specification + lab + primary sources rather than authored lessons.

## Audit 3 — Labs

- All 19 labs satisfy the 17-field standard (prerequisites, setup, tasks, expected observations, evidence, troubleshooting, cleanup, safety) — machine-verified, exit 0.
- All provided datasets exist (F-13); scope statements and authorization framing present in every lab; no unsafe instructions found (F-12).
- *Not verified this audit:* end-to-end execution of each lab in the documented environment (would require VMs and hours per lab).

## Audit 4 — Assessments

- Question counts match declarations; answer keys consistent (validator, exit 0); quizzes cite the module outcomes they measure; case studies span levels; CAP-ADV, lab challenges, and the capstone rubric complete the instruments.
- Sampled MCQs (M01, M09, M13) are unambiguous with plausible-or-clearly-absurd distractors (F-10 style note).
- No private instructor material exists in the published tree; the answer policy is deliberately public (collapsed `<details>`, attempt-before-reveal) — verified collapsed-by-default in build output.

## Audit 5 — References

- Internal links: 0 broken (source validators + built-site checker).
- External: 202 unique URLs swept; 10 real dead links fixed (F-02) with verified replacements; 19 "failures" are intentional teaching placeholders (`127.0.1`, `example.com`, `<vm-ip>`); 11 bot-blocks flagged (F-11).
- Reference library: 66 curated primary-source entries with versions/access/limitations, 110-URL manifest, flagged-for-review table — all machine-checked.

## Audit 6 — Website

- Build exit 0 on the production toolchain; 1370 internal links OK; navigation (prev/next on modules, labs, quizzes) verified live; no duplicate navigation; no images to break; root README clean for GitHub (F-15).
- Accessibility: three violation classes found on content pages and fixed (F-05); mobile (375 px) has no page-level horizontal overflow (tables/code scroll internally and are keyboard-reachable).

## Audit 7 — Repository hygiene

- Secrets/PII clean (F-14); build artifacts now ignored (F-04); licensing consistent but informal (F-07); pre-existing unrelated files (`docs-meta/`, `.freebuff/`) preserved untouched; nothing deleted, stashed, or reset.

---

## What the auditor did NOT verify

- Live GitHub Pages deployment (not deployed; production parity rests on the local github-pages toolchain build).
- End-to-end lab execution reproducibility.
- Independent re-verification of every cited publication date (the 2026-10-09 reference pass stands; this audit re-verified link liveness, not edition metadata).
- Grammar beyond repeated-word and consistency spot-checks — no full prose copy-edit.

**Companion document:** [course-completion-matrix.md](./course-completion-matrix.md) — module-by-module and CLO-by-CLO coverage map.
