---
name: youtube-outline-qc
description: QC and edit a YouTube video outline. Takes the written outline and returns a revised version with structural issues fixed. Run immediately after the outline is written — before moving to the intro. Trigger when the autodraft workflow reaches the outline QC step, or when the user says "QC the outline", "check the outline", or "fix the outline".
---

# YouTube Outline QC

Takes a written outline and returns a revised, improved version. Not a report — the output is the fixed outline ready to use.

**Before running any check:** read `../_shared/ai-slop-ban-list/ai-slop-ban-list.md` (the floor) AND `../_shared/voice-and-style.md` (the voice). The final check enforces both — but they should inform every fix you make.

---

## What You Need

- The written outline (all points with titles and descriptions)
- The video angle or title

---

## The QC Process

Run every check in order. Fix anything that fails. Leave passing sections alone.

### Check 1 — Narrative arc (question chain test)
For every point, write: "This point raises the question: ___." Then confirm the next point answers it.
- **Pass:** Each point raises a question the next point directly answers. The viewer is pulled forward.
- **Fail:** A question goes unanswered, or a later point answers a question that was never raised. Sequence feels like a list, not a story.
- **Fix:** Reorder so each question-answer pair is adjacent. If a point raises no question and answers none, it's either a Close point (put it last) or dead weight (cut it).

### Check 2 — No repeated ideas (core claim audit)
For every point, write: "The core claim of this point is: ___." Then scan all claims side by side.
- **Pass:** Every core claim is unique.
- **Fail:** Two points share the same core claim, even if worded differently.
- **Fix:** Merge into one stronger point. Keep the specific details from both. If they're one idea split across two points unnecessarily, consolidate.

### Check 3 — Title sequence test
Read only the point titles in order, ignoring descriptions. They should tell the complete story on their own.
- **Pass:** A stranger could read just the titles and follow the argument start to finish.
- **Fail:** A title is so vague it could appear anywhere ("The mindset shift", "Why this matters"). Or two titles could swap positions without the sequence breaking.
- **Fix:** Rewrite vague titles to signal the specific job that point is doing. A good title is a micro-claim, not a topic label.

### Check 4 — Each point has a unique job
Tag each point:
- **Setup** — establishes the problem or stakes
- **Proof** — makes the claim real with data, story, or example
- **Mechanism** — explains why something happens
- **Reframe** — shifts how the viewer sees the problem
- **Fix** — delivers the solution
- **Close** — payoff or call to action

Rules:
- Every video needs at least one of each: Setup, Proof, Fix, Close
- No more than two consecutive points with the same tag
- Three Fix points in a row probably belong merged into one

### Check 5 — No vague points
Is every point specific enough that a writer could pick it up and know exactly what to say?
- **Pass:** Description names the specific insight, tool, story, or data point the section covers.
- **Fail:** Description is a topic, not an insight. "Talk about the team" is vague. "Three roles, clean lanes, no overlapping responsibilities" is specific.
- **Fix:** Rewrite the description to name the actual thing being taught. If you can't name it, the point doesn't have a real insight yet — flag it.

### Check 6 — Point count
- Under 6 points: check if Setup, Proof, or Close is missing — these are most commonly dropped
- Over 10 points: at least two are probably doing the same job — run Check 2 and Check 4 again
- Target: 7–9 points for a standard 8–12 minute video

### Check 7 — Anti-slop and voice pass (REQUIRED)
Re-read `../_shared/ai-slop-ban-list/ai-slop-ban-list.md` and `../_shared/voice-and-style.md`. Scan the outline against both.
- **Fail:** Any point title or description uses pompous verbs, inflated adjectives, showy nouns, or other slop-list patterns
- **Fail:** Any structural pattern from the voice file that the outline violates
- **Fix:** Apply corrections. Flag any point description that sounds like AI-generated filler rather than a specific insight.

Output the result: `[Voice: passed]` or `[Voice: fixed — <one-line summary>]`

---

## Output Format

```
**Decision log:**
- [What changed and the specific reason — one line each]

[Voice: passed] or [Voice: fixed — <what changed>]

**Real angle:** [one sentence]

**1. [Title]** — [Job: Setup / Proof / Mechanism / Reframe / Fix / Close]
[Description — 2–4 lines, specific enough that a writer knows exactly what to cover]

**2. [Title]** — [Job]
[Description]

...and so on
```

If nothing needed fixing:

```
**Decision log:** No changes needed.
[Voice: passed]

[outline as-is with job tags added]
```
