import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class QwenLiveProofTests(unittest.TestCase):
    def test_live_proof_matches_current_client_and_keeps_secret_boundary(self) -> None:
        client_path = ROOT / "src" / "prizepilot" / "qwen_client.py"
        expected_hash = hashlib.sha256(client_path.read_bytes()).hexdigest().upper()
        markdown = (ROOT / "docs" / "qwen-live-proof.md").read_text(encoding="utf-8")
        page = (ROOT / "docs" / "qwen-live-proof" / "index.html").read_text(encoding="utf-8")
        combined = f"{markdown}\n{page}"

        self.assertIn(f"SHA256 `{expected_hash}`", markdown)
        self.assertIn(expected_hash, page)
        self.assertIn("Captured: 2026-06-13T00:25:21+08:00", markdown)
        self.assertIn("Model: `qwen-plus`", markdown)
        self.assertIn("Exit code: 0", markdown)
        self.assertIn("DASHSCOPE_API_KEY` present after cleanup: False", markdown)
        self.assertIn("without inventing account details", markdown)
        self.assertIn("No credentials stored.", markdown)
        self.assertIn("No assumed infrastructure.", markdown)
        self.assertIn("Eligibility verified first.", markdown)
        self.assertIn("does not claim a live Alibaba Cloud public endpoint", page)

        forbidden_patterns = {
            "api key value": r"\bsk-[A-Za-z0-9._-]{8,}\b",
            "email address": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
            "phone number": r"\b1[3-9]\d{9}\b",
            "card number": r"\b(?:\d[ -]?){16}\b",
            "bearer token": r"Bearer\s+[A-Za-z0-9._-]{8,}",
        }
        for label, pattern in forbidden_patterns.items():
            with self.subTest(label=label):
                self.assertIsNone(re.search(pattern, combined, flags=re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
