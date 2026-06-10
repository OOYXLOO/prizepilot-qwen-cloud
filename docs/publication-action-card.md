# Publication Action Card

Do not publish without user confirmation.

Current state on 2026-06-10:

- Qwen Devpost registration is complete for Devpost user `OOYXLOO`.
- Public GitHub repository shell exists: https://github.com/OOYXLOO/prizepilot-qwen-cloud
- Local public package is ready at `qwen-prizepilot-public.zip`.
- GitHub code push is blocked by GitHub HTTPS/SSH authorization, not by local package readiness.
- Devpost portfolio project creation is blocked by reCAPTCHA after entering project name `PrizePilot`.

Minimum public package:

- Source repository from `qwen-prizepilot-public.zip`
- README and MIT license
- Devpost project fields from `docs/devpost-project-fields.md`
- Blog draft from `docs/blog-draft.md`
- Deployment proof from `docs/alibaba-cloud-deployment-runbook.md` after it exists
- Demo GIF from `docs/screenshots/prizepilot-demo.gif`

Confirmation before public GitHub upload:

```text
Please confirm I should publish the PrizePilot Qwen package to the approved public GitHub repository. This will make the code and docs public and may associate them with my GitHub account.
```

After GitHub authorization succeeds, run:

```powershell
git push -u origin main
```

After the Devpost reCAPTCHA is completed, save the `PrizePilot` portfolio project, fill fields from `docs/devpost-project-fields.md`, then import the project into the Qwen hackathon submission flow.
