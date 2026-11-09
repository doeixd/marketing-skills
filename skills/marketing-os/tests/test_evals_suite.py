import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
EVALS = REPO / "evals"
GRADER_TYPES = {"regex", "tool_used", "tool_order", "file_exists", "llm", "baseline"}


def frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n"), "missing frontmatter"
    block = text[4:text.index("\n---", 4)]
    return dict(line.split(":", 1) for line in block.splitlines() if ":" in line)


@unittest.skipUnless(EVALS.is_dir(), "repo-level evals/ not present (skill installed standalone)")
class TestEvalSuite(unittest.TestCase):
    def cases(self):
        return sorted(d for d in EVALS.iterdir() if d.is_dir() and d.name != "results")

    def test_every_case_has_prompt_and_valid_graders(self):
        cases = self.cases()
        self.assertGreaterEqual(len(cases), 40)
        for case in cases:
            prompt = (case / "prompt.md").read_text(encoding="utf-8")
            fields = frontmatter(prompt)
            self.assertIn("tags", fields, case.name)
            self.assertTrue(prompt.split("\n---\n", 1)[1].strip(), f"{case.name}: empty prompt")
            graders = list((case / "graders").glob("*.md"))
            self.assertTrue(graders, f"{case.name}: no graders")
            for grader in graders:
                gtype = frontmatter(grader.read_text(encoding="utf-8")).get("type", "").strip()
                self.assertIn(gtype, GRADER_TYPES, f"{grader}")

    def test_routing_targets_exist(self):
        workflows = [p.name for p in (ROOT / "workflows").glob("*.md")]
        for case in self.cases():
            if not case.name.startswith("route-"):
                continue
            text = (case / "graders" / "reads-workflow.md").read_text(encoding="utf-8")
            pattern = re.search(r"input_match: '([^']+)'", text).group(1)
            for fragment in pattern.split("|"):
                self.assertTrue(any(fragment in name for name in workflows), f"{case.name}: no workflow matches {fragment}")

    def test_prompts_do_not_name_the_skill(self):
        for case in self.cases():
            body = (case / "prompt.md").read_text(encoding="utf-8").split("\n---\n", 1)[1].lower()
            self.assertNotIn("marketing os", body, case.name)
            self.assertNotIn("marketing-os", body, case.name)

    def test_portable_copy_and_plugin_manifest(self):
        portable = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
        self.assertEqual(portable["skill_name"], "marketing-os")
        self.assertGreaterEqual(len(portable["evals"]), 30)
        manifest = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        version = re.search(r"version: '([^']+)'", (ROOT / "SKILL.md").read_text(encoding="utf-8")).group(1)
        self.assertEqual(manifest["version"], version, "plugin.json version must match SKILL.md metadata.version")


if __name__ == "__main__":
    unittest.main()
