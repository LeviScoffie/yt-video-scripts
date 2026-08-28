---
name: youtube-miro-visuals
description: Create Miro board visuals for a YouTube script. Use this skill whenever the user pastes a finished script and asks to create a Miro board, add visuals to Miro, or make diagrams for their video. Trigger when they say things like "create a Miro board for this", "add this to Miro", "make visuals for this script", or "create diagrams for each point". Reads the full script, identifies each numbered point, and creates one visual per point on the Miro board. Skips CTAs, intros, and endscreens.
---

# YouTube Miro Visuals

Reads a finished YouTube script and creates one Miro visual per numbered point. Each visual is designed to be shown on screen during recording — clean, readable, no internal notes or scripting language.

## Inputs Required

- **Full script** — pasted by the user
- **Miro board URL** — ask before starting if not provided

## The Process

### Step 1 — Explore the board

Call `context_explore` on the Miro board URL to see what's already there and find a clear placement area.

Placement rules:
- Place visuals in a horizontal row, spaced 2000 units apart on the X axis
- Find the lowest Y coordinate of existing content, add 3000 units for the new row's Y position
- If the board is empty, start at x=0, y=0

### Step 2 — Read the DSL format

Call `diagram_get_dsl` with type `flowchart` once before creating any diagrams. Reuse the spec for all diagrams in the session.

### Step 3 — Identify numbered points

Scan for sections labeled "Point 1", "Point 2", etc. Extract each one. Ignore everything else.

### Step 4 — Choose the format for each point

**Use a flowchart** when the point contains:
- A process, sequence of steps, or system
- A before/after or cause/effect relationship
- A decision or branching outcome
- Data, stats, or comparisons that can be visualised

**Use a doc card** when the point contains:
- A story or anecdote with no process flow
- A quote or dialogue exchange
- A concept or mindset shift with no steps
- Content where a visual flow would feel forced

When in doubt, use a flowchart — it's more visually engaging on screen.

**Flowchart direction:**
- LR (left-to-right) for process sequences and step-by-step flows
- TB (top-to-bottom) for before/after comparisons and hierarchies

### Step 5 — Create the visuals

**Flowchart rules:**
- Node labels: 5 words max
- Use clusters for related stages
- Red nodes (#ffc6c6) — pain points, friction, things going wrong
- Green nodes (#adf0c7) — start, end, positive outcomes
- Yellow nodes (#fff6b6) — neutral process steps
- Blue nodes (#c6dcff) — decisions
- Title: describes what the diagram shows, not what the point is called

**Doc card rules:**
- Use markdown headings for structure
- Bold the key lines or contrasting elements
- Scannable — the viewer is watching a video, not reading
- Max 150 words
- Title: describes what's being shown

## Image Placeholders

When the script references a screenshot, photo, or dashboard, create a placeholder doc card at the correct position in the row:

```
# [IMAGE PLACEHOLDER]

**What to show:** [description of the image needed]

**Source:** [where to find it — e.g. "Screen record: YouTube analytics dashboard"]
```

- Place the placeholder in sequence with other visuals for that point
- If the script has a `[Screen: ...]` tag, treat it as a placeholder to create
- Never skip a screenshot reference

## What To Skip

- Intro section
- Any section labeled "Midroll CTA", "CTA", or "Endscreen"
- Anything that isn't a numbered point

## Output

After creating all visuals, tell the user:
- How many visuals were created
- Format (flowchart or doc card) and reason for each
- The Miro board URL

One line per point is enough.

## Quality Check

- [ ] Board explored — placement chosen to avoid overlaps
- [ ] DSL format loaded before first diagram
- [ ] Only numbered points visualised
- [ ] Format choice fits the content, not defaulted
- [ ] Node labels short and readable on screen
- [ ] Colors used correctly
- [ ] Titles describe what's shown, not just "Point 1"
- [ ] Consistent spacing across the row
- [ ] All `[Screen: ...]` tags have placeholder cards

## Notes

- Keep everything clean and readable at a glance — no jargon, no script notes, nothing that would look odd on camera
- If a point is very short or vague, use a doc card rather than forcing a diagram
- Never create a visual for a CTA section
- When cataloguing items on the board (e.g. an image library), use one master index doc instead of individual label cards next to each item — individual cards can't be precisely positioned and will overlap
