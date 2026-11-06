import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_copy import check


class TestCopyLint(unittest.TestCase):
    def test_valid(self):
        errors, warnings = check({"evidence": [{"id": "E1", "status": "verified"}], "angles": [{"angle_id": "A"}], "ads": [{"angle_id": "A", "primary_text": "Explore unique rings.", "headline": "Browse Rings", "description": "Shop now", "evidence_ids": ["E1"]}]})
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_missing_text(self):
        errors, _ = check({"ads": [{"headline": "A"}]})
        self.assertTrue(any("primary_text" in x for x in errors))

    def test_bad_evidence_status(self):
        errors, _ = check({"evidence": [{"id": "E1", "status": "made-up"}], "ads": [{"primary_text": "A", "headline": "B"}]})
        self.assertTrue(any("status" in x for x in errors))

    def test_advisory_length_warning(self):
        errors, warnings = check({"ads": [{"primary_text": "x" * 126, "headline": "Browse"}]})
        self.assertFalse(errors)
        self.assertTrue(any("advisory" in x for x in warnings))

    def test_duplicate_angle_ids(self):
        errors, _ = check({"angles": [{"angle_id": "A"}, {"angle_id": "A"}], "ads": [{"angle_id": "A", "primary_text": "A", "headline": "B"}]})
        self.assertTrue(any("Duplicate angle" in x for x in errors))

    def test_brand_campaign_requires_brand_cue(self):
        errors, warnings = check({"campaign_mode": "brand", "angles": [{"angle_id": "A"}], "ads": [{"angle_id": "A", "primary_text": "See our rings.", "headline": "Explore rings"}]})
        self.assertEqual(errors, [])
        self.assertTrue(any("brand_cue" in x for x in warnings))

    def test_unknown_buyer_reference_warns(self):
        errors, warnings = check({"buyer_situations": [{"id": "b1"}], "angles": [{"angle_id": "A", "buyer_situation_id": "b2"}], "ads": [{"angle_id": "A", "primary_text": "See rings.", "headline": "Explore rings"}]})
        self.assertEqual(errors, [])
        self.assertTrue(any("unknown buyer" in x for x in warnings))

    def test_repeated_motive_warns(self):
        errors, warnings = check({"angles": [{"angle_id": "A", "motivation": "gifting"}, {"angle_id": "B", "motivation": "gifting"}], "ads": [{"angle_id": "A", "primary_text": "Rings for gifting.", "headline": "Gift rings"}]})
        self.assertEqual(errors, [])
        self.assertTrue(any("same motivation" in x for x in warnings))


if __name__ == "__main__":
    unittest.main()
