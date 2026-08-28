# yt-video-scripts

A Claude Code plugin: skills for writing and QC-ing YouTube video scripts, end to end — outline → intro → body sections (hook + content) → CTAs → chapter titles → Miro visuals.

## Structure

```
.claude-plugin/
  plugin.json                     plugin manifest
skills/
  _shared/                        cross-skill reference files
    ai-slop-ban-list/ai-slop-ban-list.md   banned AI-sounding phrases/patterns
    voice-and-style.md                     channel voice & vocabulary
  <skill-name>/
    SKILL.md                      the skill itself (frontmatter + instructions)
    references/TODO.md            source docs, examples, style guides (fill in as needed)
    assets/TODO.md                templates, sample outputs (fill in as needed)
scripts/
  build_plugin.py                 validates and packages the plugin into dist/
```

Each `SKILL.md` follows the [Claude Code skill format](https://docs.claude.com/en/docs/claude-code) — YAML frontmatter (`name`, `description`) plus instructions. Install this as a plugin, or drop the `skills/` folder (or individual skill folders) into a project's `.claude/skills/` directory to use them directly.

## Skills

| Skill | Stage | What it does |
|---|---|---|
| [youtube-outline-qc](skills/youtube-outline-qc/SKILL.md) | QC | Reviews and fixes structural issues in a video outline. Run right after the outline is written. |
| [youtube-intro-writer](skills/youtube-intro-writer/SKILL.md) | Write | Generates 3 intro variations from a title, topic brain dump, and stakes/result. |
| [youtube-intro-qc](skills/youtube-intro-qc/SKILL.md) | QC | Reviews and fixes a written intro. Run right after the intro is written. |
| [youtube-hook-writer](skills/youtube-hook-writer/SKILL.md) | Write | Writes the hook (transition + curiosity line) that opens each body section. |
| [youtube-hook-qc](skills/youtube-hook-qc/SKILL.md) | QC | Reviews and fixes a written hook against the body section it leads into. |
| [youtube-body-section](skills/youtube-body-section/SKILL.md) | Write | Turns a raw brain dump into a full body section / script point. |
| [youtube-cta-writer](skills/youtube-cta-writer/SKILL.md) | Write | Writes midroll and endscreen CTAs from a finished script. |
| [youtube-chapter-titles](skills/youtube-chapter-titles/SKILL.md) | Write | Generates one chapter/timestamp title per section of a finished script. |
| [youtube-title-writer](skills/youtube-title-writer/SKILL.md) | Write | Generates 30+ video title options, researched against outlier titles in adjacent niches. |
| [youtube-miro-visuals](skills/youtube-miro-visuals/SKILL.md) | Produce | Creates one Miro board visual per numbered point in a finished script. |

## Shared reference files

Most of the writer/QC skills read two shared files for consistent voice and quality:

- `skills/_shared/ai-slop-ban-list/ai-slop-ban-list.md` — banned AI-sounding phrases and patterns
- `skills/_shared/voice-and-style.md` — the channel's voice, rhythm, and vocabulary

Every skill's `references/` and `assets/` subfolders are placeholders (`TODO.md`) — add supporting material there as needed.

## Building the plugin

```
python3 scripts/build_plugin.py
```

Validates the manifest and every skill's `SKILL.md`, then packages `.claude-plugin/`, `skills/`, and `README.md` into `dist/yt-skills-plugin-<version>.zip`. Use `--check` to validate and build without keeping the output.
