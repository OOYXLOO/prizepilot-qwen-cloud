from __future__ import annotations

import unittest

from prizepilot.cloud_readiness import build_report, render_markdown


class CloudReadinessTests(unittest.TestCase):
    def test_report_passes_without_live_secrets(self) -> None:
        report = build_report()

        self.assertEqual(report["overall"], "ready_without_live_secrets")
        self.assertEqual(report["live_claim"], "not_claimed")
        self.assertEqual(len(report["checks"]), 6)
        self.assertTrue(all(check["status"] == "pass" for check in report["checks"]))
        check_ids = {check["id"] for check in report["checks"]}
        self.assertIn("QWEN_OPENAI_COMPATIBLE_REQUEST_SHAPE", check_ids)
        self.assertIn("ALIBABA_FC_CUSTOM_CONTAINER_MANIFEST", check_ids)
        self.assertIn("PUBLIC_CLAIM_BOUNDARY", check_ids)
        self.assertIn("No API keys", report["secret_policy"])
        self.assertIn("Runtime Qwen/DashScope smoke test", report["next_live_evidence"][0])

    def test_markdown_exposes_judge_readable_table(self) -> None:
        markdown = render_markdown(build_report())

        self.assertIn("PrizePilot Cloud Readiness Report", markdown)
        self.assertIn("ready_without_live_secrets", markdown)
        self.assertIn("QWEN_RUNTIME_SECRET_BOUNDARY", markdown)
        self.assertIn("ALIBABA_PUBLIC_HTTP_PROOF_TARGETS", markdown)
        self.assertIn("Do not strengthen the public Devpost claim", markdown)


if __name__ == "__main__":
    unittest.main()
