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
        "integrity_boundary": [
            "No API key is stored in the deployed app.",
            "No public repository, video, blog post, or final Devpost submission is claimed until the user authorizes it.",
            "Live Qwen Cloud usage and Alibaba Cloud deployment proof must be captured after deployment.",
            "Novus is not claimed as installed until the official Novus account is verified and connected.",
        ],
    }


def render_dashboard(payload: dict[str, Any]) -> str:
    qwen_target = payload["qwen_plan"]["target_prize"]
    mtp_target = payload["mindtheproduct_plan"]["target_prize"]
    novus = payload["novus_readiness"]
    top_routes = payload["portfolio"]["ranked"][:4]
    rows = "\n".join(
        f"<tr><td data-label=\"#\">{index}</td><td data-label=\"Route\">{route['opportunity']['name']}</td><td data-label=\"Target\">{route['target_prize'].get('name', 'N/A')}</td><td data-label=\"Amount\">USD {route['target_prize'].get('amount_usd', 'N/A')}</td></tr>"
        for index, route in enumerate(top_routes, start=1)
    )
    boundaries = "\n".join(f"<li>{item}</li>" for item in payload["integrity_boundary"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PrizePilot Qwen Demo</title>
  <style>
    body {{ margin: 0; font-family: Arial, sans-serif; background: #f6f8fb; color: #16202a; }}
    main {{ max-width: 980px; margin: 0 auto; padding: 44px 24px 64px; }}
    h1 {{ font-size: 42px; line-height: 1.1; margin: 0 0 16px; }}
    h2 {{ margin-top: 34px; }}
    p, li {{ color: #526173; line-height: 1.55; }}
    .table-wrap {{ border: 1px solid #d9e2ec; background: white; overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 680px; }}
    th, td {{ padding: 13px 14px; border-bottom: 1px solid #d9e2ec; text-align: left; }}
    th {{ color: #526173; font-size: 13px; }}
    .pill {{ display: inline-block; margin: 6px 8px 18px 0; padding: 8px 12px; background: #0f766e; color: white; font-weight: 700; font-size: 13px; }}
    .pill.alt {{ background: #b45309; }}
    .panel {{ background: white; border-left: 6px solid #0f766e; padding: 18px 22px; margin-top: 20px; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08); }}
    code {{ background: #e8eef5; padding: 2px 5px; }}
    @media (max-width: 620px) {{
      h1 {{ font-size: 32px; }}
      main {{ padding: 30px 16px 48px; }}
      .table-wrap {{ overflow-x: visible; }}
      table {{ min-width: 0; }}
      thead {{ display: none; }}
      tbody, tr, td {{ display: block; }}
      tr {{ border-bottom: 1px solid #d9e2ec; padding: 8px 0; }}
      tr:last-child {{ border-bottom: 0; }}
      td {{ border-bottom: 0; display: grid; grid-template-columns: 82px 1fr; gap: 10px; padding: 8px 14px; }}
      td::before {{ content: attr(data-label); color: #526173; font-weight: 700; }}
    }}
  </style>
</head>
<body>
<main>
  <span class="pill">Qwen Cloud Track 4</span>
  <span class="pill alt">Autopilot Agent</span>
  <h1>PrizePilot turns prize pages into accountable execution plans.</h1>
  <p>This deployed demo presents the same deterministic planning payload used by the CLI. A live Qwen refinement pass can be added after an API key is provided at action time.</p>
  <div class="panel">
    <strong>Current Qwen target:</strong> {qwen_target.get('name')} - USD {qwen_target.get('amount_usd')} x {qwen_target.get('winners')} winners.
  </div>
  <div class="panel">
    <strong>Mind the Product target:</strong> {mtp_target.get('name')} - USD {mtp_target.get('amount_usd')} cash. Novus status: {'installed' if novus.get('novus_installed') else 'email verification required'}.
  </div>
  <h2>Portfolio Ranking</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>#</th><th>Route</th><th>Target</th><th>Amount</th></tr></thead>
      <tbody>{rows}</tbody>
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
