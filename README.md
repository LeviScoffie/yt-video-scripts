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
commands/
  <skill-name>.md                 one slash command per skill, for direct invocation
scripts/
  build_plugin.py                 validates and packages the plugin into dist/
```

Each `SKILL.md` follows the [Claude Code skill format](https://docs.claude.com/en/docs/claude-code) — YAML frontmatter (`name`, `description`) plus instructions. Install this as a plugin, or drop the `skills/` folder (or individual skill folders) into a project's `.claude/skills/` directory to use them directly.

## Two ways to use these skills

Both paths load the same `SKILL.md` files and both auto-trigger by matching a message against a skill's `description` — no explicit invocation needed either way. They differ in *how* they're activated, and that difference matters for anything that reads another file (like the `_shared/` references below).

| | Symlink into `.claude/skills/` | Plugin (`--plugin-dir` or installed) |
|---|---|---|
| Activation | Automatic — Claude Code discovers `.claude/skills/` by walking up from wherever you're working | Explicit — needs `--plugin-dir`, or a proper install via a marketplace |
| Scope | Only active inside the project tree containing that `.claude/skills/` folder | Active for the whole session, regardless of directory |
| Direct invocation | Bare skill name only, no slash command | Namespaced slash commands (`/yt-skills:youtube-hook-writer`) |
| `${CLAUDE_PLUGIN_ROOT}` | Doesn't expand — not recognized as a "real" plugin load | Expands correctly |
| Reading files via symlinks | Fragile — Claude Code's `Read` tool normalizes `../` lexically rather than following the symlink physically, so a relative path through a symlinked skill folder can silently fail even though it resolves fine in a shell (`ls`/`realpath`) | Not applicable — no symlink hop, files are read straight from the plugin's own directory |

This repo is used both ways: symlinked into `~/Desktop/video-scripts/.claude/skills/` for day-to-day auto-triggered writing, and loadable as a plugin (`claude --plugin-dir`) for direct slash-command invocation or testing. The symlink path is why the shared-file references below use a hardcoded absolute path instead of a relative one — see that section for the full story.

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

**These are referenced by hardcoded absolute path** (`/Users/leviscoffie/Desktop/yt-skills/skills/_shared/...`) inside each skill's `SKILL.md`, not a relative path. This was a deliberate fix, not an oversight: skills used here are loaded two ways — as symlinks in a project's `.claude/skills/` (the day-to-day `video-scripts` workflow) and as an installed plugin. Claude Code's `Read` tool normalizes `../` lexically rather than following symlinks physically, so a relative path or `${CLAUDE_SKILL_DIR}`-based path silently breaks under the symlinked setup, even though it looks fine to `ls`/`realpath` in a shell. `${CLAUDE_PLUGIN_ROOT}` doesn't help either — it's substituted only when a plugin is loaded via the actual plugin mechanism, not for skills reached through a `.claude/skills/` symlink. A hardcoded absolute path is the only thing that works identically in both contexts.

**If this repo is ever moved or installed on a different machine**, every hardcoded path needs updating — the two shared-file references appear across all 9 skills that use them (`grep -rn '_shared' skills/*/SKILL.md`).

Every skill's `references/` and `assets/` subfolders are placeholders (`TODO.md`) — add supporting material there as needed.

## Direct invocation

Every skill also auto-triggers by description (e.g. asking to "write hooks for this section"). If Claude picks the wrong skill or you want to be explicit, call it directly with the matching slash command: `/yt-skills:youtube-hook-writer`, `/yt-skills:youtube-outline-qc`, etc. — one command per skill, same names, under `commands/`.

## Building the plugin

```
python3 scripts/build_plugin.py
```

Validates the manifest and every skill's `SKILL.md`, then packages `.claude-plugin/`, `skills/`, and `README.md` into `dist/yt-skills-plugin-<version>.zip`. Use `--check` to validate and build without keeping the output.
