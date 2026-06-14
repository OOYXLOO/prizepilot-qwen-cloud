from __future__ import annotations

import unittest

from prizepilot.cloud_readiness import build_report, render_markdown


class CloudReadinessTests(unittest.TestCase):
    def test_report_passes_without_live_secrets(self) -> None:
        report = build_report()

        self.assertEqual(report["overall"], "qwen_live_verified_endpoint_pending")
        self.assertEqual(report["live_claim"], "qwen_dashscope_smoke_verified_alibaba_endpoint_pending")
        self.assertEqual(len(report["checks"]), 7)
        self.assertTrue(all(check["status"] != "fail" for check in report["checks"]))
        status_by_id = {check["id"]: check["status"] for check in report["checks"]}
        check_ids = {check["id"] for check in report["checks"]}
        self.assertIn("QWEN_OPENAI_COMPATIBLE_REQUEST_SHAPE", check_ids)
        self.assertIn("QWEN_LIVE_SMOKE_PROOF", check_ids)
        self.assertIn("ALIBABA_FC_CUSTOM_CONTAINER_MANIFEST", check_ids)
        self.assertIn("PUBLIC_CLAIM_BOUNDARY", check_ids)
        self.assertEqual(status_by_id["QWEN_LIVE_SMOKE_PROOF"], "pass")
        self.assertEqual(status_by_id["ALIBABA_FC_CUSTOM_CONTAINER_MANIFEST"], "source_code_prepared")
        self.assertEqual(status_by_id["ALIBABA_PUBLIC_HTTP_PROOF_TARGETS"], "prepared_not_live")
        self.assertIn("No API keys", report["secret_policy"])
        self.assertIn("Alibaba Cloud Function Compute deployment", report["next_live_evidence"][0])

    def test_markdown_exposes_judge_readable_table(self) -> None:
        markdown = render_markdown(build_report())

        self.assertIn("PrizePilot Cloud Readiness Report", markdown)
        self.assertIn("qwen_live_verified_endpoint_pending", markdown)
        self.assertIn("QWEN_RUNTIME_SECRET_BOUNDARY", markdown)
        self.assertIn("QWEN_LIVE_SMOKE_PROOF", markdown)
        self.assertIn("ALIBABA_PUBLIC_HTTP_PROOF_TARGETS", markdown)
        self.assertIn("prepared_not_live", markdown)
        self.assertIn("endpoint evidence actually exists", markdown)


if __name__ == "__main__":
    unittest.main()
