---
name: youtube-chapter-titles
description: Generate chapter titles for each section of a YouTube script. Use this skill whenever the user pastes a full script and wants chapter titles, section titles, or timestamp labels written. Trigger when they say things like "chapter titles for this script", "title each section", "write chapter markers", "give me titles for each point", or paste a script and ask for titles per section. Reads the full script, identifies each section, and writes one curiosity-building title per section — matching the channel's capitalization style, never revealing the payoff.
---

# YouTube Chapter Titles

Reads a full YouTube script and writes one chapter title per section.

Each title teases the benefit or pain without giving away the lesson. The viewer should want to watch that section, not feel like they already know what it says.

## Inputs Required

- **Full script** — pasted by the user, with sections labelled or clearly separated by topic

Pull from project context if available:
- **Target audience** — calibrates the language and pain points
- **Channel niche** — shapes what "benefit" and "pain" mean here

## The Process

### Step 1 — Map the script

Identify each distinct section. For each one, note:
- What it's actually about (the real lesson or payoff)
- What pain or desire it connects to for the viewer
- What the opening line of that section sets up

### Step 2 — Write one title per section

Each title should:
- Tease the benefit the viewer wants OR the pain they want to escape
- Not give away the answer, lesson, or framework name
- Create a reason to keep watching
- Sound like something a real person would say

The section's opening line usually signals the right angle. Start there.

If `../_shared/voice-and-style.md` is available, check it for the channel's vocabulary before writing — chapter titles should use the same words the audience uses, not generic substitutes.

### Step 3 — Apply title rules

- Match the channel's existing capitalization style consistently across all titles
- 5 to 8 words, 50 characters max
- No clickbait unrelated to the section
- No generic phrases like "the key insight" or "important lesson"
- No framework names or answers in the title — save those for inside the section
- Intriguing, not spoilery — like a chapter title in a good book

## Output Format

**1.** [chapter title]
**2.** [chapter title]
**3.** [chapter title]

No extra explanation unless the user asks why a specific title was written a certain way.

## Quality Check

- [ ] One title per section, numbered to match
- [ ] Capitalization consistent across all titles
- [ ] None give away the main lesson or framework name
- [ ] Each creates curiosity or references a real pain/benefit
- [ ] No two titles use the same angle
- [ ] None sound AI-written

## Notes

- If sections aren't labelled, use topic shifts or natural breaks to identify them
- CTA sections don't need chapter titles — skip them unless the user asks
- The best chapter title makes the viewer think "I need to know what this means" — not "I already know what this is about"
