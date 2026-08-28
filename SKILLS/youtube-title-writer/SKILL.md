---
name: youtube-title-writer
description: Generate 30+ YouTube title options from a video topic. Use this skill whenever the user wants to write, generate, or brainstorm YouTube titles. Trigger when they say things like "write titles for", "give me title options", "YouTube title", "title ideas", or just give a video topic and ask for titles. Researches outlier titles from adjacent niches using the YouTube Data API (or web search fallback), reverse engineers the frameworks, and generates 30+ titles across three audience modes. Under 67 characters, capitalization matches the channel's existing convention.
---

# YouTube Title Writer

Generates 30+ title options from a video topic. Mines outlier videos from adjacent niches for proven title structures, then applies those structures to this channel's topic space across three audience modes.

## API Key

Use `$YOUTUBE_API_KEY`. Base URL: `https://www.googleapis.com/youtube/v3`

If unavailable, fall back to web search — find top-performing titles per niche manually and estimate their outlier status from visible view counts. Jump to Step 5.

## What a Title Must Do

Every title has two jobs:
1. Make clear who this is for
2. Make clear what they get or avoid

These don't always need to be stated explicitly. Sometimes the outcome implies the audience.

## Three Audience Modes

Use all three across the 30+ titles.

**Mode 1 — Explicit:** Names the audience directly.
> "How coaches write YouTube scripts that actually get clients"

**Mode 2 — Implied:** Outcome makes the audience obvious without naming them.
> "How to write YouTube scripts that get you clients"

**Mode 3 — Broad Reach:** No audience signal. Hooks on universal value.
> "How to write a YouTube script in under 1 hour"

## The Process

### Step 1 — Choose 6 niches for framework mining

Pick 2 from each category — go wide deliberately, the goal is proven structures not relevant content:

**Far-adjacent:** cooking/recipes, fitness, relationships/dating, gaming, travel, parenting

**Mid-adjacent:** personal finance, fitness performance, career/job hunting, real estate

**Close-adjacent:** paid traffic/ads, email marketing/copywriting, sales, productivity/systems

### Step 2 — Search each niche for outlier videos

```bash
curl -s "https://www.googleapis.com/youtube/v3/search?part=snippet&q=[QUERY]&type=video&videoDuration=medium&order=viewCount&maxResults=10&key=$YOUTUBE_API_KEY"
```

`videoDuration=medium` filters out Shorts (4–20 min only). Collect video IDs and titles from each result.

### Step 3 — Get view counts

```bash
curl -s "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=[VIDEO_ID_1,VIDEO_ID_2,...]&key=$YOUTUBE_API_KEY"
```

### Step 4 — Get subscriber counts

Collect `channelId` from search results, then:

```bash
curl -s "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=[CHANNEL_ID_1,CHANNEL_ID_2,...]&key=$YOUTUBE_API_KEY"
```

### Step 5 — Score for outliers

```
ratio = viewCount / subscriberCount
```

- Ratio > 10 = strong outlier
- Ratio 3–10 = solid outlier
- Ratio 1–3 = average
- Ratio < 1 = skip

Keep only ratio > 3.

### Step 6 — Mine outlier channels for more titles

From channels scoring > 3, fetch their uploads playlist and score their top 50 videos the same way. Add any new ratio > 3 videos to the pool.

```bash
# Get uploads playlist ID
curl -s "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=[CHANNEL_ID]&key=$YOUTUBE_API_KEY"

# Fetch top 50
curl -s "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=[UPLOADS_PLAYLIST_ID]&maxResults=50&key=$YOUTUBE_API_KEY"
```

### Step 7 — Extract title frameworks

Strip each outlier title down to its bare structure:

- "I tried every Facebook ad format so you don't have to" → `I tried every [X] so you don't have to`
- "The email sequence that made me $40K in 7 days" → `The [X] that made me $[Y] in [timeframe]`
- "Why your sales calls keep failing (and the real fix)" → `Why your [X] keeps failing (and the real fix)`

Collect 8–12 frameworks.

### Step 8 — Research niche keyword vocabulary

Search the target niche and extract from top titles:

- **Concept words:** how does this niche name its core ideas? ("system" vs "framework" vs "process")
- **Audience words:** what does this niche call its people? ("clients" vs "customers")
- **Action words:** how does it describe results? ("get clients" vs "sign clients")

Read `../_shared/voice-and-style.md` if available — it holds the channel's exact vocabulary and audience labels.

### Step 9 — Generate 30+ titles

**Framework adherence is the most important step.** Each title must be a direct structural application of one extracted framework — not "inspired by" it.

Correct:
- Framework: `I tried every [X] so you don't have to`
- Title: `I tried every client retention system so you don't have to`

Incorrect:
- Framework: `I tried every [X] so you don't have to`
- Title: `Why most retention systems don't work` ← different structure entirely

Every title must map 1:1 to a framework. If it can't, cut it.

**Title rules:**
- Match the channel's existing capitalization style consistently across all 30+
- 67 characters max — count carefully
- No generic phrasing: "ultimate guide", "complete breakdown", "everything you need to know"
- Specific and real, not AI-generated
- Aim for 10+ titles per mode

## Output Format

**Outlier frameworks found:**
List 8–12 frameworks with the original title and ratio score for each.

---

Then titles grouped by mode:

### Mode 1 — Explicit
**1.** [title]
Framework: [which one]
Why: [one sentence]

### Mode 2 — Implied
...

### Mode 3 — Broad Reach
...

## Quality Check

- [ ] Real frameworks extracted from scored outliers — not invented
- [ ] Capitalization style consistent across all titles
- [ ] All titles 67 characters or under
- [ ] 10+ titles per mode
- [ ] No two titles are just word swaps of each other
- [ ] None sound generic or AI-written
- [ ] All match what the video is actually about
- [ ] Every title maps 1:1 to an extracted framework
- [ ] Titles use the channel's actual audience vocabulary (check ../_shared/voice-and-style.md if available)
