# PrizePilot

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
- Public live proof gate: https://ooyxloo.github.io/prizepilot-qwen-cloud/live-proof-gate/
- Public Qwen live proof: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-live-proof/
- Public Blog Award story: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/
- Public repository: https://github.com/OOYXLOO/prizepilot-qwen-cloud
- Submission state: submitted to Devpost; still editable until the Qwen Cloud hackathon deadline.
- Evidence gap: verified live Alibaba Cloud endpoint proof still needs to be captured before judging if account access, credit, and billing approval are available.

## Judge Quickstart

The fastest review path is:

1. Open the Devpost project and demo video above.
2. Open the public presentation deck for the 5-slide judge summary.
3. Open the public judge demo for the setup-free evidence map.
4. Open the judge evidence pack for the Track 4 / Blog Post Award matrix.
5. Open the award preflight for the Blog Post Award / Honorable Mention readiness check.
6. Open the award evidence map for the compact matrix of public proof, reproducibility, and account-gated gaps.
7. Open the cloud readiness report to verify the Qwen request shape, Alibaba Function Compute manifest, dashboard payload, and claim boundary without live secrets.
8. Open the live proof gate to see exactly how account-gated Qwen and Alibaba evidence is captured without secrets.
9. Open the Qwen live proof page to verify the completed runtime smoke test and cleanup boundary.
10. Read the Blog Award story for the current public evidence boundary.
11. Run the local dashboard:

## Local Use

```powershell
$env:PYTHONPATH='src'
python -m prizepilot plan samples/qwen_hackathon.json
python -m prizepilot plan samples/mindtheproduct_world_product_day.json
python -m prizepilot portfolio samples/splunk_agentic_ops.json samples/qwen_hackathon.json samples/mindtheproduct_world_product_day.json samples/uipath_agenthack.json samples/algora_onyx_bounty.json samples/arm_ai_optimization.json
python -m prizepilot cloud-readiness
python -m prizepilot.webapp --host 127.0.0.1 --port 8000
```

12. Inspect the machine-readable planning payload at `http://127.0.0.1:8000/api/plan`.
13. Review `docs/submission-story.md`, `docs/cloud-readiness-report.md`, `docs/qwen-live-proof.md`, `docs/live-proof-gate.md`, `docs/qwen-route-status.md`, and `docs/validation-report.md` for the evidence boundary.

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
