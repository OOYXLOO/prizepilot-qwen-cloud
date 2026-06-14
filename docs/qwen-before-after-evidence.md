# Qwen Before/After Evidence

Purpose: show the practical difference between PrizePilot's deterministic route plan and the Qwen/DashScope refinement layer without overstating proof. This is a judge-facing bridge between the live smoke proof and the public Blog Post Award story.

## Evidence Boundary

- Completed: one live Qwen/DashScope refinement pass using `qwen-plus` with a runtime-only account-owner key.
- Published safely: model name, public base URL, command shape, exit code, a short non-sensitive excerpt, and cleanup status.
- Still pending: live Alibaba Cloud public endpoint proof.
- Not published: API keys, raw headers, account metadata, billing data, payout data, tax data, KYC data, cookies, or private console state.

## Before Qwen

The deterministic planner already selected the Qwen route with an honest gate model:

| Field | Deterministic plan |
| --- | --- |
| Primary target | Blog Post Award |
| Secondary target | Top 10 Honorable Mention Projects |
| Core reason | Public project story plus Qwen Cloud evidence can be prepared, while the route still has higher upside than a pure feedback task. |
| Required proof | Qualified Devpost project, public repository, demo video, public blog/social story, Qwen usage evidence, and Alibaba deployment proof. |
| Risk policy | Do not claim cloud deployment, payout, billing, tax, or KYC status without proof. |

The plan was useful, but it read like an internal execution checklist. It needed tighter public language for judges.

## Qwen Refinement

The live Qwen/DashScope pass converted that checklist into a stricter public narrative:

| Qwen refinement | Where it appears now |
| --- | --- |
| Treat the Blog Post Award as tied to a qualified Devpost project, not as a standalone post. | `docs/blog/index.html`, `docs/judge-pack/index.html`, `docs/qwen-rule-verification.md` |
| Keep the USD 500 / 10-winner Blog Post Award value visible while naming Honorable Mention as the secondary route. | `docs/judge-pack/index.html`, `docs/award-preflight/index.html`, `docs/award-evidence-map/index.html` |
| Say exactly what the live Qwen proof establishes and what it does not establish. | `docs/qwen-live-proof.md`, `docs/live-proof-gate.md`, `docs/cloud-readiness-report.md` |
| Make no-credentials, no-premature-publishing, no-assumed-infrastructure, and eligibility-first wording prominent. | `docs/qwen-contribution-map.md`, `docs/devpost-project-fields.md`, `docs/blog/index.html` |
| Keep the Alibaba endpoint as a pending gate until `/` and `/api/plan` return HTTP 200 from a real public URL. | `docs/alibaba-endpoint-judge-checklist.md`, `docs/alibaba-endpoint-checklist/index.html`, `docs/judge-manifest.json` |

## After Qwen

The public package now presents a sharper judge path:

1. Verify the submitted Devpost project and demo.
2. Read the Blog Post Award story as the primary prize narrative.
3. Check the judge pack and award evidence map for completed proof versus pending gates.
4. Inspect Qwen live proof and this before/after evidence to see the model's role.
5. Treat Alibaba endpoint proof as a prepared but unclaimed improvement.

## Concrete Copy Improvements

| Surface | Before | After |
| --- | --- | --- |
| Blog story | Qwen route described as one route inside a broader prize portfolio. | Blog Post Award is named as the reader path, with submitted Devpost status and Qwen proof stated up front. |
| Judge pack | Qwen contribution needed explanation inside a general evidence page. | Qwen contribution has its own map plus this before/after evidence page. |
| Devpost field draft | Deployment and Qwen proof could blur together. | Qwen live proof is marked complete; Alibaba endpoint proof remains pending until captured. |
| Route status | Public artifacts and account-gated proof were tracked together. | Status separates public/submitted evidence from the single remaining live endpoint gate. |

## Reproduce Without A Key

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
python -m prizepilot plan samples/qwen_hackathon.json
python -m prizepilot qwen-status
python -m prizepilot cloud-readiness
```

Future live Qwen reruns still require an account-owner supplied runtime key. No API key should be committed, logged, pasted into public materials, or stored in this repository.
