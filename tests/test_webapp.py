import json
import unittest

from prizepilot.webapp import dashboard_payload, render_dashboard


class WebappTests(unittest.TestCase):
    def test_dashboard_payload_exposes_qwen_and_portfolio(self) -> None:
        payload = dashboard_payload()

        self.assertEqual(payload["project"], "PrizePilot")
        self.assertEqual(payload["track"], "Track 4 - Autopilot Agent")
        self.assertEqual(payload["qwen_plan"]["target_prize"]["name"], "Blog Post Award")
        self.assertEqual(payload["mindtheproduct_plan"]["target_prize"]["name"], "First Place")
        self.assertFalse(payload["novus_readiness"]["novus_installed"])
        self.assertGreaterEqual(len(payload["portfolio"]["ranked"]), 4)
        self.assertEqual(payload["submission_status"]["phase"], "submitted_can_still_improve")
        self.assertEqual(len(payload["agent_walkthrough"]), 5)
        self.assertEqual(len(payload["judge_scorecard"]), 4)
        self.assertTrue(any(gap.startswith("No live Qwen") for gap in payload["evidence_gaps"]))
        self.assertTrue(any("No API key is stored" in item for item in payload["integrity_boundary"]))

    def test_dashboard_html_links_json_endpoint_and_shows_verified_submission(self) -> None:
        html = render_dashboard(dashboard_payload())

        self.assertIn("/api/plan", html)
        self.assertIn("PrizePilot turns prize pages", html)
        self.assertIn("Mind the Product target", html)
        self.assertIn("submitted_can_still_improve", html)
        self.assertIn("https://vimeo.com/1200124146", html)
        self.assertIn("Autopilot Walkthrough", html)
        self.assertIn("Judge Scorecard", html)
        self.assertIn("Evidence gaps before judging", html)
        self.assertIn("Manual vs PrizePilot", html)
        self.assertIn("email verification required", html)
        self.assertIn("No API key is stored", html)
        self.assertIn('data-label="Target"', html)
        self.assertIn("grid-template-columns", html)
        self.assertIn("Devpost", html)

    def test_dashboard_payload_is_json_serializable(self) -> None:
        json.dumps(dashboard_payload())


if __name__ == "__main__":
    unittest.main()
