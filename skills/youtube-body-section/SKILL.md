---
name: youtube-body-section
description: Write a single YouTube main body section from a brain dump. Use this skill whenever the user wants to write, draft, or build out a body section, point, or segment of a YouTube video script. Trigger when they say things like "write this section", "turn this into a script point", "help me write this part", or paste raw notes about a concept they want to cover.
---

# YouTube Body Section Writer

Writes individual YouTube video body sections from a brain dump. Draft first, explain choices, then refine based on feedback.

Each section must work as a standalone short or clip when the transition words are removed from the hook.

## Voice

Read `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` (the AI-slop floor) AND `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/voice-and-style.md` (the creator's voice) before writing, and self-check against both before returning.

## Input

Pull from the user's message:
- **Brain dump** — raw notes, ideas, examples, stories, or points to cover
- **Section goal** — what the viewer walks away knowing or feeling (infer from brain dump if not stated)

If the brain dump is too thin to work with, ask one focused question before drafting.

## Section structure

Every section follows: **Hook → Content → Payoff**

### Hook
One sentence. Sells the benefit or result of what's coming — never the mechanism or lesson. Must work cold with transition words removed (transition words like "So," "But first," carry continuity inside the video but the core hook stands alone).

Strong hook angles:
- Specific number or result that teases the story behind it
- Calls out the exact viewer with a specific pain or goal
- Teases a method or story without naming what it is

### Content formats — pick the best fit
- **Story** — personal experience or before/after that makes the point feel real. Structure: Setup → Conflict/tension → Resolution → Lesson
- **Analogy** — for abstract concepts that need a mental shortcut. Structure: Introduce analogy → Draw the parallel → Make it concrete
- **Framework** — repeatable process or steps the viewer can apply. Structure: Name it → Walk each part with one example → Show the end result
- **Combo** — when one format alone doesn't land the point (Story + Framework is most common)

**Let the problem breathe.** When the section is built around a problem, spend time inside it before pivoting to the solution. The problem should take at least as much space as the fix.

### Payoff
Last 1-2 lines. Lands the lesson cleanly OR leaves an open loop. Never summarizes the whole section. Never pushes to the next section — that's the hook writer's job.

## Output

Produce 2 variations. For each:

**Variation [#] — [format used]**
[Voice: passed] or [Voice: fixed — <what changed>]

[Section copy. 200 words max, 300 absolute max. First person, brand voice.]

**Why this works:** Format choice, hook approach, and any key copywriting elements — one sentence each.

After both variations, ask: "Which direction do you want to go, or is there something you want to change?"

## Self-check before you return it (REQUIRED)

Run this on the actual drafted text for each variation — not from memory — before including it in the output.

- [ ] Hook sells the result, not the mechanism or lesson
- [ ] Hook works cold with transition words removed
- [ ] Format fits the content, not just the default
- [ ] Problem gets as much space as the fix
- [ ] Real numbers or specific details used
- [ ] Payoff closes the loop without restating the whole section
- [ ] 200 words max (300 absolute)
- [ ] Output includes both variations, each with a `**Variation [#] — [format]**` header, a `[Voice: ...]` line, and a "Why this works" line, followed by the closing question

**Anti-slop and voice pass (REQUIRED):**
Re-read `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` and `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/voice-and-style.md`, then run the two-pass scan the ban-list file itself defines — don't just skim it:

- **Pass 1 (Tier A — zero exceptions):** scan the drafted section for every §1 rhetorical pattern, §2 formulaic opener, §3 formulaic closer. Check specifically for the patterns that slip through most often: negative parallelism ("it's not X, it's Y" in any form), anaphora, decorative lists, patronising analogy, phantom-future projection, false suspense transitions ("Here's the thing," "Here's why that matters," "Here's what changed," etc.), and triple-countdown constructions ("Not X. Not Y. Just Z."). Rewrite any match — zero instances allowed, "only used once" is not an exception.
- **Pass 2 (Tier B — avoid clustering):** scan for clustering of §4 vocabulary, §5 structural patterns, §6 formatting tics (including em-dash overuse). Rewrite if clustered.

Set the variation's `[Voice: ...]` line to `[Voice: passed]` only if both passes are clean. Otherwise `[Voice: fixed — <one-line summary>]` and make sure the fix is reflected in the copy you return.
