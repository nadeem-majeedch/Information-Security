---
title: "Troubleshooting and Independent-Study Guide"
layout: default
---

# Troubleshooting and Independent-Study Guide

**Part of:** [Reference Library](README.md) · This course has no instructor on call. This guide is the substitute: how to fix what breaks, how to know when you're stuck *wrong*, and how to run yourself through the material.

---

## Part 1 — Troubleshooting

### 1.1 When a tool or environment breaks

Work down the list in order; stop at the first step that applies.

1. **Read the actual error, out loud, in full.** ~70% of "the lab is broken" cases are a typo, a missing flag, or a wrong working directory. `pwd`, re-run, look again.
2. **Command not found** → the tool isn't installed *or* isn't on `PATH`. Install per the [tools directory](tools.md) (official docs link is there), then open a new shell. On Windows, note whether the lab wants WSL, Git Bash, or PowerShell — mixing them is the most common Windows failure.
3. **Permission denied** → you're writing where you shouldn't (use `~/lab/`, not `/`), or you skipped `sudo`/elevation *for your own VM* (never for anything outside it). On Wireshark/tcpdump, missing capture permissions are fixed by the OS-specific capture-group steps in the [Wireshark docs](https://www.wireshark.org/docs/).
4. **Port already in use** → another service (or your previous run) holds it. Find it (`ss -lntu` / `netstat -an`), stop your own stale process or pick the alternate port the lab suggests.
5. **VM/container won't start or is dog-slow** → check the lab's stated requirements against reality: virtualization enabled in BIOS, ≥ the stated RAM free (Wazuh-class stacks want 8 GB+), snapshots taken *before* heavy steps. When a lab offers a Tier-b/lightweight path (M13 does), take it — both tiers satisfy the requirement.
6. **Network/VM can't reach the service** → confirm you're on the lab's host-only/NAT network, the guest IP matches, and a host firewall you set earlier isn't blocking your own test. Isolation is required by the [safety policy](../lab-safety-policy.md) — don't "fix" it by going to bridged/public mode.
7. **Tool version mismatch** → the docs you found describe a different major version (OpenSSL 1.1.1 vs 3.x flags differ; ATT&CK and Sigma specs move). Check `tool --version` against the docs' version banner; the [flagged list](README.md#flagged-for-review-version-sensitive-or-blocked) marks the usual suspects.
8. **Download/registration wall** → CIS benchmark PDFs and some NVD API access need a *free* account; every Core resource remains usable without payment. If a page wants money, you're on the wrong page — go via the link in the [library](README.md).
9. **A provided dataset doesn't parse or looks wrong** → don't edit it. Compute its SHA-256, compare with the lab/manifest, and re-copy from the source link. If it still differs, that's a dataset defect: note it in your portfolio and work around it (state the limitation in your write-up — honesty here is *graded*, see the [capstone evidence rules](../capstone/README.md#6b-evidence-collection-requirements)).
10. **Still broken?** Classify it: (a) *environment* → snapshot rollback + one clean retry from Setup; (b) *instructions* → re-read the stage's Expected Observations — the answer is usually a precondition you skipped; (c) *genuinely a course defect* → document it (what, where, error text, your attempted fix) in your study notes. Documenting defects is what a professional does instead of rage-quitting.

### 1.2 When *you* are stuck (the harder case)

Ask, in this order — each answer costs less than the last:

1. **Which outcome is this exercise actually grading?** Every lab lists Learning Objectives and a Completion Checklist; reread it. You may be solving a harder problem than assigned.
2. **What do I *observe* vs. what did I *expect*?** Write both. The gap usually names the concept you're missing (e.g., "I expected 443 open, got closed" → firewall state, not magic).
3. **Which module taught this?** Use the roadmap's module→topic map. If it's from an *earlier* module, that's the fix: revisit it — the [study guide's re-entry rule](#13-re-entry-rules-after-a-break) applies. (If it's from a *later* one, it's a course defect — see 1.1 step 10.)
4. **What does the primary source say?** The relevant entry in the [reference library](README.md) — official docs answer flag/syntax/behavior questions faster than any forum.
5. **Attempt the minimum viable experiment.** One variable, one command, one observation — on your lab, inside scope. Brute-forcing variations for an hour is not learning; three deliberate experiments are.
6. **Check the worked answers / expected observations — then own it.** Revealing an answer after a genuine attempt is the intended sequence everywhere in this course ([answer policy](../assessments/README.md#student-facing-answer-policy--read-this)). Write one line about *why* the answer is right; that line is the learning.
7. **Timebox and park it.** 45–60 minutes of honest effort → write the blocker in your notes with what you tried, move to another task, return in 24 h. Fresh eyes resolve what fatigue can't.

**Never do these when stuck:** scan or probe anything outside your lab (scope violations aren't troubleshooting); paste real credentials/keys anywhere; disable your isolation; fabricate evidence to fill a template ("looks right" is detectable and, per the [honesty rules](../assessment-guide.md#8-evidence-integrity-and-academic-honesty), fatal).

### 1.3 Re-entry rules (after a break)

- **≤ 2 weeks off:** retake the last module's quiz to reactivate context ([roadmap progression rules](../course-roadmap.md)).
- **≤ 2 months off:** re-read your last stage's notes + checklist status, redo the last *lab* (not just the quiz), then continue.
- **Longer:** treat it as a restart of that level — the material compounds, and Level-2 work assumes Level-1 reflexes. Budget one week to re-run gates.
- Always resume by reading **the last thing you wrote**, not the last thing you read. Your own notes are the fastest context restore you have.

---

## Part 2 — Independent-study method

### 2.1 The weekly rhythm (8–12 h/week default)

| Block | Time | What |
|---|---|---|
| **Input** | 2–3 h | Read/watch one module section; take *hand-written* summary notes (copying =/= learning) |
| **Lab** | 3–4 h | Do the module's lab **the same week** — lab within 7 days of reading is where retention happens |
| **Test** | 0.5–1 h | Module quiz ≥ 80%, unlimited retakes; after each miss, write *why* the wrong choice is wrong (that's what the worked answers model) |
| **Review** | 0.5–1 h | Compress the week into ~10 lines in `notes/module-NN.md`; update your glossary questions |
| **Buffer** | 1–2 h | Finish the lab, redo a miss, or rest — a rhythm you keep beats a rhythm you don't |

**Compress or fail:** if you can't explain a week's core idea in five plain sentences, you haven't learned it — revisit before moving on.

### 2.2 Evidence habits (they compound into the portfolio)

1. **Save as you go:** every command output you might cite goes into that stage's `evidence/` folder *immediately*, named per the [portfolio spec](../capstone/templates/portfolio-presentation-spec.md) — future-you cannot reconstruct three-week-old terminal scrollback.
2. **One running `decisions.md`:** what you chose, why, what you rejected. The capstone's "justify the decisions" grading reads straight out of this file.
3. **Safety statements early:** one line per lab session (targets, isolation) — retro-fitting them later is how people get stuck at submission.
4. **Hash what you copy** (SHA-256 in the manifest) — you'll need it for evidence integrity and it takes 10 seconds.

### 2.3 Self-testing (no instructor to test you)

- **Retrieval, not re-reading:** close the notes, write what you remember, then check. The quizzes are formative — use them as retrieval practice, not just gates.
- **Explain it out loud** (rubber-duck method): if your explanation of *why* the fix works wobbles, that's the gap — find it in the module.
- **Build your own test cases:** invent a scenario (one more log line, one more config flaw), predict the outcome, then check against the worked answers or your lab. Prediction-then-verification is the fastest way to false-confidence-free learning.
- **Spaced retakes:** retake quiz N when starting module N+2 — the progression rules already build this in.
- **The "could I grade this?" test:** take your own report, wait three days, score it with the published [rubric](../capstone/rubric.md). If you can't defend a score with a file pointer, the work isn't done.

### 2.4 When to move on (decision rules)

- **Quiz ≥ 80% + lab completion checklist ticked** → move on, even if you'd like more perfection; perfectionism stalls more self-learners than difficulty does.
- **Quiz < 80% after 2 attempts** → stop retaking; re-study the specific sections the misses point at (your miss-list from §2.1 tells you which), then retake.
- **Lab blocked > 2 hours** → apply §1.2 fully; if still blocked after a 24 h park, document the blocker, complete the *achievable* parts, and continue the course — one documented partial is survivable; stopping the course isn't. Revisit the blocker before the level gate.
- **Level gate coming** ([roadmap progression rules](../course-roadmap.md)) → finish *all* prior-level quizzes + portfolio packs first; gates assume completeness, not partials.

### 2.5 Asking for help without an instructor

1. Write the question as a **minimal reproducible description**: goal, exact command, exact error, what you expected, what you tried (3 lines each). Writing it often solves it.
2. Search **primary sources first**: official docs ([library](README.md)) → course module → glossary.
3. Community channels (forums, Reddit, Discord, Stack Overflow) are fine for *general technical* questions — **never post credentials, real target details, or proprietary data**; your labs are synthetic, so paraphrase freely.
4. When the answer is a *course* defect, you have no one to report to — so write the defect note (§1.1 step 10) and keep going. Your documented workaround becomes part of your portfolio's honesty signal.

### 2.6 Keeping momentum (the actual dropout cause)

- **Miss a day, don't miss twice.** The rhythm in §2.1 resumes at the *current* step, not a week of guilt.
- **Shrink the step:** "do the lab" is a task you'll avoid; "open the lab, run setup, take one screenshot" is a task you'll do.
- **Pair effort with a visible artifact:** each week should leave something *in the portfolio folder* — a pack, a note, a quiz score. Visible progress is motivation.
- **Plateau at labs = read again; plateau at quizzes = do labs.** The two modes feed each other; alternating breaks plateaus.
- **Finish things:** a completed mediocre portfolio beats an incomplete brilliant one — the [completion checklist](../capstone/checklists.md) exists to define "done."

---

**Related:** [Reference library](README.md) · [Tools directory](tools.md) · [Glossary](glossary.md) · [Learning pathways](pathways.md) · [Course home](../index.md)
