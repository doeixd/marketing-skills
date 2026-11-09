#!/usr/bin/env python3
"""Check a marketing context file (.marketing-context/brand-truth.md) for structure and hygiene.

Verifies required sections, valid evidence statuses in table 'Status' columns, a review date,
stale or expired dated rows, unresolved [NEEDS INPUT] markers, and obvious secrets or personal
data. It cannot tell whether a fact is true.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

VALID_STATUSES = {"verified", "buyer-reported", "inferred", "hypothesis", "unknown"}
REQUIRED_SECTIONS = ("identity", "offerings", "claim register", "voice rules")
DATE_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
SECRET_PATTERNS = (
    (re.compile(r"\bsk-[A-Za-z0-9_\-]{16,}"), "API key"),
    (re.compile(r"\bEAA[A-Za-z0-9]{20,}"), "Meta access token"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"), "GitHub token"),
    (re.compile(r"(?i)\b(password|passwd|secret|api[_ -]?key|access[_ -]?token)\s*[:=]\s*\S{6,}"), "credential"),
)
EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
MARKER = "[NEEDS INPUT"


def _parse_date(text: str) -> date | None:
    m = DATE_RE.search(text)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def check(text: str, today: date | None = None, max_age_days: int = 90) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    today = today or date.today()
    lines = text.replace("\r\n", "\n").split("\n")

    headings = [re.sub(r"^#+\s*(\d+\.\s*)?", "", l).strip().lower() for l in lines if l.startswith("#")]
    for section in REQUIRED_SECTIONS:
        if not any(h.startswith(section) for h in headings):
            errors.append(f"Missing required section: '{section}'.")

    reviewed = next((l for l in lines if l.lower().startswith("last reviewed")), None)
    reviewed_on = _parse_date(reviewed) if reviewed else None
    if reviewed_on is None:
        errors.append("Missing 'Last reviewed: YYYY-MM-DD' line.")
    elif today - reviewed_on > timedelta(days=max_age_days):
        warnings.append(f"Last reviewed {reviewed_on.isoformat()} is more than {max_age_days} days ago; re-verify time-sensitive facts.")

    header: list[str] | None = None
    for n, line in enumerate(lines, 1):
        if not line.lstrip().startswith("|"):
            header = None
            continue
        cells = _cells(line)
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        row = dict(zip(header, cells))
        status = row.get("status")
        if status is not None and status and MARKER not in status.upper() and status.lower() not in VALID_STATUSES:
            errors.append(f"Line {n}: status '{status}' must be one of {sorted(VALID_STATUSES)}.")
        expires = _parse_date(row.get("expires", ""))
        if expires and expires < today:
            warnings.append(f"Line {n}: claim expired on {expires.isoformat()}; re-verify before publishing.")
        checked = _parse_date(row.get("checked", ""))
        if checked and today - checked > timedelta(days=max_age_days):
            warnings.append(f"Line {n}: last checked {checked.isoformat()}, over {max_age_days} days ago.")
        if status and status.lower() == "verified" and "source" in row and not row["source"]:
            warnings.append(f"Line {n}: 'verified' row has no source.")

    for n, line in enumerate(lines, 1):
        for pattern, label in SECRET_PATTERNS:
            if pattern.search(line):
                errors.append(f"Line {n}: looks like a {label}; never store secrets in the context file.")
        if EMAIL_RE.search(line):
            warnings.append(f"Line {n}: contains an email address; keep customer personal data out of this file.")

    markers = sum(l.upper().count(MARKER) for l in lines)
    if markers:
        warnings.append(f"{markers} unresolved [NEEDS INPUT] marker(s); dependent deliverables stay drafts.")
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to brand-truth.md")
    parser.add_argument("--max-age-days", type=int, default=90)
    parser.add_argument("--today", help="Override today's date (YYYY-MM-DD), for reproducible checks")
    args = parser.parse_args(argv)
    try:
        text = args.input.read_text(encoding="utf-8")
    except OSError as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return 2
    today = _parse_date(args.today) if args.today else None
    if args.today and today is None:
        print("ERROR: --today must be YYYY-MM-DD", file=sys.stderr)
        return 2
    errors, warnings = check(text, today=today, max_age_days=args.max_age_days)
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARNING: {w}")
    if not errors and not warnings:
        print("PASS: context file is structurally complete and current.")
    elif not errors:
        print("PASS with warnings: resolve open inputs and stale rows before publishing claims.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
