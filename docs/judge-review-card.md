# Qwen Judge Review Card

Last updated: 2026-06-15 (+08)

This is the 60-second review card for PrizePilot, a submitted Qwen Cloud Track 4 project. It is designed for judges who want the shortest safe path through the public evidence without account access, private consoles, API keys, or local setup.

## 60-Second Path

1. Confirm the submitted Devpost identity: https://devpost.com/software/prizepilot-qwen-cloud
2. Watch the demo: https://vimeo.com/1200124146
3. Read the Blog Award story: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/

If the Vimeo player is unavailable, use the backup public WebM: https://ooyxloo.github.io/prizepilot-qwen-cloud/demo-video/prizepilot-demo.webm

## Deeper Review

- Judge evidence pack: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/
- Award thesis scorecard: https://ooyxloo.github.io/prizepilot-qwen-cloud/award-thesis-scorecard/
- Qwen before/after evidence: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-before-after/
- Qwen contribution map: https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-contribution/
- Remaining Alibaba endpoint boundary: https://ooyxloo.github.io/prizepilot-qwen-cloud/alibaba-endpoint-checklist/

## Award Thesis

PrizePilot is strongest for the Blog Post Award because the project story is itself the product: an agent choosing a realistic cash-prize route, building public proof, and stopping at human approval gates instead of inventing private/account evidence.

The secondary route is Honorable Mention because the package is public, reproducible, and honest about its one remaining high-value gap: live Alibaba Cloud endpoint proof. The award thesis scorecard ranks these routes without claiming that prize selection is predictable.

## Qwen Evidence

- Qwen/DashScope live smoke proof is recorded without storing secrets.
- The Qwen contribution map explains where Qwen improves route language, story clarity, and risk wording.
- The before/after evidence shows deterministic planning, Qwen refinement, and the public-copy improvements that followed.
- The project keeps deterministic scoring separate from model refinement so judges can reproduce the baseline without a key.

## Do Not Infer

- Do not infer that PrizePilot has won a prize.
- Do not infer that payout, tax, KYC, billing, or bank setup is complete.
- Do not infer that a live Alibaba Cloud endpoint exists until a real public URL returns HTTP 200 for `/` and `/api/plan`.
- Do not infer that API keys, cookies, account-local storage, or private console data are stored in the repository.

## Local Verification

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
python -m compileall -q src tests tools
python -m prizepilot qwen-status
python -m prizepilot cloud-readiness
python -m json.tool docs\judge-manifest.json
python -m json.tool docs\qwen-route-status.json
python -m json.tool docs\cloud-readiness-report.json
```
