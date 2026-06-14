from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from .qwen_client import DEFAULT_BASE_URL
from .webapp import dashboard_payload


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ASIA_SHANGHAI = timezone(timedelta(hours=8))


def _read(root: Path, relative_path: str) -> str:
    return (root / relative_path).read_text(encoding="utf-8")


def _has_all(text: str, fragments: list[str]) -> bool:
    return all(fragment in text for fragment in fragments)


def _check(
    check_id: str,
    label: str,
    passed: bool,
    evidence: str,
    public_next_step: str,
    status_when_passed: str = "pass",
) -> dict[str, str]:
    return {
        "id": check_id,
        "label": label,
        "status": status_when_passed if passed else "fail",
        "evidence": evidence,
        "public_next_step": public_next_step,
    }


def build_report(root: Path | str = PROJECT_ROOT, checked_at: datetime | None = None) -> dict[str, Any]:
    root = Path(root).resolve()
    current = checked_at or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    current = current.astimezone(timezone.utc)

    qwen_client = _read(root, "src/prizepilot/qwen_client.py")
    alibaba_manifest = _read(root, "deploy/alibaba-cloud/s.yaml")
    live_gate = _read(root, "docs/live-proof-gate.md")
    qwen_live_proof = _read(root, "docs/qwen-live-proof.md")
    ledger_text = _read(root, "docs/qwen-route-ledger.md").lower()
    payload = dashboard_payload()

    checks = [
        _check(
            "QWEN_OPENAI_COMPATIBLE_REQUEST_SHAPE",
            "Qwen-compatible chat request shape",
            DEFAULT_BASE_URL == "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
            and _has_all(qwen_client, ["/chat/completions", '"model"', '"messages"', '"temperature"', "qwen-plus"]),
            "The client defaults to DashScope compatible mode and posts chat/completions payloads with model, messages, and temperature.",
            "The live proof has been captured once; future reruns still require an account-owner supplied runtime key and should publish only a short non-secret excerpt.",
        ),
        _check(
            "QWEN_RUNTIME_SECRET_BOUNDARY",
            "Runtime-only secret boundary",
            _has_all(
                qwen_client,
                [
                    "DASHSCOPE_API_KEY",
                    "QWEN_API_KEY",
                    "do not store it in the project",
                    "Authorization",
                ],
            )
            and all(fragment not in ledger_text for fragment in ["sk-", "bearer ", "access_key_secret"]),
            "The client reads Qwen/DashScope keys only from runtime environment variables and the ledger does not store an API key.",
            "Keep API keys out of chat, screenshots, commits, logs, and Devpost; remove the environment variable immediately after the smoke test.",
        ),
        _check(
            "QWEN_LIVE_SMOKE_PROOF",
            "Runtime Qwen/DashScope smoke proof",
            _has_all(
                qwen_live_proof,
                [
                    "Exit code: 0",
                    "present after cleanup: False",
                    "qwen-plus",
                    "https://dashscope.aliyuncs.com/compatible-mode/v1",
                    "Refined Submission Plan",
                ],
            ),
            "A live Qwen/DashScope refinement pass succeeded through Alibaba Cloud China Bailian with a runtime-only key and no stored secret.",
            "Use only the short non-sensitive excerpt publicly; future runs still require account-owner key entry at action time.",
        ),
        _check(
            "ALIBABA_FC_CUSTOM_CONTAINER_MANIFEST",
            "Alibaba Function Compute custom-container manifest",
            _has_all(
                alibaba_manifest,
                [
                    "component: fc3",
                    "runtime: custom-container",
                    "functionName: prizepilot-qwen-cloud",
                    "port: 8000",
                    "PYTHONPATH: /app/src",
                ],
            ),
            "The checked-in Serverless Devs manifest targets Alibaba Function Compute with the PrizePilot container on port 8000.",
            "Deploy only after the account owner approves Alibaba Cloud account, credit, region, and billing implications.",
            "source_code_prepared",
        ),
        _check(
            "ALIBABA_PUBLIC_HTTP_PROOF_TARGETS",
            "Public HTTP endpoint proof targets",
            _has_all(
                alibaba_manifest,
                [
                    "healthCheckConfig",
                    "httpGetUrl: /",
                    "triggerType: http",
                    "authType: anonymous",
                    "disableURLInternet: false",
                    "GET",
                ],
            ),
            "The manifest declares a public HTTP trigger and health check path that map to the dashboard and API proof plan, but no live Alibaba URL is claimed here.",
            "After deployment, verify the public endpoint at / and /api/plan before updating Devpost.",
            "prepared_not_live",
        ),
        _check(
            "DASHBOARD_JUDGE_PAYLOAD_READY",
            "Dashboard and API judge payload",
            payload.get("project") == "PrizePilot"
            and payload.get("track") == "Track 4 - Autopilot Agent"
            and payload["qwen_plan"]["target_prize"]["name"] == "Blog Post Award"
            and payload["submission_status"]["phase"] == "submitted_can_still_improve"
            and any("Qwen/DashScope live refinement is verified" in gap for gap in payload["evidence_gaps"]),
            "The local web payload exposes the submitted Qwen target, verified Qwen live proof, route status, judge scorecard, approval queue, and remaining endpoint gap.",
            "Use the same payload as the expected success signal for a live Alibaba endpoint proof.",
        ),
        _check(
            "PUBLIC_CLAIM_BOUNDARY",
            "Public claim boundary",
            _has_all(
                live_gate,
                [
                    "Verified after gate",
                    "completed Qwen/DashScope live call",
                    "verified Alibaba Cloud endpoint",
                    "Do not publish raw request headers",
                    "Do not publish Alibaba account IDs",
                ],
            ),
            "The public live-proof gate states that Qwen live proof is verified and the Alibaba endpoint remains account-gated.",
            "Do not strengthen the public Devpost claim for Alibaba Cloud deployment until endpoint evidence actually exists.",
        ),
    ]

    overall = "qwen_live_verified_endpoint_pending" if all(item["status"] != "fail" for item in checks) else "needs_local_fix"
    return {
        "checked_at": current.isoformat(),
        "checked_at_local_asia_shanghai": current.astimezone(ASIA_SHANGHAI).isoformat(),
        "overall": overall,
        "checks": checks,
        "live_claim": "qwen_dashscope_smoke_verified_alibaba_endpoint_pending",
        "secret_policy": "No API keys, raw headers, account IDs, billing data, payout data, tax data, KYC data, cookies, or private console pages are required or stored.",
        "next_live_evidence": [
            "Alibaba Cloud Function Compute deployment approved and run by the account owner.",
            "Public endpoint proof for / and /api/plan with no private console chrome.",
            "Devpost update copy that claims only the completed Qwen smoke proof and any endpoint proof that actually exists.",
        ],
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# PrizePilot Cloud Readiness Report",
        "",
        f"Generated: {report['checked_at']}",
        f"Generated Asia/Shanghai: {report['checked_at_local_asia_shanghai']}",
        f"Overall: **{report['overall']}**",
        f"Live claim: `{report['live_claim']}`",
        "",
        report["secret_policy"],
        "",
        "## Checks",
        "",
        "| Check | Status | Evidence | Next live step |",
        "| --- | --- | --- | --- |",
    ]
    for check in report["checks"]:
        lines.append(
            f"| `{check['id']}` | `{check['status']}` | {check['evidence']} | {check['public_next_step']} |"
        )
    lines.extend(["", "## Next Live Evidence", ""])
    lines.extend(f"- {item}" for item in report["next_live_evidence"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate PrizePilot cloud readiness evidence without live secrets.")
    parser.add_argument("--root", default=str(PROJECT_ROOT))
    parser.add_argument("--json-out", default="docs/cloud-readiness-report.json")
    parser.add_argument("--md-out", default="docs/cloud-readiness-report.md")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report = build_report(root)
    (root / args.json_out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    (root / args.md_out).write_text(render_markdown(report), encoding="utf-8")
    print(f"Overall: {report['overall']}")


if __name__ == "__main__":
    main()
