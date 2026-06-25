# Qwen Public Update Digest

Last updated: 2026-06-26 (+08)

This digest is the non-sensitive decision packet for the public repository update. It does not edit Devpost, claim a prize, claim payout, claim a live Alibaba Cloud endpoint, or store secrets.

## Current Heads

- Previous public repository baseline: `6329f1ba225c3a59881882e8a5c0dd1a9fb2e33d`
- Repository update head: verify with `git rev-parse HEAD` locally and `git ls-remote https://github.com/OOYXLOO/prizepilot-qwen-cloud.git HEAD` after push.
- Public status: submitted Devpost project is live and editable until the Qwen Cloud hackathon deadline.
- Working-copy status: update packet is locally verified. Any Devpost edit remains a separate account-side action and should happen only after public URL rechecks.

## Public Link Health Boundary

Latest public baseline check on 2026-06-15 found the existing review pages live, including `demo/`, `judge-pack/`, `award-preflight/`, `award-evidence-map/`, `cloud-readiness/`, `benchmark-method/`, `live-proof-gate/`, `qwen-live-proof/`, `qwen-contribution/`, `alibaba-endpoint-checklist/`, `api/plan.json`, and `blog/`.

The new review pages must be HTTP 200 rechecked after the repository update before they are copied into Devpost: `qwen-before-after/`, `judge-review-card/`, `official-requirement-fit/`, `award-thesis-scorecard/`, `blog-share-packet/`, `public-update-checklist/`, `public-update-digest/`, and `judge-manifest.json`.

## What The Update Improves

- Adds a machine-readable judge manifest that names the submitted project, award targets, judge path, completed evidence, pending evidence, and do-not-infer boundaries.
- Adds a pre-push head-check policy so the account owner can confirm the exact local commit and public baseline before any public side effect.
- Adds Qwen before/after evidence so judges can see how deterministic route planning was refined into clearer Qwen-backed public copy.
- Adds a judge review card, Official Requirement Fit map, Award Thesis Scorecard, Blog Share Packet, and public update checklist so reviewers and the account owner have a short path through the strongest public evidence, official rule fit, ranked award thesis, and publishing gates.
- Adds a Pages-hosted WebM fallback beside the Devpost-required Vimeo demo so video review does not depend on one player.
- Links the before/after and official-fit trail from README, public hub, judge pack, Blog Award story, award preflight, award evidence map, Qwen contribution map, and Official Requirement Fit map.
- Refreshes the public status language so the project reads as submitted and improvable, not as a draft.
- Keeps the live Alibaba Cloud public endpoint as a pending account-owner proof gate instead of overclaiming it.

## What Must Not Be Claimed

- Do not claim PrizePilot has won a prize.
- Do not claim payout, tax, KYC, bank, billing, or cloud-credit setup is complete.
- Do not claim a live Alibaba Cloud public endpoint exists until `/` and `/api/plan` return HTTP 200 from a real Alibaba Cloud URL.
- Do not claim that the award thesis scorecard predicts prize selection; it is a review summary, not a win probability model.
- Do not publish API keys, request headers, account IDs, cookies, private email content, console screenshots, payment data, or localStorage.

## Devpost And Cloud Gate

Only after the account owner is present and the public URLs are rechecked:

1. Confirm the repository update has been pushed.
2. Wait for GitHub Pages to publish the new hub, judge manifest, and before/after evidence links.
3. Verify public URLs return HTTP 200.
4. Edit Devpost only with evidence that actually exists.

## Verification Snapshot

Latest local verification before this digest:

- `$env:PYTHONPATH='src'; python -m unittest discover -s tests -v`
- `$env:PYTHONPATH='src'; python -m compileall -q src tests tools`
- `$env:PYTHONPATH='src'; python -m prizepilot qwen-status`
- `$env:PYTHONPATH='src'; python -m prizepilot cloud-readiness`
- Optional deterministic evidence diff: `$env:PYTHONPATH='src'; python -m prizepilot cloud-readiness --checked-at 2026-06-15T12:30:00Z`
- `python -m json.tool docs/judge-manifest.json`

Expected state: `submitted_can_still_improve` with `qwen_live_verified_endpoint_pending`.
