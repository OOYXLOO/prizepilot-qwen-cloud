# PrizePilot Cloud Readiness Report

Generated: 2026-06-12T11:14:54.441325+00:00
Overall: **ready_without_live_secrets**
Live claim: `not_claimed`

No API keys, raw headers, account IDs, billing data, payout data, tax data, KYC data, cookies, or private console pages are required or stored.

## Checks

| Check | Status | Evidence | Next live step |
| --- | --- | --- | --- |
| `QWEN_OPENAI_COMPATIBLE_REQUEST_SHAPE` | `pass` | The client defaults to DashScope compatible mode and posts chat/completions payloads with model, messages, and temperature. | When the account owner supplies a runtime key, run the live proof command and publish only a short non-secret excerpt. |
| `QWEN_RUNTIME_SECRET_BOUNDARY` | `pass` | The client reads Qwen/DashScope keys only from runtime environment variables and the ledger does not store an API key. | Keep API keys out of chat, screenshots, commits, logs, and Devpost; remove the environment variable immediately after the smoke test. |
| `ALIBABA_FC_CUSTOM_CONTAINER_MANIFEST` | `pass` | The checked-in Serverless Devs manifest targets Alibaba Function Compute with the PrizePilot container on port 8000. | Deploy only after the account owner approves Alibaba Cloud account, credit, region, and billing implications. |
| `ALIBABA_PUBLIC_HTTP_PROOF_TARGETS` | `pass` | The manifest declares a public HTTP trigger and health check path that map to the dashboard and API proof plan. | After deployment, verify the public endpoint at / and /api/plan before updating Devpost. |
| `DASHBOARD_JUDGE_PAYLOAD_READY` | `pass` | The local web payload exposes the submitted Qwen target, route status, judge scorecard, approval queue, and evidence gaps. | Use the same payload as the expected success signal for a live Alibaba endpoint proof. |
| `PUBLIC_CLAIM_BOUNDARY` | `pass` | The public live-proof gate states what is verified and what remains account-gated. | Do not strengthen the public Devpost claim until live Qwen and/or Alibaba evidence actually exists. |

## Next Live Evidence

- Runtime Qwen/DashScope smoke test with account-owner supplied key.
- Alibaba Cloud Function Compute deployment approved and run by the account owner.
- Public endpoint proof for / and /api/plan with no private console chrome.
