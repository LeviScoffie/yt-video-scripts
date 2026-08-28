---
name: youtube-intro-qc
description: QC and edit a YouTube intro. Takes the written intro and returns a revised version with all issues fixed. Use immediately after writing the intro — before moving to the body sections. Trigger when the autodraft workflow reaches the intro QC step, or when the user says "QC the intro", "check the intro", or "fix the intro".
---

# YouTube Intro QC

Takes a written intro and returns a revised, improved version. Not a report — the output is the fixed intro ready to use.

**Before running any check:** read `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` (the floor) AND `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/voice-and-style.md` (the voice). Grade the draft against both. The final check enforces them explicitly — but they should inform every fix you make.

---

## What You Need

- The written intro
- The video title (to check congruence)

---

## The QC Process

Run every check. Fix anything that fails directly in the copy. Leave passing sections alone.

### Check 1 — Title congruence
Does the first line connect directly to the video title? If the viewer just clicked, does the first line feel like a natural continuation?
- **Fail:** First line is tangential, or opens with a greeting ("Welcome back…", "Today we're going to talk about…")
- **Fix:** Rewrite the opener to land on the exact topic or pain the title promised

### Check 2 — Specific opening moment
Is the first beat a specific personal observation, relatable failure, or concrete tension — not a generic struggle statement?
- **Fail:** "If you've been struggling with your content…" with no concrete moment. Vague stakes. Straight to the roadmap with no setup.
- **Fix:** Open with a specific moment. Name a real number, a real failure, a real situation — let stakes follow from it.

### Check 3 — Credibility shown, not claimed
Is credibility shown through specific experience or data — not just asserted?
- **Fail:** "I'm an expert in…" or "I've been doing this for years…" with no supporting detail
- **Fix:** Replace with a specific — what you've done, what you've watched happen, how many times

### Check 4 — Tension or invalidation present
After the opening observation, does the intro name the belief, default advice, or assumption the video is going to dismantle?
- **Fail:** Jumps from opening straight to the roadmap without naming what the viewer assumed and why it fails. Or the invalidation is vague ("most advice is wrong").
- **Fix:** Name the specific belief and show in one or two sentences why it doesn't work

### Check 5 — Concrete stakes
Is the risk or consequence real and specific?
- **Fail:** "…and it's costing you" with no detail on what or how much
- **Fix:** Name the actual loss — views that dropped, clients who didn't reach out, calls that didn't book

### Check 6 — Roadmap is the last beat
Is the roadmap ("in this video I'll show you…") the terminal line of the intro?
- **Fail:** A beat appears after the roadmap. Or the roadmap is used as the opener (line 1) instead of the close.
- **Fix:** Cut anything after the roadmap. The next words should be Point 1.

### Check 7 — No fluff lines
Test: remove the line. If the intro reads the same or better without it, cut it.
- Common offenders: "Let me explain what I mean", "Here's why that matters", "I'll walk you through this step by step"
- **Fix:** Delete. Do not replace.

### Check 8 — No repeated points
If two lines make the same core claim, cut the weaker one.
- **Fix:** Keep the more specific or more surprising version. Cut the other entirely.

### Check 9 — Length
- Under 75 words: check if stakes and roadmap are both present — if either is missing, that's why it's thin
- Over 150 words: run Check 7 and Check 8 again before cutting anything else

### Check 10 — Mechanics
- No em dashes → replace with comma or period
- No "Most people…" opener → rewrite
- Contractions preferred ("can't", "won't", "you're")
- No closing recap that restates who the video is for → cut it

### Check 11 — Anti-slop and voice pass (REQUIRED)
Re-read `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` and `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/voice-and-style.md`. Scan the intro against both.
- **Fail:** Any banned opener, pompous verb, inflated adjective, throat-clearer, teacher-mode announcement, or other pattern from the slop list
- **Fail:** Any rule in the voice file's quality checklist that the intro violates
- **Fix:** Apply the correction the slop list or voice file calls for. Don't strip personality — fix AI defaults, keep the brand's voice.

Output the result of this check as: `[Voice: passed]` or `[Voice: fixed — <one-line summary>]`

---

## Output Format

```
[Fixed: <one-line summary of structural changes, if any>]
[Voice: passed] or [Voice: fixed — <what changed>]

INTRO
[revised intro copy]
```

If nothing needed fixing:

```
[No changes needed]
[Voice: passed]

INTRO
[original intro copy]
```
