# Maintenance — Course Site (GitHub Pages)

**Audience: maintainers only.** Students: start at the [course overview](README.md) or the course site.
This document is kept **outside `docs/`** so it is never part of the published site build.

---

## 1. Architecture (keep it simple)

- **Publishing:** GitHub Pages with source = `docs/` folder on the default branch (repository setting — do not change without reason).
- **Generator:** Jekyll via the stock `github-pages` gem environment. Configuration lives in [`docs/_config.yml`](docs/_config.yml) and is intentionally minimal: `jekyll-theme-minimal`, no custom plugins beyond the GitHub Pages whitelist, no build steps, no API keys, no commercial services.
- **Content:** plain Markdown with two small conventions:
  - YAML front matter (`title`, `layout: default`).
  - **Relative `.md` links** (e.g. `[Prerequisites](./prerequisites.md)`), rewritten for the site by the whitelisted `jekyll-relative-links` plugin. The same links therefore work on GitHub *and* on the published site.
- **Navigation:** content-level footers (`**Navigation:** [← Previous] · [Module index] · [Next →]`) on module pages, labs, and quizzes — no layout plugins required.
- **Styling:** the stock theme plus one override stylesheet, `docs/assets/css/style.scss`, which imports the theme and appends accessibility/responsive tweaks. Keep all custom CSS there.

## 2. Local build

Prerequisites: Ruby (3.1+; developed against 3.3) and RubyGems. No admin rights needed if Ruby is installed per-user (e.g. `winget install RubyInstallerTeam.Ruby.3.3`).

```bash
gem install github-pages webrick --no-document   # one-time
jekyll build -s docs -d _site                    # production build (uses docs/_config.yml)
jekyll serve -s docs -d _site                    # http://127.0.0.1:4000/Information-Security/
```

Notes:
- `webrick` is required for `jekyll serve` on Ruby 3+.
- The site is served under the `baseurl` (`/Information-Security`), so open `http://127.0.0.1:4000/Information-Security/` — the root path 404s by design (matches production `url` + `baseurl` in `_config.yml`).
- `_site/` is build output; it must never be committed.

## 3. Publishing and configuration maintenance

- Deployment is handled by GitHub Pages itself (repository **Settings → Pages**, source `docs/`). This repo intentionally has **no deployment workflow**; do not add one without updating this file.
- If the repository is renamed or forked, update `url`/`baseurl` in `docs/_config.yml` and re-run the local build.
- Keep `_config.yml` free of plugins not whitelisted by GitHub Pages — unlisted plugins are silently ignored in production and cause "works locally, breaks live" drift. Whitelist reference: <https://pages.github.com/versions/>.
- Do not add trackers, CDNs, or services that need API keys; the site must build and serve fully offline from the repository content.

## 4. Validation before publishing

Run, in order, from the repository root (all exit 0 required):

```bash
python scripts/validate-assessments.py   # quizzes/answers consistency + links
python scripts/validate-labs.py          # 17-field lab format, safety notes, links
python scripts/validate-references.py    # reference library, cross-links, URL manifest
jekyll build -s docs -d _site            # site build must succeed
python scripts/check-site-links.py _site # internal links in the built output
```

After a theme or config change, also eyeball the served site at mobile width and run a keyboard pass (Tab order, visible focus) — see §6 of the site's About page for the accessibility intent.

## 5. Content conventions

- **Headings:** one `#` title per page, then `##` sections; keep the existing per-page structure — consistency is what makes the site navigable.
- **Callouts:** Markdown blockquotes (`> **Note:** …`), bold label first.
- **Diagrams:** prefer ASCII or fenced code (```text/```mermaid) so the "diagram" is readable as text — that is the accessibility fallback; never embed a diagram as an image without a text equivalent.
- **Tables:** keep them narrow enough to scroll horizontally on phones (the stylesheet makes tables scrollable).
- **Prev/Next footers:** every sequential page (module, lab, quiz) ends with a `**Navigation:**` line. When inserting or removing a page in a sequence, update both neighbours.- **Links:** relative `.md` paths only — never absolute site URLs inside content
  (they break on forks and on GitHub itself). **Never link a bare directory or a
  non-Markdown file relatively** (e.g. `../labs/x/data/`): pages are served at
  pretty URLs (`/capstone/scenarios/`), so the browser resolves such links one
  level deeper than GitHub does and they 404 on the site. Link the folder's
  `index.md` page instead — every dataset folder ships one, and
  `scripts/check-site-links.py` catches violations.

## 6. Answer-key policy (what may be public)

The course is self-study: worked answers are **intentionally published** behind `<details>` collapse blocks (quiz model answers), or as self-check files the lab tells you to open only at the end (e.g. `docs/labs/lab-03-password-hashes/data/ANSWERS-hashes.txt`). These are student material by design — they must stay in the build because the published lab text references them.

Rules for maintainers:

1. New answer material is public **only** if it is referenced by published student text as a self-check, or wrapped in `<details>` with a "compare your reasoning" label.
2. Genuinely instructor-only material (graders' notes, private rubrics, unreleased quizzes) must **not** live under `docs/` at all — put it in `docs-meta/` (repository root, never published) or add the path to `exclude:` in `docs/_config.yml` *and* note it here.
3. Never place answers in page metadata (titles, descriptions, image alt text, link text) — collapsed HTML is readable by anyone; metadata should never confirm an answer.
4. After adding any answer file, re-run `python scripts/validate-assessments.py` and grep the `_site/` output to confirm the exposure is the intended one.

## 7. Do-not list

- Do not commit `_site/`, `.sass-cache/`, `.jekyll-cache/`, `.jekyll-metadata`, or vendor/bundle output.
- Do not enable un-whitelisted Jekyll plugins, `github-pages` overrides, or theme forks when a stylesheet tweak suffices.
- Do not move pages without updating their prev/next neighbours and every relative link (the validators catch this).
- Do not add paid-tool dependencies to any required path — see the Reference Library's core-is-free rule (`scripts/validate-references.py` enforces it).
