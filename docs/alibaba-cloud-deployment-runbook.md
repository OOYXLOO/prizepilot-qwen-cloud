# Alibaba Cloud Deployment Runbook

Created: 2026-06-10

Purpose: prepare PrizePilot for the Qwen Cloud hackathon deployment requirement without claiming deployment before it happens.

## Local Container Contract

The repository includes a `Dockerfile` that starts the PrizePilot demo service:

```powershell
docker build -t prizepilot-qwen .
docker run --rm -p 8000:8000 prizepilot-qwen
```

Expected local checks:

- `http://localhost:8000/` renders the PrizePilot dashboard.
- `http://localhost:8000/api/plan` returns JSON with the Qwen plan and portfolio ranking.
- The dashboard explicitly states that API keys, public publishing, deployment proof, and final Devpost submission remain user-approved actions.

## Alibaba Cloud Deployment Options

Use the simplest user-approved Alibaba Cloud route available in the account at submission time:

- Function Compute custom container using `deploy/alibaba-cloud/s.yaml`.
- Container Registry + Serverless App Engine.
- Container Registry + Elastic Container Instance.
- ECS instance running the Docker image.

The final choice depends on the user's Alibaba Cloud account region, verification status, credits, and product availability.

## Evidence To Capture After Deployment

Do not fill these until the deployment actually exists.

- Alibaba Cloud product used:
- Region:
- Deployment URL:
- Deployment timestamp:
- Public code proof: https://github.com/OOYXLOO/prizepilot-qwen-cloud/blob/main/deploy/alibaba-cloud/s.yaml
- Screenshot of dashboard:
- Screenshot or response from `/api/plan`:
- Commit/package hash or ZIP filename used:
- Any Qwen Cloud API call evidence, if live mode is enabled:

## Current Local Docker Status

Docker CLI is installed on this machine, but the Docker Desktop/Linux daemon was not running during the latest check. A local `docker build` is therefore still unproven until Docker is started or an Alibaba Cloud build service is used.

## Integrity Boundary

No API key, account token, billing information, KYC data, tax data, password, OTP, or recovery code should be stored in this repository or in the local ledger.

Do not claim Alibaba Cloud deployment proof in Devpost until the URL is live and the user confirms it may be shared publicly.
