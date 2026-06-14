# PrizePilot

PrizePilot is a Qwen Cloud hackathon submission for Track 4, Autopilot Agent. It turns hackathon and bounty opportunities into ranked execution plans, public artifact drafts, and human approval checkpoints.

The project is intentionally conservative: it records public repository, blog, video, Devpost submission status, and Qwen live smoke proof only after verification, while keeping live Alibaba Cloud deployment proof, payout eligibility, tax, and KYC outside the repository until those events actually happen.

## Current Public Status

Latest review status as of 2026-06-15: the repository, Blog Award story, presentation deck, Qwen live proof, and route status files are the current source of truth for PrizePilot's submitted public state. Local reviewer packets may be ahead of the public repository; before any public update, compare `git rev-parse HEAD` with `git ls-remote https://github.com/OOYXLOO/prizepilot-qwen-cloud.git HEAD` and publish only after account-owner approval.

## Visible Now vs Prepared Locally

| Layer | Status | Boundary |
| --- | --- | --- |
| Submitted identity | Visible now: Devpost project, public repository, Vimeo demo, public Pages hub, deck, Blog Award story, and static judge demo. | These establish that the project is submitted and reviewable. They do not prove prize selection or payout. |
| Qwen live smoke proof | Visible now in the proof packet: one Qwen/DashScope `qwen-plus` run through the China Bailian endpoint with runtime-only key cleanup recorded. | This proves a live Qwen-compatible refinement path, not a live Alibaba Cloud public endpoint. |
| Judge review/update packet | Prepared locally until a user-approved push confirms the final public URLs: judge review card, Blog Share Packet, public update digest, refreshed route status, and refreshed cloud-readiness wording. | Treat these as prepared artifacts until the public HEAD is verified after a push. |
| Alibaba Cloud endpoint proof | Prepared code only: Function Compute manifest and endpoint checklist exist. | Not live endpoint proof until a public URL returns HTTP 200 at `/` and `/api/plan`. |

Baseline links verified live on 2026-06-15:

- Devpost project: https://devpost.com/software/prizepilot-qwen-cloud
- Demo video: https://vimeo.com/1200124146
- Presentation deck: https://ooyxloo.github.io/prizepilot-qwen-cloud/prizepilot-qwen-submission-deck.pptx
- Judge demo: https://ooyxloo.github.io/prizepilot-qwen-cloud/demo/
- Judge evidence pack: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/
- Award preflight: https://ooyxloo.github.io/prizepilot-qwen-cloud/award-preflight/
- Award evidence map: https://ooyxloo.github.io/prizepilot-qwen-cloud/award-evidence-map/
- Cloud readiness report: https://ooyxloo.github.io/prizepilot-qwen-cloud/cloud-readiness/
- Benchmark method: https://ooyxloo.github.io/prizepilot-qwen-cloud/benchmark-method/
- Live proof gate: https://ooyxloo.github.io/prizepilot-qwen-cloud/live-proof-gate/
- Qwen live proof: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-live-proof/
- Qwen contribution map: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-contribution/
- Alibaba endpoint checklist: https://ooyxloo.github.io/prizepilot-qwen-cloud/alibaba-endpoint-checklist/
- Static plan snapshot: https://ooyxloo.github.io/prizepilot-qwen-cloud/api/plan.json
- Blog Award story: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/
- Repository: https://github.com/OOYXLOO/prizepilot-qwen-cloud

Prepared next-update links, not public until a user-approved push and HTTP 200 recheck:

- Qwen before/after evidence: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-before-after/
- Judge Review Card: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-review-card/
- Blog Share Packet: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog-share-packet/
- Public update checklist: https://ooyxloo.github.io/prizepilot-qwen-cloud/public-update-checklist/
- Public update digest: https://ooyxloo.github.io/prizepilot-qwen-cloud/public-update-digest/
- Judge manifest: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-manifest.json
- Submission state: submitted to Devpost; still editable until the Qwen Cloud hackathon deadline.
- Evidence gap: verified live Alibaba Cloud endpoint proof still needs to be captured before judging if account access, credit, and billing approval are available.

## Judge Quickstart

The 3-link reviewer fast path is:

1. Devpost project: https://devpost.com/software/prizepilot-qwen-cloud
2. Judge Review Card: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-review-card/
3. Blog Award story: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/

This order gives judges the submitted identity, the one-minute award thesis and do-not-infer boundary, and the Blog Post Award narrative before they decide whether to open the deeper proof boundary, benchmark, Qwen contribution, before/after, live proof, manifest, or static plan files.

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
Review `docs/submission-story.md`, `docs/benchmark-method.md`, `docs/cloud-readiness-report.md`, `docs/qwen-live-proof.md`, `docs/qwen-contribution-map.md`, `docs/qwen-before-after-evidence.md`, `docs/judge-review-card.md`, `docs/blog-share-packet.md`, `docs/public-update-checklist.md`, `docs/public-update-digest.md`, `docs/live-proof-gate.md`, `docs/alibaba-endpoint-judge-checklist.md`, `docs/judge-manifest.json`, `docs/qwen-route-status.md`, and `docs/validation-report.md` for the evidence boundary.

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
