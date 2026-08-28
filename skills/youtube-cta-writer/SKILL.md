---
name: youtube-cta-writer
description: Write YouTube midroll and endscreen CTAs from a finished script. Use this skill when the user pastes a finished script and wants CTAs written, or says things like "do the CTAs", "write a CTA", "midroll CTA", "endscreen", or "send them to my offer".
---

# YouTube CTA Writer

Reads a finished YouTube script and outputs all CTAs in one pass. Every CTA follows the same core pattern:

**Transition → New Problem → Go Here To Solve It**

## Voice

Read `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` (the AI-slop floor) AND `/Users/leviscoffie/Desktop/yt-skills/skills/_shared/voice-and-style.md` (the creator's voice) before writing, and self-check against both before returning.

## Input

The user pastes their full script. Before starting, confirm:
- **Your offer(s)** — what you're promoting (free lead magnet, paid offer, affiliate link). The user supplies these — never assume or invent offer details.
- **Next video title** — needed for the endscreen CTA.

If offer details aren't in the message or project context, ask for them before writing.

## Placement logic

1. Count the points in the script.
2. Decide midroll count:
   - 1-8 points: 2 midroll CTAs
   - 9+ points: 3 midroll CTAs (only if a third offer exists)
3. Calculate positions:
   - 2 CTAs: CTA 1 after Point 1 / CTA 2 after the point closest to 65%
   - 3 CTAs: CTA 1 after Point 1 / CTA 2 near 50% / CTA 3 near 75%
4. Check for context-aware overrides: if a point directly connects to a specific offer, move that CTA to sit after it. Flag the override and explain why.
5. Always add the endscreen last.

## CTA types

### Midroll
Write 2 variations per placement. User picks one.
- **Lead magnet** — free offer (guide, checklist, email course). Low friction — viewer is still mid-video.
- **Paid offer** — paid product, community, or affiliate. Slightly stronger pull, still no hard sell.

### Endscreen
Always the last thing in the video. Sends to another video. One version, no variations.

Always exactly four lines:
1. Close the loop on what they just learned
2. Name the next problem they now have
3. Send them to the next video
4. Always end with: "I'll put the video up on the screen for you to watch next."

## Output

**CTA [#] — [Offer type] — Goes after Point [X]**

Variation A:
[CTA copy]

Variation B:
[CTA copy]

Why this placement: [One sentence — especially if it's a context-aware override]

---

**Endscreen — Goes at the end of the video**
[Four-line CTA]

## Self-check before you return it

**Midroll:**
- [ ] Transition connects directly to the previous point — not a generic "if you enjoyed this"
- [ ] New problem is the natural next question after that point
- [ ] Destination clear in 1-2 sentences
- [ ] 40-70 words
- [ ] Doesn't sound like an ad

**Endscreen:**
- [ ] Exactly four lines
- [ ] Line 4 is exactly: "I'll put the video up on the screen for you to watch next."
- [ ] No filler
- [ ] 20-40 words

**Both:**
- [ ] Passes the AI-slop floor and the voice file
