---
title: GitHub Pages Deployment (Maintainers)
layout: default
---

**Audience: maintainers only.** This file is excluded from the site build (see `exclude:` in [`_config.yml`](../_config.yml)) — students never see it. Start at the [course overview](../../README.md) instead.

# GitHub Pages Deployment

The course site is built and published by GitHub Actions. Publishing happens only when a maintainer pushes to the publishing branch (or runs the workflow by hand).

## 1. Publishing branch and triggers

| Trigger | When |
|---|---|
| `push` to **`main`** | Any commit you push to `main` publishes the site. |
| `workflow_dispatch` | Actions tab → *Deploy course site to GitHub Pages* → *Run workflow*. |

- The workflow is [`.github/workflows/deploy-pages.yml`](../../.github/workflows/deploy-pages.yml). `main` is the only branch that publishes, and there is **no `pull_request` trigger**, so untrusted fork/PR code never runs with deployment permissions.
- You commit and push; the workflow does the rest. Nothing is ever committed back — the workflow has `contents: read` only, and the generated `_site/` stays out of the repository (`.gitignore`).

## 2. One-time repository settings (manual, by a maintainer)

Deployment source must be **GitHub Actions**:

1. Repository **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions** (not "Deploy from a branch").
3. Save.

If Pages has never been enabled, choosing *GitHub Actions* as the source enables it. Do **not** use `actions/configure-pages`' `enablement` option or any API call to do this for you — that option needs a token with more privilege than the workflow's `GITHUB_TOKEN`, and the workflow deliberately does not use it. The workflow fails with a clear `configure-pages` error if Pages is not enabled.

Note: if the source is still "Deploy from a branch" (the old `main` → `/docs` publishing), the build and upload steps succeed but the **Deploy to GitHub Pages** step fails. Switching the source to *GitHub Actions* fixes it; re-run the workflow afterwards.

## 3. First publish (and every publish after that)

1. Review `git diff` / `git status` locally.
2. Commit and push to `main` (you do this yourself — the workflow never pushes).
3. **Actions** tab → *Deploy course site to GitHub Pages* → watch the run.
4. When the run is green, open the deployment URL from the run summary or the `github-pages` environment:
   `https://nadeem-majeedch.github.io/Information-Security/`

## 4. What the workflow does

**Build job**

| Step | Action | Purpose |
|---|---|---|
| Checkout | `actions/checkout` | Fetch the `main` commit. |
| Setup GitHub Pages | `actions/configure-pages` | Reads the Pages site, exposes `base_path`, exports `GITHUB_PAGES=true`. Fails if Pages is not enabled. |
| Build with Jekyll | `actions/jekyll-build-pages` | Runs the stock `github-pages` gem (GitHub's own build environment) with `source: ./docs`, `destination: ./_site`. Dependencies ship inside the action's pinned container image — no lockfile to install, no `gem install`. `JEKYLL_ENV=production`. |
| Verify build output and base path | inline `bash` | Fails the run if `_site/` or the landing page is missing, expected course pages are absent, `baseurl` disagrees with the real Pages `base_path`, rendered links lack the base path, maintainer docs leaked into the output, or `scripts/check-site-links.py` finds broken/escaping links. |
| Upload Pages artifact | `actions/upload-pages-artifact` | Uploads `_site/` as the Pages artifact. |

**Deploy job** (runs only if the build succeeded)

| Step | Action | Purpose |
|---|---|---|
| Deploy to GitHub Pages | `actions/deploy-pages` | Publishes the artifact; exposes `page_url`, bound to the `github-pages` environment URL. |
| Report deployment URL | inline `bash` | Echoes the published URL into the log. |

Actions are pinned to full commit SHAs, with the release version in a trailing comment. Bump the SHA and the comment together (§8).

## 5. Permissions, concurrency, security

- **Permissions:** `contents: read`, `pages: write`, `id-token: write` — read the repo, publish to Pages, mint the OIDC token used by the Pages deployment. No deployment tokens, PATs, passwords, or API secrets anywhere; authentication is the built-in `GITHUB_TOKEN` plus OIDC.
- **Concurrency:** group `pages`, `cancel-in-progress: false` — one deployment at a time, and an in-flight production deployment is never cancelled.
- **Scope:** triggers only on `main` and `workflow_dispatch`; no PR or fork code is executed with deployment privileges.
- **No generated output in git:** the build writes `_site/` in the runner workspace only, and the workflow has no permission (or command) to commit.

## 6. The project-site base path (`/Information-Security/`)

This is a **project site**, so everything is served under `/Information-Security/`. The base path is handled in three layers:

1. **Configuration:** [`docs/_config.yml`](../_config.yml) sets `url: https://nadeem-majeedch.github.io` and `baseurl: /Information-Security`. Jekyll — including the `github-pages` gem used in CI — bakes that prefix into every generated `href`, `src`, stylesheet, image, and Markdown link. `actions/jekyll-build-pages` does **not** pass `--baseurl`; the config is the single source of truth, so CI output matches your local `jekyll build -s docs -d _site`.
2. **Cross-check in CI:** the verify step compares `baseurl` from `_config.yml` with `steps.pages.outputs.base_path` from `actions/configure-pages` (the path GitHub actually serves) and fails on mismatch, then confirms rendered links carry the prefix.
3. **Link audit:** `python3 scripts/check-site-links.py _site` resolves every internal link in the built output — pretty URLs, baseurl prefixes, nested module/lab paths — and flags any absolute link that escapes the base path, any unrewritten `.md` link, and any maintainer file in the output.

Trailing slashes are safe: permalinks are `pretty` (`/modules/…/` directories with `index.html`), and relative `.md` links are rewritten by the whitelisted `jekyll-relative-links` plugin. Never write absolute site URLs inside content — relative `.md` paths work on GitHub and on the site.

If the repository is renamed or forked, update `url`/`baseurl` in `docs/_config.yml`; the workflow fails with an explicit message until you do.

## 7. Inspecting runs and diagnosing failures

**Actions tab → *Deploy course site to GitHub Pages* → select the run:**

- A red **Build site** job:
  - *Setup GitHub Pages* fails → Pages is not enabled or not using an Actions source (§2).
  - *Build with Jekyll* fails → a Jekyll/kramdown error in `docs/`; the step logs carry the gem's `::error::` annotation, and nothing is published (the old site stays up).
  - *Verify build output and base path* fails → read the `::error::` line; it names the exact check (missing page, base-path mismatch, broken link, leaked maintainer file).
- A green build but red **Deploy to GitHub Pages** job → the artifact was built but not accepted; most often the Pages source is still "Deploy from a branch" (§2). Details are in the step log and under **Settings → Pages → Deployments**.
- Re-run safely: *Run workflow* (`workflow_dispatch`), or push to `main`. The concurrency group serialises deployments; queued runs between the active one and the newest are skipped, never the other way round.

**Per-environment history:** **Settings → Environments → github-pages** lists every deployment with its commit, run, and URL.

## 8. Updating the pinned action versions

Each `uses:` line is pinned as `actions/<name>@<full-sha> # <version>`. To upgrade: check the release in the official `actions` organisation, replace the SHA, and update the comment in the same commit so the two never disagree. The current set (verified 2026-10-10):

| Action | Version | SHA |
|---|---|---|
| `actions/checkout` | v7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| `actions/configure-pages` | v6.0.0 | `45bfe0192ca1faeb007ade9deae92b16b8254a0d` |
| `actions/jekyll-build-pages` | v1.0.13 | `44a6e6beabd48582f863aeeb6cb2151cc1716697` |
| `actions/upload-pages-artifact` | v5.0.0 | `fc324d3547104276b827a68afc52ff2a11cc49c9` |
| `actions/deploy-pages` | v5.0.1 | `368f82528645a54fb793d4d04e342629a3f51346` |

Keep `upload-pages-artifact` and `deploy-pages` on compatible release lines (v3 artifacts need `deploy-pages` v4+; the artifact format is versioned between them).

## 9. Verifying the published site

1. Open `https://nadeem-majeedch.github.io/Information-Security/` — the landing page renders, not a 404 or a directory listing.
2. Spot-check the base path: page source must reference `/Information-Security/assets/…`, and following a nested link such as Module 01 under `modules/…` must land on a real page with working CSS.
3. Confirm the run you expect is the live one: **Settings → Environments → github-pages** (deployment time, commit SHA, URL).
4. Local pre-flight before you push (from the repository root):

   ```bash
   python3 scripts/validate-assessments.py
   python3 scripts/validate-labs.py
   python3 scripts/validate-references.py
   jekyll build -s docs -d _site
   python3 scripts/check-site-links.py _site
   ```

   These are the same checks the workflow's verify step re-runs against the freshly built output.

Pages serves the deployment as soon as the run completes; if the page looks stale, hard-refresh and confirm the deployment SHA matches the commit you pushed.

## 10. Do-not list

- Do not add `pull_request` triggers, third-party actions, secrets, or deployment tokens to this workflow.
- Do not switch the Pages source back to a branch unless you also remove the workflow (and update `MAINTENANCE.md`).
- Do not commit `_site/` or any generated output.
- Do not set `cancel-in-progress: true` on the `pages` concurrency group — it aborts live production deployments.
- Do not document deployment in the student-facing root `README.md`; it belongs here and in `MAINTENANCE.md`.
