# Qwen Public Update Checklist

Last updated: 2026-06-14

Use this checklist before any future public push or Devpost edit for PrizePilot. It is intentionally conservative because public hackathon pages are part of the judged artifact.

## Local Checks

- [ ] `PYTHONPATH=src python -m unittest discover -s tests -v`
- [ ] `PYTHONPATH=src python -m compileall -q src tests tools`
- [ ] `PYTHONPATH=src python -m prizepilot qwen-status`
- [ ] `PYTHONPATH=src python -m prizepilot cloud-readiness`
- [ ] `python -m json.tool docs/judge-manifest.json`
- [ ] `python -m json.tool docs/qwen-route-status.json`
- [ ] `python -m json.tool docs/cloud-readiness-report.json`
- [ ] `git diff --check`

## Public Checks After User-Approved Push

- [ ] If a GitHub Actions workflow exists on the public branch, it is green; if no workflow is present, record the local verification commands and Pages HTTP checks instead.
- [ ] GitHub Pages hub returns HTTP 200.
- [ ] Judge pack, judge review card, Blog Share Packet, public update digest, and Alibaba endpoint checklist return HTTP 200.
- [ ] Devpost project page still loads publicly.
- [ ] Vimeo page loads publicly.
- [ ] Backup WebM demo loads publicly: `https://ooyxloo.github.io/prizepilot-qwen-cloud/demo-video/prizepilot-demo.webm`.
- [ ] Devpost embedded video playback is checked by the account owner if the Devpost page will mention video playback.

## Claim Boundary

- [ ] No prize, finalist, payout, tax, KYC, billing, bank, or cloud-credit claim.
- [ ] No live Alibaba endpoint claim until `/` and `/api/plan` return HTTP 200 from a real Alibaba Cloud URL.
- [ ] No API keys, request headers, account IDs, cookies, private email, private console screenshots, payment data, or localStorage.
- [ ] Public copy describes only evidence that actually exists.

## Devpost Edit Rule

Edit Devpost only after the account owner is present and explicitly approves the public account action. If any public evidence link fails, do not edit Devpost.
