"""Structural tests for Google Ads RSA draft preflight."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_search_ads", ROOT / "scripts" / "check_search_ads.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def ad():
    return {
        "name": "Test",
        "headlines": ["Example Brand", "A useful product", "See real details"],
        "descriptions": ["A truthful short description.", "Review the actual features and product page."],
        "brand_name": "Example Brand",
        "require_brand_cue": True,
        "publication_approved": False,
    }


class TestGoogleSearchAds(unittest.TestCase):
    def test_example_file(self):
        data = json.loads((ROOT / "examples" / "google-search-rsa-draft.json").read_text(encoding="utf-8"))
        self.assertEqual(validator.validate(data), [])

    def test_lengths(self):
        value = ad()
        value["headlines"][0] = "X" * 31
        value["descriptions"][0] = "Y" * 91
        errors = validator.validate({"ads": [value]})
        self.assertTrue(any("max 30" in e for e in errors))
        self.assertTrue(any("max 90" in e for e in errors))

    def test_asset_counts(self):
        value = ad()
        value["headlines"] = ["Only one"]
        value["descriptions"] = ["One"]
        errors = validator.validate({"ads": [value]})
        self.assertTrue(any("3–15" in e for e in errors))
        self.assertTrue(any("2–4" in e for e in errors))

    def test_duplicates_and_brand(self):
        value = ad()
        value["headlines"] = ["Amazing Thing", " amazing   thing ", "More details"]
        errors = validator.validate({"ads": [value]})
        self.assertTrue(any("duplicate headline" in e for e in errors))
        self.assertTrue(any("brand cue" in e for e in errors))

    def test_unapproved_draft_allowed(self):
        self.assertEqual(validator.validate({"ads": [ad()]}), [])

    def test_publish_safety(self):
        value = ad()
        value["publication_approved"] = True
        value["final_url"] = "https://example.com/draft"
        errors = validator.validate({"ads": [value]})
        self.assertTrue(any("claims_verified" in e for e in errors))
        self.assertTrue(any("conversion_validated" in e for e in errors))
        self.assertTrue(any("non-example https final_url" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
