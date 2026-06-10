# PrizePilot

PrizePilot is a Qwen Cloud hackathon submission for Track 4, Autopilot Agent. It turns hackathon and bounty opportunities into ranked execution plans, public artifact drafts, and human approval checkpoints.

The project is intentionally conservative: it records public repository and blog publication after verification, but it does not claim final Devpost submission, live Alibaba Cloud deployment, Qwen API usage, or payout eligibility until those events actually happen.

## Local Use

```powershell
$env:PYTHONPATH='src'
python -m prizepilot plan samples/qwen_hackathon.json
python -m prizepilot portfolio samples/splunk_agentic_ops.json samples/qwen_hackathon.json samples/uipath_agenthack.json samples/algora_onyx_bounty.json samples/arm_ai_optimization.json
python -m prizepilot.webapp --host 127.0.0.1 --port 8000
```

Live Qwen refinement is optional and requires `DASHSCOPE_API_KEY` or `QWEN_API_KEY` at action time only.

## Demo Assets

- Dashboard screenshots: `docs/screenshots/prizepilot-dashboard-desktop.png` and `docs/screenshots/prizepilot-dashboard-mobile.png`
- Short demo GIF: `docs/screenshots/prizepilot-demo.gif`
- Devpost architecture upload: `architecture.png`
- Recording page: `docs/demo-recording-page.html`
- Recording runbook: `docs/demo-recording-runbook.md`
