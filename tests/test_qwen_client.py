import json
import os
import unittest
from unittest import mock

from prizepilot.qwen_client import QwenClient, QwenClientError


class QwenClientTests(unittest.TestCase):
    def test_missing_key_gives_actionable_error(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(QwenClientError, "DASHSCOPE_API_KEY or QWEN_API_KEY"):
                QwenClient()

    def test_qwen_key_overrides_dashscope_key(self) -> None:
        with mock.patch.dict(os.environ, {"DASHSCOPE_API_KEY": "dash", "QWEN_API_KEY": "qwen"}, clear=True):
            client = QwenClient()

        self.assertEqual(client.api_key, "qwen")

    def test_uses_dashscope_key_and_chat_completions_endpoint(self) -> None:
        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def read(self):
                return json.dumps({"choices": [{"message": {"content": "ok"}}]}).encode("utf-8")

        captured = {}

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["timeout"] = timeout
            captured["headers"] = dict(request.header_items())
            return FakeResponse()

        with mock.patch.dict(os.environ, {"DASHSCOPE_API_KEY": "dash"}, clear=True):
            with mock.patch("urllib.request.urlopen", fake_urlopen):
                client = QwenClient()
                result = client.chat([{"role": "user", "content": "hello"}], timeout=7)

        self.assertEqual(result, "ok")
        self.assertTrue(captured["url"].endswith("/chat/completions"))
        self.assertEqual(captured["timeout"], 7)
        self.assertEqual(captured["headers"]["Authorization"], "Bearer dash")


if __name__ == "__main__":
    unittest.main()
