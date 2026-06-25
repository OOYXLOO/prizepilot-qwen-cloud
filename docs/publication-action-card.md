# Publication Action Card

Do not edit Devpost or change account-side proof without action-time account-owner verification.

Current state on 2026-06-26:

## Live Baseline

- Qwen Devpost project is submitted and public: https://devpost.com/software/prizepilot-qwen-cloud
- Public repository is live: https://github.com/OOYXLOO/prizepilot-qwen-cloud
- Public evidence hub is live: https://ooyxloo.github.io/prizepilot-qwen-cloud/
- Public Vimeo demo page is reachable and linked from the submitted project; Devpost playback should be checked user-present before any stronger playback claim: https://vimeo.com/1200124146
- Public baseline links currently live include the Devpost project, public repository, public evidence hub, public Vimeo demo page, Blog Award story, judge demo, and existing proof pages that have already been pushed.

## Repository Update Packet

- Judge review card, Official Requirement Fit map, Award Thesis Scorecard, Blog Share Packet, award preflight, award evidence map, Qwen contribution map, Qwen before/after evidence, public update checklist, public update digest, static plan JSON, and judge manifest are part of the repository update packet and must be HTTP 200 rechecked before any Devpost copy references them.
- Public update digest is available at `docs/public-update-digest.md` and `docs/public-update-digest/` to explain the previous public baseline, repository update, proof improvements, HTTP 200 recheck requirement, and do-not-claim boundaries.
- One live Qwen/DashScope smoke proof has been captured safely with a runtime-only account-owner key.
- The remaining high-value proof gap is a verified live Alibaba Cloud endpoint. Do not claim that endpoint until a real public URL returns HTTP 200 for `/` and `/api/plan`.

## Superseded 2026-06-10 Blockers

The earlier notes about GitHub push authorization, Devpost portfolio creation reCAPTCHA, Vimeo setup, and final Devpost submission are historical. They should not be treated as the current state.

Current blocker type:

- Qwen package improvements can be published to the repository after local verification.
- Devpost edits still require account-owner action because they change an external submission page.
- Alibaba endpoint proof requires account-owner approval for cloud account, credits or billing, deployment, and public endpoint verification.

## Minimum Check Before Devpost Update

Use this checklist before editing Devpost:

```text
Confirm the latest PrizePilot Qwen public links are live and should be copied into Devpost. The update must only claim evidence that already exists.
```

Before editing Devpost, verify the public package first:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
python -m compileall -q src tests tools
python -m prizepilot qwen-status
python -m prizepilot cloud-readiness
python -m prizepilot cloud-readiness --checked-at 2026-06-15T12:30:00Z
python -m json.tool docs/judge-manifest.json
```

The `--checked-at` command is an optional deterministic diff check, not a substitute for the fresh action-time `cloud-readiness` run. Verify public URLs before editing Devpost. If GitHub Pages or any public evidence link returns a non-200 status, do not update Devpost.
