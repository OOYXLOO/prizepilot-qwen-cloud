# Validation Report

Latest verification: 2026-06-13 after adding Qwen/DashScope live smoke proof

## Passed Gates

- 33 unit tests pass with `PYTHONPATH=src; python -m unittest discover -s tests -v`.
- `python -m compileall -q src tests tools` passes.
- Editable presentation deck is present at `docs/prizepilot-qwen-submission-deck.pptx`, opens as a valid PPTX archive, and contains 5 slides.
- `python -m prizepilot plan samples/qwen_hackathon.json` targets the Blog Post Award.
- `python -m prizepilot portfolio ...` keeps Splunk first and Qwen second when run with current sample names.
- `python -m prizepilot qwen-status` generates `docs/qwen-route-status.md/json` with local artifacts complete, Qwen Devpost submitted, Qwen live smoke proof complete, and phase `submitted_can_still_improve` while Alibaba endpoint proof remains open.
- `python -m prizepilot cloud-readiness` generates `docs/cloud-readiness-report.md/json` with overall status `qwen_live_verified_endpoint_pending` and seven passing checks: Qwen request shape, runtime-only secret boundary, Qwen live smoke proof, Alibaba Function Compute manifest, public HTTP proof targets, dashboard judge payload, and public claim boundary.
- Qwen/DashScope client tests verify `DASHSCOPE_API_KEY` support, `QWEN_API_KEY` precedence, OpenAI-compatible `/chat/completions` request shape, and missing-key errors.
- Deployable demo service checks verify `/`, `/api/plan`, JSON serializability, target prize output, submission status, agent walkthrough, judge scorecard, evidence gaps, and integrity-boundary copy.
- Static HTTP checks returned 200 for the public evidence pages including `/qwen-live-proof/`.
- Browser check on `docs/cloud-readiness/` passed in desktop and 390px mobile viewports: expected heading/checks/no-secret boundary were visible, no console errors were recorded, and no horizontal overflow was detected.
- External local process smoke test passed on 2026-06-10 after recovery: a hidden Python process served `/` and `/api/plan`, both returned 200, project was `PrizePilot`, target was `Blog Post Award`, and the portfolio still ranked Splunk first.
- Browser check passed on 2026-06-10 after recovery: desktop and 390px mobile views showed the PrizePilot headline, target prize, prize amount, and integrity-boundary copy with no horizontal overflow.
- Demo recording page check passed on 2026-06-10 through a temporary local server at `127.0.0.1`: desktop and 390px mobile layouts had no horizontal overflow, the dashboard screenshots loaded, and autoplay advanced through Qwen/demo chapters.
- Public GitHub repository, public Vimeo demo video, blog/social post, Devpost final submission, public judge evidence pack, public cloud readiness report, Qwen live proof page, and public presentation deck are done locally and ready for publication.
- Public judge evidence pack, cloud readiness report, and presentation deck are linked from the GitHub Pages evidence hub and README.
- Screenshots were rebuilt on 2026-06-10 from the local web service:
  - `docs/screenshots/prizepilot-dashboard-desktop.png`
  - `docs/screenshots/prizepilot-dashboard-mobile.png`

## Still Not Proven

- Alibaba Cloud deployment proof has not been created.
- Docker CLI is installed locally, but Docker Desktop/Linux daemon was not running during the 2026-06-10 check, so a local `docker build` has not been proven in this environment.
- Alibaba Cloud live endpoint proof still needs to be strengthened before judging.
