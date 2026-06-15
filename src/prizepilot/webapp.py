from __future__ import annotations

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .agent import Opportunity, plan_locally, plan_portfolio

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLES_DIR = PROJECT_ROOT / "samples"


def _load_opportunity(name: str) -> Opportunity:
    return Opportunity.from_file(str(SAMPLES_DIR / name))


def dashboard_payload() -> dict[str, Any]:
    qwen = _load_opportunity("qwen_hackathon.json")
    mindtheproduct = _load_opportunity("mindtheproduct_world_product_day.json")
    portfolio = plan_portfolio(
        [
            _load_opportunity("splunk_agentic_ops.json"),
            qwen,
            mindtheproduct,
            _load_opportunity("uipath_agenthack.json"),
            _load_opportunity("algora_onyx_bounty.json"),
            _load_opportunity("arm_ai_optimization.json"),
        ]
    )
    return {
        "project": "PrizePilot",
        "track": "Track 4 - Autopilot Agent",
        "qwen_plan": plan_locally(qwen),
        "mindtheproduct_plan": plan_locally(mindtheproduct),
        "portfolio": portfolio,
        "novus_readiness": {
            "required_for": "Mind the Product World Product Day",
            "registered_on_devpost": True,
            "novus_signup_started": True,
            "email_verification_required": True,
            "novus_installed": False,
            "next_action": "Verify the Novus email, create the password on the official link, then connect or install Novus before Devpost submission.",
        },
        "submission_status": {
            "phase": "submitted_can_still_improve",
            "devpost_url": "https://devpost.com/software/prizepilot-qwen-cloud",
            "repository_url": "https://github.com/OOYXLOO/prizepilot-qwen-cloud",
            "demo_video_url": "https://vimeo.com/1200124146",
            "blog_url": "https://ooyxloo.github.io/prizepilot-qwen-cloud/blog/",
            "qwen_live_proof_url": "https://ooyxloo.github.io/prizepilot-qwen-cloud/qwen-live-proof/",
            "deadline": "July 09, 2026 at 05:00pm EDT",
        },
        "qwen_agent_flow": [
            {
                "stage": "1. Public prize page",
                "input": "Rules, awards, dates, required artifacts, and account-gated actions.",
                "qwen_role": "Frames the opportunity as a judge-facing story instead of a loose TODO list.",
                "proof": "samples/qwen_hackathon.json and qwen-before-after evidence.",
            },
            {
                "stage": "2. Deterministic rank",
                "input": "Prize amount, winner count, deadline pressure, blockers, and evidence gaps.",
                "qwen_role": "Receives an auditable route plan rather than inventing the target from memory.",
                "proof": "portfolio ranking in /api/plan and docs/api/plan.json.",
            },
            {
                "stage": "3. Qwen refinement",
                "input": "Blog Post Award route plus verified public artifact list.",
                "qwen_role": "Tightens the public narrative, risk wording, and update copy for judges.",
                "proof": "live qwen-plus smoke receipt with non-sensitive output excerpt.",
            },
            {
                "stage": "4. Approval gate",
                "input": "Any secret, public posting, cloud billing, payout, tax, or KYC step.",
                "qwen_role": "Stops before irreversible account actions and records the human-controlled gate.",
                "proof": "approval queue and integrity boundary in this dashboard.",
            },
            {
                "stage": "5. Public proof packet",
                "input": "Repo, Devpost, Vimeo, blog, judge hub, static plan JSON, and proof pages.",
                "qwen_role": "Turns the chosen route into a reviewable evidence trail without overclaiming.",
                "proof": "judge pack, award evidence map, contribution map, and live proof page.",
            },
        ],
        "qwen_proof_snapshot": {
            "verified": "One Qwen/DashScope qwen-plus refinement pass ran with a runtime-only key and published non-sensitive evidence.",
            "current_public_artifacts": "Devpost, GitHub repository, Vimeo demo, Blog Award story, Pages hub, static judge demo, static plan JSON, Qwen contribution map, and Qwen live proof.",
            "still_pending": "Live Alibaba Cloud endpoint proof remains unclaimed until a public URL returns HTTP 200 at / and /api/plan.",
            "judge_takeaway": "PrizePilot is strongest as an honest autopilot: it accelerates route choice and submission evidence while keeping risky account actions visible.",
        },
        "agent_walkthrough": [
            {
                "role": "Contest Analyst",
                "responsibility": "Normalize prize pages into comparable opportunity records.",
                "output": "Deadline, prize, winner-count, blocker, and evidence fields.",
            },
            {
                "role": "Competitor Scout",
                "responsibility": "Compare the route against public winning-project patterns.",
                "output": "Differentiators that judges can understand in under five minutes.",
            },
            {
                "role": "Differentiation Strategist",
                "responsibility": "Choose the most reachable target instead of chasing the largest headline pool.",
                "output": "Blog Post Award / Honorable Mention path with explicit proof needs.",
            },
            {
                "role": "Submission Coach",
                "responsibility": "Draft Devpost, blog, video, and deployment evidence assets.",
                "output": "Public links, scripts, runbooks, and update-ready copy.",
            },
            {
                "role": "Risk Reviewer",
                "responsibility": "Hold account, billing, public posting, payout, tax, and KYC actions for human control.",
                "output": "Approval queue and evidence gap register.",
            },
        ],
        "judge_scorecard": [
            {
                "criterion": "Innovation",
                "weight": "30%",
                "proof": "Autopilot for prize-route execution plus verified live Qwen refinement.",
                "gap": "Turn the live proof into tighter public Devpost copy before judging.",
            },
            {
                "criterion": "Technical Depth",
                "weight": "30%",
                "proof": "Deterministic planner, Qwen-compatible client, HTTP API, Docker, Alibaba manifest.",
                "gap": "Capture verified Alibaba Cloud endpoint proof.",
            },
            {
                "criterion": "Problem Value",
                "weight": "25%",
                "proof": "Turns a real money-seeking workflow into auditable actions and evidence gates.",
                "gap": "Add more post-submission feedback if maintainers or judges request changes.",
            },
            {
                "criterion": "Presentation",
                "weight": "15%",
                "proof": "Public Devpost, Vimeo demo, blog, repo, and judge quickstart.",
                "gap": "Refresh screenshots if the dashboard changes materially.",
            },
        ],
        "approval_queue": [
            {"action": "Runtime Qwen/DashScope API key", "status": "completed once; future runs stay human-gated", "risk": "secret"},
            {"action": "Alibaba Cloud live deployment", "status": "human-gated", "risk": "billing/account"},
            {"action": "Devpost submission updates", "status": "allowed after review", "risk": "public claim"},
            {"action": "Prize payout, tax, or KYC", "status": "user-only", "risk": "financial identity"},
        ],
        "evidence_gaps": [
            "Qwen/DashScope live refinement is verified with a runtime key and no stored secret.",
            "Alibaba Cloud Function Compute manifest exists, but no live endpoint has been verified.",
        ],
        "benchmark": [
            {"metric": "Manual prize triage", "baseline": "60-90 minutes", "prizepilot": "one structured plan run"},
            {"metric": "Evidence tracking", "baseline": "spread across tabs and memory", "prizepilot": "status ledger plus dashboard"},
            {"metric": "Risky actions", "baseline": "easy to mix with automation", "prizepilot": "explicit approval queue"},
        ],
        "integrity_boundary": [
            "No API key is stored in the deployed app.",
            "Public repository, video, blog post, and Devpost submission are recorded only after verification.",
            "Live Qwen Cloud usage is captured as non-sensitive proof; Alibaba Cloud endpoint proof must still be captured before that claim is strengthened.",
            "Novus is not claimed as installed until the official Novus account is verified and connected.",
        ],
    }


def render_dashboard(payload: dict[str, Any]) -> str:
    qwen_target = payload["qwen_plan"]["target_prize"]
    mtp_target = payload["mindtheproduct_plan"]["target_prize"]
    novus = payload["novus_readiness"]
    status = payload["submission_status"]
    top_routes = payload["portfolio"]["ranked"][:4]
    rows = "\n".join(
        f"<tr><td data-label=\"#\">{index}</td><td data-label=\"Route\">{route['opportunity']['name']}</td><td data-label=\"Target\">{route['target_prize'].get('name', 'N/A')}</td><td data-label=\"Amount\">USD {route['target_prize'].get('amount_usd', 'N/A')}</td></tr>"
        for index, route in enumerate(top_routes, start=1)
    )
    public_links = "\n".join(
        f"<li><a href=\"{url}\">{label}</a></li>"
        for label, url in [
            ("Devpost project", status["devpost_url"]),
            ("Repository", status["repository_url"]),
            ("Vimeo demo", status["demo_video_url"]),
            ("Build journal", status["blog_url"]),
            ("Qwen live proof", status["qwen_live_proof_url"]),
        ]
    )
    agents = "\n".join(
        f"<section class=\"tile\"><h3>{agent['role']}</h3><p>{agent['responsibility']}</p><strong>{agent['output']}</strong></section>"
        for agent in payload["agent_walkthrough"]
    )
    scorecard = "\n".join(
        f"<tr><td data-label=\"Criterion\">{item['criterion']}</td><td data-label=\"Weight\">{item['weight']}</td><td data-label=\"Proof\">{item['proof']}</td><td data-label=\"Gap\">{item['gap']}</td></tr>"
        for item in payload["judge_scorecard"]
    )
    approvals = "\n".join(
        f"<tr><td data-label=\"Action\">{item['action']}</td><td data-label=\"Status\">{item['status']}</td><td data-label=\"Risk\">{item['risk']}</td></tr>"
        for item in payload["approval_queue"]
    )
    qwen_flow = "\n".join(
        f"<section class=\"flow-step\"><h3>{item['stage']}</h3><p><strong>Input:</strong> {item['input']}</p><p><strong>Qwen role:</strong> {item['qwen_role']}</p><p><strong>Proof:</strong> {item['proof']}</p></section>"
        for item in payload["qwen_agent_flow"]
    )
    qwen_proof = payload["qwen_proof_snapshot"]
    qwen_proof_rows = "\n".join(
        f"<li><strong>{label}:</strong> {qwen_proof[key]}</li>"
        for label, key in [
            ("Verified", "verified"),
            ("Public artifacts", "current_public_artifacts"),
            ("Still pending", "still_pending"),
            ("Judge takeaway", "judge_takeaway"),
        ]
    )
    gaps = "\n".join(f"<li>{item}</li>" for item in payload["evidence_gaps"])
    benchmark = "\n".join(
        f"<tr><td data-label=\"Metric\">{item['metric']}</td><td data-label=\"Manual\">{item['baseline']}</td><td data-label=\"PrizePilot\">{item['prizepilot']}</td></tr>"
        for item in payload["benchmark"]
    )
    boundaries = "\n".join(f"<li>{item}</li>" for item in payload["integrity_boundary"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PrizePilot Qwen Demo</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Arial, sans-serif; background: #f6f8fb; color: #16202a; overflow-x: hidden; }}
    main {{ width: 100%; max-width: 980px; margin: 0 auto; padding: 44px 24px 64px; }}
    h1 {{ font-size: 42px; line-height: 1.1; margin: 0 0 16px; }}
    h2 {{ margin-top: 34px; }}
    main, h1, h2, h3, p, li, td, strong, a, .panel, .tile, .table-wrap, table {{ min-width: 0; overflow-wrap: anywhere; }}
    p, li {{ color: #526173; line-height: 1.55; }}
    a {{ color: #0f766e; font-weight: 700; }}
    .table-wrap {{ border: 1px solid #d9e2ec; background: white; overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 680px; }}
    th, td {{ padding: 13px 14px; border-bottom: 1px solid #d9e2ec; text-align: left; }}
    th {{ color: #526173; font-size: 13px; }}
    .pill {{ display: inline-block; margin: 6px 8px 18px 0; padding: 8px 12px; background: #0f766e; color: white; font-weight: 700; font-size: 13px; }}
    .pill.alt {{ background: #b45309; }}
    .panel {{ background: white; border-left: 6px solid #0f766e; padding: 18px 22px; margin-top: 20px; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08); }}
    .panel.warn {{ border-left-color: #b45309; }}
    .grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin-top: 16px; }}
    .tile {{ background: white; border: 1px solid #d9e2ec; padding: 16px; min-height: 148px; }}
    .tile h3 {{ margin: 0 0 8px; font-size: 17px; }}
    .tile strong {{ display: block; color: #16202a; font-size: 13px; line-height: 1.4; }}
    .flow {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; margin-top: 16px; }}
    .flow-step {{ background: white; border: 1px solid #d9e2ec; border-top: 5px solid #0f766e; padding: 14px; min-width: 0; }}
    .flow-step h3 {{ margin: 0 0 8px; font-size: 15px; }}
    .flow-step p {{ margin: 8px 0 0; font-size: 13px; line-height: 1.42; }}
    .flow-step strong {{ color: #16202a; }}
    code {{ background: #e8eef5; padding: 2px 5px; }}
    @media (max-width: 900px) {{
      .flow {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 620px) {{
      h1 {{ font-size: 24px; line-height: 1.16; }}
      h2 {{ font-size: 24px; }}
      p, li, td {{ font-size: 15px; }}
      main {{ padding: 30px 16px 48px; }}
      .panel {{ padding: 16px 20px; }}
      .tile {{ min-height: 0; }}
      .tile strong {{ font-size: 12px; }}
      .grid {{ grid-template-columns: 1fr; }}
      .flow {{ grid-template-columns: 1fr; }}
      .table-wrap {{ overflow-x: visible; }}
      table {{ min-width: 0; }}
      thead {{ display: none; }}
      tbody, tr, td {{ display: block; }}
      tr {{ border-bottom: 1px solid #d9e2ec; padding: 8px 0; }}
      tr:last-child {{ border-bottom: 0; }}
      td {{ border-bottom: 0; display: grid; grid-template-columns: minmax(64px, 82px) minmax(0, 1fr); gap: 10px; padding: 8px 14px; }}
      td::before {{ content: attr(data-label); color: #526173; font-weight: 700; }}
    }}
  </style>
</head>
<body>
<main>
  <span class="pill">Qwen Cloud Track 4</span>
  <span class="pill alt">Autopilot Agent</span>
  <h1>PrizePilot turns prize pages into accountable execution plans.</h1>
  <p>This submitted demo presents the same deterministic planning payload used by the CLI. It is designed for a fast judge review while keeping unverified sponsor evidence clearly separated from completed public artifacts.</p>
  <div class="panel">
    <strong>Submission status:</strong> {status['phase']} through Devpost. Public repo, Vimeo demo, and build journal are live; the project can still be improved until {status['deadline']}.
    <ul>{public_links}</ul>
  </div>
  <div class="panel">
    <strong>Current Qwen target:</strong> {qwen_target.get('name')} - USD {qwen_target.get('amount_usd')} x {qwen_target.get('winners')} winners.
  </div>
  <h2>Qwen Agent Flow</h2>
  <div class="flow">{qwen_flow}</div>
  <div class="panel">
    <strong>Qwen proof snapshot:</strong>
    <ul>{qwen_proof_rows}</ul>
  </div>
  <div class="panel">
    <strong>Mind the Product target:</strong> {mtp_target.get('name')} - USD {mtp_target.get('amount_usd')} cash. Novus status: {'installed' if novus.get('novus_installed') else 'email verification required'}.
  </div>
  <h2>Autopilot Walkthrough</h2>
  <div class="grid">{agents}</div>
  <h2>Portfolio Ranking</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>#</th><th>Route</th><th>Target</th><th>Amount</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
  <h2>Judge Scorecard</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>Criterion</th><th>Weight</th><th>Proof</th><th>Gap</th></tr></thead>
      <tbody>{scorecard}</tbody>
    </table>
  </div>
  <h2>Trust and Control</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>Action</th><th>Status</th><th>Risk</th></tr></thead>
      <tbody>{approvals}</tbody>
    </table>
  </div>
  <div class="panel warn">
    <strong>Evidence gaps before judging:</strong>
    <ul>{gaps}</ul>
  </div>
  <h2>Manual vs PrizePilot</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>Metric</th><th>Manual</th><th>PrizePilot</th></tr></thead>
      <tbody>{benchmark}</tbody>
    </table>
  </div>
  <h2>Integrity Boundary</h2>
  <ul>{boundaries}</ul>
  <p>Machine-readable plan: <code>/api/plan</code></p>
</main>
</body>
</html>"""


class PrizePilotHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        route = urlparse(self.path).path
        if route == "/":
            self._send("text/html; charset=utf-8", render_dashboard(dashboard_payload()).encode("utf-8"))
            return
        if route == "/api/plan":
            self._send("application/json; charset=utf-8", json.dumps(dashboard_payload(), indent=2).encode("utf-8"))
            return
        if route == "/api/novus-readiness":
            self._send("application/json; charset=utf-8", json.dumps(dashboard_payload()["novus_readiness"], indent=2).encode("utf-8"))
            return
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _send(self, content_type: str, body: bytes) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def serve(host: str = "0.0.0.0", port: int = 8000) -> None:
    server = ThreadingHTTPServer((host, port), PrizePilotHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the PrizePilot demo web service.")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    serve(args.host, args.port)


if __name__ == "__main__":
    main()
