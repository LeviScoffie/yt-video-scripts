---
name: youtube-hook-qc
description: QC and edit a YouTube section hook. Takes the written hook and the body section it leads into, then returns a revised hook with all issues fixed. Run immediately after writing each hook. Trigger when the autodraft workflow reaches the hook QC step, or when the user says "QC the hook", "check this hook", or "fix the hook".
---

# YouTube Hook QC

Takes a written hook (and its transition line if present) and the body section it introduces, then returns a revised version. Not a report — the output is the fixed opening block ready to use.

The hook and any transition line live at the TOP of the current section. The transition grounds the viewer in context from the previous section. The hook builds the curiosity. Neither belongs at the end of the previous section.

**Before running any check:** read `../_shared/ai-slop-ban-list/ai-slop-ban-list.md` (the floor) AND `../_shared/voice-and-style.md` (the voice). Grade the hook against both.

---

## What You Need

- The written hook (and transition line if present)
- The body section it introduces (needed for the leak test)
- The full script (needed for the repetition check)

---

## The QC Process

### Check 1 — Length
Is the hook 1–2 lines maximum?
- **Fail:** Hook runs to 3+ sentences
- **Fix:** Cut to the single strongest line. A second line only stays if it adds genuine tension — not if it restates the first.

### Check 2 — The leak test (most important check)
Could someone read this hook and roughly guess what the section teaches?
- **Fail:** "Here's why your watch time doesn't matter anymore" — tells them the section's lesson
- **Fix:** Rewrite to create a gap without showing what fills it. Keep the mechanism vague enough that the only resolution is to keep watching.
- **How to run it:** read only the hook, then guess what the section is about. If the guess is close, it leaked. Rewrite.

### Check 3 — Genuine curiosity gap
Does the hook make the viewer feel something that pulls them forward — not just describe what's coming?
- **Fail:** "In this section I'm going to explain why generic content gets buried"
- **Fix:** Lead with pain, a hidden cost, or a result they want — keep the mechanism vague

### Check 4 — Specific enough to be real
Could this hook apply to any video on any topic?
- **Fail:** "There's something most people don't know about this…"
- **Fix:** Add a detail that anchors it — a number, a named consequence, a specific situation

### Check 5 — Cold open test
Does the hook work if someone saw it with zero context — as a standalone clip?
- **Fail:** Hook relies on knowing what was covered in a previous section
- **Fix:** Rewrite so the tension is self-contained

### Check 6 — Transition line re-states result or pain
Does the transition line give a cold viewer enough context to understand what this section is about and why they should care?
- **Fail:** "Here's the team." / "Here's what happened next." — no result, no context
- **Fix:** Re-state the specific result or pain. Even if it repeats something from an earlier section, that's fine — every section should re-sell the promise.

### Check 7 — Desired result is present
Does the hook point toward something the viewer actually wants — an outcome, or the avoidance of a specific pain?
- **Fail:** Hook creates curiosity but doesn't connect to anything the viewer cares about getting or avoiding
- **Fix:** Anchor the curiosity to a real desire. Curiosity is the vehicle; desire is the engine.

### Check 8 — No repetition with earlier script
Does the hook say something that hasn't already been said in the intro or a previous section?
- **Fail:** Hook restates a claim, number, or insight the viewer already heard
- **Fix:** Rewrite to open a new angle

### Check 9 — Mechanics
- No em dashes → replace with comma or period
- No dramatic standalone fragments ("Not even close." "Dead wrong.") → rewrite as complete sentences
- Normal sentence case throughout
- Sounds like a real person talking, not a copywriter performing

### Check 10 — Anti-slop and voice pass (REQUIRED)
Re-read `../_shared/ai-slop-ban-list/ai-slop-ban-list.md` and `../_shared/voice-and-style.md`. Scan the hook against both.
- **Fail:** Any banned opener, pompous verb, inflated adjective, throat-clearer, fake curiosity drumroll, or other pattern from the slop list
- **Fail:** Any rule in the voice file the hook violates
- **Fix:** Apply the correction. Don't flatten personality — fix AI defaults, keep the brand's voice.

Output the result: `[Voice: passed]` or `[Voice: fixed — <one-line summary>]`

---

## Output Format

```
[Fixed: <one-line summary, if anything changed>]
[Voice: passed] or [Voice: fixed — <what changed>]

HOOK — Point [X]
[revised hook]
```

If nothing needed fixing:

```
[No changes needed]
[Voice: passed]

HOOK — Point [X]
[original hook]
```
