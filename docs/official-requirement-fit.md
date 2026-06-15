# Official Requirement Fit

Last updated: 2026-06-15 (+08)

Purpose: give Qwen Cloud judges a compact, honest map from the official Devpost requirements to PrizePilot's public evidence. This is a review aid, not a claim that PrizePilot has won or that payout, tax, KYC, billing, or live Alibaba endpoint proof is complete.

Source reviewed: the public Qwen Cloud Devpost overview/rules page, including the Track 4 Autopilot Agent prompt, submission requirements, prize routes, and judging criteria.

## Fast Verdict

PrizePilot is strongest for the Blog Post Award and Top 10 Honorable Mention because the submitted public package is reviewable without private account access, shows a real money-seeking autopilot workflow, includes one live Qwen/DashScope proof, and keeps the remaining Alibaba endpoint proof explicit instead of implied.

## Requirement Map

| Official requirement or judging signal | PrizePilot evidence | Status |
| --- | --- | --- |
| Build with Qwen models available on Qwen Cloud | `src/prizepilot/qwen_client.py`, tests, `docs/qwen-live-proof.md`, `docs/qwen-contribution-map.md`, and `docs/qwen-before-after-evidence.md` show the Qwen-compatible client, one live `qwen-plus` refinement pass, and how Qwen improved the public narrative. | Verified Qwen/DashScope smoke proof captured. |
| Track 4 Autopilot Agent | `src/prizepilot/agent.py`, `src/prizepilot/webapp.py`, static `docs/api/plan.json`, and the judge demo show route ranking, artifact planning, external-tool proof gates, and human checkpoints. | Public review ready. |
| Public open-source repository with license and run instructions | GitHub repository, `LICENSE`, `README.md`, `pyproject.toml`, `Dockerfile`, source, tests, samples, screenshots, and docs are included. | Public baseline is live; local update requires user-approved push. |
| Proof of Alibaba Cloud deployment / Alibaba services use | `deploy/alibaba-cloud/s.yaml`, `deploy/alibaba-cloud/README.md`, `docs/alibaba-cloud-deployment-runbook.md`, `docs/alibaba-cloud-deployment-proof-template.md`, and `docs/alibaba-endpoint-judge-checklist.md` document the Function Compute path and exact HTTP success signal. | Prepared code proof only; live public endpoint proof remains pending. |
| Architecture diagram | `architecture.png`, `architecture.svg`, and `ARCHITECTURE.md` describe the planner, Qwen/DashScope refinement path, web API, static evidence, and Alibaba Function Compute adapter. | Public artifact ready. |
| Public demo video around three minutes | Vimeo demo is the primary public video; `docs/demo-video/prizepilot-demo.webm` is a Pages-hosted fallback. | Public video path ready. |
| Text description and track selection | Devpost project fields, `docs/devpost-project-fields.md`, `docs/submission-story.md`, and README state Track 4 and describe the workflow. | Submitted and documented. |
| Optional Blog Post Award story | `docs/blog/index.html`, `docs/blog-share-packet.md`, and `docs/award-thesis-scorecard.md` frame the build journey and explain the Qwen role. | Primary award route ready. |
| Technical depth and engineering | Deterministic planner, Qwen-compatible client, local HTTP API, static JSON snapshot, tests, Dockerfile, and Alibaba manifest show modularity and reproducibility. | Public evidence ready; endpoint proof can strengthen it later. |
| Presentation and documentation | Public evidence hub, judge pack, award preflight, evidence map, deck, blog, screenshots, and machine-readable manifest give judges multiple review depths. | Public review ready. |

## Do Not Infer

- Do not infer that a live Alibaba Cloud public endpoint exists until a public URL returns HTTP 200 at `/` and `/api/plan`.
- Do not infer prize selection, payout, tax, KYC, billing, bank, or cloud-credit completion.
- Do not publish API keys, raw request headers, account IDs, cookies, private console screenshots, private email, payment data, or localStorage.

## Best Next Public Update

After account-owner approval, push the local update, recheck this page and all new links for HTTP 200, then update Devpost only with claims that are already public. If the Alibaba endpoint proof is not completed, keep the wording as "prepared code proof only."
