# Publication Action Card

Do not push, publish, edit Devpost, or change account-side proof without user confirmation at action time.

Current state on 2026-06-14:

- Qwen Devpost project is submitted and public: https://devpost.com/software/prizepilot-qwen-cloud
- Public repository is live: https://github.com/OOYXLOO/prizepilot-qwen-cloud
- Public evidence hub is live: https://ooyxloo.github.io/prizepilot-qwen-cloud/
- Public Vimeo demo page is reachable and linked from the submitted project; Devpost playback should be checked user-present before any stronger playback claim: https://vimeo.com/1200124146
- Public Blog Award story, judge pack, judge review card, Award Thesis Scorecard, Blog Share Packet, award preflight, award evidence map, Qwen live proof, Qwen contribution map, Qwen before/after evidence, public update checklist, static plan JSON, and judge manifest are part of the prepared public package.
- Public update digest is prepared at `docs/public-update-digest.md` and `docs/public-update-digest/` to explain the public baseline, working-copy update, proof improvements, HTTP 200 recheck requirement, and do-not-claim boundaries before any user-approved push.
- One live Qwen/DashScope smoke proof has been captured safely with a runtime-only account-owner key.
- The remaining high-value proof gap is a verified live Alibaba Cloud endpoint. Do not claim that endpoint until a real public URL returns HTTP 200 for `/` and `/api/plan`.

## Superseded 2026-06-10 Blockers

The earlier notes about GitHub push authorization, Devpost portfolio creation reCAPTCHA, Vimeo setup, and final Devpost submission are historical. They should not be treated as the current state.

Current blocker type:

- Public Qwen package improvements can be prepared locally.
- Public push/Devpost edits still require explicit user approval because they change external public pages.
- Alibaba endpoint proof requires account-owner approval for cloud account, credits or billing, deployment, and public endpoint verification.

## Minimum Approval Before Public Update

Use this confirmation before pushing the local Qwen update packet or editing Devpost:

```text
Please confirm I should publish the latest PrizePilot Qwen update packet. This will push public repository/GitHub Pages changes and may require updating Devpost copy. The update must only claim evidence that already exists.
```

After approval, verify the public package first:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
python -m compileall -q src tests tools
python -m prizepilot qwen-status
python -m prizepilot cloud-readiness
python -m json.tool docs/judge-manifest.json
```

Then push and verify public URLs before editing Devpost. If GitHub Pages or any public evidence link returns a non-200 status, do not update Devpost.
