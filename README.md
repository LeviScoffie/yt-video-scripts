# yt-video-scripts

Claude Code skills for writing and QC-ing YouTube video scripts, end to end: outline → intro → body sections (hook + content) → CTAs → chapter titles → Miro visuals.

## Structure

```
SKILLS/
  _shared/                        cross-skill reference files
    ai-slop-ban-list/ai-slop-ban-list.md   banned AI-sounding phrases/patterns (TODO)
    voice-and-style.md                     channel voice & vocabulary (TODO)
  <skill-name>/
    SKILL.md                      the skill itself (frontmatter + instructions)
    references/TODO.md            source docs, examples, style guides (fill in as needed)
    assets/TODO.md                 templates, sample outputs (fill in as needed)
```

Each `SKILL.md` follows the [Claude Code skill format](https://docs.claude.com/en/docs/claude-code) — YAML frontmatter (`name`, `description`) plus instructions. Drop the whole `SKILLS/` folder (or individual skill folders) into a project's `.claude/skills/` directory to use them, or point Claude at this repo directly.

## Skills

| Skill | Stage | What it does |
|---|---|---|
| [youtube-outline-qc](SKILLS/youtube-outline-qc/SKILL.md) | QC | Reviews and fixes structural issues in a video outline. Run right after the outline is written. |
| [youtube-intro-writer](SKILLS/youtube-intro-writer/SKILL.md) | Write | Generates 3 intro variations from a title, topic brain dump, and stakes/result. |
| [youtube-intro-qc](SKILLS/youtube-intro-qc/SKILL.md) | QC | Reviews and fixes a written intro. Run right after the intro is written. |
| [youtube-hook-writer](SKILLS/youtube-hook-writer/SKILL.md) | Write | Writes the hook (transition + curiosity line) that opens each body section. |
| [youtube-hook-qc](SKILLS/youtube-hook-qc/SKILL.md) | QC | Reviews and fixes a written hook against the body section it leads into. |
| [youtube-body-section](SKILLS/youtube-body-section/SKILL.md) | Write | Turns a raw brain dump into a full body section / script point. |
| [youtube-cta-writer](SKILLS/youtube-cta-writer/SKILL.md) | Write | Writes midroll and endscreen CTAs from a finished script. |
| [youtube-chapter-titles](SKILLS/youtube-chapter-titles/SKILL.md) | Write | Generates one chapter/timestamp title per section of a finished script. |
| [youtube-title-writer](SKILLS/youtube-title-writer/SKILL.md) | Write | Generates 30+ video title options, researched against outlier titles in adjacent niches. |
| [youtube-miro-visuals](SKILLS/youtube-miro-visuals/SKILL.md) | Produce | Creates one Miro board visual per numbered point in a finished script. |

## Setup

Two shared files are referenced by most of the writer/QC skills and are currently placeholders — fill them in before relying on those skills:

- `SKILLS/_shared/ai-slop-ban-list/ai-slop-ban-list.md`
- `SKILLS/_shared/voice-and-style.md`

Every skill's `references/` and `assets/` subfolders are also placeholders (`TODO.md`) — add supporting material there as needed.
