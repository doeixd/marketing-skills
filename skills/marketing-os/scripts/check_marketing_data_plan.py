#!/usr/bin/env python3
"""Validate a proposed ecommerce marketing-data pipeline manifest (offline only).

Usage: python scripts/check_marketing_data_plan.py examples/marketing-data-pipeline-manifest.json

Checks structure and internal consistency. This cannot verify live platform
permissions, event receipt, API schemas, lawful consent, financial reconciliation,
upload approval, or whether tracking has been deployed.
"""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

SOURCES = {"shopify", "etsy", "amazon_sp_api", "amazon_ads", "meta_ads",
           "meta_pixel", "google_ads", "ga4", "email", "crm", "csv", "other"}
STATUSES = {"draft", "review", "active"}
UTM_REQUIRED = {"utm_source", "utm_medium", "utm_campaign"}
PRIVATE_PARAMS = {"email", "e_mail", "phone", "phone_number", "address",
                  "name", "customer_id", "access_token", "api_key", "password",
                  "secret", "token", "authorization"}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(data):
    if not isinstance(data, dict):
        return ["Root must be a JSON object"]
    errors = []
    for field in ("purpose", "sources", "events", "audiences", "campaign_urls"):
        if field not in data:
            errors.append(f"missing root field {field}")
    if not nonempty(data.get("purpose")):
        errors.append("purpose must explain what decision this pipeline supports")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a nonempty array")
        sources = []
    source_ids = set()
    for index, source in enumerate(sources):
        p = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{p}: expected object")
            continue
        source_id = source.get("id")
        if not nonempty(source_id) or source_id in source_ids:
            errors.append(f"{p}: missing or duplicate id")
        else:
            source_ids.add(source_id)
        if source.get("platform") not in SOURCES:
            errors.append(f"{p}: invalid platform")
        for field in ("account_scope", "grain", "privacy_policy",
                      "destination", "reconciliation_owner"):
            if not nonempty(source.get(field)):
                errors.append(f"{p}: missing {field}")
        keys = source.get("primary_key")
        if not isinstance(keys, list) or not keys or not all(nonempty(x) for x in keys):
            errors.append(f"{p}: primary_key must list stable source-scoped fields")
        elif len(keys) != len(set(keys)):
            errors.append(f"{p}: primary_key repeats fields")
        if source.get("mode") not in {"api", "bulk", "webhook", "report", "file"}:
            errors.append(f"{p}: unknown ingestion mode")
        if source.get("status", "draft") not in STATUSES:
            errors.append(f"{p}: unknown status")
        if source.get("status", "draft") == "active":
            for field in ("access_authorized", "reconciliation_tested", "privacy_reviewed"):
                if source.get(field) is not True:
                    errors.append(f"{p}: active requires {field}=true")

    events = data.get("events")
    if not isinstance(events, list):
        errors.append("events must be an array")
        events = []
    event_ids = set()
    for index, event in enumerate(events):
        p = f"events[{index}]"
        if not isinstance(event, dict):
            errors.append(f"{p}: expected object")
            continue
        event_id = event.get("id")
        if not nonempty(event_id) or event_id in event_ids:
            errors.append(f"{p}: missing or duplicate id")
        else:
            event_ids.add(event_id)
        if event.get("origin_source") not in source_ids:
            errors.append(f"{p}: origin_source must reference listed sources")
        if not nonempty(event.get("canonical_name")):
            errors.append(f"{p}: canonical_name missing")
        if not nonempty(event.get("consent_rule")):
            errors.append(f"{p}: consent_rule missing")
        destinations = event.get("destinations")
        if not isinstance(destinations, list):
            errors.append(f"{p}: destinations must be an array")
            destinations = []
        meta = [d for d in destinations if isinstance(d, dict) and d.get("platform") == "meta"]
        if any(not nonempty(d.get("event_id_field")) for d in meta):
            errors.append(f"{p}: Meta destination missing event_id_field")
        browser = [d for d in meta if d.get("transport") == "browser"]
        server = [d for d in meta if d.get("transport") == "server"]
        if browser and server:
            names = {d.get("event_name") for d in browser + server}
            ids = {d.get("event_id_field") for d in browser + server}
            if len(names) != 1 or len(ids) != 1 or None in names:
                errors.append(f"{p}: Meta browser/server must share event_name and event_id_field")
        for d in destinations:
            if not isinstance(d, dict) or not nonempty(d.get("event_name")):
                errors.append(f"{p}: destination missing event_name")
        if event.get("canonical_name") == "purchase":
            for field in ("order_id_field", "currency_field", "value_field"):
                if not nonempty(event.get(field)):
                    errors.append(f"{p}: purchase missing {field}")
        if event.get("status", "draft") == "active":
            for field in ("approval_recorded", "consent_tested", "order_reconciled"):
                if event.get(field) is not True:
                    errors.append(f"{p}: active requires {field}=true")

    audiences = data.get("audiences")
    if not isinstance(audiences, list):
        errors.append("audiences must be an array")
        audiences = []
    for index, audience in enumerate(audiences):
        p = f"audiences[{index}]"
        if not isinstance(audience, dict):
            errors.append(f"{p}: expected object")
            continue
        for field in ("id", "source", "purpose", "eligibility_rule", "suppression_rule"):
            if not nonempty(audience.get(field)):
                errors.append(f"{p}: missing {field}")
        if audience.get("source") not in source_ids:
            errors.append(f"{p}: source must reference listed source")
        if audience.get("status", "draft") == "active":
            for field in ("consent_verified", "platform_terms_reviewed",
                          "deletion_propagation_tested", "upload_authorized"):
                if audience.get(field) is not True:
                    errors.append(f"{p}: active requires {field}=true")
        if audience.get("source_platform") in {"etsy", "amazon_sp_api"} and audience.get("status") == "active":
            if audience.get("marketplace_data_use_explicitly_permitted") is not True:
                errors.append(f"{p}: marketplace audience needs explicit platform permission")

    urls = data.get("campaign_urls")
    if not isinstance(urls, list):
        errors.append("campaign_urls must be an array")
        urls = []
    for index, item in enumerate(urls):
        p = f"campaign_urls[{index}]"
        if not isinstance(item, dict) or not nonempty(item.get("url")):
            errors.append(f"{p}: missing URL")
            continue
        try:
            url = urlsplit(item["url"])
            params = parse_qsl(url.query, keep_blank_values=True)
        except ValueError:
            errors.append(f"{p}: invalid URL")
            continue
        if url.scheme != "https" or not url.netloc or url.username or url.password:
            errors.append(f"{p}: URL must be a plain https URL")
        names = [k.lower() for k, _ in params]
        for name in UTM_REQUIRED:
            if names.count(name) != 1:
                errors.append(f"{p}: expected exactly one {name}")
        if any(names.count(n) > 1 for n in UTM_REQUIRED):
            errors.append(f"{p}: duplicate campaign parameter")
        for key, val in params:
            kl = key.casefold()
            if kl in PRIVATE_PARAMS or any(s in kl for s in ("email", "phone", "access_token", "api_key")):
                errors.append(f"{p}: potentially private URL parameter {key}")
            if kl.startswith("utm_") and not val.strip():
                errors.append(f"{p}: empty tracking parameter {key}")
        for name in UTM_REQUIRED:
            values = [v for k, v in params if k.lower() == name]
            if values and (values[0] != values[0].lower() or " " in values[0]):
                errors.append(f"{p}: {name} must follow proposed lowercase no-space taxonomy")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        obj = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print("ERROR: cannot read JSON:", exc, file=sys.stderr)
        return 1
    errors = validate(obj)
    for e in errors:
        print("ERROR:", e, file=sys.stderr)
    if errors:
        print(f"Marketing pipeline preflight: {len(errors)} structural issue(s)", file=sys.stderr)
        return 1
    print("Marketing pipeline preflight: OK — structural checks only.")
    print("Real privacy/permissions, API access, Meta/GA4 receipt and financial QA are not validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
