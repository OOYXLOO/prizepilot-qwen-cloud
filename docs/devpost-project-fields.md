# Devpost Project Fields Draft

Project: PrizePilot
Track: Track 4 - Autopilot Agent
Targets: Blog Post Award, USD 500 x10; Top 10 Honorable Mention Projects, USD 500 x10

PrizePilot turns hackathon and bounty opportunities into executable submission plans, public asset drafts, and human approval checkpoints. It uses deterministic scoring locally and can call Qwen Cloud through the OpenAI-compatible DashScope endpoint for reasoning refinement.

Rule interpretation: the Blog Post Award is a bonus target and still requires a qualified Devpost project submission. The Honorable Mention route is the secondary project target. Do not claim Qwen Cloud usage, Alibaba Cloud deployment, public repository publication, public blog posting, or final submission until those actions actually happen.

## Short Description

An autopilot agent that ranks cash-prize opportunities, prepares submission assets, and queues risky external actions for human approval.

## Built With

Python, standard-library HTTP server, Qwen Cloud OpenAI-compatible API, Alibaba Cloud deployment target, Devpost, Docker.

## Try It

Run the local service with:

```powershell
$env:PYTHONPATH='src'
python -m prizepilot.webapp --host 127.0.0.1 --port 8000
```

## Demo Media

- `docs/screenshots/prizepilot-demo.gif`
- `docs/screenshots/prizepilot-dashboard-desktop.png`
- `docs/screenshots/prizepilot-dashboard-mobile.png`
- `docs/demo-recording-page.html` for recording a public demo video after publication gates are ready.
