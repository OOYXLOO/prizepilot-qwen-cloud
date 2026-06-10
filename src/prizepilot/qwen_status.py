from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

QWEN_DEADLINE_UTC = datetime(2026, 7, 9, 21, 0, tzinfo=timezone.utc)
FIELD_RE = re.compile(r"^\s*-\s*([^:\n]+):\s*(.*)$", re.MULTILINE)

REQUIRED_ARTIFACTS = {
    "README.md": "Project README",
    "LICENSE": "License",
    "Dockerfile": "Deployment container file",
    "pyproject.toml": "Python project metadata",
    "ARCHITECTURE.md": "Architecture notes",
    "architecture.svg": "Architecture diagram",
    "web/index.html": "Static dashboard demo",
    "docs/blog-draft.md": "Blog/social post draft",
    "docs/demo-video-script.md": "Demo video script",
    "docs/demo-video/prizepilot-demo.webm": "Generated silent demo WebM",
    "docs/demo-video-url-candidates.md": "Demo video URL candidate notes",
    "tools/record_demo_webm.mjs": "Automated WebM recording script",
    "docs/devpost-project-fields.md": "Devpost field draft",
    "docs/qwen-start-handoff-template.md": "User launch handoff template",
    "docs/qwen-cloud-live-check.md": "Live Qwen check runbook",
    "docs/alibaba-cloud-deployment-runbook.md": "Alibaba Cloud deployment runbook",
    "docs/alibaba-cloud-deployment-proof-template.md": "Deployment proof template",
    "docs/publication-action-card.md": "Publication action card",
    "docs/public-package-checklist.md": "Public package checklist",
    "docs/validation-report.md": "Validation report",
    "docs/screenshots/prizepilot-dashboard-desktop.png": "Desktop dashboard screenshot",
    "docs/screenshots/prizepilot-dashboard-mobile.png": "Mobile dashboard screenshot",
    "docs/screenshots/prizepilot-demo.gif": "Demo GIF",
}

PUBLIC_GATES = {
    "devpost hackathon joined": "Join Qwen Devpost hackathon.",
    "devpost portfolio project created": "Complete the Devpost reCAPTCHA, save the PrizePilot portfolio project, and import it into the Qwen submission flow.",
    "qwen/alibaba cloud account ready": "Create/access Qwen or Alibaba Cloud account.",
    "qwen live check completed": "Run Qwen/DashScope live check with user-provided API key at action time.",
    "alibaba cloud deployment proof": "Deploy or otherwise produce approved Alibaba Cloud proof.",
    "public github repository": "Publish approved code to the existing public GitHub repository.",
    "public demo video": "Publish approved public demo video.",
    "public blog/social post": "Publish approved blog/social post for Blog Post Award.",
    "devpost final submitted": "Submit final Devpost project after review and explicit confirmation.",
}

def parse_iso_datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)

def parse_ledger_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for match in FIELD_RE.finditer(text):
        fields[match.group(1).strip().lower()] = match.group(2).strip()
    return fields

def is_yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "done", "submitted", "published"}

def public_gate_next_action(gate: str, status: str, default_action: str) -> str:
    normalized = status.strip().lower()
    if gate == "public github repository" and "partial" in normalized:
        return "Authorize GitHub push/publication, then run `git push -u origin main` to publish the prepared package."
    if gate == "devpost portfolio project created" and ("recaptcha" in normalized or "captcha" in normalized):
        return "Complete the visible Devpost reCAPTCHA, save the PrizePilot portfolio project, then continue the Qwen import/submission flow."
    if gate == "public demo video" and "partial" in normalized:
        return "Review whether Devpost accepts the GitHub-hosted WebM URL; otherwise upload the generated WebM to an approved public video host."
    return default_action

def inspect_artifacts(root: Path) -> list[dict[str, object]]:
    checks = []
    for relative_path, description in REQUIRED_ARTIFACTS.items():
        path = root / relative_path
        checks.append(
            {
                "path": relative_path,
                "description": description,
                "exists": path.is_file(),
                "size": path.stat().st_size if path.is_file() else 0,
            }
        )
    return checks

def hours_until(now: datetime, deadline: datetime) -> float:
    return round((deadline - now).total_seconds() / 3600, 2)

def build_status(root: Path, ledger_path: Path, now: datetime | None = None) -> dict[str, object]:
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    current = current.astimezone(timezone.utc)

    fields = parse_ledger_fields(ledger_path.read_text(encoding="utf-8"))
    artifact_checks = inspect_artifacts(root)
    missing_artifacts = [item for item in artifact_checks if not item["exists"]]
    incomplete_public_gates = [
        {
            "gate": gate,
            "status": fields.get(gate, ""),
            "next_action": public_gate_next_action(gate, fields.get(gate, ""), action),
        }
        for gate, action in PUBLIC_GATES.items()
        if not is_yes(fields.get(gate, ""))
    ]

    final_submitted = is_yes(fields.get("devpost final submitted", ""))
    if missing_artifacts:
        phase = "local_package_incomplete"
        severity = "FIX_LOCAL"
        next_action = "Restore or regenerate missing local Qwen submission artifacts before public/account work."
    elif final_submitted:
        phase = "submitted_waiting_for_results"
        severity = "OK"
        next_action = "Monitor Devpost/Qwen email, Devpost notifications, and official winner channels."
    elif current >= QWEN_DEADLINE_UTC:
        phase = "deadline_passed"
        severity = "CLOSED_OR_HIGH_RISK"
        next_action = "Do not assume Qwen remains viable unless official channels confirm late submission is accepted."
    elif hours_until(current, QWEN_DEADLINE_UTC) <= 72:
        phase = "public_submission_steps_urgent"
        severity = "URGENT"
        next_action = "Prioritize account, live check, deployment proof, public repo, video, blog/social post, and final Devpost submission."
    else:
        phase = "ready_for_user_publication_steps"
        severity = "ACTION_NEEDED"
        if not is_yes(fields.get("devpost portfolio project created", "")):
            next_action = "Complete the Devpost reCAPTCHA and save the PrizePilot portfolio project, then import it into the Qwen submission flow."
        elif "partial" in fields.get("public github repository", "").lower():
            next_action = "Authorize GitHub publication and push the prepared local package to the existing public repository."
        else:
            next_action = "Use docs/qwen-start-handoff-template.md for the remaining Qwen/Alibaba, deployment, blog/video, and final submission gates."

    return {
        "checked_at": current.isoformat(),
        "phase": phase,
        "severity": severity,
        "next_action": next_action,
        "deadline_utc": QWEN_DEADLINE_UTC.isoformat(),
        "hours_until_deadline": hours_until(current, QWEN_DEADLINE_UTC),
        "artifact_checks": artifact_checks,
        "missing_artifacts": missing_artifacts,
        "incomplete_public_gates": incomplete_public_gates,
        "ledger_path": str(ledger_path),
        "reference_files": [
            "docs/qwen-route-ledger.md",
            "docs/qwen-start-handoff-template.md",
            "docs/qwen-human-action-card.md",
            "docs/devpost-project-fields.md",
            "docs/blog-draft.md",
            "docs/alibaba-cloud-deployment-runbook.md",
            "docs/validation-report.md",
        ],
    }

def render_markdown(status: dict[str, object]) -> str:
    lines = [
        "# Qwen PrizePilot Route Status",
        "",
        f"Generated: {status['checked_at']}",
        f"Phase: **{status['phase']}**",
        f"Severity: **{status['severity']}**",
        "",
        f"Next action: {status['next_action']}",
        "",
        "## Deadline",
        "",
        f"- Deadline UTC: `{status['deadline_utc']}`",
        f"- Hours until deadline: `{status['hours_until_deadline']}`",
        "",
        "## Local Artifact Gate",
        "",
        f"- Missing artifacts: `{len(status['missing_artifacts'])}`",
    ]
    if status["missing_artifacts"]:
        for item in status["missing_artifacts"]:
            lines.append(f"- MISSING: `{item['path']}` - {item['description']}")

    lines.extend(["", "## Public/Account Gates", ""])
    lines.append(f"- Incomplete public/account gates: `{len(status['incomplete_public_gates'])}`")
    for gate in status["incomplete_public_gates"]:
        lines.append(f"- `{gate['gate']}`: `{gate['status'] or 'unset'}` - {gate['next_action']}")

    lines.extend(["", "## Reference Files", ""])
    lines.extend(f"- `{item}`" for item in status["reference_files"])
    return "\n".join(lines) + "\n"

def main() -> None:
    parser = argparse.ArgumentParser(description="Qwen PrizePilot route status generator")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--ledger", default="docs/qwen-route-ledger.md")
    parser.add_argument("--now", help="UTC or offset-aware ISO timestamp for deterministic checks.")
    parser.add_argument("--json-out", default="docs/qwen-route-status.json")
    parser.add_argument("--md-out", default="docs/qwen-route-status.md")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    ledger_path = (root / args.ledger).resolve()
    now = parse_iso_datetime(args.now) if args.now else None
    status = build_status(root, ledger_path, now=now)
    (root / args.json_out).write_text(json.dumps(status, indent=2), encoding="utf-8")
    (root / args.md_out).write_text(render_markdown(status), encoding="utf-8")
    print(f"Wrote {args.json_out} and {args.md_out}")
    print(f"Phase: {status['phase']}")
    print(f"Severity: {status['severity']}")

if __name__ == "__main__":
    main()
