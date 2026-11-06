"""Ensure the modular marketing workflows and handoffs remain present."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestWorkflows(unittest.TestCase):
    def test_all_nine_workflows_present(self):
        files = sorted((ROOT / "workflows").glob("[0-9][0-9]-*.md"))
        self.assertEqual(len(files), 9)
        for p in files:
            txt = p.read_text(encoding="utf-8")
            self.assertIn("Workflow ", txt)
            self.assertIn("Handoff", txt)

    def test_core_handoffs_present(self):
        for name in ("WORKFLOWS.md", "templates/operating-brief.md", "templates/creative-production-brief.md", "templates/experiment-decision-log.md", "examples/workflow-from-research-to-sales.md"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_skill_links_to_orchestration(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("(WORKFLOWS.md)", skill)
        self.assertIn("decision packet", skill)

if __name__ == "__main__":
    unittest.main()
