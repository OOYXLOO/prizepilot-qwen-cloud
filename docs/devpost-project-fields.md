# Devpost Project Fields Draft

Project: PrizePilot
Track: Track 4 - Autopilot Agent
Targets: Blog Post Award, USD 500 x10; Top 10 Honorable Mention Projects, USD 500 x10

PrizePilot turns hackathon and bounty opportunities into executable submission plans, public asset drafts, and human approval checkpoints. It uses deterministic scoring locally and can call Qwen Cloud through the OpenAI-compatible DashScope endpoint for reasoning refinement.

Rule interpretation: the Blog Post Award is a bonus target and still requires a qualified Devpost project submission. The Honorable Mention route is the secondary project target. Public repository, blog, Vimeo demo, and Devpost submission are verified. Do not claim Qwen Cloud live usage or Alibaba Cloud live deployment until those actions actually happen.

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

- Public Vimeo demo: https://vimeo.com/1200124146
- Public judge evidence pack: https://ooyxloo.github.io/prizepilot-qwen-cloud/judge-pack/
- `docs/screenshots/prizepilot-demo.gif`
- `docs/screenshots/prizepilot-dashboard-desktop.png`
- `docs/screenshots/prizepilot-dashboard-mobile.png`
- `architecture.png`
- `docs/demo-recording-page.html` for rebuilding the demo video if the dashboard changes materially.
- Public blog/build journal: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/
- Alibaba Cloud code proof: https://github.com/OOYXLOO/prizepilot-qwen-cloud/blob/main/deploy/alibaba-cloud/s.yaml
- Video upload metadata: `docs/demo-video-upload-pack.md`

## Project Story

Paste from `docs/submission-story.md`.

## Additional Info Draft

- Submitter type: Individual
- Country of residence: confirm directly in the official Devpost form with the account owner.
- Project type: New
- Start date: 06-10-26
- Started before May 26 explanation: Project started on 06-10-26, after May 26. During the submission period I built the planner, dashboard, public repository, blog, demo assets, and Alibaba Cloud deployment adapter.
- Track: Track 4: Autopilot Agent
- Code repository: https://github.com/OOYXLOO/prizepilot-qwen-cloud
- Alibaba Cloud deployment proof code file: https://github.com/OOYXLOO/prizepilot-qwen-cloud/blob/main/deploy/alibaba-cloud/s.yaml
- Architecture diagram: `architecture.png`
- Blog/social post: https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/
- AI tools used: Qwen Cloud / DashScope-compatible API path for optional refinement, Codex for implementation assistance, GitHub for source publication, and local Python validation tools.
- Learning level: Significant

## Current Devpost State

The Devpost project is submitted at https://devpost.com/software/prizepilot-qwen-cloud and can still be edited until the Qwen Cloud hackathon deadline. Future updates should focus on stronger live evidence: Qwen/DashScope refinement proof and a verified Alibaba Cloud endpoint, if account access is available in time.
