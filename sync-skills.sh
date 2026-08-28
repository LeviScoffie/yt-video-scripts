#!/bin/bash
# Keeps video-scripts/.claude/skills/ in sync with yt-skills/skills/.
# Adds a symlink for any new skill folder; flags symlinks whose source skill was removed.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
TARGET_DIR="$HOME/Desktop/video-scripts/.claude/skills"

mkdir -p "$TARGET_DIR"

added=0
for src in "$SKILLS_SRC"/*/; do
  name="$(basename "$src")"
  [ "$name" = "_shared" ] && continue
  link="$TARGET_DIR/$name"
  if [ ! -e "$link" ] && [ ! -L "$link" ]; then
    ln -s "../../../yt-skills/skills/$name" "$link"
    echo "linked: $name"
    added=$((added + 1))
  fi
done

stale=0
for link in "$TARGET_DIR"/*/; do
  name="$(basename "$link")"
  if [ -L "${link%/}" ] && [ ! -e "$link" ]; then
    echo "warning: stale symlink for removed skill '$name' — remove manually with: rm '$TARGET_DIR/$name'"
    stale=$((stale + 1))
  fi
done

if [ "$added" -eq 0 ] && [ "$stale" -eq 0 ]; then
  echo "skills already in sync"
fi
