#!/usr/bin/env python3
"""Structural check of a media plan JSON (Workflow 5P). Not a forecast or performance guarantee.

Checks that budgets add up, every channel has a role, markets and KPI, conversion-optimized
channels can plausibly reach a learning threshold, forecasts are ordered ranges, and the plan
has targets, a source of truth, stop conditions and an approval.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROLES = {"create", "capture", "convert", "retain"}
LEARNING_EVENTS_PER_WEEK = 50
MARKER = "[NEEDS INPUT"


def _number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _count_markers(node) -> int:
    if isinstance(node, str):
        return 1 if MARKER in node.upper() else 0
    if isinstance(node, dict):
        return sum(_count_markers(v) for v in node.values())
    if isinstance(node, list):
        return sum(_count_markers(v) for v in node)
    return 0


def check(data) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return ["Root must be a JSON object."], warnings

    total = data.get("total_budget")
    period = data.get("period_days")
    if not _number(total) or total <= 0:
        errors.append("'total_budget' must be a positive number.")
    if not _number(period) or period <= 0:
        errors.append("'period_days' must be a positive number.")
    channels = data.get("channels")
    if not isinstance(channels, list) or not channels:
        errors.append("'channels' must be a nonempty array.")
        return errors, warnings

    allocated = 0.0
    for i, ch in enumerate(channels):
        label = f"channels[{i}]"
        if not isinstance(ch, dict):
            errors.append(f"{label} must be an object.")
            continue
        name = ch.get("name")
        if isinstance(name, str) and name.strip():
            label = f"channels[{i}] ({name})"
        else:
            errors.append(f"{label}.name must be nonempty text.")
        if ch.get("role") not in ROLES:
            errors.append(f"{label}.role must be one of {sorted(ROLES)}.")
        markets = ch.get("markets")
        if not isinstance(markets, list) or not markets:
            errors.append(f"{label}.markets must list the countries or regions served; geography may not be left open.")
        if not isinstance(ch.get("primary_kpi"), str) or not ch["primary_kpi"].strip():
            errors.append(f"{label}.primary_kpi is required.")
        budget = ch.get("budget")
        if not _number(budget) or budget < 0:
            errors.append(f"{label}.budget must be a non-negative number.")
            continue
        allocated += budget

        event = ch.get("optimization_event")
        cost = ch.get("expected_cost_per_event")
        if event:
            if not _number(cost) or cost <= 0:
                warnings.append(f"{label}: optimization_event set but expected_cost_per_event is missing; cannot check signal volume.")
            elif _number(period) and period > 0:
                ad_sets = ch.get("ad_sets", 1)
                ad_sets = ad_sets if _number(ad_sets) and ad_sets >= 1 else 1
                weekly = budget / period * 7 / cost / ad_sets
                if weekly < LEARNING_EVENTS_PER_WEEK:
                    warnings.append(
                        f"{label}: about {weekly:.0f} '{event}' events per ad set per week "
                        f"(below ~{LEARNING_EVENTS_PER_WEEK}); expect slow or limited learning. "
                        "Consolidate, fund properly, or document the compromise."
                    )
        forecast = ch.get("forecast")
        if isinstance(forecast, dict):
            for metric, rng in forecast.items():
                if not isinstance(rng, dict) or not all(_number(rng.get(k)) for k in ("low", "base", "high")):
                    errors.append(f"{label}.forecast.{metric} needs numeric low, base and high.")
                elif not rng["low"] <= rng["base"] <= rng["high"]:
                    errors.append(f"{label}.forecast.{metric} must satisfy low <= base <= high.")

    reserve = data.get("unallocated_reserve", 0)
    if not _number(reserve) or reserve < 0:
        errors.append("'unallocated_reserve' must be a non-negative number when provided.")
        reserve = 0
    if _number(total) and total > 0:
        planned = allocated + reserve
        if planned > total * 1.001:
            errors.append(f"Channel budgets plus reserve ({planned:g}) exceed total_budget ({total:g}).")
        elif planned < total * 0.95:
            warnings.append(f"Only {planned:g} of {total:g} is allocated; state what the remainder is for.")
        if len(channels) > 1:
            for ch in channels:
                if isinstance(ch, dict) and _number(ch.get("budget")) and ch["budget"] > total * 0.8:
                    warnings.append(f"{ch.get('name', 'A channel')} holds over 80% of the budget; note the dependency risk.")

    targets = data.get("targets")
    if not isinstance(targets, dict) or not (_number(targets.get("allowable_cac")) or _number(targets.get("breakeven_roas"))):
        warnings.append("No numeric allowable_cac or breakeven_roas in 'targets'; scaling decisions have no economic anchor.")
    measurement = data.get("measurement")
    if not isinstance(measurement, dict) or not measurement.get("source_of_truth"):
        errors.append("'measurement.source_of_truth' is required (store orders or CRM, not a platform report).")
    if not data.get("stop_conditions"):
        warnings.append("No 'stop_conditions' defined.")
    if not data.get("reallocation_rules"):
        warnings.append("No 'reallocation_rules' defined before launch.")
    if not data.get("approved_by"):
        warnings.append("No 'approved_by'; treat as a draft and do not spend.")
    markers = _count_markers(data)
    if markers:
        warnings.append(f"{markers} unresolved [NEEDS INPUT] marker(s); the plan is a draft.")
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Media plan JSON file")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return 2
    errors, warnings = check(data)
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARNING: {w}")
    if not errors and not warnings:
        print("PASS: media plan structure is complete.")
    elif not errors:
        print("PASS with warnings: structure is valid; review the warnings with the budget owner.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
