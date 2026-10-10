#!/usr/bin/env python3
"""Validate the assessment system: question counts, answer consistency, coverage, links.

Run from the repository root:  python scripts/validate-assessments.py
Exits non-zero if any check fails.
"""
import os
import re
import sys
import unicodedata

DOCS = "docs"
ASSESS = os.path.join(DOCS, "assessments")

# Expected quiz formats from docs/course-roadmap.md: total questions, MCQ count
# M03 is 10 quiz questions + 1 scenario essay (the essay is numbered Q11 on the page).
QUIZ_SPEC = {
    1: (12, 8), 2: (12, 8), 3: (11, 6), 4: (12, 8), 5: (12, 8),
    6: (14, 10), 7: (12, 8), 8: (12, 8), 9: (14, 10), 10: (12, 8), 11: (10, 6),
    12: (12, 7), 13: (12, 8), 14: (14, 9), 15: (12, 8),
    16: (12, 8), 17: (12, 8), 18: (10, 6),
}
LEVEL_DIR = {**{n: "level-1" for n in range(1, 6)},
             **{n: "level-2" for n in range(6, 12)},
             **{n: "level-3" for n in range(12, 16)},
             **{n: "level-4" for n in range(16, 19)}}

errors = []
notes = []


def err(msg):
    errors.append(msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def gh_slug(heading):
    """GitHub-style heading anchor slug."""
    h = heading.strip().strip("#").strip()
    h = re.sub(r"`", "", h)
    # drop markdown link syntax to its text
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = h.lower()
    # keep letters/numbers/spaces/hyphens/underscores (unicode-aware), drop the rest
    out = []
    for ch in h:
        if ch.isalnum() or ch in " -_":
            out.append(ch)
    slug = "".join(out).replace(" ", "-")
    return slug


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


# ---------------------------------------------------------------- quiz checks
quiz_files = {}
for n in range(1, 19):
    p = os.path.join(ASSESS, LEVEL_DIR[n], "quiz-m%02d.md" % n)
    if not os.path.exists(p):
        err("MISSING quiz file: %s" % p)
        continue
    quiz_files[n] = p

for n, path in sorted(quiz_files.items()):
    t = read(path)
    total_expected, mcq_expected = QUIZ_SPEC[n]

    # --- question counts (identity by number, not just count)
    q_nums = sorted({int(m) for m in re.findall(r"^\*\*Q(\d+)\.", t, re.M)})
    if len(q_nums) != total_expected or q_nums != list(range(1, total_expected + 1)):
        err("%s: expected Q1..Q%d (%d), found %s" % (path, total_expected, total_expected, q_nums))

    # --- MCQ structure: only questions inside the "Multiple choice" part count
    head = re.search(r"^#{1,3}\s+.*Multiple choice.*$", t, re.M)
    if not head:
        err("%s: no multiple-choice section found" % path)
        region = ""
    else:
        nxt = re.search(r"^#{1,3}\s+Part\s+[B-Z]", t[head.end():], re.M)
        wc = t.find("## Worked answers")
        end_rel = nxt.start() if nxt else max(0, wc - head.end())
        region = t[head.end():head.end() + end_rel]
    qmarks = list(re.finditer(r"^\*\*Q(\d+)\.", region, re.M))
    mcq_count = 0
    for i, m in enumerate(qmarks):
        block = region[m.start(): qmarks[i + 1].start() if i + 1 < len(qmarks) else len(region)]
        opts = re.findall(r"^- \(([a-d])\)", block, re.M)
        if opts:
            mcq_count += 1
            if opts != ["a", "b", "c", "d"]:
                err("%s Q%s: options are %s, expected [a,b,c,d] in order"
                    % (path, m.group(1), opts))
    if mcq_count != mcq_expected:
        err("%s: expected %d MCQs in the multiple-choice part, found %d"
            % (path, mcq_expected, mcq_count))

    # --- required quiz furniture
    checks = {
        "instructions": r"\*\*Instructions\.\*\*",
        "pass mark": r"[Pp]ass mark",
        "outcome/roadmap coverage": r"[Cc]overage.*course-roadmap\.md|roadmap.*#[mM]\d\d",
        "link to lesson": r"\[Module %02d lesson\]" % n,
        "worked answers heading": r"^## Worked answers",
        "review exercises": r"^## Module-end review exercises",
        "back-link to hub": r"\.\./README\.md",
        "safety note": r"[Ss]afety",
    }
    for name, pat in checks.items():
        if not re.search(pat, t, re.M | re.S):
            err("%s: missing %s" % (path, name))

    # --- answer consistency: every question has a worked answer; MCQ keys valid
    ans_keys = dict(re.findall(r"\*\*Q(\d+) — \(([a-d])\)", t))
    if len(ans_keys) != mcq_count:
        err("%s: %d MCQ answer keys found, expected %d" % (path, len(ans_keys), mcq_count))
    answered = {int(x) for x in re.findall(r"\*\*Q(\d+)[.\s—]", t.split("## Worked answers")[-1])}
    missing_ans = [q for q in q_nums if q not in answered]
    if missing_ans:
        err("%s: no worked answer for Q%s" % (path, missing_ans))

    # --- wrong-choice explanations: ≥90% of MCQ key paragraphs must explain
    # why wrong options are wrong (explicit other-option reference or
    # misconception/distractor language)
    ans_block = t.split("## Worked answers")[-1]
    kw = re.compile(r"misconception|distractor|wrongly|wrong|trap|confus|unlike|"
                    r"others are|not the same|rather than|instead", re.I)
    key_ms = list(re.finditer(r"\*\*Q(\d+) — \(([a-d])\)", ans_block))
    explained = 0
    for i, km in enumerate(key_ms):
        para = ans_block[km.start(): key_ms[i + 1].start() if i + 1 < len(key_ms) else len(ans_block)]
        others = {x for x in re.findall(r"\(([a-d])\)", para)} - {km.group(2)}
        if others or kw.search(para):
            explained += 1
    if key_ms and explained < 0.9 * len(key_ms):
        err("%s: only %d/%d MCQ answers explain wrong choices (need >= 90%%)"
            % (path, explained, len(key_ms)))

    # --- no obfuscation tricks (honest policy)
    if re.search(r"<script", t, re.I):
        err("%s: contains <script> (misleading hidden-answer pattern)" % path)
    if not re.search(r"<details>", t):
        err("%s: answers not in collapsible <details> blocks" % path)

    notes.append("quiz-m%02d: %d questions (%d MCQ) OK-shape" % (n, len(q_nums), mcq_count))

# ---------------------------------------------------------------- case studies
cs_files = sorted(os.listdir(os.path.join(ASSESS, "case-studies")))
if len(cs_files) != 4:
    err("expected 4 case studies, found %d" % len(cs_files))
for f in cs_files:
    p = os.path.join(ASSESS, "case-studies", f)
    t = read(p)
    if not re.search(r"^## Rubric", t, re.M):
        err("%s: missing rubric" % p)
    if len(re.findall(r"^## Model answers", t, re.M)) != 1:
        err("%s: missing model answers" % p)
    if "<script" in t.lower():
        err("%s: contains script tag" % p)
    qs = re.findall(r"\*\*Q(\d+) ", t)
    if sorted({int(q) for q in qs}) != list(range(1, 7)):
        err("%s: expected Q1..Q6, found %s" % (p, sorted({int(q) for q in qs})))
    if not re.search(r"[Ss]afety|RoE|authorization", t):
        err("%s: no safety/authorization reasoning" % p)

# ---------------------------------------------------------------- final docs
final_required = {
    "lab-challenges.md": [r"LC-1", r"LC-2", r"LC-3", r"LC-4", r"[Ee]valuation criteria", r"[Dd]eliverables"],
    "advanced-final.md": [r"CAP-ADV|Advanced Final", r"\*\*Instructions\.\*\*", r"## Worked answers",
                          r"[Ss]ample|[Ee]pected|point", r"[Cc]overage"],
    "capstone-rubric.md": [r"Stage A", r"Stage B", r"Stage C", r"Stage D", r"Stage E",
                           r"Exemplary", r"Proficient", r"Developing", r"Inadequate"],
}
for fname, pats in final_required.items():
    p = os.path.join(ASSESS, "final", fname)
    if not os.path.exists(p):
        err("MISSING %s" % p)
        continue
    t = read(p)
    for pat in pats:
        if not re.search(pat, t):
            err("%s: missing %s" % (p, pat))
    if "<script" in t.lower():
        err("%s: contains script tag" % p)

# CAP-ADV: expectations are derived from the page's own header (self-consistency),
# then checked against the questions and the worked-answer point bands.
adv = read(os.path.join(ASSESS, "final", "advanced-final.md"))
hdr_q = re.search(r"Questions:\*\* (\d+) \((\d+) multiple choice \+ (\d+) constructed response\)", adv)
hdr_tot = re.search(r"\*\*Total:\*\* (\d+) points", adv)
hdr_pass = re.search(r"≥ 70% \((\d+) of (\d+) points\)", adv)
if not (hdr_q and hdr_tot and hdr_pass):
    err("CAP-ADV: header line missing questions/total/pass structure")
    hdr_q = hdr_q or type("H", (), {"group": lambda s, i: 0})()
    hdr_tot = hdr_tot or type("H", (), {"group": lambda s, i: 0})()
    hdr_pass = hdr_pass or type("H", (), {"group": lambda s, i: 0})()
exp_total_q, exp_mcq, exp_cr = int(hdr_q.group(1)), int(hdr_q.group(2)), int(hdr_q.group(3))
exp_total_pts, exp_pass = int(hdr_tot.group(1)), int(hdr_pass.group(1))
if int(hdr_pass.group(2)) != exp_total_pts:
    err("CAP-ADV: pass line says %s of %s points but Total is %d"
        % (hdr_pass.group(1), hdr_pass.group(2), exp_total_pts))
flat = [int(tup) for tup in re.findall(r"\((?:Constructed|Configuration analysis|Practical investigation|"
                                      r"Threat-model judgment|Log interpretation|Scope/ethics|IR sequencing|"
                                      r"Malware-to-defense|Scenario judgment|Privacy|Integration capstone-preview), "
                                      r"(\d+) pts\)", adv)]
mcq_count_adv = len(re.findall(r"\(MCQ, 1 pt\)", adv))
adv_q_count = len(re.findall(r"^\*\*Q\d+\.", adv.split("## Worked answers")[0], re.M))
if adv_q_count != exp_total_q:
    err("CAP-ADV: header claims %d questions, page has %d" % (exp_total_q, adv_q_count))
if mcq_count_adv != exp_mcq:
    err("CAP-ADV: header claims %d MCQ, found %d" % (exp_mcq, mcq_count_adv))
if len(flat) != exp_cr:
    err("CAP-ADV: header claims %d constructed response, found %d" % (exp_cr, len(flat)))
if sum(flat) + mcq_count_adv != exp_total_pts:
    err("CAP-ADV: point bands sum to %d but header Total is %d"
        % (sum(flat) + mcq_count_adv, exp_total_pts))
import math
if exp_pass != math.ceil(0.70 * exp_total_pts):
    err("CAP-ADV: pass mark %d is not >=70%% of %d" % (exp_pass, exp_total_pts))

# ---------------------------------------------------------------- hub coverage
hub = read(os.path.join(ASSESS, "README.md"))
if "student-facing answer policy" not in hub.lower():
    err("hub: missing student-facing answer policy section")
all_assess_files = []
for root, _, files in os.walk(ASSESS):
    for f in files:
        if f.endswith(".md"):
            all_assess_files.append(os.path.join(root, f))
for p in all_assess_files:
    rel = os.path.relpath(p, ASSESS).replace(os.sep, "/")
    if rel == "README.md":
        continue
    if "./" + rel not in hub:
        err("hub does not link %s" % rel)

# ---------------------------------------------------------------- link check
slug_cache = {}
link_re = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

def resolve_links(path):
    text = read(path)
    bad = []
    for m in link_re.finditer(text):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        file_part, _, anchor = target.partition("#")
        if not file_part:
            continue
        base = os.path.dirname(path)
        resolved = os.path.normpath(os.path.join(base, file_part))
        if not os.path.exists(resolved):
            bad.append(target)
            continue
        if anchor and resolved.endswith(".md"):
            if resolved not in slug_cache:
                slug_cache[resolved] = heading_slugs(read(resolved))
            if anchor not in slug_cache[resolved]:
                bad.append("%s (anchor '#%s' not found)" % (target, anchor))
    return bad

link_targets = all_assess_files + [
    os.path.join(DOCS, "index.md"),
    os.path.join(DOCS, "assessment-guide.md"),
    os.path.join(DOCS, "modules", "README.md"),
] + [os.path.join(DOCS, "modules", d, "README.md") for d in os.listdir(os.path.join(DOCS, "modules"))
     if d.startswith("module-")]
capstone_files = []
for root, _, files in os.walk(os.path.join(DOCS, "capstone")):
    for f in files:
        if f.endswith(".md"):
            capstone_files.append(os.path.join(root, f))
link_targets = capstone_files + link_targets

# ---------------------------------------------------------------- capstone package
if not capstone_files:
    err("capstone package missing: docs/capstone not found")
CAP_REQ = {
    "README.md": [r"## 1\. Overview and student brief", r"## 2\. Project objectives",
                  r"## 3\. Choosing your scenario", r"## 4\. Scope, assumptions, constraints",
                  r"No attacking, scanning, or probing public", r"No purchasing software",
                  r"No accessing university", r"No real organizational or personal data",
                  r"## 5\. Prerequisites", r"\*\*1\. Understand the organization",
                  r"\*\*7\. Produce the final report",
                  r"Evidence collection requirements", r"## 7\. Skills provenance",
                  r"## 8\. Optional extensions"],
    "scenarios.md": [r"Scenario A", r"Scenario B"],
    "rubric.md": [r"Technical correctness", r"Investigation quality", r"Risk prioritization",
                  r"Remediation", r"Ethical practice", r"Crosswalk to the Assessment Guide"],
    "checklists.md": [r"Completion checklist", r"Submission checklist"],
    os.path.join("templates", "report-template.md"): [r"Executive summary", r"remediation roadmap", r"Appendices"],
    os.path.join("templates", "risk-register-template.md"): [r"treatment", r"residual", r"rationale"],
    os.path.join("templates", "threat-model-template.md"): [r"STRIDE", r"[Tt]rust boundar"],
    os.path.join("templates", "findings-remediation-template.md"): [r"\*\*Evidence", r"\*\*Severity", r"Retest"],
    os.path.join("templates", "portfolio-presentation-spec.md"): [r"Folder structure", r"presentation"],
}
cap_root = os.path.join(DOCS, "capstone")
for rel, pats in CAP_REQ.items():
    p = os.path.join(cap_root, rel)
    if not os.path.exists(p):
        err("capstone: MISSING %s" % p)
        continue
    ct = read(p)
    for pat in pats:
        if not re.search(pat, ct):
            err("capstone %s: missing required section/pattern %r" % (rel, pat))
    if "<script" in ct.lower():
        err("capstone %s: contains script tag" % rel)
# every prior module must appear in the skills-provenance table (nothing taught only at capstone)
if os.path.exists(os.path.join(cap_root, "README.md")):
    capreadme = read(os.path.join(cap_root, "README.md"))
    missing_mods = [n for n in range(1, 19) if ("M%02d" % n) not in capreadme]
    if missing_mods:
        err("capstone README: skills provenance never mentions modules %s" % missing_mods)

total_links = 0
for p in link_targets:
    total_links += len(link_re.findall(read(p)))
    for bad in resolve_links(p):
        err("%s: broken link -> %s" % (p, bad))

# ---------------------------------------------------------------- curriculum coverage
# every module M01-M19 must be linked from the hub or reachable from a quiz/case/final page
coverage = set()
for p in all_assess_files:
    t = read(p)
    coverage |= {int(x) for x in re.findall(r"module-(\d\d)-", t)}
    coverage |= {int(x) for x in re.findall(r"\bM(\d\d)\b", t)}
missing = [n for n in range(1, 20) if n not in coverage]
if missing:
    err("assessments never reference modules: %s" % missing)

# ---------------------------------------------------------------- report
print("== validate-assessments.py ==")
for line in notes:
    print("  " + line)
print("  case studies: %d, final docs: %d, assessment pages: %d" %
      (len(cs_files), len(final_required), len(all_assess_files)))
print("  links checked: %d across %d files" % (total_links, len(link_targets)))
print("  capstone package: %d files checked for required sections" % len(capstone_files))
print("  module coverage: M01-M19 all referenced" if not [e for e in errors if "never reference" in e]
      else "  module coverage: INCOMPLETE")
if errors:
    print("\nFAIL (%d):" % len(errors))
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print("\nPASS: question counts, answer consistency, coverage, and links all OK")
