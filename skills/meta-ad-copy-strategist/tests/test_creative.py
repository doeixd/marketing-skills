"""Check creative manifest linting and release gates."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT / "scripts"))
from check_creative import check


class TestCreative(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample = json.loads((ROOT / "examples/creative-manifest.json").read_text())

    def test_example_manifest_is_a_valid_draft(self):
        errors, _ = check(self.sample)
        self.assertFalse(errors, errors)

    def test_publish_requires_permission_and_rights(self):
        sample = json.loads(json.dumps(self.sample))
        sample["status"] = "publish_ready"
        errors, _ = check(sample)
        self.assertTrue(any("rights not cleared" in x for x in errors))
        self.assertTrue(any("explicit_launch_approval" in x for x in errors))

    def test_vertical_wrong_ratio_warns(self):
        sample = json.loads(json.dumps(self.sample))
        sample["assets"][0]["width"] = 1440
        sample["assets"][0]["height"] = 1800
        errors, warnings = check(sample)
        self.assertFalse(errors)
        self.assertTrue(any("not a 9:16 master" in x for x in warnings))

    def test_overlay_outside_safe_zone_warns(self):
        sample = json.loads(json.dumps(self.sample))
        sample["assets"][0]["overlay_boxes"][0]["y"] = 0.90
        errors, warnings = check(sample)
        self.assertFalse(errors)
        self.assertTrue(any("safe zone" in x for x in warnings))

    def test_overlay_outside_frame_errors(self):
        sample = json.loads(json.dumps(self.sample))
        sample["assets"][0]["overlay_boxes"][0]["y"] = 1.01
        errors, _ = check(sample)
        self.assertTrue(any("frame bounds" in x for x in errors))

    def test_duplicated_concepts_rejected(self):
        sample = json.loads(json.dumps(self.sample))
        sample["concepts"][1]["id"] = sample["concepts"][0]["id"]
        errors, _ = check(sample)
        self.assertTrue(any("unique nonempty id" in x for x in errors))

    def test_references_available(self):
        for file in [
            "references/visual-direction.md", "references/meta-placement-playbook.md",
            "references/video-storytelling.md", "references/platform-idioms-and-voice.md",
            "references/creator-partnerships-and-rights.md", "references/creative-quality-control.md",
            "templates/creative-direction-brief.md", "templates/shot-list-and-storyboard.md",
            "templates/creative-review-scorecard.md", "examples/reels-creative-direction.md",
        ]:
            self.assertTrue((ROOT / file).exists(), file)
