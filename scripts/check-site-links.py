#!/usr/bin/env python3
"""Check internal links in the built Jekyll site (_site).

Run after `jekyll build -s docs -d _site`:

    python scripts/check-site-links.py [_site]

What it verifies:
  * every internal href/src in built HTML resolves to a file in the output tree
    (pretty permalinks, baseurl prefixes, and directory URLs all handled);
  * no unrewritten `.md` links remain (would 404 on the published site —
    means the jekyll-relative-links plugin did not run);
  * no source-root maintainer files leaked into the output.

Exit status: 0 = clean, 1 = problems found.
"""
import os
import re
import sys

SITE = sys.argv[1] if len(sys.argv) > 1 else "_site"
CONFIG = os.path.join("docs", "_config.yml")

# baseurl from the site config, so the check matches production paths.
baseurl = ""
if os.path.exists(CONFIG):
    m = re.search(r"^baseurl:\s*(\S+)", open(CONFIG, encoding="utf-8").read(), re.MULTILINE)
    if m:
        baseurl = m.group(1).strip("'\"")

if not os.path.isdir(SITE):
    print(f"FAIL: built site not found at '{SITE}' — run the Jekyll build first")
    sys.exit(1)

HREF_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
# Files that must never appear in the published output.
FORBIDDEN_IN_OUTPUT = ["MAINTENANCE.md", "docs-meta", "Gemfile"]

failures = []
checked = 0
md_links = 0
html_files = []

for root, _dirs, files in os.walk(SITE):
    for f in files:
        if f.endswith((".html", ".htm")):
            html_files.append(os.path.join(root, f))

def page_url(path):
    """Served URL path for a file in the output tree (baseurl + pretty URL)."""
    rel = os.path.relpath(path, SITE).replace(os.sep, "/")
    if rel.endswith("/index.html"):
        rel = rel[: -len("index.html")]
    elif rel == "index.html":
        rel = ""
    return "/" + rel

def resolve(from_url, target):
    """Return a site-root-relative path (no baseurl) for an internal target."""
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None  # pure fragment — same page
    if target.startswith("/"):
        if baseurl and target.startswith(baseurl + "/"):
            target = target[len(baseurl):]
        elif target == baseurl:
            target = "/"
        else:
            return "!" + target  # absolute path outside baseurl
        path = target
    else:
        # relative to the current page's directory
        cur_dir = os.path.dirname(from_url)
        parts = (cur_dir + "/" + target).split("/")
        stack = []
        for p in parts:
            if p in ("", "."):
                continue
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        path = "/" + "/".join(stack)
    return path

def exists(path):
    """Map a served URL path to a file in the output tree."""
    fs = os.path.join(SITE, path.lstrip("/"))
    if os.path.isfile(fs):
        return True
    if path.endswith("/"):
        return os.path.isfile(os.path.join(fs, "index.html"))
    return (
        os.path.isfile(fs + ".html")
        or os.path.isfile(os.path.join(fs, "index.html"))
        or os.path.isfile(fs.rstrip("/") + "/index.html")
    )

for page in sorted(html_files):
    url = page_url(page)
    text = open(page, encoding="utf-8", errors="replace").read()
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)  # comments are not live markup
    for target in HREF_RE.findall(text):
        if target.startswith(("http://", "https://", "//", "mailto:", "tel:", "data:", "javascript:")):
            continue
        checked += 1
        if target.split("#", 1)[0].split("?", 1)[0].endswith(".md"):
            md_links += 1
            failures.append(f"{url}: unrewritten .md link -> {target}")
            continue
        resolved = resolve(url, target)
        if resolved is None:
            continue
        if resolved.startswith("!"):
            failures.append(f"{url}: link escapes baseurl -> {target}")
            continue
        if not exists(resolved):
            failures.append(f"{url}: broken internal link -> {target}")

# Leak check: maintainer-only files must not be in the output.
leaks = []
for root, _dirs, files in os.walk(SITE):
    for f in files:
        if f in FORBIDDEN_IN_OUTPUT:
            leaks.append(os.path.relpath(os.path.join(root, f), SITE))
for leak in leaks:
    failures.append(f"maintainer file leaked into build: {leak}")

if failures:
    print(f"FAILURES ({len(failures)}):")
    for f in failures:
        print("  -", f)
else:
    print(
        f"PASS: {checked} internal links across {len(html_files)} built pages OK "
        f"(baseurl '{baseurl}', 0 unrewritten .md links, 0 maintainer leaks)"
    )
sys.exit(1 if failures else 0)
