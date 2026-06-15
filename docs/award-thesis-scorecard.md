# Qwen Award Thesis Scorecard

Last updated: 2026-06-15 (+08)

Purpose: give Qwen Cloud judges and the account owner a compact, evidence-linked view of why PrizePilot's strongest award route is the Blog Post Award, with Honorable Mention as the secondary route. This is not a statistical prediction of winning, and it does not claim prize selection, payout, or a live Alibaba Cloud public endpoint.

## Ranked Award Thesis

| Rank | Award route | Why this is the strongest honest route | Evidence |
| --- | --- | --- | --- |
| 1 | Blog Post Award | The story is the product loop: PrizePilot uses Qwen to choose a realistic cash-prize route, build public proof, and stop at human approval gates instead of inventing private/account evidence. | `docs/blog/`, `docs/blog-share-packet.md`, `docs/qwen-before-after-evidence.md`, `docs/qwen-contribution-map.md` |
| 2 | Top 10 Honorable Mention Projects | The submission is public, reproducible, and unusually clear about completed evidence versus pending sponsor proof. | `docs/judge-pack/`, `docs/award-evidence-map/`, `docs/cloud-readiness-report.md`, `docs/judge-manifest.json` |
| 3 | Track 4 Autopilot Agent fit | The core product is an autopilot agent for route triage, artifact planning, and human gate management. | `src/prizepilot/agent.py`, `src/prizepilot/qwen_client.py`, `docs/api/plan.json`, `tests/` |

## Judge-Visible Strengths

- Public submission identity: Devpost, GitHub repo, Vimeo demo, Pages hub, deck, static demo, and public blog are reviewable without private account access.
- Qwen contribution: live Qwen/DashScope smoke proof exists, and the before/after evidence shows how Qwen sharpens route language, story clarity, and risk wording.
- Reproducibility: deterministic planning still works without a model key, so Qwen refinement improves the narrative without hiding the baseline.
- Integrity boundary: Alibaba endpoint proof remains pending until a real public URL returns HTTP 200 at `/` and `/api/plan`.

## Do Not Infer

- Do not infer PrizePilot has won, been shortlisted, or received a payout.
- Do not infer payout, tax, KYC, billing, bank, or cloud-credit setup is complete.
- Do not infer a live Alibaba Cloud public endpoint exists until public HTTP proof is captured.
- Do not publish API keys, request headers, account IDs, cookies, private console screenshots, private email, payment data, or localStorage.

## Local Verification

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
python -m compileall -q src tests tools
python -m prizepilot qwen-status
python -m prizepilot cloud-readiness
python -m json.tool docs\judge-manifest.json
```
