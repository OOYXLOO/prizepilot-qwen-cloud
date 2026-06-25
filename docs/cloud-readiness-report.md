# PrizePilot Cloud Readiness Report

Generated: 2026-06-25T21:57:53.875164+00:00
Generated Asia/Shanghai: 2026-06-26T05:57:53.875164+08:00
Overall: **qwen_live_verified_endpoint_pending**
Live claim: `qwen_dashscope_smoke_verified_alibaba_endpoint_pending`

No API keys, raw headers, account IDs, billing data, payout data, tax data, KYC data, cookies, or private console pages are required or stored.

## Checks

| Check | Status | Evidence | Next live step |
| --- | --- | --- | --- |
| `QWEN_OPENAI_COMPATIBLE_REQUEST_SHAPE` | `pass` | The client defaults to DashScope compatible mode and posts chat/completions payloads with model, messages, and temperature. | The live proof has been captured once; future reruns still require an account-owner supplied runtime key and should publish only a short non-secret excerpt. |
| `QWEN_RUNTIME_SECRET_BOUNDARY` | `pass` | The client reads Qwen/DashScope keys only from runtime environment variables and the ledger does not store an API key. | Keep API keys out of chat, screenshots, commits, logs, and Devpost; remove the environment variable immediately after the smoke test. |
| `QWEN_LIVE_SMOKE_PROOF` | `pass` | A live Qwen/DashScope refinement pass succeeded through Alibaba Cloud China Bailian with a runtime-only key and no stored secret. | Use only the short non-sensitive excerpt publicly; future runs still require account-owner key entry at action time. |
| `ALIBABA_FC_CUSTOM_CONTAINER_MANIFEST` | `source_code_prepared` | The checked-in Serverless Devs manifest targets Alibaba Function Compute with the PrizePilot container on port 8000. | Deploy only after the account owner approves Alibaba Cloud account, credit, region, and billing implications. |
| `ALIBABA_PUBLIC_HTTP_PROOF_TARGETS` | `prepared_not_live` | The manifest declares a public HTTP trigger and health check path that map to the dashboard and API proof plan, but no live Alibaba URL is claimed here. | After deployment, verify the public endpoint at / and /api/plan before updating Devpost. |
| `DASHBOARD_JUDGE_PAYLOAD_READY` | `pass` | The local web payload exposes the submitted Qwen target, verified Qwen live proof, route status, judge scorecard, approval queue, and remaining endpoint gap. | Use the same payload as the expected success signal for a live Alibaba endpoint proof. |
| `PUBLIC_CLAIM_BOUNDARY` | `pass` | The public live-proof gate states that Qwen live proof is verified and the Alibaba endpoint remains account-gated. | Do not strengthen the public Devpost claim for Alibaba Cloud deployment until endpoint evidence actually exists. |

## Next Live Evidence

- Alibaba Cloud Function Compute deployment approved and run by the account owner.
- Public endpoint proof for / and /api/plan with no private console chrome.
- Devpost update copy that claims only the completed Qwen smoke proof and any endpoint proof that actually exists.
