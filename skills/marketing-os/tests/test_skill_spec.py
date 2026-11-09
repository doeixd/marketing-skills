import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_skill_spec import check


def make_skill(tmp: Path, dirname: str, frontmatter: str, body: str = "# Skill\n") -> Path:
    skill = tmp / dirname
    (skill / "workflows").mkdir(parents=True)
    (skill / "SKILL.md").write_text(f"---\n{frontmatter}\n---\n\n{body}", encoding="utf-8")
    return skill


class TestSkillSpec(unittest.TestCase):
    def test_repository_skill_passes(self):
        errors, warnings = check(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_name_must_match_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = make_skill(Path(tmp), "real-name", "name: other-name\ndescription: Does a thing.")
            errors, _ = check(skill)
            self.assertTrue(any("match directory" in e for e in errors))

    def test_invalid_name_and_long_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = make_skill(Path(tmp), "Bad_Name", f"name: Bad_Name\ndescription: {'x' * 1025}")
            errors, _ = check(skill)
            self.assertTrue(any("lowercase" in e for e in errors))
            self.assertTrue(any("description is 1025" in e for e in errors))

    def test_token_budget_and_unrouted_workflow(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = make_skill(Path(tmp), "big", "name: big\ndescription: Big.", "word " * 5000)
            (skill / "workflows" / "01-orphan.md").write_text("# Orphan\n", encoding="utf-8")
            errors, _ = check(skill)
            self.assertTrue(any("tokens" in e for e in errors))
            self.assertTrue(any("01-orphan.md is not routed" in e for e in errors))

    def test_context_file_and_needs_input_contract_wired(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(".marketing-context/brand-truth.md", skill)
        self.assertIn("(templates/marketing-context.md)", skill)
        self.assertIn("[NEEDS INPUT", skill)
        self.assertIn("(references/core-reasoning-chain.md)", skill)
        for wf in ("workflows/01a-offering-discovery-and-marketing-plan.md", "workflows/03a-brand-discovery-and-messaging.md", "WORKFLOWS.md"):
            self.assertIn("marketing-context.md", (ROOT / wf).read_text(encoding="utf-8"), wf)
        template = (ROOT / "templates/marketing-context.md").read_text(encoding="utf-8")
        for term in ("Claim register", "Voice rules", "[NEEDS INPUT", "No secrets"):
            self.assertIn(term, template)


if __name__ == "__main__":
    unittest.main()
