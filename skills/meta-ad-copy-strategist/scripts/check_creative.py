#!/usr/bin/env python3
"""Lint a planned Meta creative manifest. Does not check factual claims or approve ads."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

VIDEO_PLACEMENTS = {"instagram_reels", "facebook_reels", "instagram_stories", "facebook_stories"}
FEED_PLACEMENTS = {"instagram_feed", "facebook_feed"}
VALID_TYPES = {"image", "video", "carousel"}
SAFE_RECT = (0.06, 0.14, 0.94, 0.65)  # conservative Reels/Stories 9:16 guide, not a Meta hard rule


def check(data: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return ["Creative manifest must be a JSON object"], []
    concepts, assets = data.get("concepts"), data.get("assets")
    if not isinstance(concepts, list) or not concepts:
        errors.append("'concepts' must be a nonempty array")
        concepts = []
    if not isinstance(assets, list) or not assets:
        errors.append("'assets' must be a nonempty array")
        assets = []
    ids = set()
    motivations = set()
    for i, concept in enumerate(concepts):
        if not isinstance(concept, dict):
            errors.append(f"concepts[{i}] must be an object")
            continue
        cid = concept.get("id")
        if not isinstance(cid, str) or not cid.strip() or cid in ids:
            errors.append(f"concepts[{i}] requires a unique nonempty id")
        else:
            ids.add(cid)
        for required in ("buyer_motivation", "promise", "brand_cue"):
            if not isinstance(concept.get(required), str) or not concept[required].strip():
                warnings.append(f"concepts[{i}] missing {required}")
        if concept.get("buyer_motivation"):
            motivations.add(str(concept["buyer_motivation"]).strip().casefold())
    if len(concepts) >= 2 and len(motivations) == 1:
        warnings.append("Concepts share one buyer motivation; inspect strategic differentiation")
    seen_assets = set()
    publish = data.get("status") == "publish_ready"
    for i, asset in enumerate(assets):
        pfx = f"assets[{i}]"
        if not isinstance(asset, dict):
            errors.append(f"{pfx} must be an object")
            continue
        aid = asset.get("id")
        if not isinstance(aid, str) or not aid.strip() or aid in seen_assets:
            errors.append(f"{pfx} requires a unique nonempty id")
        else:
            seen_assets.add(aid)
        if asset.get("concept_id") not in ids:
            errors.append(f"{pfx} references unknown concept_id")
        if asset.get("type") not in VALID_TYPES:
            errors.append(f"{pfx}.type must be image/video/carousel")
        placements = asset.get("placements", [])
        if not isinstance(placements, list) or not placements or not all(isinstance(x, str) for x in placements):
            errors.append(f"{pfx}.placements must be a nonempty string list")
            placements = []
        w, h = asset.get("width"), asset.get("height")
        if not isinstance(w, int) or not isinstance(h, int) or w <= 0 or h <= 0:
            errors.append(f"{pfx} requires positive integer width/height")
            continue
        if VIDEO_PLACEMENTS.intersection(placements) and abs(w / h - 9 / 16) > 0.02:
            warnings.append(f"{pfx} is aimed at Stories/Reels but is not a 9:16 master")
        if FEED_PLACEMENTS.intersection(placements) and asset.get("type") != "carousel":
            if abs(w / h - 4 / 5) > 0.03 and abs(w / h - 1) > 0.03:
                warnings.append(f"{pfx} feed aspect ratio needs manual crop preview")
        if asset.get("type") == "video":
            if not asset.get("captions"):
                warnings.append(f"{pfx} has no caption/subtitle plan")
            if not asset.get("silent_comprehensible"):
                warnings.append(f"{pfx} has no muted-viewing plan")
        if not asset.get("brand_visible"):
            warnings.append(f"{pfx} has no confirmed recognizable brand cue")
        boxes = asset.get("overlay_boxes", [])
        if not isinstance(boxes, list):
            errors.append(f"{pfx}.overlay_boxes must be array")
            continue
        for j, box in enumerate(boxes):
            if not isinstance(box, dict):
                errors.append(f"{pfx}.overlay_boxes[{j}] must be an object")
                continue
            dims = [box.get(k) for k in ("x", "y", "w", "h")]
            if any(not isinstance(v, (int, float)) for v in dims):
                errors.append(f"{pfx}.overlay_boxes[{j}] missing numeric x/y/w/h")
                continue
            x, y, bw, bh = dims
            if bw <= 0 or bh <= 0 or x < 0 or y < 0 or x + bw > 1 or y + bh > 1:
                errors.append(f"{pfx}.overlay_boxes[{j}] out of 0..1 frame bounds")
            elif box.get("essential") and VIDEO_PLACEMENTS.intersection(placements):
                x0, y0, x1, y1 = SAFE_RECT
                if x < x0 or y < y0 or x + bw > x1 or y + bh > y1:
                    warnings.append(f"{pfx}.overlay_boxes[{j}] essential overlay outside conservative 9:16 safe zone; preview actual placement")
        if publish:
            if asset.get("rights_status") != "cleared":
                errors.append(f"{pfx} publication blocked: rights not cleared")
            if asset.get("type") == "video" and asset.get("audio_rights_status") not in {"cleared", "no_audio"}:
                errors.append(f"{pfx} publication blocked: audio rights not cleared")
            if asset.get("preview_status") != "passed":
                errors.append(f"{pfx} publication blocked: placement preview not passed")
            if asset.get("claims_status") != "verified":
                errors.append(f"{pfx} publication blocked: product claims not verified")
    if publish and not data.get("explicit_launch_approval"):
        errors.append("Publication blocked: explicit_launch_approval required")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}")
        return 2
    errors, warnings = check(data)
    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARNING: {msg}")
    if not errors:
        print("PASS with warnings" if warnings else "PASS")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
