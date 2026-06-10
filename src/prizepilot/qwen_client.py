from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, Iterable


DEFAULT_BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"


class QwenClientError(RuntimeError):
    pass


class QwenClient:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None) -> None:
        self.api_key = api_key or os.getenv("QWEN_API_KEY") or os.getenv("DASHSCOPE_API_KEY")
        self.base_url = (base_url or os.getenv("QWEN_BASE_URL") or os.getenv("DASHSCOPE_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.model = model or os.getenv("QWEN_MODEL") or os.getenv("DASHSCOPE_MODEL") or "qwen-plus"
        if not self.api_key:
            raise QwenClientError("Set DASHSCOPE_API_KEY or QWEN_API_KEY at runtime only; do not store it in the project.")

    def chat(self, messages: Iterable[Dict[str, str]], timeout: int = 30) -> str:
        payload = json.dumps({"model": self.model, "messages": list(messages), "temperature": 0.2}).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data: Dict[str, Any] = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise QwenClientError(f"Qwen request failed with HTTP {exc.code}: {body[:240]}") from exc
        except OSError as exc:
            raise QwenClientError(f"Qwen request failed: {exc}") from exc
        try:
            return str(data["choices"][0]["message"]["content"])
        except (KeyError, IndexError, TypeError) as exc:
            raise QwenClientError("Qwen response did not include choices[0].message.content") from exc
