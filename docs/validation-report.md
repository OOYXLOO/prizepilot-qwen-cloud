# Validation Report

Latest verification: 2026-06-10 after adding demo recording assets

## Passed Gates

- 17 unit tests pass with `PYTHONPATH=src; python -m unittest discover -s tests -v`.
- `python -m compileall -q .` passes.
- `python -m prizepilot plan samples/qwen_hackathon.json` targets the Blog Post Award.
- `python -m prizepilot portfolio ...` keeps Splunk first and Qwen second when run with current sample names.
- `python -m prizepilot qwen-status` generates `docs/qwen-route-status.md/json` with local artifacts complete, 8 public/account gates incomplete, and phase `ready_for_user_publication_steps`.
- Qwen/DashScope client tests verify `DASHSCOPE_API_KEY` support, `QWEN_API_KEY` precedence, OpenAI-compatible `/chat/completions` request shape, and missing-key errors.
- Deployable demo service checks verify `/`, `/api/plan`, JSON serializability, target prize output, and integrity-boundary copy.
- External local process smoke test passed on 2026-06-10 after recovery: a hidden Python process served `/` and `/api/plan`, both returned 200, project was `PrizePilot`, target was `Blog Post Award`, and the portfolio still ranked Splunk first.
- Browser check passed on 2026-06-10 after recovery: desktop and 390px mobile views showed the PrizePilot headline, target prize, prize amount, and integrity-boundary copy with no horizontal overflow.
- Demo recording page check passed on 2026-06-10 through a temporary local server at `127.0.0.1`: desktop and 390px mobile layouts had no horizontal overflow, the dashboard screenshots loaded, and autoplay advanced through Qwen/demo chapters.
- Public ZIP inspection after adding Qwen route status: 44 entries, missing required entries 0, forbidden cache/private entries 0. Exact byte size is not a gate.
- Screenshots were rebuilt on 2026-06-10 from the local web service:
  - `docs/screenshots/prizepilot-dashboard-desktop.png`
  - `docs/screenshots/prizepilot-dashboard-mobile.png`

## Still Not Proven

- Real Qwen Cloud model usage has not been run because it requires a user-provided API key at action time.
- Alibaba Cloud deployment proof has not been created.
- Docker CLI is installed locally, but Docker Desktop/Linux daemon was not running during the 2026-06-10 check, so a local `docker build` has not been proven in this environment.
- Public GitHub repository, public demo video, blog/social post, and Devpost final submission are not done.
