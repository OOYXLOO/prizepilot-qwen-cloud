import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicPagesTests(unittest.TestCase):
    def test_judge_pack_is_linked_from_public_hub(self) -> None:
        hub = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        judge_pack = (ROOT / "docs" / "judge-pack" / "index.html").read_text(encoding="utf-8")

        self.assertIn("./judge-pack/", hub)
        self.assertIn("./award-preflight/", hub)
        self.assertIn("./live-proof-gate/", hub)
        self.assertIn("./prizepilot-qwen-submission-deck.pptx", hub)
        self.assertIn("Judge Evidence Pack", hub)
        self.assertIn("Award Preflight", hub)
        self.assertIn("Live Proof Gate", hub)
        self.assertIn("Presentation Deck", hub)
        self.assertIn("Blog Award Story", hub)
        self.assertIn("Qwen Cloud Track 4 judge packet", judge_pack)
        self.assertIn("https://devpost.com/software/prizepilot-qwen-cloud", judge_pack)
        self.assertIn("https://vimeo.com/1200124146", judge_pack)
        self.assertIn("../award-preflight/", judge_pack)
        self.assertIn("../live-proof-gate/", judge_pack)
        self.assertIn("../prizepilot-qwen-submission-deck.pptx", judge_pack)
        self.assertIn("../screenshots/prizepilot-dashboard-desktop.png", judge_pack)
        self.assertTrue((ROOT / "docs" / "prizepilot-qwen-submission-deck.pptx").is_file())
        self.assertTrue((ROOT / "docs" / "screenshots" / "prizepilot-dashboard-desktop.png").is_file())
        self.assertTrue((ROOT / "docs" / "award-preflight" / "index.html").is_file())

    def test_readme_exposes_judge_pack_url(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/award-preflight/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/live-proof-gate/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/prizepilot-qwen-submission-deck.pptx", readme)
        self.assertIn("Public Blog Award story", readme)

    def test_blog_post_award_story_has_judge_path(self) -> None:
        blog = (ROOT / "docs" / "blog" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Cloud Hackathon blog award story", blog)
        self.assertIn("Blog Post Award reader path", blog)
        self.assertIn("../judge-pack/", blog)
        self.assertIn("https://vimeo.com/1200124146", blog)
        self.assertIn("https://github.com/OOYXLOO/prizepilot-qwen-cloud", blog)
        self.assertIn("what remains account-gated", blog)

    def test_live_proof_gate_names_secret_boundaries(self) -> None:
        gate = (ROOT / "docs" / "live-proof-gate.md").read_text(encoding="utf-8")
        gate_html = (ROOT / "docs" / "live-proof-gate" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen/DashScope Live Proof", gate)
        self.assertIn("Alibaba Cloud Endpoint Proof", gate)
        self.assertIn("Do not publish raw request headers", gate)
        self.assertIn("Do not publish Alibaba account IDs", gate)
        self.assertIn("Devpost updated only with proof that actually happened", gate)
        self.assertIn("PrizePilot Live Proof Gate", gate_html)
        self.assertIn("Live proof is a gated action", gate_html)
        self.assertIn("Do not publish raw request headers", gate_html)
        self.assertIn("Do not publish Alibaba account IDs", gate_html)

    def test_award_preflight_keeps_live_claims_gated(self) -> None:
        preflight = (ROOT / "docs" / "award-preflight" / "index.html").read_text(encoding="utf-8")

        self.assertIn("PrizePilot Qwen Award Preflight", preflight)
        self.assertIn("Blog Post Award", preflight)
        self.assertIn("Honorable Mention", preflight)
        self.assertIn("Submitted", preflight)
        self.assertIn("Qwen/DashScope integration", preflight)
        self.assertIn("live endpoint not claimed", preflight)
        self.assertIn("Do not publish API keys", preflight)

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
