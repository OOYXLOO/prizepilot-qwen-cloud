from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from prizepilot.qwen_status import REQUIRED_ARTIFACTS, build_status, parse_ledger_fields, render_markdown

LEDGER_TEXT = """# Ledger

## Gate Status

- Devpost hackathon joined: {joined}
- Devpost portfolio project created: {portfolio_project}
- Devpost additional info saved: {additional_info}
- Qwen/Alibaba Cloud account ready: {account_ready}
- Qwen live check completed: {live_check}
- Alibaba Cloud deployment proof: {deployment}
- Public GitHub repository: {repo}
- Public demo video: {video}
- Public blog/social post: {blog}
- Devpost final submitted: {submitted}
"""

def write_required_artifacts(root: Path) -> None:
    for relative_path in REQUIRED_ARTIFACTS:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("ok", encoding="utf-8")

def write_ledger(root: Path, **overrides: str) -> Path:
    values = {
        "joined": "no/unknown",
        "portfolio_project": "no",
        "additional_info": "no",
        "account_ready": "no/unknown",
        "live_check": "no",
        "deployment": "no",
        "repo": "no",
        "video": "no",
        "blog": "no",
        "submitted": "no",
    }
    values.update(overrides)
    path = root / "docs" / "qwen-route-ledger.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LEDGER_TEXT.format(**values), encoding="utf-8")
    return path

class QwenStatusTests(unittest.TestCase):
    def test_parse_ledger_fields(self) -> None:
        fields = parse_ledger_fields("- Public GitHub repository: yes\n")

        self.assertEqual(fields["public github repository"], "yes")

    def test_yes_status_accepts_explanatory_suffixes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(
                root,
                joined="yes - joined on Devpost",
                portfolio_project="yes - imported from public repo",
                additional_info="yes - architecture.png uploaded",
                account_ready="yes - console reached",
                live_check="yes - safe smoke test passed",
                deployment="yes - endpoint proof recorded",
                repo="yes - public",
                video="yes - Vimeo URL accepted",
                blog="yes - public URL",
                submitted="yes - Devpost confirmation displayed",
            )

            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        self.assertEqual(status["phase"], "submitted_waiting_for_results")
        self.assertEqual(len(status["incomplete_public_gates"]), 0)

    def test_reports_missing_local_artifacts_first(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            ledger = write_ledger(root)

            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        self.assertEqual(status["phase"], "local_package_incomplete")
        self.assertEqual(status["severity"], "FIX_LOCAL")
        self.assertGreater(len(status["missing_artifacts"]), 0)

    def test_ready_for_public_steps_when_local_package_complete(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(root)

            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        self.assertEqual(status["phase"], "ready_for_user_publication_steps")
        self.assertEqual(status["severity"], "ACTION_NEEDED")
        self.assertIn("reCAPTCHA", status["next_action"])
        self.assertEqual(len(status["missing_artifacts"]), 0)
        self.assertGreater(len(status["incomplete_public_gates"]), 0)

    def test_partial_github_repo_gets_push_specific_next_action(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(root, joined="yes", portfolio_project="yes", repo="partial - empty repository created")

            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        self.assertIn("Authorize GitHub", status["next_action"])
        github_gate = next(item for item in status["incomplete_public_gates"] if item["gate"] == "public github repository")
        self.assertIn("git push", github_gate["next_action"])

    def test_partial_additional_info_gets_file_upload_next_action(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(
                root,
                joined="yes",
                portfolio_project="yes",
                additional_info="partial - fields filled in browser; architecture file upload/save pending",
            )

            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        self.assertIn("architecture.png", status["next_action"])
        additional_gate = next(item for item in status["incomplete_public_gates"] if item["gate"] == "devpost additional info saved")
        self.assertIn("Save & continue", additional_gate["next_action"])

    def test_partial_demo_video_gets_hosting_specific_next_action(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(root, joined="yes", portfolio_project="yes", repo="yes", video="partial - generated WebM in public repository")

            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        video_gate = next(item for item in status["incomplete_public_gates"] if item["gate"] == "public demo video")
        self.assertIn("YouTube", video_gate["next_action"])
        self.assertIn("Vimeo", status["next_action"])

    def test_urgent_near_deadline(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(root)

            status = build_status(root, ledger, now=datetime(2026, 7, 8, tzinfo=timezone.utc))

        self.assertEqual(status["phase"], "public_submission_steps_urgent")
        self.assertEqual(status["severity"], "URGENT")

    def test_submitted_waits_for_results(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(
                root,
                joined="yes",
                portfolio_project="yes",
                additional_info="yes",
                account_ready="yes",
                live_check="yes",
                deployment="yes",
                repo="yes",
                video="yes",
                blog="yes",
                submitted="yes",
            )

            status = build_status(root, ledger, now=datetime(2026, 7, 9, 1, tzinfo=timezone.utc))

        self.assertEqual(status["phase"], "submitted_waiting_for_results")
        self.assertEqual(status["severity"], "OK")
        self.assertEqual(len(status["incomplete_public_gates"]), 0)

    def test_submitted_with_evidence_gaps_can_still_improve(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(
                root,
                joined="yes",
                portfolio_project="yes",
                additional_info="yes",
                account_ready="partial - email verification pending",
                live_check="no",
                deployment="partial - manifest prepared but live endpoint not verified",
                repo="yes",
                video="yes",
                blog="yes",
                submitted="yes",
            )

            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        self.assertEqual(status["phase"], "submitted_can_still_improve")
        self.assertEqual(status["severity"], "OK_WITH_EVIDENCE_GAPS")
        self.assertIn("Strengthen evidence", status["next_action"])
        self.assertEqual(len(status["incomplete_public_gates"]), 3)

    def test_markdown_includes_gates_and_references(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_required_artifacts(root)
            ledger = write_ledger(root)
            status = build_status(root, ledger, now=datetime(2026, 6, 20, tzinfo=timezone.utc))

        markdown = render_markdown(status)

        self.assertIn("ready_for_user_publication_steps", markdown)
        self.assertIn("docs/qwen-start-handoff-template.md", markdown)
        self.assertIn("public github repository", markdown)

if __name__ == "__main__":
    unittest.main()
