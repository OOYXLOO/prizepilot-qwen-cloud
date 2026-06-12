# PrizePilot

[![Verify PrizePilot](https://github.com/OOYXLOO/prizepilot-qwen-cloud/actions/workflows/verify.yml/badge.svg)](https://github.com/OOYXLOO/prizepilot-qwen-cloud/actions/workflows/verify.yml)
[![Public demo](https://img.shields.io/badge/Public%20demo-GitHub%20Pages-0969da)](https://ooyxloo.github.io/prizepilot-qwen-cloud/)
[![Devpost](https://img.shields.io/badge/Devpost-submitted-003e54)](https://devpost.com/software/prizepilot-qwen-cloud)

PrizePilot is a Qwen Cloud hackathon submission for Track 4, Autopilot Agent. It turns hackathon and bounty opportunities into ranked execution plans, public artifact drafts, and human approval checkpoints.

The project is intentionally conservative: it records public repository, blog, video, Devpost submission status, and Qwen live smoke proof only after verification, while keeping live Alibaba Cloud deployment proof, payout eligibility, tax, and KYC outside the repository until those events actually happen.

## Current Public Status

Latest review status as of 2026-06-13: the repository, Blog Award story, presentation deck, Qwen live proof, and route status files are the current source of truth for PrizePilot's submission state.

- Devpost project: https://devpost.com/software/prizepilot-qwen-cloud
- Public demo video: https://vimeo.com/1200124146
- Public presentation deck: https://ooyxloo.github.io/prizepilot-qwen-cloud/prizepilot-qwen-submission-deck.pptx
- Public judge demo: https://ooyxloo.github.io/prizepilot-qwen-cloud/demo/
- Public judge evidence pack: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/
- Public award preflight: https://ooyxloo.github.io/prizepilot-qwen-cloud/award-preflight/
- Public award evidence map: https://ooyxloo.github.io/prizepilot-qwen-cloud/award-evidence-map/
- Public cloud readiness report: https://ooyxloo.github.io/prizepilot-qwen-cloud/cloud-readiness/
- Public benchmark method: https://ooyxloo.github.io/prizepilot-qwen-cloud/benchmark-method/
- Public live proof gate: https://ooyxloo.github.io/prizepilot-qwen-cloud/live-proof-gate/
- Public Qwen live proof: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-live-proof/
- Public Qwen contribution map: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-contribution/
- Public Alibaba endpoint checklist: https://ooyxloo.github.io/prizepilot-qwen-cloud/alibaba-endpoint-checklist/
- Public static plan snapshot: https://ooyxloo.github.io/prizepilot-qwen-cloud/api/plan.json
- Public Blog Award story: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/
- Public repository: https://github.com/OOYXLOO/prizepilot-qwen-cloud
- Submission state: submitted to Devpost; still editable until the Qwen Cloud hackathon deadline.
- Evidence gap: verified live Alibaba Cloud endpoint proof still needs to be captured before judging if account access, credit, and billing approval are available.

## Judge Quickstart

The 90-second review path is:

1. Open the Devpost project, Vimeo demo, and 5-slide presentation deck.
2. Open the public judge evidence pack for the prize decision summary and Track 4 / Blog Post Award matrix.
3. Open the award evidence map for completed proof versus remaining account-gated work.
4. Open the benchmark method to see how the route ranking is scored and what the sample portfolio proves.
5. Open the Qwen contribution map and Qwen live proof page for the verified runtime smoke test, contribution depth, and cleanup boundary.
6. Open the Alibaba endpoint checklist for the exact remaining public HTTP 200 proof gate.
7. Inspect the static machine-readable plan snapshot at https://ooyxloo.github.io/prizepilot-qwen-cloud/api/plan.json.

For deeper local verification, run the dashboard:

## Local Use

```powershell
$env:PYTHONPATH='src'
python -m prizepilot plan samples/qwen_hackathon.json
python -m prizepilot plan samples/mindtheproduct_world_product_day.json
python -m prizepilot portfolio samples/splunk_agentic_ops.json samples/qwen_hackathon.json samples/mindtheproduct_world_product_day.json samples/uipath_agenthack.json samples/algora_onyx_bounty.json samples/arm_ai_optimization.json
python -m prizepilot cloud-readiness
python -m prizepilot.webapp --host 127.0.0.1 --port 8000
```

Then inspect the live machine-readable planning payload at `http://127.0.0.1:8000/api/plan`.
Review `docs/submission-story.md`, `docs/benchmark-method.md`, `docs/cloud-readiness-report.md`, `docs/qwen-live-proof.md`, `docs/qwen-contribution-map.md`, `docs/live-proof-gate.md`, `docs/alibaba-endpoint-judge-checklist.md`, `docs/qwen-route-status.md`, and `docs/validation-report.md` for the evidence boundary.

Live Qwen refinement has been verified once with a runtime-only key; future runs still require `DASHSCOPE_API_KEY` or `QWEN_API_KEY` at action time only.
The Mind the Product route additionally requires Novus email verification and official Novus installation before final Devpost submission. The web service exposes `/api/novus-readiness` so that gate can be tracked without claiming completion early.

## Demo Assets

- Dashboard screenshots: `docs/screenshots/prizepilot-dashboard-desktop.png` and `docs/screenshots/prizepilot-dashboard-mobile.png`
- Short demo GIF: `docs/screenshots/prizepilot-demo.gif`
- Editable presentation deck: `docs/prizepilot-qwen-submission-deck.pptx`
- Static judge demo: `docs/demo/index.html`
- Devpost architecture upload: `architecture.png`
- Recording page: `docs/demo-recording-page.html`
- Recording runbook: `docs/demo-recording-runbook.md`
