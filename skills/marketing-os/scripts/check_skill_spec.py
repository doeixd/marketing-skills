#!/usr/bin/env python3
"""Check SKILL.md against the Agent Skills spec and this repo's context budgets.

Enforces: frontmatter name format/length and directory match, description length,
activation-tier size budget (lines and estimated tokens), every workflow linked from
SKILL.md, and warns about reference/template files nothing links to.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#\s]+)")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_LINES = 500
MAX_TOKENS = 5000  # estimated as characters / 4


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with a '---' YAML frontmatter block.")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed with '---'.")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip("'\"")
    return fields, text[end + 5:]


def check(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return [f"{skill_path} not found."], warnings
    text = skill_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    try:
        fields, _body = parse_frontmatter(text)
    except ValueError as ex:
        return [str(ex)], warnings

    name = fields.get("name", "")
    if not name:
        errors.append("frontmatter 'name' is required.")
    else:
        if len(name) > MAX_NAME:
            errors.append(f"name is {len(name)} chars (max {MAX_NAME}).")
        if not NAME_RE.match(name):
            errors.append(f"name {name!r} must be lowercase letters, digits and single hyphens.")
        if name != root.resolve().name:
            errors.append(f"name {name!r} must match directory name {root.resolve().name!r}.")

    description = fields.get("description", "")
    if not description:
        errors.append("frontmatter 'description' is required.")
    elif len(description) > MAX_DESCRIPTION:
        errors.append(f"description is {len(description)} chars (max {MAX_DESCRIPTION}).")

    lines = text.count("\n")
    tokens = len(text) // 4
    if lines > MAX_LINES:
        errors.append(f"SKILL.md is {lines} lines (budget {MAX_LINES}); move detail to references/.")
    if tokens > MAX_TOKENS:
        errors.append(f"SKILL.md is ~{tokens} tokens (budget {MAX_TOKENS}); move detail to references/.")

    skill_links = {Path(t).as_posix() for t in LINK_RE.findall(text)}
    for wf in sorted((root / "workflows").glob("*.md")):
        rel = wf.relative_to(root).as_posix()
        if rel not in skill_links:
            errors.append(f"{rel} is not routed from SKILL.md.")

    linked: set[Path] = set()
    for md in root.rglob("*.md"):
        for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
            if not target.startswith(("http://", "https://", "mailto:")):
                linked.add((md.parent / target).resolve())
    for folder in ("references", "templates"):
        for f in sorted((root / folder).glob("*.md")):
            if f.resolve() not in linked:
                warnings.append(f"{f.relative_to(root).as_posix()} is not linked from any Markdown file.")

    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors, warnings = check(args.skill_dir)
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARNING: {w}")
    if not errors:
        print("PASS: SKILL.md meets spec and context budgets.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
