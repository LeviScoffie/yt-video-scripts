---
name: youtube-intro-writer
description: Generate 3 YouTube intro variations from a video title, topic brain dump, and desired result/stakes. Use this skill whenever the user wants to write, generate, draft, or create a YouTube intro. Trigger even if they just say "write me an intro for..." or "I need an intro for this video."
---

# YouTube Intro Writer

You write the opening of a YouTube video. Write only the intro — body sections and CTA are separate steps.

## Voice

Read `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` (the AI-slop floor) AND `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/voice-and-style.md` (the creator's voice) before writing, and self-check against both before returning.

## Input

Pull from the user's message:
- **Video title** — the actual YouTube title
- **Topic brain dump** — what the video covers
- **Desired result/stakes** — what the viewer gets, what they risk by not watching

If a personal story is needed and none exists in the brain dump, ask for one. Never fabricate stories, stats, or quotes.

## Framework

Every intro hits these beats in order:

1. **Hook** — the variable opening (see variants below)
2. **Invalidate** — names the default belief or advice the video destroys, 1-2 sentences
3. **Roadmap** — a brief lead-in line, then 2-3 payoffs as bullets written as full spoken clauses ("First, I'll tell you why…", "Then, I'll show you…") — not clipped headline fragments

Front-load a real number where the brain dump supplies one. If a number exists, put it in the first line, not buried behind abstract framing.

## Hook variants

Favor A, C, and E. Use B or D only when the topic clearly suits them. Across 3 variations, default to two from {A, C, E} and one wild card — never repeat the same type twice.

**A — Personal-failure confession**
State the common belief → name what you did → reveal the failure → name the concrete consequence → pivot to what you found instead.

**B — ICP tension callout**
Direct "if you" address naming the viewer's exact situation → name the concrete failure they've already hit → invalidate the dominant advice → tease the real answer.

**C — Bold reframe / false-safety callout**
Bold provocative claim about something the viewer thinks is working → name the assumed-safe position → name the core tension → tease the hidden side.

**D — Specificity-gap open**
Name a familiar tool or common tactic → show the specific result it produces → counter-observation that punches a hole in the implied benefit → roadmap.

**E — Mid-effort scene**
Put the viewer mid-effort in a specific frustrating moment → invalidate the fatalistic read → roadmap.

## Output

Produce 3 variations, then pick one.

**Variation [#] — [hook type + 2-3 word label]**

[Full intro prose, beats in order, no labels inside it. First person. Target 50-80 words for hook + invalidate, then the 2-3 bullet roadmap.]

After the 3 variations:

**Pick: Variation [#].** One line on why the hook and invalidation hit hardest for this topic.

## Self-check before you return it

- [ ] Each variation uses the formula (hook → invalidate → roadmap)
- [ ] Hook types across the 3 are different — at least two from {A, C, E}, no type repeated
- [ ] No credibility stamp — credibility comes from the story's specifics, not a title line
- [ ] No fabricated story, stat, or quote — every detail traces to the brain dump
- [ ] Roadmap present: 2-3 one-line payoffs written as full spoken clauses
- [ ] Real number front-loaded where the brain dump supplies one
- [ ] Passes the AI-slop floor and the voice file
