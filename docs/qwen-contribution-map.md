# Qwen Contribution Map

Purpose: make the Qwen role legible to judges without overstating it. PrizePilot keeps deterministic route scoring local, then uses Qwen/DashScope as a refinement layer for submission reasoning, story clarity, and risk-boundary wording.

## Judge Takeaway

Qwen is not presented as a magic prize predictor. Its useful role is to turn a structured plan into a sharper, constraint-aware submission narrative while preserving the agent's evidence gates:

- the project route remains tied to the qualified Devpost submission;
- account, deployment, payout, tax, and KYC claims remain gated;
- the public materials only quote a short non-sensitive excerpt from the live model call;
- the deterministic plan can still be reproduced without an API key.

## Contribution Matrix

| Agent stage | Deterministic input | Qwen contribution | Public artifact | Boundary |
| --- | --- | --- | --- | --- |
| Route selection | Prize amount, winners, deadline, submission state, blockers, and evidence gaps from `samples/qwen_hackathon.json`. | Refines the planned Blog Post Award route into a concise, judge-readable plan. | `docs/qwen-live-proof.md`, `docs/qwen-live-proof/`, and `docs/qwen-before-after-evidence.md`. | Qwen does not decide that a prize will be won. |
| Story shaping | Local route ledger, benchmark method, and public proof status. | Makes the narrative more factual: qualified Devpost project first, Blog Award as target, no unsupported account claims. | `docs/submission-story.md`, `docs/blog/`, `docs/judge-pack/`, and `docs/qwen-before-after/`. | No private account metadata or hidden proof is published. |
| Risk wording | Human action queue and live-proof gates. | Helps sharpen constraints such as no credentials stored, no premature publishing, no assumed infrastructure, and eligibility first. | `docs/live-proof-gate.md` and this map. | CAPTCHA, OTP, keys, cloud billing, payout, tax, and KYC remain human-only. |
| Evidence packaging | Public repo, Vimeo demo, GitHub Pages, static plan JSON, and tests. | Turns the proof boundary into language a judge can verify quickly. | `docs/award-evidence-map/`, `docs/award-preflight/`, and `docs/cloud-readiness/`. | Alibaba endpoint proof is still pending until a public endpoint exists. |

## Before And After

Before Qwen, PrizePilot had a deterministic plan: target the Qwen Cloud Blog Post Award and Honorable Mention route, prepare Devpost assets, keep sensitive gates outside automation, and avoid unsupported deployment claims.

The live Qwen/DashScope call refined that into public-facing submission language. The sanitized excerpt emphasized:

- Blog Post Award target and USD 500 value;
- 10-winner prize structure;
- prerequisite that the blog route must be tied to a qualified Devpost project;
- no credentials stored;
- no premature publishing;
- no assumed infrastructure;
- eligibility verified first.

Those points are now reflected across the public story and judge materials.

For the concrete copy trail, see `docs/qwen-before-after-evidence.md` and the public `docs/qwen-before-after/` page. That evidence page maps the deterministic plan, the live Qwen refinement, and the exact public surfaces that changed.

## Reproducible Without A Key

The non-account-gated path remains:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
python -m prizepilot plan samples/qwen_hackathon.json
python -m prizepilot qwen-status
python -m prizepilot cloud-readiness
```

Future live Qwen reruns still require an account-owner supplied runtime key. No API key should be committed, logged, pasted into public chat, or stored in the repository.
