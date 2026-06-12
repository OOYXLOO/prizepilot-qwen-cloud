import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicPagesTests(unittest.TestCase):
    def test_judge_pack_is_linked_from_public_hub(self) -> None:
        hub = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        judge_pack = (ROOT / "docs" / "judge-pack" / "index.html").read_text(encoding="utf-8")

        self.assertIn("./judge-pack/", hub)
        self.assertIn("./award-preflight/", hub)
        self.assertIn("./award-evidence-map/", hub)
        self.assertIn("./cloud-readiness/", hub)
        self.assertIn("./benchmark-method/", hub)
        self.assertIn("./live-proof-gate/", hub)
        self.assertIn("./qwen-live-proof/", hub)
        self.assertIn("./qwen-contribution/", hub)
        self.assertIn("./alibaba-endpoint-checklist/", hub)
        self.assertIn("./api/plan.json", hub)
        self.assertIn("./prizepilot-qwen-submission-deck.pptx", hub)
        self.assertIn("Primary judge actions", hub)
        self.assertIn("Watch Demo", hub)
        self.assertIn("Read Blog Award Story", hub)
        self.assertIn("Verify Proof Boundary", hub)
        self.assertIn("Judge Evidence Pack", hub)
        self.assertIn("Award Preflight", hub)
        self.assertIn("Award Evidence Map", hub)
        self.assertIn("Cloud Readiness", hub)
        self.assertIn("Benchmark Method", hub)
        self.assertIn("Live Proof Gate", hub)
        self.assertIn("Qwen Live Proof", hub)
        self.assertIn("Qwen Contribution Map", hub)
        self.assertIn("Alibaba Endpoint Checklist", hub)
        self.assertIn("Static Plan JSON", hub)
        self.assertIn("Presentation Deck", hub)
        self.assertIn("Blog Award Story", hub)
        self.assertIn("Qwen Cloud Track 4 judge packet", judge_pack)
        self.assertIn("https://devpost.com/software/prizepilot-qwen-cloud", judge_pack)
        self.assertIn("https://vimeo.com/1200124146", judge_pack)
        self.assertIn("../award-preflight/", judge_pack)
        self.assertIn("../award-evidence-map/", judge_pack)
        self.assertIn("../cloud-readiness/", judge_pack)
        self.assertIn("../benchmark-method/", judge_pack)
        self.assertIn("../live-proof-gate/", judge_pack)
        self.assertIn("../qwen-live-proof/", judge_pack)
        self.assertIn("../qwen-contribution/", judge_pack)
        self.assertIn("../alibaba-endpoint-checklist/", judge_pack)
        self.assertIn("../api/plan.json", judge_pack)
        self.assertIn("../prizepilot-qwen-submission-deck.pptx", judge_pack)
        self.assertIn("Prize Decision Summary", judge_pack)
        self.assertIn("Blog Post Award first", judge_pack)
        self.assertIn("Honorable Mention second", judge_pack)
        self.assertIn("Qwen Contribution Depth", judge_pack)
        self.assertIn("stage-by-stage contribution evidence", judge_pack)
        self.assertIn("endpoint checklist", judge_pack)
        self.assertIn("It does not claim that prize selection is statistically predictable", judge_pack)
        self.assertIn("../screenshots/prizepilot-dashboard-desktop.png", judge_pack)
        self.assertTrue((ROOT / "docs" / "prizepilot-qwen-submission-deck.pptx").is_file())
        self.assertTrue((ROOT / "docs" / "screenshots" / "prizepilot-dashboard-desktop.png").is_file())
        self.assertTrue((ROOT / "docs" / "award-preflight" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "award-evidence-map" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "cloud-readiness" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "benchmark-method" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "benchmark-method.md").is_file())
        self.assertTrue((ROOT / "docs" / "qwen-live-proof" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "qwen-contribution" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "qwen-contribution-map.md").is_file())
        self.assertTrue((ROOT / "docs" / "alibaba-endpoint-checklist" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "alibaba-endpoint-judge-checklist.md").is_file())
        self.assertTrue((ROOT / "docs" / "api" / "plan.json").is_file())

    def test_readme_exposes_judge_pack_url(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/award-preflight/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/award-evidence-map/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/cloud-readiness/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/benchmark-method/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/live-proof-gate/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-live-proof/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-contribution/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/alibaba-endpoint-checklist/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/api/plan.json", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/prizepilot-qwen-submission-deck.pptx", readme)
        self.assertIn("Public Blog Award story", readme)

    def test_static_plan_snapshot_matches_public_claim_boundary(self) -> None:
        snapshot = json.loads((ROOT / "docs" / "api" / "plan.json").read_text(encoding="utf-8"))

        self.assertEqual(snapshot["project"], "PrizePilot")
        self.assertEqual(snapshot["track"], "Track 4 - Autopilot Agent")
        self.assertEqual(snapshot["qwen_plan"]["target_prize"]["name"], "Blog Post Award")
        self.assertEqual(snapshot["submission_status"]["phase"], "submitted_can_still_improve")
        self.assertEqual(
            snapshot["submission_status"]["qwen_live_proof_url"],
            "https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-live-proof/",
        )
        self.assertIn(
            "Qwen/DashScope live refinement is verified",
            snapshot["evidence_gaps"][0],
        )
        self.assertIn(
            "no live endpoint has been verified",
            snapshot["evidence_gaps"][1],
        )

    def test_blog_post_award_story_has_judge_path(self) -> None:
        blog = (ROOT / "docs" / "blog" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Cloud Hackathon blog award story", blog)
        self.assertIn("Blog Post Award reader path", blog)
        self.assertIn("../judge-pack/", blog)
        self.assertIn("../cloud-readiness/", blog)
        self.assertIn("https://vimeo.com/1200124146", blog)
        self.assertIn("https://github.com/OOYXLOO/prizepilot-qwen-cloud", blog)
        self.assertIn("what remains account-gated", blog)
        self.assertIn("../benchmark-method/", blog)
        self.assertIn("Benchmark method", blog)

    def test_benchmark_method_documents_scoring_limits(self) -> None:
        markdown = (ROOT / "docs" / "benchmark-method.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "benchmark-method" / "index.html").read_text(encoding="utf-8")

        self.assertIn("PrizePilot Benchmark Method", markdown)
        self.assertIn("Sample Portfolio", markdown)
        self.assertIn("Scoring Method", markdown)
        self.assertIn("not a statistical prediction of winning", markdown)
        self.assertIn("PrizePilot benchmark method", page)
        self.assertIn("Sample Portfolio", page)
        self.assertIn("Reproduce Locally", page)
        self.assertIn("../api/plan.json", page)

    def test_cloud_readiness_page_names_no_secret_checks(self) -> None:
        page = (ROOT / "docs" / "cloud-readiness" / "index.html").read_text(encoding="utf-8")

        self.assertIn("PrizePilot Cloud Readiness", page)
        self.assertIn("python -m prizepilot cloud-readiness", page)
        self.assertIn("Qwen-compatible request shape", page)
        self.assertIn("Alibaba Function Compute manifest", page)
        self.assertIn("Runtime-only secret boundary", page)
        self.assertIn("Qwen live smoke proof", page)
        self.assertIn("../cloud-readiness-report.md", page)

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
        self.assertIn("../qwen-live-proof/", gate_html)

    def test_qwen_contribution_map_explains_live_model_role(self) -> None:
        markdown = (ROOT / "docs" / "qwen-contribution-map.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "qwen-contribution" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Contribution Map", markdown)
        self.assertIn("not presented as a magic prize predictor", markdown)
        self.assertIn("route-plan clarity", (ROOT / "docs" / "submission-story.md").read_text(encoding="utf-8"))
        self.assertIn("PrizePilot Qwen Contribution Map", page)
        self.assertIn("Qwen refines PrizePilot's plan", page)
        self.assertIn("Contribution Matrix", page)
        self.assertIn("no premature publishing", page)
        self.assertIn("../qwen-live-proof/", page)

    def test_alibaba_endpoint_checklist_keeps_endpoint_pending(self) -> None:
        markdown = (ROOT / "docs" / "alibaba-endpoint-judge-checklist.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "alibaba-endpoint-checklist" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Alibaba Endpoint Judge Checklist", markdown)
        self.assertIn("Do not mark any item complete until a live public endpoint exists", markdown)
        self.assertIn("GET /api/plan", page)
        self.assertIn("Live Alibaba public endpoint", page)
        self.assertIn("Pending", page)
        self.assertIn("account-owner-approved Alibaba endpoint proof", (ROOT / "docs" / "devpost-project-fields.md").read_text(encoding="utf-8"))

    def test_award_preflight_keeps_live_claims_gated(self) -> None:
        preflight = (ROOT / "docs" / "award-preflight" / "index.html").read_text(encoding="utf-8")

        self.assertIn("PrizePilot Qwen Award Preflight", preflight)
        self.assertIn("public-evidence ready", preflight)
        self.assertIn("../cloud-readiness/", preflight)
        self.assertIn("Blog Post Award", preflight)
        self.assertIn("Honorable Mention", preflight)
        self.assertIn("Submitted", preflight)
        self.assertIn("Public evidence ready", preflight)
        self.assertIn("Narrative ready and public", preflight)
        self.assertIn("Public review ready", preflight)
        self.assertIn("Qwen/DashScope integration", preflight)
        self.assertIn("Live Qwen/DashScope smoke proof verified", preflight)
        self.assertIn("live endpoint not claimed", preflight)
        self.assertIn("Do not publish API keys", preflight)
        self.assertIn("../award-evidence-map/", preflight)
        self.assertIn("../qwen-live-proof/", preflight)

    def test_award_evidence_map_compresses_public_and_gated_signals(self) -> None:
        evidence_map = (ROOT / "docs" / "award-evidence-map" / "index.html").read_text(encoding="utf-8")

        self.assertIn("PrizePilot Qwen Award Evidence Map", evidence_map)
        self.assertIn("../cloud-readiness/", evidence_map)
        self.assertIn("Blog Post Award", evidence_map)
        self.assertIn("Top 10 Honorable Mention", evidence_map)
        self.assertIn("Track 4 Autopilot Agent", evidence_map)
        self.assertIn("35", evidence_map)
        self.assertIn("Narrative ready", evidence_map)
        self.assertIn("Public review ready", evidence_map)
        self.assertIn("Agent fit ready", evidence_map)
        self.assertIn("Reproducible", evidence_map)
        self.assertIn("Qwen/DashScope live model proof", evidence_map)
        self.assertIn("Alibaba Cloud endpoint proof", evidence_map)
        self.assertIn("Account-gated", evidence_map)
        self.assertIn("completed live Qwen/DashScope smoke proof", evidence_map)
        self.assertIn("../qwen-live-proof/", evidence_map)

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
