# Validation Report

Latest verification: 2026-06-12 after adding the public judge evidence pack

## Passed Gates

- 25 unit tests pass with `PYTHONPATH=src; python -m unittest discover -s tests -v`.
- `python -m compileall -q .` passes.
- `python -m prizepilot plan samples/qwen_hackathon.json` targets the Blog Post Award.
- `python -m prizepilot portfolio ...` keeps Splunk first and Qwen second when run with current sample names.
- `python -m prizepilot qwen-status` generates `docs/qwen-route-status.md/json` with local artifacts complete, Qwen Devpost submitted, and phase `submitted_can_still_improve` while Qwen/Alibaba live evidence gaps remain.
- Qwen/DashScope client tests verify `DASHSCOPE_API_KEY` support, `QWEN_API_KEY` precedence, OpenAI-compatible `/chat/completions` request shape, and missing-key errors.
- Deployable demo service checks verify `/`, `/api/plan`, JSON serializability, target prize output, submission status, agent walkthrough, judge scorecard, evidence gaps, and integrity-boundary copy.
- External local process smoke test passed on 2026-06-10 after recovery: a hidden Python process served `/` and `/api/plan`, both returned 200, project was `PrizePilot`, target was `Blog Post Award`, and the portfolio still ranked Splunk first.
- Browser check passed on 2026-06-10 after recovery: desktop and 390px mobile views showed the PrizePilot headline, target prize, prize amount, and integrity-boundary copy with no horizontal overflow.
- Demo recording page check passed on 2026-06-10 through a temporary local server at `127.0.0.1`: desktop and 390px mobile layouts had no horizontal overflow, the dashboard screenshots loaded, and autoplay advanced through Qwen/demo chapters.
- Public tree inspection after adding the judge evidence pack: 64 tracked files, missing required entries 0, forbidden cache/private entries 0. Exact byte size and ZIP entry count are not gates.
- Screenshots were rebuilt on 2026-06-10 from the local web service:
  - `docs/screenshots/prizepilot-dashboard-desktop.png`
  - `docs/screenshots/prizepilot-dashboard-mobile.png`

## Still Not Proven

- Real Qwen Cloud model usage has not been run because it requires a user-provided API key at action time.
- Alibaba Cloud deployment proof has not been created.
- Docker CLI is installed locally, but Docker Desktop/Linux daemon was not running during the 2026-06-10 check, so a local `docker build` has not been proven in this environment.
- Public GitHub repository, public Vimeo demo video, blog/social post, and Devpost final submission are done.
- Public judge evidence pack is linked from the GitHub Pages evidence hub and README.
- Real Qwen/Alibaba Cloud account readiness and live endpoint proof still need to be strengthened before judging.
