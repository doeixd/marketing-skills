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

    def test_brand_discovery_subworkflow(self):
        paths = (
            'workflows/03a-brand-discovery-and-messaging.md',
            'references/brand-voice-and-copy-system.md',
            'templates/brand-discovery-intake.md',
            'templates/brand-messaging-library.md',
            'examples/brand-discovery-to-copy.md',
        )
        for name in paths:
            self.assertTrue((ROOT / name).is_file(), name)
        workflow = (ROOT / paths[0]).read_text(encoding='utf-8')
        for heading in ('brand reality', 'voice', 'selling points', 'headline', 'description', 'Handoff'):
            self.assertIn(heading.lower(), workflow.lower())

    def test_offering_discovery_subworkflow(self):
        paths = (
            'workflows/01a-offering-discovery-and-marketing-plan.md',
            'references/offering-research-and-marketing-planning.md',
            'templates/offering-discovery-intake.md',
            'templates/offering-dossier-and-marketing-plan.md',
            'examples/offering-discovery-to-marketing-plan.md',
        )
        for name in paths:
            self.assertTrue((ROOT / name).is_file(), name)
        workflow = (ROOT / paths[0]).read_text(encoding='utf-8').lower()
        for term in ('brand', 'buyer', 'alternatives', 'feature', 'benefit', 'drawback', 'objection', 'pricing', 'assurances', 'creative', 'headline', 'description', 'handoff'):
            self.assertIn(term, workflow)
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('(workflows/01a-offering-discovery-and-marketing-plan.md)', skill)
        plan = (ROOT / 'WORKFLOWS.md').read_text(encoding='utf-8')
        self.assertIn('Workflow 1A', plan)

    def test_core_handoffs_present(self):
        for name in ("WORKFLOWS.md", "templates/operating-brief.md", "templates/creative-production-brief.md", "templates/experiment-decision-log.md", "examples/workflow-from-research-to-sales.md"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_skill_links_to_orchestration(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("(WORKFLOWS.md)", skill)
        self.assertIn("decision packet", skill)

if __name__ == "__main__":
    unittest.main()
