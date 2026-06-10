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
        self.assertTrue(any("No API key is stored" in item for item in payload["integrity_boundary"]))

    def test_dashboard_html_links_json_endpoint_and_does_not_claim_submission(self) -> None:
        html = render_dashboard(dashboard_payload())

        self.assertIn("/api/plan", html)
        self.assertIn("PrizePilot turns prize pages", html)
        self.assertIn("Mind the Product target", html)
        self.assertIn("email verification required", html)
        self.assertIn("No API key is stored", html)
        self.assertIn('data-label="Target"', html)
        self.assertIn("grid-template-columns", html)
        self.assertNotIn("submitted to devpost", html.lower())

    def test_dashboard_payload_is_json_serializable(self) -> None:
        json.dumps(dashboard_payload())


if __name__ == "__main__":
    unittest.main()
