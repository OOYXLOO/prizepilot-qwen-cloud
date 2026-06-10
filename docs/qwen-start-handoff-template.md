# Qwen Start Handoff Template

Created: 2026-06-10
Purpose: collect only the minimum user decisions needed to move PrizePilot from local package to a real Qwen Cloud hackathon submission.

Do not paste passwords, OTPs, API keys, recovery codes, payment data, tax data, KYC data, or cloud billing details into chat.

## Current Target

- Hackathon: https://qwencloud-hackathon.devpost.com/
- Primary prize target: Blog Post Award, USD 500 cash + USD 500 cloud credits, 10 winners.
- Secondary prize target: Top 10 Honorable Mention Projects, USD 500 cash + USD 500 cloud credits, 10 winners.
- Project: PrizePilot, an Autopilot Agent for turning prize/hackathon pages into executable submission plans and human action queues.
- Current account state: Qwen Devpost registration complete as `OOYXLOO`; Devpost portfolio project and Qwen submission draft are created.
- Current repository state: public GitHub repository is published at https://github.com/OOYXLOO/prizepilot-qwen-cloud.
- Current video state: local silent WebM exists at `docs/demo-video/prizepilot-demo.webm`, but Devpost requires a YouTube, Facebook Video, Vimeo, or Youku URL for the Qwen Project details page.

The blog prize is not standalone. It still requires a qualified Devpost project submission, public repo, demo/video, blog or social post, and Alibaba Cloud deployment proof.

## Reply To Send Codex Later

Use this only after the Splunk feedback route is either submitted or no longer viable, or if you want to start Qwen in parallel.

```text
Qwen PrizePilot launch fields:

Devpost email/account status:
Devpost Username:
Qwen/Alibaba Cloud account status:
Preferred Alibaba Cloud/DashScope region:
GitHub publication preference: existing repo URL / create new repo / I will create empty repo
Public blog/social platform preference:
Public demo video platform preference:

Eligibility confirmation:
I confirm I am eligible for the Qwen Cloud Global AI Hackathon under the official rules, including age, location, employment/conflict, and non-sanctioned-region requirements. I understand that if selected as a potential winner, identity, qualification, tax, and payment verification may be required before any prize is delivered.

Preparation authorization:
Please prepare the Qwen PrizePilot public package, live-check commands, deployment checklist, blog draft, demo script, and Devpost submission fields for my review. Do not create accounts, publish repositories, deploy cloud resources, upload videos, publish blog/social posts, or submit Devpost forms without separate action-time confirmation.
```

## Current Two-Minute Unblock Prompt

Use this after you upload the generated WebM to a supported video host:

```text
I uploaded the PrizePilot demo video. The accepted video URL is: <paste URL>. Continue the Qwen PrizePilot submission flow from the current browser and local repo state.
```

## Separate Confirmations Needed

These are separate because each one creates a public or account-side effect:

```text
Please confirm I should upload or publish the generated PrizePilot demo video to the approved video host. This will make the video public and may associate it with my account.
```

```text
Please confirm I should run the Qwen/DashScope live check using the API key I provide at action time. The key must not be stored in files, docs, command history, or the ledger.
```

```text
Please confirm I should deploy PrizePilot to the approved Alibaba Cloud service and record non-sensitive deployment proof for the Qwen hackathon submission. This may use cloud credits or billable cloud resources depending on the account configuration.
```

```text
Please confirm I should publish the approved PrizePilot blog/social post for the Qwen Blog Post Award. This will make the post public and may associate it with my account.
```

```text
Please confirm I should submit PrizePilot to the Qwen Cloud Devpost hackathon using the approved public repository, demo video, blog/social post, and Alibaba Cloud deployment proof. This is a public contest submission eligible for judging and possible USD 500 prize consideration.
```

## Minimum Evidence Ladder

1. Local package and tests pass.
2. Qwen/DashScope live check succeeds without storing the API key.
3. Alibaba Cloud deployment proof exists.
4. Public GitHub repo is live and clean.
5. Demo video and blog/social post are public.
6. Devpost submission is reviewed and explicitly submitted.
