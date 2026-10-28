#!/usr/bin/env python3
"""Build desks/<NN-name>/: the exact files to load into each ChatGPT Project.

Run from the repo root:  python3 scripts/build_desks.py
It reads manifest.json, so the desks always match the charters, skills, routines and SOPs.
Each desk folder gets:
  INSTRUCTIONS.md     the charter's Profile block, pasted into the Project's Instructions
  charter.md          the full charter
  skill-<name>.md     each skill the desk uses (save as a ChatGPT skill, or keep as a file)
  routine-<name>.md   each scheduled task the desk owns (created paused)
  sop-<NN-name>.md    the SOPs the desk follows
  plus the team rules every desk needs.
It also builds desks-compact/<NN-name>/ for plans that hold fewer project files: the same
INSTRUCTIONS.md and skill files, with everything else joined into one reference.md.
A project's files sit side by side, so links between them are rewritten to the copied file
names. A link to a file the desk doesn't get becomes plain text naming its place in the repo.
"""
import json
import posixpath
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMON = {"PROJECT_CHARTER.md": "PROJECT_CHARTER.md", "policies/APPROVALS.md": "APPROVALS.md",
          "policies/DATA.md": "DATA.md", "docs/CHATGPT-PLATFORM.md": "CHATGPT-PLATFORM.md"}
LEAD_EXTRA = {"START-HERE.md": "START-HERE.md", "OPEN_QUESTIONS.md": "OPEN_QUESTIONS.md",
              "client-context/CLIENT-CONTEXT.template.md": "CLIENT-CONTEXT.template.md",
              "sops/README.md": "sop-index.md", "sops/SOP-TEMPLATE.md": "sop-template.md",
              "sops/HOW-WE-WRITE-SOPS.md": "sop-how-we-write.md"}
PROFILE = re.compile(r"^## Profile\s*\n+```[a-z]*\n(.*?)\n```", re.S | re.M)
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def relink(text: str, src: str, names: dict[str, str]) -> str:
    """Point each relative link at the desk's copy of its target, or name the repo path."""
    def sub(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            return m.group(0)
        path, _, anchor = href.partition("#")
        target = posixpath.normpath(posixpath.join(posixpath.dirname(src), path)).rstrip("/")
        if target in names:
            return f"[{label}]({names[target]}{'#' + anchor if anchor else ''})"
        return f"{label} (repo: `{target}`)"
    return LINK.sub(sub, text)


def profile(charter: Path) -> str:
    m = PROFILE.search(charter.read_text())
    if not m:
        sys.exit(f"{charter}: no fenced Profile block")
    return m.group(1).strip() + "\n"


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text())
    out_root = ROOT / "desks"
    if out_root.exists():
        shutil.rmtree(out_root)
    compact_root = ROOT / "desks-compact"
    if compact_root.exists():
        shutil.rmtree(compact_root)
    for agent in manifest["agents"]:
        charter = ROOT / agent["charter"]
        num = charter.name[:2]
        if int(num) >= 90:
            continue                      # reserved desks are built at their milestone
        desk = out_root / charter.stem
        desk.mkdir(parents=True)
        names = {agent["charter"]: "charter.md", **COMMON, **(LEAD_EXTRA if num == "01" else {})}
        names.update({f"skills/{n}/SKILL.md": f"skill-{n}.md" for n in agent.get("skills", [])})
        names.update({f"skills/{n}": f"skill-{n}.md" for n in agent.get("skills", [])})
        names.update({rel: f"routine-{Path(rel).stem}.md" for rel in agent.get("routines", [])})
        names.update({rel: f"sop-{Path(rel).name}" for rel in agent.get("sops", [])})
        (desk / "INSTRUCTIONS.md").write_text(profile(charter))
        for rel, name in names.items():
            src = ROOT / rel
            if src.is_file():
                (desk / name).write_text(relink(src.read_text(), rel, names))
        files = sorted(p.name for p in desk.iterdir())
        print(f"{desk.relative_to(ROOT)}: {len(files)} files")
        compact = compact_root / charter.stem
        compact.mkdir(parents=True)
        cnames = {rel: (name if name.startswith("skill-") else "reference.md") for rel, name in names.items()}
        parts = [f"# {charter.stem}: reference\n\nEvery file this desk uses, joined into one, for plans that hold "
                 "fewer project files. Each section starts with the file's own name.\n"]
        (compact / "INSTRUCTIONS.md").write_text(profile(charter))
        for rel, name in names.items():
            src = ROOT / rel
            if not src.is_file():
                continue
            text = relink(src.read_text(), rel, cnames)
            if name.startswith("skill-"):
                (compact / name).write_text(text)
            else:
                parts.append(f"\n---\n\n<!-- file: {name} -->\n\n{text}")
        (compact / "reference.md").write_text("".join(parts))
    readme = out_root / "README.md"
    readme.write_text(
        "# Desks: what to load into each ChatGPT Project\n\n"
        "Generated by `scripts/build_desks.py` from `manifest.json`. Don't edit these copies; edit the originals "
        "and run the script again.\n\n"
        "For each desk: paste `INSTRUCTIONS.md` into the Project's Instructions, then add every other file in the "
        "folder to the Project's Files, plus `owner.md` and `routines-on.md` from the AI Team folder. "
        "See START-HERE Step 6. If the plan holds fewer files, use `desks-compact/` instead (START-HERE Step 2).\n")


if __name__ == "__main__":
    main()
