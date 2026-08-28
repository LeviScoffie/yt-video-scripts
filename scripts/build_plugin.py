"""Build and validate the distributable yt-skills plugin archive."""

from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
DIST = ROOT / "dist"
SKILLS_ROOT = ROOT / "skills"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate without keeping build output")
    return parser.parse_args()


def skill_dirs() -> list[Path]:
    return sorted(p for p in SKILLS_ROOT.iterdir() if p.is_dir() and p.name != "_shared")


def validate_source(manifest: dict) -> None:
    required = ("name", "version", "description", "author")
    missing = [key for key in required if not manifest.get(key)]
    if missing:
        raise SystemExit(f"Missing manifest fields: {', '.join(missing)}")

    if not SKILLS_ROOT.is_dir():
        raise SystemExit(f"Missing skills directory: {SKILLS_ROOT.relative_to(ROOT)}")

    for skill_dir in skill_dirs():
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            raise SystemExit(f"Missing SKILL.md for skill: {skill_dir.relative_to(ROOT)}")


def build_plugin(manifest: dict) -> tuple[Path, Path]:
    plugin_root = DIST / "yt-skills"
    if plugin_root.exists():
        shutil.rmtree(plugin_root)

    (plugin_root / ".claude-plugin").mkdir(parents=True)
    shutil.copy2(MANIFEST, plugin_root / ".claude-plugin" / "plugin.json")

    shutil.copytree(SKILLS_ROOT, plugin_root / "skills")

    readme = ROOT / "README.md"
    if readme.is_file():
        shutil.copy2(readme, plugin_root / "README.md")

    archive = DIST / f"yt-skills-plugin-{manifest['version']}.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for path in sorted(plugin_root.rglob("*")):
            if path.is_file():
                output.write(path, path.relative_to(DIST))

    return plugin_root, archive


def validate_build(plugin_root: Path, archive: Path) -> None:
    for skill_dir in skill_dirs():
        source_skill_md = skill_dir / "SKILL.md"
        packaged_skill_md = plugin_root / "skills" / skill_dir.name / "SKILL.md"
        if not packaged_skill_md.is_file():
            raise SystemExit(f"Packaged skill missing SKILL.md: {skill_dir.name}")
        if packaged_skill_md.read_bytes() != source_skill_md.read_bytes():
            raise SystemExit(f"Packaged SKILL.md does not match the canonical file: {skill_dir.name}")

    packaged_manifest = plugin_root / ".claude-plugin" / "plugin.json"
    if packaged_manifest.read_bytes() != MANIFEST.read_bytes():
        raise SystemExit("Packaged plugin.json does not match the canonical file")

    if not zipfile.is_zipfile(archive):
        raise SystemExit("Plugin archive is not a valid ZIP file")


def main() -> None:
    args = parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    validate_source(manifest)
    plugin_root, archive = build_plugin(manifest)
    validate_build(plugin_root, archive)
    print(f"Built {archive.relative_to(ROOT)}")
    if args.check:
        shutil.rmtree(plugin_root)
        archive.unlink()
        try:
            DIST.rmdir()
        except OSError:
            pass


if __name__ == "__main__":
    main()
