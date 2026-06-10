# Demo Recording Runbook

Purpose: create the public demo video required by the Qwen Cloud Devpost submission after account, repository, Qwen, and deployment proof gates are ready.

Current state: `docs/demo-recording-page.html` is a local, self-contained recording page. It uses the existing dashboard screenshots and demo GIF. It does not publish anything by itself.

## Record

1. Open `docs/demo-recording-page.html` in a browser.
2. Set the viewport near 1280 x 720.
3. Start a 60 second screen recording.
4. Let the page advance through all five chapters.
5. Optional voiceover:
   - "Prize pages are noisy."
   - "PrizePilot ranks reachable routes first."
   - "Qwen can refine narratives after a real API key is available."
   - "External effects stay human-gated."
   - "The project is fast where it can be fast and careful where it must be careful."

## Upload Checklist

- Public repository URL is live.
- Alibaba Cloud deployment proof exists.
- Qwen live check result is recorded, or the video clearly says live Qwen usage is still pending.
- No passwords, API keys, OTPs, account recovery data, billing data, tax/KYC data, or private URLs are visible.
- The Devpost project links to the public repository, deployment URL, blog/social post, and demo video URL.

## Video Description Draft

PrizePilot is an accountable autopilot agent for hackathon execution. It ranks cash-prize opportunities, prepares submission assets, and queues sensitive external actions for human approval. The demo shows route ranking, Qwen-ready planning, approval checkpoints, and the integrity boundary between local preparation and public submission.
