# Qwen/DashScope Live Smoke Proof

Captured: 2026-06-13T00:25:21+08:00

Purpose: prove that PrizePilot can run a live Qwen-compatible refinement pass with an account-owner supplied runtime key, while keeping secrets out of the repository, docs, screenshots, Devpost, and local ledgers.

## Result

- Region/account path: Alibaba Cloud China Bailian / DashScope
- Model: `qwen-plus`
- Base URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`
- Runtime environment override used for this China Bailian smoke test: `DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1` and `DASHSCOPE_MODEL=qwen-plus`; the code default remains the international-compatible endpoint unless a runtime env var overrides it.
- Client provenance at capture time: `src/prizepilot/qwen_client.py` SHA256 `A476ACA07D524D3F50739949F5D04D6FA896D077216695B12ED37E1139E4FDF6`
- Command: `python -X utf8 -m prizepilot plan samples/qwen_hackathon.json --use-qwen`
- Exit code: 0
- `DASHSCOPE_API_KEY` present after cleanup: False

## Non-Sensitive Output Excerpt

```text
Here's a refined, factual, and constraint-respecting version of your hackathon submission plan, strictly adhering to the provided data, without inventing account details, deployment mechanics, payout logistics, or any external assumptions:

Refined Submission Plan: Blog Post Award (Qwen Cloud Hackathon)

Target Prize:
- Name: Blog Post Award
- Value: $500 USD
- Winners: 10
- Prerequisite: Must be tied to a qualified Devpost project submission, not standalone.

Critical Constraints:
- No credentials stored.
- No premature publishing.
- No assumed infrastructure.
- Eligibility verified first.
```

## Boundary

This proof verifies a live Qwen/DashScope refinement path only. It does not claim a live Alibaba Cloud public endpoint, prize award, payout, tax/KYC completion, bank verification, billing status, or private console state.

Do not publish API keys, raw request headers, full account metadata, billing screens, private console pages, cookies, payment data, tax data, KYC data, or recovery material.
