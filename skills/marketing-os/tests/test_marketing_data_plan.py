"""Marketing pipeline manifest preflight tests. No live data or customer identity."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_marketing_data_plan", ROOT / "scripts" / "check_marketing_data_plan.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def fixture():
    return json.loads((ROOT / "examples" / "marketing-data-pipeline-manifest.json").read_text(encoding="utf-8"))


class MarketingDataPlanTest(unittest.TestCase):
    def test_sample_fixture(self):
        self.assertEqual(v.validate(fixture()), [])

    def test_duplicate_and_unscoped_source(self):
        x = fixture()
        x["sources"][1]["id"] = x["sources"][0]["id"]
        x["sources"][1]["primary_key"] = []
        errors = v.validate(x)
        self.assertTrue(any("duplicate id" in e for e in errors))
        self.assertTrue(any("primary_key" in e for e in errors))

    def test_purchase_identity_and_currency_required(self):
        x = fixture()
        e = x["events"][0]
        del e["order_id_field"]
        del e["currency_field"]
        errors = v.validate(x)
        self.assertTrue(any("purchase missing order_id_field" in e for e in errors))
        self.assertTrue(any("purchase missing currency_field" in e for e in errors))

    def test_meta_browser_server_event_id_and_name(self):
        x = fixture()
        x["events"][0]["destinations"][2]["event_id_field"] = "new_uuid_on_retry"
        errors = v.validate(x)
        self.assertTrue(any("share event_name and event_id_field" in e for e in errors))
        x = fixture()
        x["events"][0]["destinations"][2]["event_name"] = "Checkout"
        self.assertTrue(any("share event_name" in e for e in v.validate(x)))

    def test_url_pii_and_duplicate_campaign_tag(self):
        x = fixture()
        x["campaign_urls"][0]["url"] += "&email=foo%40example.com&utm_medium=other"
        errors = v.validate(x)
        self.assertTrue(any("potentially private URL parameter email" in e for e in errors))
        self.assertTrue(any("duplicate campaign parameter" in e for e in errors))

    def test_utm_case(self):
        x = fixture()
        x["campaign_urls"][0]["url"] = x["campaign_urls"][0]["url"].replace("utm_source=facebook", "utm_source=Facebook")
        self.assertTrue(any("lowercase" in e for e in v.validate(x)))

    def test_not_ready_to_activate_audience(self):
        x = fixture()
        x["audiences"][0]["status"] = "active"
        errors = v.validate(x)
        self.assertTrue(any("consent_verified" in e for e in errors))
        self.assertTrue(any("upload_authorized" in e for e in errors))
        self.assertTrue(any("deletion_propagation_tested" in e for e in errors))

    def test_marketplace_audience_requires_explicit_permission(self):
        x = fixture()
        a = x["audiences"][0]
        a.update({"source":"etsy_receipts","source_platform":"etsy","status":"active",
                  "consent_verified":True,"platform_terms_reviewed":True,
                  "deletion_propagation_tested":True,"upload_authorized":True})
        self.assertTrue(any("marketplace audience" in e for e in v.validate(x)))

    def test_active_event_requires_real_checkpoints(self):
        x = fixture()
        x["events"][0]["status"] = "active"
        errors = v.validate(x)
        self.assertTrue(any("consent_tested" in e for e in errors))
        self.assertTrue(any("order_reconciled" in e for e in errors))

    def test_active_source_requires_reconciliation(self):
        x = fixture()
        x["sources"][0]["status"] = "active"
        errors = v.validate(x)
        self.assertTrue(any("access_authorized" in e for e in errors))
        self.assertTrue(any("reconciliation_tested" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
