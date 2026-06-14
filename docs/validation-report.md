# Validation Report

Latest verification: 2026-06-14 after Qwen judge-manifest and before/after evidence refresh.

## Passed Gates

- 40 unit tests pass with `PYTHONPATH=src; python -m unittest discover -s tests -v`.
- `python -m compileall -q src tests tools` passes.
- `python -m json.tool docs/judge-manifest.json`, `python -m json.tool docs/qwen-route-status.json`, and `python -m json.tool docs/cloud-readiness-report.json` parse the machine-readable judge packets.
- Editable presentation deck is present at `docs/prizepilot-qwen-submission-deck.pptx`, opens as a valid PPTX archive, and contains 5 slides.
- `python -m prizepilot plan samples/qwen_hackathon.json` targets the Blog Post Award.
- `python -m prizepilot portfolio ...` keeps Splunk first and Qwen second when run with current sample names.
- `python -m prizepilot qwen-status` generates `docs/qwen-route-status.md/json` with local artifacts complete, Qwen Devpost submitted, Qwen live smoke proof complete, phase `submitted_can_still_improve`, and Alibaba endpoint proof still open.
- `python -m prizepilot cloud-readiness` generates `docs/cloud-readiness-report.md/json` with overall status `qwen_live_verified_endpoint_pending` and seven passing checks: Qwen request shape, runtime-only secret boundary, Qwen live smoke proof, Alibaba Function Compute manifest, public HTTP proof targets, dashboard judge payload, and public claim boundary.
- Qwen/DashScope client tests verify `DASHSCOPE_API_KEY` support, `QWEN_API_KEY` precedence, OpenAI-compatible `/chat/completions` request shape, and missing-key errors.
- Deployable demo service checks verify `/`, `/api/plan`, JSON serializability, target prize output, submission status, agent walkthrough, judge scorecard, evidence gaps, and integrity-boundary copy.
- Public repository, Devpost project, Vimeo demo, Blog Award story, judge pack, Qwen live proof, Qwen contribution map, Qwen before/after evidence, static plan JSON, cloud readiness report, and presentation deck are represented in the local public package.
- Playwright browser layout checks pass on desktop and 390px mobile for the public hub, judge pack, Qwen before/after evidence, Qwen contribution map, Blog Award story, award evidence map, and award preflight, with no console errors or horizontal overflow.
- Screenshots rebuilt from the local web service are included:
  - `docs/screenshots/prizepilot-dashboard-desktop.png`
  - `docs/screenshots/prizepilot-dashboard-mobile.png`

## Current Evidence Boundary

- Verified: submitted Devpost project, public repo, public demo video, public Blog Award story, public judge hub, static plan snapshot, and one live Qwen/DashScope refinement pass.
- Prepared but not claimed: Alibaba Cloud Function Compute deployment path and public endpoint proof.
- Not handled by the repository: payout, tax, KYC, bank, billing, cookies, private console pages, private email, OTPs, and API keys.

## Still Not Proven

- Alibaba Cloud live endpoint proof has not been created.
- Docker CLI is installed locally, but Docker Desktop/Linux daemon was not running during the earlier check, so a local `docker build` has not been proven in this environment.
- Any public Devpost copy update after this local refresh requires user-present approval and should happen only after public links return HTTP 200.
