# Public Package Checklist

Required: README, LICENSE, pyproject.toml, ARCHITECTURE.md, architecture.svg, architecture.png, Dockerfile, `.dockerignore`, Alibaba Cloud deployment adapter, `src/prizepilot/`, `tests/`, samples, `web/`, dashboard screenshots, demo GIF, editable presentation deck, demo recording page/runbook, blog draft, public blog page, judge evidence pack page, live proof gate page, judge manifest JSON, demo video upload pack, Devpost fields, submission story, QA checklist, `docs/qwen-human-action-card.md`, `docs/qwen-start-handoff-template.md`, `docs/live-proof-gate.md`, `docs/qwen-route-ledger.md`, `docs/qwen-route-status.md`, `docs/judge-manifest.json`, `docs/qwen-cloud-live-check.md`, `docs/qwen-rule-verification.md`, `docs/alibaba-cloud-deployment-runbook.md`, and validation report.

Forbidden: `.env`, API keys, passwords, OTPs, payment data, tax data, KYC data, `__pycache__`, `*.pyc`, `.pytest_cache`, `.venv`, `dist`, `build`.

Latest inspection on 2026-06-12 after adding the judge evidence pack and presentation deck:

- Source: tracked public repository tree on `main`
- Tracked files: 65
- Missing required entries: 0
- Forbidden cache/private entries: 0
- Exact byte count and ZIP entry count are not gates.

Presentation deck: `docs/prizepilot-qwen-submission-deck.pptx` is included and linked from the public evidence hub, README, and judge evidence pack.
