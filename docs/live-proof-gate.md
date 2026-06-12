# PrizePilot Live Proof Gate

Use this page only when the account owner is present and can complete official Qwen or Alibaba Cloud account steps. It is designed to capture stronger sponsor evidence without storing secrets or overstating the current Devpost project.

## Current Public Boundary

- Public Devpost project: https://devpost.com/software/prizepilot-qwen-cloud
- Public evidence hub: https://ooyxloo.github.io/prizepilot-qwen-cloud/
- Public judge pack: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/
- Public build journal: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/
- Public repository: https://github.com/OOYXLOO/prizepilot-qwen-cloud
- Verified today in the project story: repository, Vimeo demo, GitHub Pages evidence, blog, tests, Qwen client code path, and Alibaba Cloud deployment manifest.
- Not yet claimed: completed Qwen/DashScope live call, verified Alibaba Cloud endpoint, prize award, payout, tax, KYC, or bank verification.

## Human Gates

Stop and ask the account owner to act directly when any step asks for:

- CAPTCHA or human verification.
- Email, SMS, or authenticator code.
- API key, secret, access token, cookie, recovery code, or local account storage.
- Cloud credit, billing, card, bank, payout, tax, KYC, or identity data.
- Final public Devpost update after new evidence is captured.

## Qwen/DashScope Live Proof

Purpose: prove that PrizePilot can run a live Qwen-compatible refinement pass without storing the key.

1. The account owner opens the official Qwen/Alibaba key page and creates or selects the key.
2. The key is pasted only into the current terminal environment variable, never into chat, docs, screenshots, commits, or logs.
3. From the project root, run:

```powershell
$env:PYTHONPATH='src'
$env:DASHSCOPE_API_KEY='runtime-only'
python -m prizepilot plan samples/qwen_hackathon.json --use-qwen
Remove-Item Env:\DASHSCOPE_API_KEY
```

Acceptable public evidence after the run:

- timestamp;
- selected non-sensitive model name, for example `qwen-plus`;
- selected public base URL region, if visible and non-secret;
- short excerpt showing the model refined the PrizePilot plan;
- confirmation that the API key was removed from the environment after the run.

Do not publish raw request headers, full responses containing account metadata, API keys, billing screens, or private console pages.

## Alibaba Cloud Endpoint Proof

Purpose: prove that the prepared Function Compute deployment path can serve the PrizePilot dashboard from an Alibaba Cloud endpoint.

1. The account owner confirms that using Alibaba Cloud credits or billing is acceptable.
2. Deploy using the prepared manifest:

```powershell
cd deploy/alibaba-cloud
s deploy
```

3. Open the resulting public endpoint in a browser.
4. Verify that `/` renders the PrizePilot dashboard and `/api/plan` returns a JSON planning payload.

Acceptable public evidence:

- endpoint URL;
- timestamp;
- HTTP status for `/` and `/api/plan`;
- one screenshot of the public dashboard with no private console chrome;
- one short JSON snippet showing route names and evidence gates.

Do not publish Alibaba account IDs, billing screens, access keys, RAM policies, console cookies, private logs, or deployment tokens.

## Devpost Update Rule

Only edit the Qwen Devpost project after new proof is real and captured. Suggested update text:

> Added live proof evidence for the Qwen/DashScope refinement path and/or Alibaba Cloud endpoint. The project still keeps account, billing, payout, tax, and KYC material outside the repository and only publishes non-sensitive proof.

If either proof is still missing, keep the current honest wording: live Qwen execution and live Alibaba deployment are prepared paths, not completed claims.

## Evidence Checklist

- [ ] Qwen/Alibaba account verification completed by account owner.
- [ ] Runtime-only API key used and removed from environment.
- [ ] Live Qwen output captured without secrets.
- [ ] Alibaba deployment approved by account owner before any billing or credit use.
- [ ] Public endpoint verified at `/` and `/api/plan`.
- [ ] Devpost updated only with proof that actually happened.
- [ ] `docs/qwen-route-ledger.md` updated with non-sensitive status.
- [ ] `python -m unittest discover -s tests -v` still passes.
