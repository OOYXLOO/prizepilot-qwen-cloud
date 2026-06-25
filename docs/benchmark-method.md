# PrizePilot Benchmark Method

Last updated: 2026-06-13

PrizePilot is evaluated as a route-selection and evidence-management agent, not as a claim that any prize has already been won. This note explains how the sample ranking is produced and what a judge can reproduce without account access.

## What Is Being Measured

PrizePilot answers one operational question: which cash-prize route should a small builder work on next, given prize value, winner count, deadline pressure, public artifact requirements, and human-gated actions.

The benchmark therefore checks four signals:

| Signal | Why It Matters | Public Evidence |
| --- | --- | --- |
| Reachable value | A smaller multi-winner route may be more rational than a single grand prize. | `samples/*.json`, `src/prizepilot/agent.py`, and `docs/api/plan.json` |
| Evidence readiness | Public proof should exist before a public claim is made. | Judge pack, cloud readiness report, Qwen live proof page, route ledger |
| Human-gate clarity | Account, API key, billing, payout, tax, and KYC steps must not be hidden inside automation. | Approval queue in `/api/plan` and dashboard |
| Reproducibility | Judges should be able to inspect the plan without logging in. | Static plan JSON, local CLI, local web/API service |

## Sample Portfolio

The current portfolio uses six structured examples:

| Route | Target | Why It Is Included |
| --- | --- | --- |
| Splunk Agentic Ops | Most Valuable Feedback | Near-term multi-winner feedback route with low build friction |
| Qwen Cloud | Blog Post Award / Honorable Mention | Submitted Qwen project route with USD 500 upside and sponsor-tool evidence requirements |
| Mind the Product World Product Day | Product analytics path | Example of a product route blocked by third-party account verification |
| UiPath AgentHack | Agent/product feedback route | Higher prize pool but access and product setup gates |
| Onyx Algora bounty | Public PR bounty | Public code contribution route with maintainer-review gate |
| Arm AI Optimization | Cloud/hardware route | Illustrates high technical upside with heavier setup cost |

## Scoring Method

The deterministic scorer is intentionally simple and inspectable:

- Prize amount contributes up to a capped value so a single long-shot grand prize does not dominate.
- Winner count adds material weight because multi-winner categories are more reachable.
- Feedback, blog, and honorable-mention tags receive bonuses because they match fast, evidence-rich routes.
- Single-winner, public-PR, product-analytics, cloud-deployment, and non-cash tags apply penalties based on execution risk.
- Participant count and human blockers reduce the route score.
- A route marked `primary` receives a bonus; a route marked `backup` receives a small penalty.

The relevant implementation is `_prize_score()` and `_route_score()` in `src/prizepilot/agent.py`.

## Reproducible Commands

From the repository root:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
python -m prizepilot plan samples/qwen_hackathon.json
python -m prizepilot portfolio samples/splunk_agentic_ops.json samples/qwen_hackathon.json samples/mindtheproduct_world_product_day.json samples/uipath_agenthack.json samples/algora_onyx_bounty.json samples/arm_ai_optimization.json
python -m prizepilot qwen-status
python -m prizepilot cloud-readiness
python -m prizepilot.webapp --host 127.0.0.1 --port 8000
```

The public setup-free equivalent is `docs/api/plan.json`.

## Current Result

The current sample ranking keeps Splunk first because it is a near-term, multi-winner feedback route with limited build friction. Qwen is the stronger submitted project route because it has public assets, a verified Qwen/DashScope smoke proof, and Blog Post Award / Honorable Mention upside, but it still has one account-gated improvement: live Alibaba Cloud endpoint proof.

## Limits

- The portfolio is a decision-support sample, not a statistical prediction of winning.
- Public sample data must be refreshed when prize pages, deadlines, participant counts, or rules change.
- Live Qwen/DashScope proof has been captured once; future reruns still require action-time account-owner key entry.
- Live Alibaba Cloud endpoint proof is not claimed until a public endpoint exists.
- Prize awards, payout, tax, KYC, and bank steps are outside the repository and must stay on official claim channels.
