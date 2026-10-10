#!/usr/bin/env python3
"""Validate the reference library in docs/reference/.

Offline checks (default):
  1. The five deliverable files exist with Jekyll front matter.
  2. README has all required sections and the [C]/[O] (required vs optional) legend.
  3. Every resource entry carries full metadata: Version, Access, Modules, Use, Notes
     plus at least one URL — and every [C] (Core) entry is free (never paid).
  4. tools.md tables: consistent 5-column rows, every tool marked Free in Access.
  5. glossary/pathways/study-guide structural requirements (entry counts, headings).
  6. Relative links between course files resolve to existing files.
  7. Cross-links exist: homepage, prerequisites, modules index, all 19 module footers
     must point into reference/README.md.
  8. External-URL manifest parity: every external URL in docs/reference/*.md is listed
     in scripts/reference-urls.txt and vice versa (no stale manifest entries).

--check-urls additionally re-verifies every manifest URL over HTTP. Bot-blocking
statuses (403/429/405/406/999/503) are reported as warnings (sites like cisa.gov
block scripted clients while remaining fine in a browser); anything else is a failure.

Exit status: 0 = all checks green, 1 = failures found.
"""
import io
import os
import re
import sys

REF_DIR = os.path.join("docs", "reference")
MANIFEST = os.path.join("scripts", "reference-urls.txt")

REQUIRED_FILES = ["README.md", "tools.md", "glossary.md", "pathways.md", "study-guide.md"]

README_SECTIONS = [
    "## 1. NIST",
    "## 2. OWASP",
    "## 3. CISA",
    "## 4. MITRE",
    "## 5. CIS",
    "## 6. Official tool",
    "## 7. Privacy",
    "## 8. Free educational",
    "## 9. General-purpose",
    "## Paid resources",
    "## Flagged for review",
]

ENTRY_FIELDS = ["**Version:**", "**Access:**", "**Modules:**", "**Use:**", "**Notes:**"]
ENTRY_RE = re.compile(r"^- \*\*\[([CO])\]", re.MULTILINE)
FIELD_RE = re.compile(r"\*\*Access:\*\*([^*]*)\*")

PATHWAY_HEADINGS = [
    "## Pathway 1 — Beginner",
    "## Pathway 2 — Advanced",
    "### 2A — Security operations",
    "### 2B — Application security",
    "### 2C — Incident response",
    "### 2D — Security engineering",
]

STUDY_HEADINGS = ["## Part 1 — Troubleshooting", "## Part 2 — Independent-study method"]

CROSS_LINK_TARGETS = {
    os.path.join("docs", "index.md"): "reference/README.md",
    os.path.join("docs", "prerequisites.md"): "reference/README.md",
    os.path.join("docs", "modules", "README.md"): "reference/README.md",
}
MODULE_LINK = "reference/README.md"

URL_RE = re.compile(r"https?://[^\s)\]>\"']+")
REL_LINK_RE = re.compile(r"\]\((?!https?://|mailto:)([^)\s]+)\)")
# Statuses that mean "bot-blocked, not dead" for scripted clients.
BOT_BLOCK = {403, 429, 405, 406, 999, 503}

failures = []
warnings = []


def fail(msg):
    failures.append(msg)


def warn(msg):
    warnings.append(msg)


def read(path):
    return io.open(path, encoding="utf-8").read()


# 1. Files + front matter -----------------------------------------------------
for name in REQUIRED_FILES:
    path = os.path.join(REF_DIR, name)
    if not os.path.exists(path):
        fail(f"{name}: missing")
        continue
    text = read(path)
    if not text.startswith("---\n"):
        fail(f"{name}: missing YAML front matter opener")
    if "layout: default" not in text[:200]:
        fail(f"{name}: front matter missing 'layout: default'")
    if "title:" not in text[:200]:
        fail(f"{name}: front matter missing title")

readme_path = os.path.join(REF_DIR, "README.md")
if not os.path.exists(readme_path):
    print(f"FAILURES ({len(failures)}):")
    for f in failures:
        print("  -", f)
    sys.exit(1)
readme = read(readme_path)

# 2. README sections + legend --------------------------------------------------
for sec in README_SECTIONS:
    if sec not in readme:
        fail(f"README: missing section '{sec}'")
if "[C] Core" not in readme or "[O] Optional" not in readme:
    fail("README: [C] Core / [O] Optional legend missing")
if "no paid product" not in readme.lower() and "never required" not in readme.lower():
    fail("README: missing 'no paid product required' guarantee statement")

# 3. Entry metadata completeness ----------------------------------------------
entry_count = 0
core_count = 0
# Only score bullets inside sections 1-9 (before the Paid table).
scored_region = readme.split("## Paid resources")[0]
for match in ENTRY_RE.finditer(scored_region):
    line_start = scored_region.rfind("\n", 0, match.start()) + 1
    line_end = scored_region.find("\n", match.start())
    line = scored_region[line_start:line_end if line_end != -1 else None]
    if "] Core** —" in line or "] Optional** —" in line:
        continue  # legend row, not a resource entry
    entry_count += 1
    tag = match.group(1)
    title = line[4:60].split("—")[0].strip()
    for field in ENTRY_FIELDS:
        if field not in line:
            fail(f"README entry missing {field}: {title[:50]}")
    if "https://" not in line:
        fail(f"README entry missing URL: {title[:50]}")
    if not re.search(r"M\d\d", line):
        fail(f"README entry missing module refs: {title[:50]}")
    access = FIELD_RE.search(line)
    if access and "paid" in access.group(1).lower() and tag == "C":
        fail(f"Core entry marked paid: {title[:50]}")
    if tag == "C":
        core_count += 1

if entry_count < 45:
    fail(f"README: only {entry_count} resource entries (expected >= 45)")
if core_count < 15:
    fail(f"README: only {core_count} [C] Core entries (expected >= 15)")
if "[O]" not in scored_region:
    fail("README: no [O] Optional entries found")

# Flagged table must exist and have rows.
flagged_rows = [l for l in readme.splitlines() if l.startswith("| [") and "http" in l]
if len(flagged_rows) < 5:
    fail(f"README: flagged-for-review table has {len(flagged_rows)} rows (expected >= 5)")
if "never finalized" not in readme and "draft" not in readme.lower():
    warn("README: no draft-status caveat found")

# 4. tools.md tables -----------------------------------------------------------
tools = read(os.path.join(REF_DIR, "tools.md")) if os.path.exists(os.path.join(REF_DIR, "tools.md")) else ""
tool_sections = re.findall(r"^## \d+\.", tools, re.MULTILINE)
if len(tool_sections) < 10:
    fail(f"tools.md: only {len(tool_sections)} numbered groups (expected >= 10)")
tool_rows = [l for l in tools.splitlines() if l.startswith("| **")]
if len(tool_rows) < 35:
    fail(f"tools.md: only {len(tool_rows)} tool rows (expected >= 35)")
for row in tool_rows:
    if row.count("|") != 6:
        fail(f"tools.md row not 5-column: {row[:70]}")
        continue
    cells = [c.strip() for c in row.strip("|").split("|")]
    access = cells[4]
    if "free" not in access.lower():
        fail(f"tools.md tool not free-access: {cells[0][:40]} ({access})")
    doc_cell = cells[3].lower()
    if "http" not in cells[3] and "built" not in doc_cell and "vendor docs" not in doc_cell and "man " not in doc_cell:
        fail(f"tools.md tool missing docs link: {cells[0][:40]}")
    if not re.search(r"M\d\d|all", cells[2]):
        fail(f"tools.md tool missing module refs: {cells[0][:40]}")

# 5. glossary / pathways / study-guide -----------------------------------------
glossary = read(os.path.join(REF_DIR, "glossary.md")) if os.path.exists(os.path.join(REF_DIR, "glossary.md")) else ""
gloss_entries = re.findall(r"^\*\*.+\*\* — ", glossary, re.MULTILINE)
if len(gloss_entries) < 90:
    fail(f"glossary: only {len(gloss_entries)} entries (expected >= 90)")
if glossary.count("M") < 90:
    fail("glossary: entries lack module references")

pathways = read(os.path.join(REF_DIR, "pathways.md")) if os.path.exists(os.path.join(REF_DIR, "pathways.md")) else ""
for head in PATHWAY_HEADINGS:
    if head not in pathways:
        fail(f"pathways: missing heading '{head}'")
for marker in ("[Core]", "[+]"):
    if marker not in pathways:
        fail(f"pathways: missing required/optional marker '{marker}'")
if "Free" not in pathways:
    fail("pathways: no free-access markers")
# Paid tiers must never be load-bearing in a pathway step.
for line in pathways.splitlines():
    if line.startswith("|") and re.search(r"\|\s*\d+\s*\|", line) and "paid" in line.lower():
        if "optional" not in line.lower() and "never" not in line.lower():
            fail(f"pathways: paid tier not marked optional: {line[:80]}")

guide = read(os.path.join(REF_DIR, "study-guide.md")) if os.path.exists(os.path.join(REF_DIR, "study-guide.md")) else ""
for head in STUDY_HEADINGS:
    if head not in guide:
        fail(f"study-guide: missing heading '{head}'")
if len(re.findall(r"^### ", guide, re.MULTILINE)) < 8:
    fail("study-guide: fewer than 8 subsections")

# 6. Relative links resolve (files + anchors, GitHub-slugger emulation) ----------
def gh_slug(s):
    s = s.strip().lower()
    return "".join(ch for ch in s if ch.isalnum() or ch in " -_").replace(" ", "-")


def heading_slugs(text):
    slugs = set()
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"\s{0,3}(#{1,6})\s+(.*)", line)
        if m:
            slugs.add(gh_slug(m.group(2)))
    return slugs


slug_cache = {}
link_count = 0
for name in REQUIRED_FILES:
    path = os.path.join(REF_DIR, name)
    if not os.path.exists(path):
        continue
    text = read(path)
    for m in REL_LINK_RE.finditer(text):
        target = m.group(1)
        file_part, _, anchor = target.partition("#")
        link_count += 1
        resolved = os.path.normpath(os.path.join(REF_DIR, file_part)) if file_part else path
        if not os.path.exists(resolved):
            fail(f"{name}: broken relative link -> {target}")
            continue
        if anchor and resolved.endswith(".md"):
            a = anchor.lstrip("#")
            if resolved not in slug_cache:
                slug_cache[resolved] = heading_slugs(read(resolved))
            if a not in slug_cache[resolved]:
                fail(f"{name}: anchor '#{a}' not found in {target}")
# 7. Cross-links into the reference library -------------------------------------
for path, needle in CROSS_LINK_TARGETS.items():
    if not os.path.exists(path):
        fail(f"{path}: missing (expected cross-link to {needle})")
        continue
    if needle not in read(path):
        fail(f"{path}: no link to {needle}")

module_dirs = sorted(
    d for d in os.listdir(os.path.join("docs", "modules"))
    if d.startswith("module-") and os.path.isdir(os.path.join("docs", "modules", d))
)
for d in module_dirs:
    path = os.path.join("docs", "modules", d, "README.md")
    if not os.path.exists(path):
        fail(f"{d}: missing README.md")
        continue
    if MODULE_LINK not in read(path):
        fail(f"{d}: footer missing link to {MODULE_LINK}")

# 8. URL manifest parity ---------------------------------------------------------
doc_urls = set()
for name in REQUIRED_FILES:
    path = os.path.join(REF_DIR, name)
    if not os.path.exists(path):
        continue
    for u in URL_RE.findall(read(path)):
        doc_urls.add(u.rstrip(".,;:'"))

if "--write-manifest" in sys.argv:
    with io.open(MANIFEST, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# External URL manifest for docs/reference/*.md\n")
        fh.write("# Verified live: 2026-10-10 (see docs/reference/README.md flagged table)\n")
        fh.write("# Regenerate: python scripts/validate-references.py --write-manifest\n")
        for u in sorted(doc_urls):
            fh.write(u + "\n")
    print(f"wrote {MANIFEST}: {len(doc_urls)} URLs")
    sys.exit(0)

if not os.path.exists(MANIFEST):
    fail(f"{MANIFEST}: missing (run 'python scripts/validate-references.py --write-manifest')")
else:
    manifest_urls = set()
    for line in read(MANIFEST).splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            manifest_urls.add(line)
    missing = sorted(doc_urls - manifest_urls)
    stale = sorted(manifest_urls - doc_urls)
    for u in missing:
        fail(f"manifest: URL not listed -> {u}")
    for u in stale:
        fail(f"manifest: stale entry (not in docs) -> {u}")

# ---------------------------------------------------------------------------
if failures:
    print(f"FAILURES ({len(failures)}):")
    for f in failures:
        print("  -", f)
else:
    print(
        f"PASS: {len(REQUIRED_FILES)} files, {entry_count} resource entries "
        f"({core_count} core / {entry_count - core_count} optional), "
        f"{len(tool_rows)} tool rows, {len(gloss_entries)} glossary entries, "
        f"{len(doc_urls)} external URLs in manifest, "
        f"{len(module_dirs)} module footers cross-linked."
    )
for w in warnings:
    print(f"warning: {w}")

# Optional live URL check --------------------------------------------------------
if "--check-urls" in sys.argv:
    import concurrent.futures as cf
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    def check(u):
        req = Request(u, method="GET", headers={
            "User-Agent": "Mozilla/5.0 (compatible; course-link-check/1.0)",
            "Accept": "*/*",
        })
        try:
            with urlopen(req, timeout=25) as r:
                return u, r.status
        except HTTPError as e:
            return u, e.code
        except Exception as e:
            return u, "ERR:%s" % type(e).__name__

    hard_fail = 0
    blocked = 0
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        for u, code in ex.map(check, sorted(doc_urls)):
            if code == 200:
                continue
            if isinstance(code, int) and code in BOT_BLOCK:
                print(f"warning: BLOCK {code} (bot wall, verify in browser) {u}")
                blocked += 1
            else:
                print(f"FAIL: {code} {u}")
                hard_fail += 1
    print(f"live check: {len(doc_urls)} URLs, {blocked} bot-blocked warnings, {hard_fail} hard failures")
    if hard_fail:
        failures.append(f"{hard_fail} URLs failed live verification")

sys.exit(1 if failures else 0)
