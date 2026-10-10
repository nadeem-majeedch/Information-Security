#!/usr/bin/env python3
"""Validate the lab collection: 17-field format, links, real placeholders, safety notes."""
import pathlib, re, sys

labs_dir = pathlib.Path("docs/labs")
failures = []

REQUIRED_PATTERNS = [
    ("1 Header (ID/title/difficulty/duration)", r"\*\*Lab ID:\*\*.*\*\\*Difficulty:\\*\\*.*\*\\*Estimated duration:\\*\\*"),
    ("2 Scenario", r"^## Scenario"),
    ("3 Learning objectives", r"^## Learning Objectives"),
    ("4 Prerequisites", r"^## Prerequisites"),
    ("5 Tools/OS/versions", r"^## Tools, Operating Systems"),
    ("6 Setup + permissions", r"^## Setup \(Free\) and Required Permissions"),
    ("7 Environment/starting state", r"^## Lab Environment and Starting State"),
    ("8 Tasks", r"^## Tasks"),
    ("9 Expected observations", r"^## Expected Observations"),
    ("10 Investigation questions", r"^## Investigation Questions"),
    ("11 Troubleshooting", r"^## Troubleshooting"),
    ("12 Evidence to collect", r"^## Evidence to Collect"),
    ("13 Deliverable + report structure", r"^## Deliverable and Report Structure"),
    ("14 Completion checklist", r"^## Completion Checklist"),
    ("15 Cleanup and reset", r"^## Cleanup and Reset"),
    ("16 Optional challenges", r"^## Optional Challenges"),
    ("17 References and safety notes", r"^## References and Safety Notes"),
]

# Real placeholder phrases only (NOT the word "placeholder" in technical teaching prose
# such as SQL parameterized-query placeholders).
PLACEHOLDER_RE = re.compile(
    r"to be added|\bTBD\b|coming soon|lorem ipsum|repeat the (previous|last)|content to be added",
    re.IGNORECASE,
)
FORBIDDEN_RE = re.compile(
    r"git push|git commit|deploy to production|steal (the |your |these |real )?credentials|brute[- ]force (a )?(real|someone else)",
    re.IGNORECASE,
)
SAFETY_RE = re.compile(r"safe|safety", re.IGNORECASE)

lab_dirs = sorted(d for d in labs_dir.iterdir() if d.is_dir() and d.name.startswith("lab-"))
print(f"Found {len(lab_dirs)} lab directories\n")

for d in lab_dirs:
    readme = d / "README.md"
    if not readme.exists():
        failures.append(f"{d.name}: missing README.md")
        continue
    text = readme.read_text(encoding="utf-8")
    for label, pat in REQUIRED_PATTERNS:
        if not re.search(pat, text, re.MULTILINE):
            failures.append(f"{d.name}: missing element '{label}'")
    m = PLACEHOLDER_RE.search(text)
    if m:
        failures.append(f"{d.name}: placeholder text -> '{m.group(0)}' at offset {m.start()}")
    m = FORBIDDEN_RE.search(text)
    if m:
        failures.append(f"{d.name}: forbidden language -> '{m.group(0)}'")
    if not SAFETY_RE.search(text):
        failures.append(f"{d.name}: no safety note found")

LINK_RE = re.compile(r"\]\((\.{1,2}/[^)#\s]+)(#[^)\s]*)?\)")
link_count = 0
for md in sorted(labs_dir.rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    for target, _anchor in LINK_RE.findall(text):
        link_count += 1
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            failures.append(f"{md.relative_to(labs_dir)}: broken link -> {target}")

index = (labs_dir / "README.md").read_text(encoding="utf-8")
for d in lab_dirs:
    lab_id = d.name.split("-")[1].upper()
    if f"LAB-{lab_id}" not in index:
        failures.append(f"labs index: missing {lab_id}")

if failures:
    print(f"FAILURES ({len(failures)}):")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("ALL CHECKS PASSED")
print(f"  - {len(lab_dirs)} labs each have all 17 required elements")
print("  - no real placeholder text found")
print("  - no forbidden offensive/commit/deploy language found")
print("  - every lab includes a safety note")
print(f"  - all {link_count} relative links resolve")
print("  - all labs listed in the labs index")
