# Qwen Cloud Live Check

Created: 2026-06-10

Use this only after the user has created or logged into their Qwen Cloud / Alibaba Cloud account and provided the API key at action time. Do not store the key in this project, in docs, or in the ledger.

## Official API References

- Qwen first API call: https://www.alibabacloud.com/help/en/model-studio/first-api-call-to-qwen
- OpenAI-compatible chat API: https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope

Rechecked against official Alibaba Cloud docs on 2026-06-10. The official docs use the OpenAI-compatible `/chat/completions` endpoint, `DASHSCOPE_API_KEY`, and `qwen-plus` examples. They also warn that API keys and base URLs are region-specific.

## Supported Environment Variables

- `DASHSCOPE_API_KEY` or `QWEN_API_KEY`: required for live mode.
- `QWEN_MODEL` or `DASHSCOPE_MODEL`: optional, defaults to `qwen-plus`.
- `QWEN_BASE_URL` or `DASHSCOPE_BASE_URL`: optional, defaults to Singapore:
  `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Known official base URLs:

- Singapore: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
- US Virginia: `https://dashscope-us.aliyuncs.com/compatible-mode/v1`
- China Beijing: `https://dashscope.aliyuncs.com/compatible-mode/v1`
- Hong Kong China: `https://cn-hongkong.dashscope.aliyuncs.com/compatible-mode/v1`

For raw HTTP calls, always re-check the official OpenAI-compatible chat endpoint table for the selected account region before the live run.

## PowerShell Smoke Test

Run this from the project root:

```powershell
$env:PYTHONPATH='src'
$env:DASHSCOPE_API_KEY='set-at-runtime-only'
python -m prizepilot plan samples/qwen_hackathon.json --use-qwen
```

Expected result:

- The command returns concise Markdown.
- The output should refine the local PrizePilot plan rather than inventing account details, deployment proof, public URLs, payout status, or eligibility.
- If the request fails, check that the API key region matches the selected base URL.

## Integrity Boundary

This live check can prove Qwen model usage for the project story, but it does not by itself prove Alibaba Cloud deployment. Deployment proof and any new public Devpost evidence claim still require separate verification before they are added to the submitted project.
