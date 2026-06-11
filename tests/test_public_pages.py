import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicPagesTests(unittest.TestCase):
    def test_judge_pack_is_linked_from_public_hub(self) -> None:
        hub = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        judge_pack = (ROOT / "docs" / "judge-pack" / "index.html").read_text(encoding="utf-8")

        self.assertIn("./judge-pack/", hub)
        self.assertIn("Judge Evidence Pack", hub)
        self.assertIn("Qwen Cloud Track 4 judge packet", judge_pack)
        self.assertIn("https://devpost.com/software/prizepilot-qwen-cloud", judge_pack)
        self.assertIn("https://vimeo.com/1200124146", judge_pack)
        self.assertIn("../screenshots/prizepilot-dashboard-desktop.png", judge_pack)
        self.assertTrue((ROOT / "docs" / "screenshots" / "prizepilot-dashboard-desktop.png").is_file())

    def test_readme_exposes_judge_pack_url(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/", readme)

    def test_devpost_fields_do_not_publish_identity_inferences(self) -> None:
        fields = (ROOT / "docs" / "devpost-project-fields.md").read_text(encoding="utf-8")

        forbidden_fragments = [
            "phone number",
            "Asia/Shanghai",
            "inferred from",
        ]
        for fragment in forbidden_fragments:
            self.assertNotIn(fragment, fields)


if __name__ == "__main__":
    unittest.main()
