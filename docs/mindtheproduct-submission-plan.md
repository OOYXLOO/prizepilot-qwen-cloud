# Mind the Product Submission Plan

Status: registered on Devpost; blocked on Novus email verification.

## Target

- Event: Mind the Product presents World Product Day: Everyone Ships Now
- Public page: https://mindtheproduct.devpost.com/
- Deadline: 2026-06-21 00:00 GMT+8
- Cash prize targets: First Place USD 5,000, Second Place USD 3,000, Third Place USD 2,000
- Required technology: Novus.ai installed on the deployed project before submission

## Positioning

PrizePilot should be presented as a product for builders shipping under prize and deadline pressure. It turns public hackathon and bounty pages into:

- ranked route decisions
- eligibility and payout-risk checklists
- human-gate action cards for email verification, video uploads, API keys, deployment proof, and payout/KYC
- a deployable dashboard with machine-readable planning output

## Current Product Evidence

- CLI planner: `python -m prizepilot plan samples/mindtheproduct_world_product_day.json`
- Portfolio ranking: `python -m prizepilot portfolio samples/splunk_agentic_ops.json samples/qwen_hackathon.json samples/mindtheproduct_world_product_day.json samples/uipath_agenthack.json`
- Web dashboard: `/`
- Machine-readable plan: `/api/plan`
- Novus readiness endpoint: `/api/novus-readiness`

## Remaining Gates

1. Verify the Novus email and create the Novus password using the official email link.
2. Connect or install Novus on the deployed project.
3. Deploy the product to a public URL.
4. Record a Devpost-compatible demo video URL.
5. Submit on Devpost before the deadline.

## Do Not Claim Yet

- Do not claim Novus is installed until the official account is verified and connected.
- Do not claim production deployment until a public deployed URL exists.
- Do not claim final Devpost submission until Devpost confirms it.
- Do not store passwords, OTPs, API keys, payment, tax, KYC, or recovery data.
