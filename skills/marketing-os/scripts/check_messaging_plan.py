#!/usr/bin/env python3
"""Check draft marketing email/SMS manifests for structural and approval gaps.

Usage: python scripts/check_messaging_plan.py examples/messaging-plan-draft.json

This is a local STRUCTURAL checker, not proof of marketing consent, DNS
authentication, legal compliance, sender registration, deliverability, live
account settings, truth of claims, or actual authorization to send.
"""
import argparse
import json
import sys
from pathlib import Path

VALID_CHANNELS = {"email", "sms"}
VALID_STATUSES = {"draft", "review", "publish_ready"}


def validate(data: object) -> list[str]:
    if not isinstance(data, dict) or not isinstance(data.get("messages"), list):
        return ["Root must be an object with a 'messages' array"]
    messages = data["messages"]
    if not messages:
        return ["At least one message draft is required"]
    errors: list[str] = []
    seen_ids: set[str] = set()

    for i, m in enumerate(messages, 1):
        label = f"messages[{i}]"
        if not isinstance(m, dict):
            errors.append(f"{label}: must be an object")
            continue
        msg_id = m.get("id")
        if not isinstance(msg_id, str) or not msg_id.strip():
            errors.append(f"{label}: id must be a nonempty string")
        elif msg_id in seen_ids:
            errors.append(f"{label}: duplicate message id {msg_id!r}")
        else:
            seen_ids.add(msg_id)
        channel = m.get("channel")
        if channel not in VALID_CHANNELS:
            errors.append(f"{label}: channel must be email or sms")
            continue
        status = m.get("status", "draft")
        if status not in VALID_STATUSES:
            errors.append(f"{label}: unknown status {status!r}")
            continue
        for field in ("audience", "body", "landing_url_or_action"):
            if not isinstance(m.get(field), str) or not m[field].strip():
                errors.append(f"{label}: {field} must be a nonempty string")
        if channel == "email":
            for field in ("subject", "preheader"):
                if not isinstance(m.get(field), str) or not m[field].strip():
                    errors.append(f"{label}: email {field} must be nonempty")
        if channel == "sms":
            # Carrier encoding/segments must be checked with actual provider.
            if "subject" in m or "preheader" in m:
                errors.append(f"{label}: SMS uses body only, not email subject/preheader")
        if status == "publish_ready":
            common = (
                "recipient_eligibility_verified",
                "suppression_verified",
                "claims_verified",
                "destination_verified",
                "channel_policy_reviewed",
                "activated_by_authorized_human",
            )
            for field in common:
                if m.get(field) is not True:
                    errors.append(f"{label}: publish_ready requires {field}=true")
            if not isinstance(m.get("approved_by"), str) or not m["approved_by"].strip():
                errors.append(f"{label}: publish_ready requires actual approved_by name/role")
            if channel == "email":
                for field in ("sending_domain_verified", "unsubscribe_verified"):
                    if m.get(field) is not True:
                        errors.append(f"{label}: publish_ready email requires {field}=true")
                if m.get("gmail_bulk_sender", False) and m.get("one_click_unsubscribe_verified") is not True:
                    errors.append(f"{label}: bulk promotional email requires verified one-click unsubscribe")
            if channel == "sms":
                for field in (
                    "sms_specific_opt_in_verified",
                    "sender_route_verified",
                    "stop_help_tested",
                    "quiet_hours_checked",
                    "provider_segment_cost_checked",
                ):
                    if m.get(field) is not True:
                        errors.append(f"{label}: publish_ready SMS requires {field}=true")
        # Never assume this flag implies any real authorization to send.
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.json_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load JSON: {exc}", file=sys.stderr)
        return 1
    errors = validate(payload)
    for e in errors:
        print("ERROR:", e, file=sys.stderr)
    if errors:
        print(f"Messaging preflight: {len(errors)} structural issue(s)", file=sys.stderr)
        return 1
    print(f"Messaging preflight: OK ({len(payload['messages'])} draft(s)).")
    print("Structural validation only — consent, provider rules, law, claims, sending and approval remain real-world checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
