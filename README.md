# PrizePilot

PrizePilot is a Qwen Cloud hackathon submission for Track 4, Autopilot Agent. It turns hackathon and bounty opportunities into ranked execution plans, public artifact drafts, and human approval checkpoints.

The project is intentionally conservative: it records public repository, blog, video, Devpost submission status, and Qwen live smoke proof only after verification, while keeping live Alibaba Cloud deployment proof, payout eligibility, tax, and KYC outside the repository until those events actually happen.

## Current Public Status

Latest review status as of 2026-06-26: the repository, Blog Award story, presentation deck, Qwen live proof, route status files, and judge review packet are the current source of truth for PrizePilot's submitted public state. Before copying any newly added public link into Devpost, compare `git rev-parse HEAD` with `git ls-remote https://github.com/OOYXLOO/prizepilot-qwen-cloud.git HEAD` and recheck the public URLs.

## Visible Now vs External Gates

| Layer | Status | Boundary |
| --- | --- | --- |
| Submitted identity | Visible now: Devpost project, public repository, Vimeo demo, public Pages hub, deck, Blog Award story, and static judge demo. | These establish that the project is submitted and reviewable. They do not prove prize selection or payout. |
| Qwen live smoke proof | Visible now in the proof packet: one Qwen/DashScope `qwen-plus` run through the China Bailian endpoint with runtime-only key cleanup recorded. | This proves a live Qwen-compatible refinement path, not a live Alibaba Cloud public endpoint. |
| Judge review/update packet | Included in this repository update: judge review card, official requirement fit map, Award Thesis Scorecard, Blog Share Packet, public update digest, refreshed route status, and refreshed cloud-readiness wording. | Verify the exact public HEAD and HTTP 200 links before copying these links into Devpost. |
| Alibaba Cloud endpoint proof | Prepared code only: Function Compute manifest and endpoint checklist exist. | Not live endpoint proof until a public URL returns HTTP 200 at `/` and `/api/plan`. |

Baseline links verified live on 2026-06-15 and rechecked after the 2026-06-26 repository update:

- Devpost project: https://devpost.com/software/prizepilot-qwen-cloud
- Demo video: https://vimeo.com/1200124146
- Backup public WebM video: https://ooyxloo.github.io/prizepilot-qwen-cloud/demo-video/prizepilot-demo.webm
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

New review links that must be HTTP 200 rechecked after the repository update:

- Qwen before/after evidence: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-before-after/
- Judge Review Card: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-review-card/
- Official Requirement Fit: https://ooyxloo.github.io/prizepilot-qwen-cloud/official-requirement-fit/
- Award Thesis Scorecard: https://ooyxloo.github.io/prizepilot-qwen-cloud/award-thesis-scorecard/
- Blog Share Packet: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog-share-packet/
- Public update checklist: https://ooyxloo.github.io/prizepilot-qwen-cloud/public-update-checklist/
- Public update digest: https://ooyxloo.github.io/prizepilot-qwen-cloud/public-update-digest/
- Judge manifest: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-manifest.json
- Submission state: submitted to Devpost; still editable until the Qwen Cloud hackathon deadline.
- Evidence gap: verified live Alibaba Cloud endpoint proof still needs to be captured before judging if account access, credit, and billing approval are available.

## Judge Quickstart

The 3-link reviewer fast path is:

1. Devpost project: https://devpost.com/software/prizepilot-qwen-cloud
2. Demo video: https://vimeo.com/1200124146
3. Blog Award story: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/

Video path: use Vimeo as the Devpost-required hosted video, and keep the Pages-hosted WebM as a backup playback link if Vimeo embedding is unavailable for a reviewer.

This order gives judges the submitted identity, the working demo, and the Blog Post Award narrative before they decide whether to open the Judge Review Card, Official Requirement Fit map, proof boundary, benchmark, Qwen contribution, before/after, live proof, manifest, or static plan files.

For deeper local verification, run the dashboard:

## Local Use

```powershell
$env:PYTHONPATH='src'
python -m prizepilot plan samples/qwen_hackathon.json
python -m prizepilot plan samples/mindtheproduct_world_product_day.json
python -m prizepilot portfolio samples/splunk_agentic_ops.json samples/qwen_hackathon.json samples/mindtheproduct_world_product_day.json samples/uipath_agenthack.json samples/algora_onyx_bounty.json samples/arm_ai_optimization.json
python -m prizepilot cloud-readiness
python -m prizepilot cloud-readiness --checked-at 2026-06-15T12:30:00Z
python -m prizepilot.webapp --host 127.0.0.1 --port 8000
```

Then inspect the local runtime machine-readable planning payload at `http://127.0.0.1:8000/api/plan`. This local server payload is not live Alibaba endpoint proof.
Use `--checked-at` only when a deterministic evidence rebuild is needed for review or diffing; live public updates should regenerate the report with the current action-time timestamp.
Review `docs/submission-story.md`, `docs/benchmark-method.md`, `docs/cloud-readiness-report.md`, `docs/qwen-live-proof.md`, `docs/qwen-contribution-map.md`, `docs/qwen-before-after-evidence.md`, `docs/judge-review-card.md`, `docs/official-requirement-fit.md`, `docs/award-thesis-scorecard.md`, `docs/blog-share-packet.md`, `docs/public-update-checklist.md`, `docs/public-update-digest.md`, `docs/live-proof-gate.md`, `docs/alibaba-endpoint-judge-checklist.md`, `docs/judge-manifest.json`, `docs/qwen-route-status.md`, and `docs/validation-report.md` for the evidence boundary.

Live Qwen refinement has been verified once with a runtime-only key; future runs still require `DASHSCOPE_API_KEY` or `QWEN_API_KEY` at action time only.
The Mind the Product route additionally requires Novus email verification and official Novus installation before final Devpost submission. The web service exposes `/api/novus-readiness` so that gate can be tracked without claiming completion early.

## Demo Assets

- Dashboard screenshots: `docs/screenshots/prizepilot-dashboard-desktop.png` and `docs/screenshots/prizepilot-dashboard-mobile.png`
- Short demo GIF: `docs/screenshots/prizepilot-demo.gif`
- Backup silent WebM: `docs/demo-video/prizepilot-demo.webm`
- Editable presentation deck: `docs/prizepilot-qwen-submission-deck.pptx`
- Static judge demo: `docs/demo/index.html`
- Devpost architecture upload: `architecture.png`
- Recording page: `docs/demo-recording-page.html`
- Recording runbook: `docs/demo-recording-runbook.md`
