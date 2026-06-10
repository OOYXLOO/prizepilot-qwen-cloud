# Submission Story

## Inspiration

Hackathon agents are usually judged by the app they produce. PrizePilot looks at the work before the app exists: deciding which prize route is actually reachable, which proof is missing, and which actions should stay gated because they affect accounts, public pages, cloud billing, or payout eligibility.

I built PrizePilot around a real portfolio: a near-term USD 200 feedback prize, the Qwen Blog Post Award / Honorable Mention route, and higher-friction open-source bounty backups. The goal is to make an autopilot agent useful without letting it overclaim evidence or press irreversible buttons blindly.

## What it does

PrizePilot turns structured prize pages into:

- ranked execution plans with deadline, prize, winner-count, and blocker scoring;
- public artifact drafts for Devpost, blogs, videos, and deployment evidence;
- a local dashboard and API for reviewing the current plan;
- a human action queue for sensitive steps such as API keys, OAuth, public uploads, cloud deployment, final submission, payment, tax, and KYC.

## How it is built

The core planner is a deterministic Python package so every ranking can be audited locally. The web dashboard is a small standard-library HTTP service that exposes the same planning payload through `/` and `/api/plan`. A Dockerfile and Alibaba Cloud Function Compute manifest prepare the service for cloud deployment proof.

PrizePilot is Qwen-ready through an OpenAI-compatible DashScope client. When a Qwen or DashScope API key is provided at runtime, the local plan can be refined into sharper reasoning and submission narratives. The key is not stored in the repository or ledger.

## Qwen Cloud and Alibaba Cloud path

The project targets Track 4: Autopilot Agent because it automates a messy real-world workflow end to end: opportunity intake, route selection, artifact generation, evidence tracking, and human-in-the-loop approval checkpoints.

The repository includes an Alibaba Cloud deployment adapter at `deploy/alibaba-cloud/s.yaml` and a proof runbook. The Devpost deployment field points to the public code file that demonstrates the Alibaba Cloud service path; a live endpoint should only be claimed after the account and deployment are actually verified.

## Challenges

The hardest part was designing the integrity boundary. A money-seeking agent can easily blur "prepared", "submitted", "deployed", and "won". PrizePilot keeps those states separate, records public URLs only after verification, and treats CAPTCHA, OTP, API keys, cloud spending, payout, and final submission as checkpoints.

## What I learned

For prize automation, the valuable agent behavior is not just writing text faster. It is maintaining a current map of deadlines, evidence gaps, public artifacts, and irreversible external actions. That makes the system useful under pressure while still staying honest for judges and sponsors.

## What's next

The next step is to complete Qwen Cloud account verification, run a live Qwen refinement check, deploy the dashboard on Alibaba Cloud, upload the demo video to an approved public video host, and submit the final Devpost project once the proof is complete.
