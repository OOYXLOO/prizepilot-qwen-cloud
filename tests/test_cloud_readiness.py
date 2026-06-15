from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from prizepilot.cloud_readiness import build_report, parse_checked_at, render_markdown


class CloudReadinessTests(unittest.TestCase):
    def test_report_passes_without_live_secrets(self) -> None:
        report = build_report()

        self.assertEqual(report["overall"], "qwen_live_verified_endpoint_pending")
        self.assertEqual(report["live_claim"], "qwen_dashscope_smoke_verified_alibaba_endpoint_pending")
        self.assertIn("T", report["checked_at_local_asia_shanghai"])
        self.assertTrue(report["checked_at_local_asia_shanghai"].endswith("+08:00"))
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

    def test_checked_at_can_be_supplied_for_reproducible_reports(self) -> None:
        checked_at = datetime(2026, 6, 15, 12, 30, tzinfo=timezone.utc)

        report = build_report(checked_at=checked_at)

        self.assertEqual(report["checked_at"], "2026-06-15T12:30:00+00:00")
        self.assertEqual(report["checked_at_local_asia_shanghai"], "2026-06-15T20:30:00+08:00")

    def test_parse_checked_at_accepts_z_suffix_and_naive_utc(self) -> None:
        self.assertEqual(parse_checked_at("2026-06-15T12:30:00Z").isoformat(), "2026-06-15T12:30:00+00:00")
        self.assertEqual(parse_checked_at("2026-06-15T12:30:00").isoformat(), "2026-06-15T12:30:00+00:00")

    def test_cli_checked_at_writes_deterministic_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            json_out = Path(temp_dir) / "cloud-readiness.json"
            md_out = Path(temp_dir) / "cloud-readiness.md"

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "prizepilot",
                    "cloud-readiness",
                    "--checked-at",
                    "2026-06-15T12:30:00Z",
                    "--json-out",
                    str(json_out),
                    "--md-out",
                    str(md_out),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            report = json.loads(json_out.read_text(encoding="utf-8"))
            markdown = md_out.read_text(encoding="utf-8")

        self.assertIn("Overall: qwen_live_verified_endpoint_pending", completed.stdout)
        self.assertEqual(report["checked_at"], "2026-06-15T12:30:00+00:00")
        self.assertEqual(report["checked_at_local_asia_shanghai"], "2026-06-15T20:30:00+08:00")
        self.assertIn("Generated: 2026-06-15T12:30:00+00:00", markdown)

    def test_markdown_exposes_judge_readable_table(self) -> None:
        markdown = render_markdown(build_report())

        self.assertIn("PrizePilot Cloud Readiness Report", markdown)
        self.assertIn("Generated Asia/Shanghai:", markdown)
        self.assertIn("qwen_live_verified_endpoint_pending", markdown)
        self.assertIn("QWEN_RUNTIME_SECRET_BOUNDARY", markdown)
        self.assertIn("QWEN_LIVE_SMOKE_PROOF", markdown)
        self.assertIn("ALIBABA_PUBLIC_HTTP_PROOF_TARGETS", markdown)
        self.assertIn("prepared_not_live", markdown)
        self.assertIn("endpoint evidence actually exists", markdown)


if __name__ == "__main__":
    unittest.main()
