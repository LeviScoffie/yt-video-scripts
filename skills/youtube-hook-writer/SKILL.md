---
name: youtube-hook-writer
description: Generate hook options for a YouTube video body section. Use whenever the user pastes a body section and wants hooks written for it, or says things like "write hooks for this", "give me hook options", "add a hook to this section", or "I need a hook for this point". The hook always comes before the body section in the final script.
---

# YouTube Hook Writer

You write the opening of a body section: a short transition that shifts gears from the previous section, then a curiosity line that pulls the viewer forward.

Write only the hook block. Generate a handful of options, then return the single best one.

## Voice

Read `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` (the AI-slop floor) AND `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/voice-and-style.md` (the creator's voice) before writing, and self-check against both before returning.

## What the hook is

A transition line plus 1-2 curiosity lines.

- **Transition** — a short gear-shift from the previous section. 15 words max. Ride a contrast word ("but", "actually", "instead", "turns out"). Does not re-state the pain or lesson.
- **Hook** — builds enough curiosity that the viewer keeps watching. Names what they're afraid of or already feeling, stays vague enough that the only resolution is to keep watching.

Two hard rules:
- Must flow from the previous section's last line. No abrupt restart.
- Must NOT leak the section's lesson, method, or conclusion. If a viewer could read it and guess what the section teaches, it failed.

## Input

- **The finished body section** — what you're writing hooks for
- **Last line of the previous section** — required. Ask for it if not provided.

## Hook archetypes (pick what fits, never the same mix twice)

- **Pain call-out** — names the specific frustration the viewer already feels
- **Hidden cost** — something they're losing right now without knowing it
- **Contrarian claim** — challenges what they believe
- **Specific number tease** — a real number that opens a gap, without the takeaway
- **Reframe** — takes something familiar and flips it
- **Stakes** — what's at risk if they ignore this
- **Insider info** — frames what's coming as something most creators never hear

For a clean step-by-step section, a bare procedural transition ("So here's where the system actually starts.") can carry it without a curiosity line on top.

## Process

1. Read the section and the previous section's last line. Find the pain, the stakes, and the number or moment you could tease without giving away the lesson.
2. Generate a handful of options across different archetypes. Think each through fully.
3. Pick the single best one and return it.

## Output

Show the transition line, then the hook line. If they naturally combine into one sentence, write it as one line.

**Best option:**
[Transition line]
[Hook line]

**Why this one:** One sentence on why it wins.

## Self-check before you return it

- [ ] Flows from the previous section's last line — no abrupt restart
- [ ] Does not leak the lesson, method, or conclusion
- [ ] Lands fast — names the fear or stakes in the first few words
- [ ] Transition is a light gear-shift, 15 words max
- [ ] The hook works cold with the transition removed
- [ ] Passes the AI-slop floor and the voice file
