#!/usr/bin/env python3
"""Structural preflight for draft Google responsive search ads (RSAs).

Usage: python scripts/check_search_ads.py examples/google-search-rsa-draft.json

NOT a Google policy, factual-claim, landing-page, or account validator.
Characters are counted using Python Unicode code points as a conservative
local approximation; Google Ads editor is authoritative, particularly when
dynamic insertion or wide/combining characters are used.
"""
import argparse
import json
import sys
from pathlib import Path

HEADLINE_MAX = 30
DESCRIPTION_MAX = 90
HEADLINES_MIN = 3
HEADLINES_MAX = 15
DESCRIPTIONS_MIN = 2
DESCRIPTIONS_MAX = 4


def norm(s: str) -> str:
    return " ".join(s.casefold().strip().split())


def validate(data: object) -> list[str]:
    errors = []
    if not isinstance(data, dict) or not isinstance(data.get("ads"), list):
        return ["Root must be an object with an 'ads' array"]
    if not data["ads"]:
        return ["At least one ad draft is required"]

    for i, ad in enumerate(data["ads"], start=1):
        label = f"ad[{i}]"
        if not isinstance(ad, dict):
            errors.append(f"{label}: must be an object")
            continue
        name = ad.get("name")
        if isinstance(name, str) and name.strip():
            label += f" ({name})"
        heads, descriptions = ad.get("headlines"), ad.get("descriptions")
        if not isinstance(heads, list) or not HEADLINES_MIN <= len(heads) <= HEADLINES_MAX:
            errors.append(f"{label}: headlines must contain {HEADLINES_MIN}–{HEADLINES_MAX} strings")
            heads = heads if isinstance(heads, list) else []
        if not isinstance(descriptions, list) or not DESCRIPTIONS_MIN <= len(descriptions) <= DESCRIPTIONS_MAX:
            errors.append(f"{label}: descriptions must contain {DESCRIPTIONS_MIN}–{DESCRIPTIONS_MAX} strings")
            descriptions = descriptions if isinstance(descriptions, list) else []
        for asset_type, assets, max_chars in (
            ("headline", heads, HEADLINE_MAX),
            ("description", descriptions, DESCRIPTION_MAX),
        ):
            seen = set()
            for index, content in enumerate(assets, start=1):
                field = f"{label}: {asset_type}[{index}]"
                if not isinstance(content, str) or not content.strip():
                    errors.append(f"{field} must be nonblank string")
                    continue
                if len(content) > max_chars:
                    errors.append(f"{field} is {len(content)} characters (max {max_chars})")
                if "\n" in content or "\r" in content:
                    errors.append(f"{field} cannot contain newlines")
                if norm(content) in seen:
                    errors.append(f"{field} is a duplicate {asset_type}")
                seen.add(norm(content))
        if ad.get("require_brand_cue", False):
            brand = ad.get("brand_name")
            if not isinstance(brand, str) or not brand.strip():
                errors.append(f"{label}: require_brand_cue needs brand_name")
            elif not any(isinstance(h, str) and norm(brand) in norm(h) for h in heads):
                errors.append(f"{label}: brand cue '{brand}' absent from headlines")
        if ad.get("publication_approved", False):
            if not ad.get("claims_verified", False):
                errors.append(f"{label}: publication_approved requires claims_verified=true")
            if not ad.get("conversion_validated", False):
                errors.append(f"{label}: publication_approved requires conversion_validated=true")
            url = ad.get("final_url")
            if not isinstance(url, str) or not url.startswith("https://") or "example.com" in url:
                errors.append(f"{label}: publication_approved requires a verified non-example https final_url")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.json_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load JSON: {exc}", file=sys.stderr)
        return 1
    errors = validate(data)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Google RSA structural preflight: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print(f"Google RSA structural preflight: OK ({len(data['ads'])} draft(s)).")
    print("NOTE: claim truth, platform policy, live destination, tracking, AI Max, rights and spend approval remain HUMAN checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
