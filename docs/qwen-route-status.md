# Qwen PrizePilot Route Status

Generated: 2026-06-10T08:33:30.057100+00:00
Phase: **ready_for_user_publication_steps**
Severity: **ACTION_NEEDED**

Next action: Enter the Qwen Cloud email verification code in the active browser, then continue account setup until benefits/console access is verified.

## Deadline

- Deadline UTC: `2026-07-09T21:00:00+00:00`
- Hours until deadline: `708.44`

## Local Artifact Gate

- Missing artifacts: `0`

## Public/Account Gates

- Incomplete public/account gates: `5`
- `qwen/alibaba cloud account ready`: `partial - GitHub OAuth authorized for qwencloud.com and verification code sent to registered email; browser is waiting for the email code` - Enter the Qwen Cloud email verification code in the active browser, then confirm whether the account reaches the benefits/console page.
- `qwen live check completed`: `no` - Run Qwen/DashScope live check with user-provided API key at action time.
- `alibaba cloud deployment proof`: `partial - Function Compute custom-container manifest prepared at deploy/alibaba-cloud/s.yaml; live Alibaba Cloud endpoint not verified` - Use the prepared Function Compute manifest with the user's Alibaba Cloud account, then record the live URL and proof evidence.
- `public demo video`: `partial - generated local WebM at docs/demo-video/prizepilot-demo.webm; Devpost rejected GitHub raw WebM and requires YouTube, Facebook Video, Vimeo, or Youku URL` - Upload the generated WebM to a Devpost-supported video host: YouTube, Facebook Video, Vimeo, or Youku.
- `devpost final submitted`: `no` - Submit final Devpost project after review and explicit confirmation.

## Reference Files

- `docs/qwen-route-ledger.md`
- `docs/qwen-start-handoff-template.md`
- `docs/qwen-human-action-card.md`
- `docs/devpost-project-fields.md`
- `docs/blog-draft.md`
- `docs/alibaba-cloud-deployment-runbook.md`
- `docs/validation-report.md`
