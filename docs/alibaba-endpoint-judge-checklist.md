# Alibaba Endpoint Judge Checklist

Purpose: give judges and the account owner one compact success checklist for the remaining Alibaba Cloud proof. This file is a prepared proof plan only. Do not mark any item complete until a live public endpoint exists.

## Current Status

- Qwen/DashScope live smoke proof: complete.
- Alibaba Function Compute manifest: prepared at `deploy/alibaba-cloud/s.yaml`.
- Live Alibaba public endpoint: not yet claimed.
- Devpost deployment wording: should stay endpoint-pending until public proof exists.

## Expected Success Signal

After the account owner approves region, credits, and any billing implications, the deployment proof should show:

| Check | Expected result | Public evidence to keep |
| --- | --- | --- |
| Public root URL | `GET /` returns HTTP 200 and renders the PrizePilot dashboard. | URL, timestamp, HTTP status, one dashboard screenshot with no private console chrome. |
| Public plan API | `GET /api/plan` returns HTTP 200 and JSON with `project`, `track`, `routes`, and `evidence_gaps`. | Short JSON snippet with route names and gates only. |
| Claim boundary | Page still says Qwen live proof is captured and Alibaba endpoint proof is newly verified only after the URL works. | Screenshot or excerpt from public page. |
| Secret boundary | No API keys, cookies, account IDs, billing pages, RAM policies, deployment tokens, payout, tax, KYC, or bank data appear. | Reviewer note only; no secret screenshots. |

## Minimal Verification Commands

Replace the endpoint placeholder only after deployment exists:

```powershell
$endpoint='https://example-public-endpoint/'
Invoke-WebRequest -Uri $endpoint -UseBasicParsing
Invoke-WebRequest -Uri ($endpoint.TrimEnd('/') + '/api/plan') -UseBasicParsing
```

Expected JSON fields in `/api/plan`:

```json
{
  "project": "PrizePilot",
  "track": "Track 4 - Autopilot Agent",
  "submission_status": {
    "phase": "submitted_can_still_improve"
  },
  "evidence_gaps": [
    "Qwen/DashScope live refinement is verified..."
  ]
}
```

## Devpost Update After Real Proof

Only after the endpoint works publicly:

```text
Added Alibaba Cloud endpoint proof for PrizePilot: the public dashboard returns HTTP 200 at the deployed root URL and /api/plan returns the machine-readable planning payload. The repository continues to keep API keys, account metadata, billing, payout, tax, KYC, and bank material out of public artifacts.
```

If endpoint proof is still missing, use this honest wording:

```text
PrizePilot has verified Qwen/DashScope live smoke proof and a prepared Alibaba Function Compute deployment path. Live Alibaba endpoint proof remains account-gated and is not claimed until a public URL is verified.
```

## Stop Conditions

Stop and ask the account owner to act directly if any step asks for CAPTCHA, OTP, email/SMS verification, API keys, access tokens, cookies, RAM credentials, credit card, billing approval, payout, tax, KYC, identity data, or private console state.
