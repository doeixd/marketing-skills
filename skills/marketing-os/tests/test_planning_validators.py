import json
import sys
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_context_file
import check_media_plan
import check_page_meta

TODAY = date(2026, 11, 9)


def plan(**overrides):
    base = {
        "period_days": 28,
        "total_budget": 4000,
        "targets": {"allowable_cac": 30},
        "measurement": {"source_of_truth": "Store orders"},
        "channels": [{"name": "Meta", "role": "convert", "markets": ["US"], "budget": 4000,
                      "optimization_event": "purchase", "expected_cost_per_event": 16, "primary_kpi": "New customers"}],
        "reallocation_rules": {"review_cadence": "weekly"},
        "stop_conditions": ["Tracking fails"],
        "approved_by": "Owner",
    }
    base.update(overrides)
    return base


class TestMediaPlan(unittest.TestCase):
    def test_example_has_no_errors(self):
        data = json.loads((ROOT / "examples/media-plan.json").read_text(encoding="utf-8"))
        errors, _ = check_media_plan.check(data)
        self.assertEqual(errors, [])

    def test_clean_plan_passes(self):
        self.assertEqual(check_media_plan.check(plan()), ([], []))

    def test_overallocation_and_missing_markets_are_errors(self):
        data = plan(total_budget=3000)
        data["channels"][0]["markets"] = []
        errors, _ = check_media_plan.check(data)
        self.assertTrue(any("exceed total_budget" in e for e in errors))
        self.assertTrue(any("markets" in e for e in errors))

    def test_low_signal_volume_warns(self):
        data = plan()
        data["channels"][0]["ad_sets"] = 4
        errors, warnings = check_media_plan.check(data)
        self.assertEqual(errors, [])
        self.assertTrue(any("events per ad set per week" in w for w in warnings))

    def test_forecast_order_and_source_of_truth(self):
        data = plan(measurement={})
        data["channels"][0]["forecast"] = {"conversions": {"low": 90, "base": 60, "high": 120}}
        errors, _ = check_media_plan.check(data)
        self.assertTrue(any("low <= base <= high" in e for e in errors))
        self.assertTrue(any("source_of_truth" in e for e in errors))

    def test_draft_signals_warn(self):
        data = plan(approved_by="", targets={"allowable_cac": "[NEEDS INPUT: margin]"})
        _, warnings = check_media_plan.check(data)
        self.assertTrue(any("draft" in w for w in warnings))
        self.assertTrue(any("economic anchor" in w for w in warnings))
        self.assertTrue(any("NEEDS INPUT" in w for w in warnings))


CONTEXT = """# Brand truth — Test
Last reviewed: 2026-11-01

## 1. Identity
| Field | Value | Status | Source | Checked |
|---|---|---|---|---|
| Name | Test Co | verified | Intake | 2026-11-01 |

## 2. Offerings
## 4. Claim register
| Claim ID | Exact approved wording | Proof / source | Restrictions | Status | Expires |
|---|---|---|---|---|---|
| C1 | Ships in 2 days | Policy page | US | verified | 2027-01-01 |

## 7. Voice rules
"""


class TestContextFile(unittest.TestCase):
    def test_example_has_no_errors(self):
        text = (ROOT / "examples/brand-truth-example.md").read_text(encoding="utf-8")
        errors, warnings = check_context_file.check(text, today=TODAY)
        self.assertEqual(errors, [])
        self.assertTrue(any("NEEDS INPUT" in w for w in warnings))

    def test_clean_file_passes(self):
        self.assertEqual(check_context_file.check(CONTEXT, today=TODAY), ([], []))

    def test_invalid_status_and_missing_section(self):
        text = CONTEXT.replace("| verified | Intake |", "| proven | Intake |").replace("## 7. Voice rules\n", "")
        errors, _ = check_context_file.check(text, today=TODAY)
        self.assertTrue(any("status 'proven'" in e for e in errors))
        self.assertTrue(any("voice rules" in e for e in errors))

    def test_stale_and_expired_warn(self):
        errors, warnings = check_context_file.check(CONTEXT, today=date(2027, 6, 1))
        self.assertEqual(errors, [])
        self.assertTrue(any("Last reviewed" in w for w in warnings))
        self.assertTrue(any("expired" in w for w in warnings))

    def test_secrets_are_errors(self):
        errors, _ = check_context_file.check(CONTEXT + "\napi_key: abcdef123456\n", today=TODAY)
        self.assertTrue(any("never store secrets" in e for e in errors))


class TestPageMeta(unittest.TestCase):
    def test_example_page_is_clean(self):
        html = (ROOT / "examples/landing-page-skeleton.html").read_text(encoding="utf-8")
        self.assertEqual(check_page_meta.check(html), ([], []))

    def test_missing_basics_are_errors(self):
        errors, warnings = check_page_meta.check("<html><body><img src='a.jpg'><input name='email'></body></html>")
        for needle in ("<title>", "meta description", "viewport", "<h1>", "alt attribute", "no label"):
            self.assertTrue(any(needle in e for e in errors), needle)
        self.assertTrue(any("og:title" in w for w in warnings))

    def test_design_and_copy_warnings(self):
        links = "".join(f'<a href="/p{i}">Page {i}</a>' for i in range(12))
        dense = "Notwithstanding organizational considerations, comprehensive implementation methodologies necessitate extraordinarily sophisticated infrastructural prerequisites. " * 10
        html = ('<html lang="en"><head><title>T</title><meta name="description" content="d">'
                '<meta name="viewport" content="width=device-width"><script src="a.js"></script></head><body>'
                '<h1>Hi</h1><h3>Skipped</h3><img src="a.jpg" alt="a" loading="lazy">'
                '<form><label for="e">Email</label><input id="e" name="email" type="text">'
                '<label>Phone <input name="phone"></label><button>Submit</button></form>'
                + links + "<p>" + dense + "</p></body></html>")
        errors, warnings = check_page_meta.check(html)
        self.assertEqual(errors, [])
        for needle in ("skip from h1 to h3", "width and height", "lazy-loaded", "without async or defer",
                       'type="email"', 'type="tel"', "Generic button", "links lead away", "reads at about grade"):
            self.assertTrue(any(needle in w for w in warnings), needle)

    def test_reading_grade_is_low_for_plain_copy(self):
        grade, words = check_page_meta.reading_grade("We ship in two days. You can send it back. It is made of silver. " * 10)
        self.assertGreater(words, 100)
        self.assertLess(grade, 6)

    def test_bad_jsonld_and_marker(self):
        html = (ROOT / "examples/landing-page-skeleton.html").read_text(encoding="utf-8")
        html = html.replace('"@type": "Product",', '"@type": "Product"').replace("$68.", "[NEEDS INPUT: price].")
        errors, _ = check_page_meta.check(html)
        self.assertTrue(any("not valid JSON" in e for e in errors))
        self.assertTrue(any("unresolved" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
