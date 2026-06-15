from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .agent import Opportunity, plan_locally, plan_portfolio
from .cloud_readiness import build_report as build_cloud_readiness_report
from .cloud_readiness import parse_checked_at as parse_cloud_readiness_checked_at
from .cloud_readiness import render_markdown as render_cloud_readiness_markdown
from .qwen_client import QwenClient
from .qwen_status import build_status as build_qwen_status
from .qwen_status import parse_iso_datetime as parse_qwen_status_datetime
from .qwen_status import render_console_summary as render_qwen_status_console_summary
from .qwen_status import render_markdown as render_qwen_status_markdown


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def _print_plan(plan: dict) -> None:
    print(f"# {plan['opportunity']['name']}")
    print()
    print(f"Target: {plan['target_prize']['name']} (USD {plan['target_prize']['amount_usd']} x {plan['target_prize']['winners']})")
    print(f"Strategy: {plan['strategy']}")
    print()
    print("Approval checkpoints:")
    for item in plan["approval_checkpoints"]:
        print(f"- {item}")


def main() -> None:
    _configure_stdout()
    parser = argparse.ArgumentParser(description="PrizePilot planning CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan")
    plan_parser.add_argument("opportunity")
    plan_parser.add_argument("--json", action="store_true")
    plan_parser.add_argument("--use-qwen", action="store_true")

    portfolio_parser = subparsers.add_parser("portfolio")
    portfolio_parser.add_argument("opportunities", nargs="+")
    portfolio_parser.add_argument("--json", action="store_true")

    status_parser = subparsers.add_parser("qwen-status")
    status_parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    status_parser.add_argument("--ledger", default="docs/qwen-route-ledger.md")
    status_parser.add_argument("--now")
    status_parser.add_argument("--json-out", default="docs/qwen-route-status.json")
    status_parser.add_argument("--md-out", default="docs/qwen-route-status.md")

    readiness_parser = subparsers.add_parser("cloud-readiness")
    readiness_parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    readiness_parser.add_argument("--checked-at", help="UTC or offset-aware ISO timestamp for deterministic report generation.")
    readiness_parser.add_argument("--json-out", default="docs/cloud-readiness-report.json")
    readiness_parser.add_argument("--md-out", default="docs/cloud-readiness-report.md")

    args = parser.parse_args()
    if args.command == "plan":
        plan = plan_locally(Opportunity.from_file(args.opportunity))
        if args.use_qwen:
            client = QwenClient()
            content = client.chat(
                [
                    {"role": "system", "content": "Refine this hackathon submission plan without inventing account, deployment, or payout facts."},
                    {"role": "user", "content": json.dumps(plan, indent=2)},
                ]
            )
            print(content)
            return
        if args.json:
            print(json.dumps(plan, indent=2))
        else:
            _print_plan(plan)
        return

    if args.command == "qwen-status":
        root = Path(args.root).resolve()
        now = parse_qwen_status_datetime(args.now) if args.now else None
        status = build_qwen_status(root, (root / args.ledger).resolve(), now=now)
        (root / args.json_out).write_text(json.dumps(status, indent=2), encoding="utf-8")
        (root / args.md_out).write_text(render_qwen_status_markdown(status), encoding="utf-8")
        for line in render_qwen_status_console_summary(status):
            print(line)
        return

    if args.command == "cloud-readiness":
        root = Path(args.root).resolve()
        checked_at = parse_cloud_readiness_checked_at(args.checked_at) if args.checked_at else None
        report = build_cloud_readiness_report(root, checked_at=checked_at)
        (root / args.json_out).write_text(json.dumps(report, indent=2), encoding="utf-8")
        (root / args.md_out).write_text(render_cloud_readiness_markdown(report), encoding="utf-8")
        print(f"Overall: {report['overall']}")
        return

    opportunities = [Opportunity.from_file(str(Path(path))) for path in args.opportunities]
    portfolio = plan_portfolio(opportunities)
    if args.json:
        print(json.dumps(portfolio, indent=2))
    else:
        for index, item in enumerate(portfolio["ranked"], start=1):
            prize = item["target_prize"]
            print(f"{index}. {item['opportunity']['name']} - {prize['name']} - USD {prize['amount_usd']} - score {item['score']}")


if __name__ == "__main__":
    main()
