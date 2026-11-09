#!/usr/bin/env python3
"""Heuristic Meta ad-copy linter. Not a fact-checker or compliance certification."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VALID_STATUSES = {"verified", "buyer-reported", "inferred", "hypothesis", "unknown"}
DEFAULT_TARGETS = {"primary_text": 125, "headline": 40, "description": 30}
UNRESOLVED_MARKERS = ("[NEEDS INPUT", "[NEEDS HUMAN REVIEW")
COPY_FIELDS = ("primary_text", "headline", "description", "cta")


def check(data: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return ["Root must be a JSON object."], warnings
    ads = data.get("ads")
    if not isinstance(ads, list) or not ads:
        return ["'ads' must be a nonempty array."], warnings
    evidence = data.get("evidence", [])
    if not isinstance(evidence, list):
        errors.append("'evidence' must be an array when provided.")
        evidence = []
    evidence_ids = set()
    for i, item in enumerate(evidence):
        if not isinstance(item, dict):
            errors.append(f"evidence[{i}] must be an object.")
            continue
        if item.get("status") not in VALID_STATUSES:
            errors.append(f"evidence[{i}].status must be one of {sorted(VALID_STATUSES)}")
        if not item.get("id"):
            errors.append(f"evidence[{i}] requires an id.")
        elif item["id"] in evidence_ids:
            errors.append(f"Duplicate evidence ID {item['id']}.")
        else:
            evidence_ids.add(item["id"])
    angles = data.get("angles", [])
    if not isinstance(angles, list):
        errors.append("'angles' must be an array when provided.")
        angles = []
    angle_ids: set[str] = set()
    for i, angle in enumerate(angles):
        if not isinstance(angle, dict):
            errors.append(f"angles[{i}] must be an object.")
            continue
        angle_id = angle.get("angle_id")
        if not isinstance(angle_id, str) or not angle_id.strip():
            errors.append(f"angles[{i}].angle_id must be nonempty text.")
        elif angle_id in angle_ids:
            errors.append(f"Duplicate angle ID {angle_id}.")
        else:
            angle_ids.add(angle_id)
    buyer_situations = data.get("buyer_situations", [])
    buyer_ids = {b.get("id") for b in buyer_situations if isinstance(b, dict)} if isinstance(buyer_situations, list) else set()
    if not isinstance(buyer_situations, list):
        errors.append("'buyer_situations' must be an array when provided.")
    for i, angle in enumerate(angles):
        if not isinstance(angle, dict):
            continue
        buyer_ref = angle.get("buyer_situation_id")
        if buyer_ref is not None and buyer_ref not in buyer_ids:
            warnings.append(f"angles[{i}] references unknown buyer_situation_id {buyer_ref}.")
    brand_mode = data.get("campaign_mode") in {"brand", "brand-building", "brand_building"}
    copies = set()
    for i, ad in enumerate(ads):
        if not isinstance(ad, dict):
            errors.append(f"ads[{i}] must be an object.")
            continue
        for field in ("primary_text", "headline"):
            if not isinstance(ad.get(field), str) or not ad[field].strip():
                errors.append(f"ads[{i}].{field} must be nonempty text.")
        for field in COPY_FIELDS:
            value = ad.get(field)
            if isinstance(value, str) and any(m in value.upper() for m in UNRESOLVED_MARKERS):
                errors.append(f"ads[{i}].{field} contains an unresolved [NEEDS INPUT]/[NEEDS HUMAN REVIEW] marker; resolve it before treating copy as publishable.")
        for field, target in DEFAULT_TARGETS.items():
            value = ad.get(field, "")
            if isinstance(value, str) and len(value) > target:
                warnings.append(f"ads[{i}].{field}: {len(value)} characters (advisory display target {target}; not a platform max).")
        if ad.get("angle_id") not in angle_ids:
            warnings.append(f"ads[{i}] angle_id not found in angles table.")
        refs = ad.get("evidence_ids", [])
        if not isinstance(refs, list):
            errors.append(f"ads[{i}].evidence_ids must be an array.")
        else:
            for ref in refs:
                if ref not in evidence_ids:
                    warnings.append(f"ads[{i}] references unknown evidence ID {ref}.")
        if brand_mode and not ad.get("brand_cue"):
            warnings.append(f"ads[{i}] is for brand-building but has no identifiable brand_cue; review the creative and brand asset plan.")
        pair = (ad.get("primary_text"), ad.get("headline"))
        if pair in copies:
            warnings.append(f"ads[{i}] repeats an identical copy combination.")
        copies.add(pair)
    if len(angles) >= 2:
        named_motives = [str(a.get("motivation", "")).strip().casefold() for a in angles if isinstance(a, dict) and a.get("motivation")]
        if len(named_motives) >= 2 and len(set(named_motives)) == 1:
            warnings.append("All angles cite the same motivation; review whether concepts differ strategically rather than just in wording.")
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file with ads array and evidence")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return 2
    errors, warnings = check(data)
    for err in errors:
        print(f"ERROR: {err}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if not errors and not warnings:
        print("PASS: structure is valid and within heuristic text targets.")
    elif not errors:
        print("PASS with warnings: review placement previews and source claims manually.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
