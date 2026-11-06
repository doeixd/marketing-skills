#!/usr/bin/env python3
"""Check Markdown relative links stay within repo and point to existing files."""
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
issues = []
for path in ROOT.rglob("*.md"):
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("https://", "http://", "mailto:")):
            continue
        dest = (path.parent / unquote(target)).resolve()
        if not dest.is_relative_to(ROOT.resolve()) or not dest.exists():
            issues.append(f"{path.relative_to(ROOT)}: broken link {target!r}")
for issue in issues:
    print("ERROR:", issue)
print(f"Checked Markdown links: {len(issues)} issue(s)")
raise SystemExit(1 if issues else 0)
