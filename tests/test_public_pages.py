import json
import re
import unittest
from pathlib import Path

from prizepilot.webapp import dashboard_payload

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
        self.assertIn("./qwen-before-after/", hub)
        self.assertIn("./judge-review-card/", hub)
        self.assertIn("./official-requirement-fit/", hub)
        self.assertIn("./award-thesis-scorecard/", hub)
        self.assertIn("./blog-share-packet/", hub)
        self.assertIn("./public-update-checklist/", hub)
        self.assertIn("./public-update-digest/", hub)
        self.assertIn("./alibaba-endpoint-checklist/", hub)
        self.assertIn("./judge-manifest.json", hub)
        self.assertIn("./api/plan.json", hub)
        self.assertIn("./prizepilot-qwen-submission-deck.pptx", hub)
        self.assertIn("Primary judge actions", hub)
        self.assertIn("Open Devpost", hub)
        self.assertIn("Watch Demo", hub)
        self.assertIn("Read Blog Award Story", hub)
        self.assertNotIn("<strong>Open Judge Card</strong>", hub)
        self.assertIn("3-link reviewer fast path", hub)
        self.assertIn("Confirm the submitted identity", hub)
        self.assertIn("Watch the", hub)
        self.assertIn("After those three actions", hub)
        self.assertIn("do-not-infer boundary", hub)
        self.assertIn("Judge Evidence Pack", hub)
        self.assertIn("Award Preflight", hub)
        self.assertIn("Award Evidence Map", hub)
        self.assertIn("Cloud Readiness", hub)
        self.assertIn("Benchmark Method", hub)
        self.assertIn("Live Proof Gate", hub)
        self.assertIn("Qwen Live Proof", hub)
        self.assertIn("Qwen Contribution Map", hub)
        self.assertIn("Qwen Before/After Evidence", hub)
        self.assertIn("Judge Review Card", hub)
        self.assertIn("Official Requirement Fit", hub)
        self.assertIn("Award Thesis Scorecard", hub)
        self.assertIn("Blog Share Packet", hub)
        self.assertIn("Public Update Checklist", hub)
        self.assertIn("Public Update Digest", hub)
        self.assertIn("Alibaba Endpoint Checklist", hub)
        self.assertIn("Judge Manifest JSON", hub)
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
        self.assertIn("../qwen-before-after/", judge_pack)
        self.assertIn("../judge-review-card/", judge_pack)
        self.assertIn("../official-requirement-fit/", judge_pack)
        self.assertIn("../award-thesis-scorecard/", judge_pack)
        self.assertIn("../blog-share-packet/", judge_pack)
        self.assertIn("../public-update-checklist/", judge_pack)
        self.assertIn("../alibaba-endpoint-checklist/", judge_pack)
        self.assertIn("../judge-manifest.json", judge_pack)
        self.assertIn("../api/plan.json", judge_pack)
        self.assertIn("../prizepilot-qwen-submission-deck.pptx", judge_pack)
        self.assertIn("Prize Decision Summary", judge_pack)
        self.assertIn("Blog Post Award first", judge_pack)
        self.assertIn("Award Thesis Scorecard", judge_pack)
        self.assertIn("3-link reviewer fast path", judge_pack)
        self.assertIn("submitted Devpost project", judge_pack)
        self.assertIn("watch the", judge_pack)
        self.assertIn("Blog Award Story", judge_pack)
        self.assertIn("still-pending Alibaba endpoint proof", judge_pack)
        self.assertIn("Honorable Mention second", judge_pack)
        self.assertIn("Qwen Contribution Depth", judge_pack)
        self.assertIn("stage-by-stage contribution evidence", judge_pack)
        self.assertIn("deterministic-plan to refined-copy trail", judge_pack)
        self.assertIn("Official Requirement Fit", judge_pack)
        self.assertIn("official Qwen requirements", judge_pack)
        self.assertIn("endpoint checklist", judge_pack)
        self.assertIn("local runtime", judge_pack)
        self.assertIn("not live Alibaba endpoint proof", judge_pack)
        self.assertNotIn("live machine-readable", judge_pack)
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
        self.assertTrue((ROOT / "docs" / "qwen-before-after" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "qwen-before-after-evidence.md").is_file())
        self.assertTrue((ROOT / "docs" / "judge-review-card" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "judge-review-card.md").is_file())
        self.assertTrue((ROOT / "docs" / "official-requirement-fit" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "official-requirement-fit.md").is_file())
        self.assertTrue((ROOT / "docs" / "award-thesis-scorecard" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "award-thesis-scorecard.md").is_file())
        self.assertTrue((ROOT / "docs" / "blog-share-packet" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "blog-share-packet.md").is_file())
        self.assertTrue((ROOT / "docs" / "public-update-checklist" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "public-update-checklist.md").is_file())
        self.assertTrue((ROOT / "docs" / "public-update-digest" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "public-update-digest.md").is_file())
        self.assertTrue((ROOT / "docs" / "alibaba-endpoint-checklist" / "index.html").is_file())
        self.assertTrue((ROOT / "docs" / "alibaba-endpoint-judge-checklist.md").is_file())
        self.assertTrue((ROOT / "docs" / "judge-manifest.json").is_file())
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
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-before-after/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-review-card/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/official-requirement-fit/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/award-thesis-scorecard/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/blog-share-packet/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/public-update-checklist/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/public-update-digest/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/alibaba-endpoint-checklist/", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-manifest.json", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/api/plan.json", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/prizepilot-qwen-submission-deck.pptx", readme)
        self.assertIn("https://ooyxloo.github.io/prizepilot-qwen-cloud/demo-video/prizepilot-demo.webm", readme)
        self.assertIn("Baseline links verified live on 2026-06-15", readme)
        self.assertIn("Next-update links that must be HTTP 200 rechecked after a user-approved push", readme)
        self.assertIn("Pages-hosted WebM as a backup playback link", readme)
        self.assertIn("Blog Award story", readme)
        self.assertIn("3-link reviewer fast path", readme)
        self.assertIn("Demo video: https://vimeo.com/1200124146", readme)
        self.assertIn("open the Judge Review Card", readme)
        self.assertIn("Official Requirement Fit map", readme)
        self.assertIn("local runtime machine-readable planning payload", readme)
        self.assertIn("not live Alibaba endpoint proof", readme)
        self.assertNotIn("live machine-readable planning payload", readme)

    def test_judge_manifest_is_machine_readable_and_boundary_safe(self) -> None:
        manifest = json.loads((ROOT / "docs" / "judge-manifest.json").read_text(encoding="utf-8"))

        self.assertEqual(manifest["project"], "PrizePilot")
        self.assertEqual(manifest["submission_status"], "submitted_can_still_improve")
        self.assertNotIn("local_update_base_head", manifest)
        self.assertIn("git rev-parse HEAD", manifest["prepared_head_policy"])
        self.assertEqual(
            [item["label"] for item in manifest["pre_push_required_checks"]],
            ["Final local prepared head", "Current public baseline", "Public side-effect approval"],
        )
        self.assertTrue(
            any("git ls-remote https://github.com/OOYXLOO/prizepilot-qwen-cloud.git HEAD" == item["command"] for item in manifest["pre_push_required_checks"])
        )
        self.assertEqual(manifest["award_targets"][0]["name"], "Blog Post Award")
        self.assertEqual(manifest["award_targets"][0]["amount_usd"], 500)
        self.assertEqual([item["label"] for item in manifest["reviewer_fast_path"]], ["Devpost project", "Demo Video", "Blog Award story"])
        self.assertIn("public demo", manifest["reviewer_fast_path"][1]["purpose"])
        self.assertIn("Blog Post Award fit", manifest["reviewer_fast_path"][2]["purpose"])
        self.assertEqual([item["label"] for item in manifest["demo_video_fallbacks"]], ["Devpost-required hosted video", "Backup Pages-hosted WebM"])
        self.assertIn("demo-video/prizepilot-demo.webm", manifest["demo_video_fallbacks"][1]["url"])
        self.assertIn("not a replacement", manifest["demo_video_fallbacks"][1]["purpose"])
        self.assertEqual(manifest["alibaba_code_proof"]["status"], "prepared_code_only")
        self.assertIn("deploy/alibaba-cloud/s.yaml", manifest["alibaba_code_proof"]["code_file"])
        self.assertIn("not live endpoint proof", manifest["alibaba_code_proof"]["boundary"])
        self.assertEqual(manifest["judge_path"][0]["label"], "Devpost project")
        self.assertEqual(manifest["judge_path"][-1]["label"], "Public update digest")
        self.assertTrue(any(item["label"] == "Demo video" for item in manifest["judge_path"]))
        self.assertTrue(any(item["label"] == "Qwen before/after evidence" for item in manifest["judge_path"]))
        self.assertTrue(any(item["label"] == "Judge review card" for item in manifest["judge_path"]))
        self.assertTrue(any(item["label"] == "Official Requirement Fit" for item in manifest["judge_path"]))
        self.assertTrue(any(item["label"] == "Award Thesis Scorecard" for item in manifest["judge_path"]))
        self.assertTrue(any(item["label"] == "Blog Share Packet" for item in manifest["judge_path"]))
        self.assertTrue(any(item["label"] == "Public update checklist" for item in manifest["judge_path"]))
        self.assertTrue(any(item["label"] == "Public update digest" for item in manifest["judge_path"]))
        self.assertIn("Qwen/DashScope live smoke proof has been recorded without storing secrets.", manifest["completed_evidence"])
        self.assertIn("Backup Pages-hosted WebM demo is available for reviewer playback fallback.", manifest["completed_evidence"])
        self.assertIn("Qwen before/after evidence maps deterministic planning to Qwen-refined public copy.", manifest["completed_evidence"])
        self.assertIn("Official Requirement Fit map connects Qwen rules and judging signals to public evidence while preserving the endpoint boundary.", manifest["completed_evidence"])
        self.assertIn("Judge review card, Award Thesis Scorecard, Blog Share Packet, and public update checklist are prepared for faster review and safer publishing.", manifest["completed_evidence"])
        self.assertEqual(
            [item["requirement"] for item in manifest["official_requirement_fit"]],
            ["Qwen model use", "Track 4 Autopilot Agent", "Alibaba Cloud proof", "Public presentation assets"],
        )
        self.assertEqual(manifest["official_requirement_fit"][2]["status"], "prepared_code_proof_only_live_endpoint_pending")
        self.assertEqual(manifest["pending_evidence"][0]["gate"], "Live Alibaba Cloud endpoint proof")
        self.assertEqual(manifest["pending_evidence"][0]["status"], "pending_account_owner_approval")
        self.assertIn("Do not infer that PrizePilot has won a prize.", manifest["do_not_infer"])
        self.assertIn("Do not infer that payout, tax, KYC, billing, or bank setup is complete.", manifest["do_not_infer"])
        self.assertTrue(manifest["safety_boundary"]["no_secrets"])
        self.assertTrue(manifest["safety_boundary"]["no_live_endpoint_claim_until_verified"])

    def test_official_requirement_fit_page_is_boundary_safe(self) -> None:
        markdown = (ROOT / "docs" / "official-requirement-fit.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "official-requirement-fit" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Official Requirement Fit", markdown)
        self.assertIn("Source reviewed: the public Qwen Cloud Devpost overview/rules page", markdown)
        self.assertIn("Build with Qwen models available on Qwen Cloud", markdown)
        self.assertIn("Track 4 Autopilot Agent", markdown)
        self.assertIn("Proof of Alibaba Cloud deployment / Alibaba services use", markdown)
        self.assertIn("Prepared code proof only; live public endpoint proof remains pending", markdown)
        self.assertIn("Qwen Cloud official requirement fit", page)
        self.assertIn("Build with Qwen models available on Qwen Cloud", page)
        self.assertIn("Track 4 Autopilot Agent", page)
        self.assertIn("Prepared code proof only; live public endpoint remains pending", page)
        self.assertIn("Blog Award Story", page)
        self.assertIn("Do not infer prize selection", page)
        self.assertIn("HTTP 200 at <code>/</code> and <code>/api/plan</code>", page)
        self.assertNotIn("has won", page.lower())
        self.assertNotIn("payout is complete", page.lower())

    def test_public_update_digest_explains_local_public_boundary(self) -> None:
        markdown = (ROOT / "docs" / "public-update-digest.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "public-update-digest" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Public Update Digest", markdown)
        self.assertIn("Last updated: 2026-06-16 (+08)", markdown)
        self.assertNotIn("Last updated: 2026-06-15 (+08)", markdown)
        self.assertNotIn("Last updated: 2026-06-14", markdown)
        self.assertIn("Public repository baseline", markdown)
        self.assertIn("Local prepared update", markdown)
        self.assertIn("Working-copy status", markdown)
        self.assertIn("git ls-remote https://github.com/OOYXLOO/prizepilot-qwen-cloud.git HEAD", markdown)
        self.assertIn("Do not claim PrizePilot has won a prize.", markdown)
        self.assertIn("Do not claim a live Alibaba Cloud public endpoint exists", markdown)
        self.assertIn("Do not claim that the award thesis scorecard predicts prize selection", markdown)
        self.assertIn("official-requirement-fit/", markdown)
        self.assertIn("award-thesis-scorecard/", markdown)
        self.assertIn("Official Requirement Fit map", markdown)
        self.assertIn("Only after the account owner is present", markdown)
        self.assertIn("PrizePilot's public update packet is ready for approval.", page)
        self.assertIn("public repository baseline", page)
        self.assertIn("working copy contains prepared commits after that baseline", page)
        self.assertIn("git ls-remote https://github.com/OOYXLOO/prizepilot-qwen-cloud.git HEAD", page)
        self.assertIn("Link health boundary", page)
        self.assertIn("Recheck", page)
        self.assertIn("HTTP 200 after an approved push", page)
        self.assertIn("Backup Pages-hosted WebM", page)
        self.assertIn("Official Requirement Fit map", page)
        self.assertIn("Award Thesis Scorecard", page)
        self.assertIn("No claim that the Award Thesis Scorecard predicts prize selection", page)
        self.assertIn("No live Alibaba Cloud public endpoint claim", page)
        self.assertIn("../judge-manifest.json", page)
        self.assertIn("../qwen-before-after/", page)
        self.assertIn("../official-requirement-fit/", page)
        self.assertIn("../award-thesis-scorecard/", page)

    def test_judge_review_and_share_packets_keep_claims_safe(self) -> None:
        review_md = (ROOT / "docs" / "judge-review-card.md").read_text(encoding="utf-8")
        review_page = (ROOT / "docs" / "judge-review-card" / "index.html").read_text(encoding="utf-8")
        share_md = (ROOT / "docs" / "blog-share-packet.md").read_text(encoding="utf-8")
        share_page = (ROOT / "docs" / "blog-share-packet" / "index.html").read_text(encoding="utf-8")
        checklist_md = (ROOT / "docs" / "public-update-checklist.md").read_text(encoding="utf-8")
        checklist_page = (ROOT / "docs" / "public-update-checklist" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Judge Review Card", review_md)
        self.assertIn("Last updated: 2026-06-15 (+08)", review_md)
        self.assertNotIn("Last updated: 2026-06-14", review_md)
        self.assertIn("60-Second Path", review_md)
        self.assertIn("Confirm the submitted Devpost identity", review_md)
        self.assertIn("Read the Blog Award story", review_md)
        self.assertIn("Deeper Review", review_md)
        self.assertIn("Qwen before/after evidence", review_md)
        self.assertIn("Award Thesis", review_md)
        self.assertIn("award thesis scorecard", review_md)
        self.assertIn("Do not infer that PrizePilot has won a prize.", review_md)
        self.assertIn("PrizePilot can be reviewed in one minute", review_page)
        self.assertIn("confirm Devpost, watch the demo, read the Blog Award story", review_page)
        self.assertIn("Confirm the submitted Devpost identity", review_page)
        self.assertIn("Read the Blog Award story", review_page)
        self.assertIn("Deeper review:", review_page)
        self.assertIn("../qwen-before-after/", review_page)
        self.assertIn("../award-thesis-scorecard/", review_page)
        self.assertIn("../alibaba-endpoint-checklist/", review_page)

        self.assertIn("Qwen Blog Share Packet", share_md)
        self.assertIn("Last updated: 2026-06-15 (+08)", share_md)
        self.assertNotIn("Last updated: 2026-06-14", share_md)
        self.assertIn("Safe Social Copy", share_md)
        self.assertIn("Most Evidence-Ready", share_md)
        self.assertNotIn("Most Winnable", share_md)
        self.assertIn("Do Not Say", share_md)
        self.assertIn("Do not say PrizePilot won", share_md)
        self.assertIn("Share PrizePilot without overstating", share_page)
        self.assertIn("Most Evidence-Ready", share_page)
        self.assertNotIn("Most Winnable", share_page)
        self.assertIn("../judge-review-card/", share_page)
        self.assertIn("../public-update-checklist/", share_page)

        self.assertIn("Qwen Public Update Checklist", checklist_md)
        self.assertIn("Last updated: 2026-06-15 (+08)", checklist_md)
        self.assertNotIn("Last updated: 2026-06-14", checklist_md)
        self.assertIn("Devpost embedded video playback", checklist_md)
        self.assertIn("$env:PYTHONPATH='src'; python -m unittest discover -s tests -v", checklist_md)
        self.assertIn("$env:PYTHONPATH='src'; python -m unittest discover -s tests -v", checklist_page)
        self.assertIn("Edit Devpost only after the account owner is present", checklist_md)
        self.assertIn("Do not publish stronger claims", checklist_page)
        self.assertIn("Award Thesis Scorecard", checklist_page)
        self.assertIn("No claim that the Award Thesis Scorecard predicts prize selection", checklist_page)
        self.assertIn("../blog-share-packet/", checklist_page)
        self.assertIn("../judge-manifest.json", checklist_page)

    def test_public_ledger_does_not_expose_account_process_residue(self) -> None:
        ledger = (ROOT / "docs" / "qwen-route-ledger.md").read_text(encoding="utf-8").lower()

        for forbidden in [
            "logged-in",
            "active browser",
            "2/5 steps",
            "4/5 steps",
            "edit url",
            "deep link",
            "native windows file picker",
            "final terms box",
        ]:
            self.assertNotIn(forbidden, ledger)

        self.assertIn("no private management urls", ledger)
        self.assertIn("public-safe outcome facts", ledger)

    def test_award_thesis_scorecard_ranks_routes_without_prediction_claim(self) -> None:
        markdown = (ROOT / "docs" / "award-thesis-scorecard.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "award-thesis-scorecard" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Award Thesis Scorecard", markdown)
        self.assertIn("Last updated: 2026-06-15 (+08)", markdown)
        self.assertIn("Blog Post Award", markdown)
        self.assertIn("Top 10 Honorable Mention Projects", markdown)
        self.assertIn("Track 4 Autopilot Agent fit", markdown)
        self.assertIn("not a statistical prediction of winning", markdown)
        self.assertIn("does not claim prize selection, payout, or a live Alibaba Cloud public endpoint", markdown)
        self.assertIn("Award thesis summary", page)
        self.assertIn("strongest route is the Blog Post Award", page)
        self.assertIn("Honorable Mention", page)
        self.assertIn("Endpoint overclaim", page)
        self.assertIn("No live Alibaba endpoint claim exists", page)
        self.assertIn("not a statistical prediction of winning", page)
        self.assertIn("../qwen-before-after/", page)
        self.assertIn("../qwen-contribution/", page)
        self.assertIn("../cloud-readiness/", page)
        self.assertIn("../judge-manifest.json", page)

    def test_public_copy_avoids_devpost_video_overclaim(self) -> None:
        scanned_paths = [
            ROOT / "docs" / "demo" / "index.html",
            ROOT / "docs" / "judge-pack" / "index.html",
            ROOT / "docs" / "publication-action-card.md",
            ROOT / "docs" / "qwen-route-ledger.md",
            ROOT / "docs" / "blog-share-packet.md",
            ROOT / "docs" / "blog-share-packet" / "index.html",
            ROOT / "docs" / "public-update-checklist.md",
            ROOT / "docs" / "public-update-checklist" / "index.html",
            ROOT / "docs" / "demo-video-upload-pack.md",
            ROOT / "docs" / "demo-recording-runbook.md",
            ROOT / "docs" / "qwen-route-ledger.md",
            ROOT / "docs" / "qwen-start-handoff-template.md",
        ]
        forbidden = [
            "accepted by Devpost",
            "Vimeo URL accepted",
            "accepted public demo video",
            "Accepted public Vimeo URL",
            "accepted by the submitted Devpost project",
            "Alibaba Cloud deployment proof exists.",
            "browser/email inbox",
            "GitHub OAuth authorized",
            "clicked `Send Code`",
            "Most Winnable",
        ]

        for path in scanned_paths:
            text = path.read_text(encoding="utf-8")
            for fragment in forbidden:
                self.assertNotIn(fragment, text, msg=f"{fragment!r} found in {path}")

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
        self.assertEqual(snapshot, dashboard_payload())

    def test_core_static_artifacts_do_not_drift_or_break_local_refs(self) -> None:
        checked_pages = [
            ROOT / "web" / "index.html",
            ROOT / "docs" / "index.html",
            ROOT / "docs" / "demo" / "index.html",
            ROOT / "docs" / "judge-pack" / "index.html",
            ROOT / "docs" / "judge-review-card" / "index.html",
            ROOT / "docs" / "blog" / "index.html",
        ]
        stale_copy = [
            "public repository, public post, cloud deployment, or final Devpost submission is claimed until user approval",
            "Last updated June 11",
            "GitHub code push is blocked",
            "Devpost portfolio project creation is blocked",
        ]

        for page_path in checked_pages:
            text = page_path.read_text(encoding="utf-8")
            for fragment in stale_copy:
                self.assertNotIn(fragment, text, msg=f"{fragment!r} found in {page_path}")
            for ref in re.findall(r'(?:href|src)="([^"]+)"', text):
                if ref.startswith(("http://", "https://", "mailto:", "#")) or "${" in ref:
                    continue
                target = ref.split("#", 1)[0].split("?", 1)[0]
                if not target:
                    continue
                resolved = (page_path.parent / target).resolve()
                if target.endswith("/"):
                    resolved = resolved / "index.html"
                self.assertTrue(resolved.exists(), msg=f"{page_path} references missing local asset {ref}")

    def test_blog_post_award_story_has_judge_path(self) -> None:
        blog = (ROOT / "docs" / "blog" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Cloud Hackathon blog award story", blog)
        self.assertIn("Blog Post Award reader path", blog)
        self.assertIn("fastest review path is three steps", blog)
        self.assertIn("../judge-pack/", blog)
        self.assertIn("../demo/", blog)
        self.assertIn("../qwen-live-proof/", blog)
        self.assertIn("../cloud-readiness/", blog)
        self.assertIn("https://vimeo.com/1200124146", blog)
        self.assertIn("https://github.com/OOYXLOO/prizepilot-qwen-cloud", blog)
        self.assertIn("As of June 15, 2026", blog)
        self.assertIn("Last updated June 15, 2026", blog)
        self.assertNotIn("As of June 13, 2026", blog)
        self.assertNotIn("Last updated June 13, 2026", blog)
        self.assertNotIn("../judge-review-card/", blog)
        self.assertNotIn("../qwen-before-after/", blog)
        self.assertNotIn("../blog-share-packet/", blog)
        self.assertNotIn("prepared locally", blog)
        self.assertNotIn("after an account-owner-approved public push", blog)
        self.assertIn("what remains account-gated", blog)
        self.assertIn("current public review path is live now", blog)
        self.assertIn("unpublished proof links", blog)
        self.assertIn("../benchmark-method/", blog)
        self.assertIn("Benchmark method", blog)

    def test_publication_action_card_separates_live_baseline_from_prepared_push(self) -> None:
        card = (ROOT / "docs" / "publication-action-card.md").read_text(encoding="utf-8")

        self.assertIn("Current state on 2026-06-16", card)
        self.assertNotIn("Current state on 2026-06-15", card)
        self.assertNotIn("Current state on 2026-06-14", card)
        self.assertIn("## Live Baseline", card)
        self.assertIn("## Prepared After Approved Push", card)
        self.assertIn("Public baseline links currently live", card)
        self.assertIn("prepared next-update package until pushed and rechecked", card)
        self.assertIn("Official Requirement Fit map", card)
        self.assertNotIn("part of the prepared public package", card)

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
        self.assertIn("docs/qwen-before-after-evidence.md", markdown)
        self.assertIn("route-plan clarity", (ROOT / "docs" / "submission-story.md").read_text(encoding="utf-8"))
        self.assertIn("PrizePilot Qwen Contribution Map", page)
        self.assertIn("Qwen refines PrizePilot's plan", page)
        self.assertIn("Contribution Matrix", page)
        self.assertIn("no premature publishing", page)
        self.assertIn("../qwen-live-proof/", page)
        self.assertIn("../qwen-before-after/", page)

    def test_qwen_before_after_evidence_explains_refinement_chain(self) -> None:
        markdown = (ROOT / "docs" / "qwen-before-after-evidence.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "qwen-before-after" / "index.html").read_text(encoding="utf-8")

        self.assertIn("Qwen Before/After Evidence", markdown)
        self.assertIn("Before Qwen", markdown)
        self.assertIn("Qwen Refinement", markdown)
        self.assertIn("After Qwen", markdown)
        self.assertIn("live Alibaba Cloud public endpoint proof remains pending", page)
        self.assertIn("deterministic route plan", page)
        self.assertIn("Qwen refinement pass", page)
        self.assertIn("../qwen-live-proof/", page)
        self.assertIn("../alibaba-endpoint-checklist/", page)
        self.assertIn("./alibaba-endpoint-checklist/", (ROOT / "docs" / "index.html").read_text(encoding="utf-8"))

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
        self.assertIn("../qwen-before-after/", preflight)
        self.assertIn("../official-requirement-fit/", preflight)
        self.assertIn("Official Requirement Fit", preflight)
        self.assertIn("live endpoint not claimed", preflight)
        self.assertIn("Do not publish API keys", preflight)
        self.assertIn("../award-evidence-map/", preflight)
        self.assertIn("../qwen-live-proof/", preflight)

    def test_award_evidence_map_compresses_public_and_gated_signals(self) -> None:
        evidence_map = (ROOT / "docs" / "award-evidence-map" / "index.html").read_text(encoding="utf-8")

        self.assertIn("PrizePilot Qwen Award Evidence Map", evidence_map)
        self.assertIn("../cloud-readiness/", evidence_map)
        self.assertIn("../qwen-before-after/", evidence_map)
        self.assertIn("Blog Post Award", evidence_map)
        self.assertIn("Top 10 Honorable Mention", evidence_map)
        self.assertIn("Track 4 Autopilot Agent", evidence_map)
        self.assertIn("Full", evidence_map)
        self.assertIn("local unittest suite", evidence_map)
        self.assertIn("Narrative ready", evidence_map)
        self.assertIn("Public review ready", evidence_map)
        self.assertIn("Agent fit ready", evidence_map)
        self.assertIn("Reproducible", evidence_map)
        self.assertIn("Qwen/DashScope live model proof", evidence_map)
        self.assertIn("Alibaba Cloud endpoint proof", evidence_map)
        self.assertIn("Account-gated", evidence_map)
        self.assertIn("completed live Qwen/DashScope smoke proof", evidence_map)
        self.assertIn("../qwen-live-proof/", evidence_map)

    def test_status_files_do_not_reintroduce_old_publication_blockers(self) -> None:
        action_card = (ROOT / "docs" / "publication-action-card.md").read_text(encoding="utf-8")
        validation = (ROOT / "docs" / "validation-report.md").read_text(encoding="utf-8")

        self.assertIn("Superseded 2026-06-10 Blockers", action_card)
        self.assertIn("Qwen Devpost project is submitted and public", action_card)
        self.assertNotIn("GitHub code push is blocked", action_card)
        self.assertNotIn("Devpost portfolio project creation is blocked", action_card)
        self.assertIn("Current Evidence Boundary", validation)
        self.assertIn("Qwen before/after evidence", validation)
        self.assertNotIn("done locally and ready for publication", validation)

    def test_devpost_fields_do_not_publish_identity_inferences(self) -> None:
        fields = (ROOT / "docs" / "devpost-project-fields.md").read_text(encoding="utf-8")

        self.assertIn("Qwen-refined public submission copy", fields)
        self.assertIn("before/after chain", fields)
        self.assertIn("a deterministic planner picked the Blog Post Award route", fields)
        self.assertIn("a live Qwen/DashScope pass refined the public story and risk language", fields)
        self.assertIn("deterministic ranking chose the Blog Post Award route", fields)
        self.assertIn("before/after evidence shows exactly what changed", fields)
        self.assertIn("Still pending: account-owner-approved Alibaba endpoint proof.", fields)

        forbidden_fragments = [
            "phone number",
            "Asia/Shanghai",
            "inferred from",
        ]
        for fragment in forbidden_fragments:
            self.assertNotIn(fragment, fields)


if __name__ == "__main__":
    unittest.main()
