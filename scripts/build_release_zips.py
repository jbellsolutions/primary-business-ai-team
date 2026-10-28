#!/usr/bin/env python3
"""Build the one-click setup downloads into dist/. They are attached to the GitHub release, never committed.

Run from the repo root:  python3 scripts/build_release_zips.py
Then upload them:        gh release upload setup dist/*.zip --clobber
Re-run it after scripts/build_desks.py whenever a desk changes. The install guides link to
releases/latest/download/<name>.zip, so keep these names the same.

  AI-Team-folder.zip        the OneDrive "AI Team" starter folder, with the starter SOPs in AI Team/sops/
  NN-<desk>.zip             everything to drag into that desk's ChatGPT project Files
  NN-<desk>-compact.zip     the same desk in fewer files, for plans with a lower file limit
"""
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKIP = {".DS_Store"}


def add_tree(z: zipfile.ZipFile, src: Path, prefix: str) -> int:
    n = 0
    for p in sorted(src.rglob("*")):
        if p.is_file() and p.name not in SKIP:
            z.write(p, f"{prefix}/{p.relative_to(src).as_posix()}")
            n += 1
    return n


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    with zipfile.ZipFile(DIST / "AI-Team-folder.zip", "w", zipfile.ZIP_DEFLATED) as z:
        n = add_tree(z, ROOT / "team-folder", "AI Team") + add_tree(z, ROOT / "sops", "AI Team/sops")
    print(f"AI-Team-folder.zip: {n} files")
    names = {Path(a["charter"]).stem: a["name"] for a in json.loads((ROOT / "manifest.json").read_text())["agents"]}
    for desk in sorted(p for p in (ROOT / "desks").iterdir() if p.is_dir()):
        title = f"{desk.name[:2]} {names[desk.name]}"
        for src, suffix in [(desk, ""), (ROOT / "desks-compact" / desk.name, "-compact")]:
            with zipfile.ZipFile(DIST / f"{desk.name}{suffix}.zip", "w", zipfile.ZIP_DEFLATED) as z:
                n = add_tree(z, src, f"{title} files{' (compact)' if suffix else ''}")
            print(f"{desk.name}{suffix}.zip: {n} files")


if __name__ == "__main__":
    main()
