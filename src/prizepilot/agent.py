from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List


@dataclass(frozen=True)
class Prize:
    name: str
    amount_usd: int
    winners: int = 1
    tags: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Prize":
        return cls(
            name=str(data["name"]),
            amount_usd=int(data.get("amount_usd", 0)),
            winners=int(data.get("winners", 1)),
            tags=list(data.get("tags", [])),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "amount_usd": self.amount_usd,
            "winners": self.winners,
            "tags": self.tags,
        }


@dataclass(frozen=True)
class Opportunity:
    name: str
    url: str
    deadline: str
    prizes: List[Prize]
    participants: int = 0
    status: str = "unknown"
    human_blockers: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

    @classmethod
    def from_file(cls, path: str) -> "Opportunity":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(
            name=str(data["name"]),
            url=str(data["url"]),
            deadline=str(data["deadline"]),
            participants=int(data.get("participants", 0)),
            status=str(data.get("status", "unknown")),
            prizes=[Prize.from_dict(item) for item in data.get("prizes", [])],
            human_blockers=list(data.get("human_blockers", [])),
            notes=list(data.get("notes", [])),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "url": self.url,
            "deadline": self.deadline,
            "participants": self.participants,
            "status": self.status,
            "prizes": [prize.to_dict() for prize in self.prizes],
            "human_blockers": self.human_blockers,
            "notes": self.notes,
        }


def _prize_score(prize: Prize) -> int:
    # Cap amount influence so the planner does not chase a single long-shot
    # grand prize when a smaller multi-winner route has better odds.
    score = min(prize.amount_usd, 1000) // 5
    score += min(prize.winners, 10) * 70
    tags = set(prize.tags)
    if "feedback" in tags:
        score += 500
    if "blog" in tags:
        score += 350
    if "honorable_mention" in tags:
        score += 300
    if "product_usage_required" in tags:
        score -= 150
    if "single_winner" in tags:
        score -= 500
    if "public_pr" in tags:
        score -= 250
    if "cloud_deployment" in tags:
        score -= 100
    if "product_analytics_required" in tags:
        score -= 120
    if "non_cash" in tags:
        score -= 1000
    return score


def _route_score(opportunity: Opportunity, prize: Prize) -> int:
    score = _prize_score(prize)
    score -= min(opportunity.participants // 250, 30)
    score -= len(opportunity.human_blockers) * 20
    if opportunity.status == "primary":
        score += 250
    if opportunity.status == "backup":
        score -= 20
    return score


def choose_prize(opportunity: Opportunity) -> Prize:
    if not opportunity.prizes:
        raise ValueError(f"{opportunity.name} has no prizes")
    return max(opportunity.prizes, key=_prize_score)


def approval_checkpoints(opportunity: Opportunity, prize: Prize) -> List[str]:
    checkpoints = [
        "Confirm eligibility for the target event and prize.",
        "Confirm before creating accounts, joining hackathons, publishing repos, posting videos/blogs, or submitting forms.",
        "Do not store passwords, OTPs, API keys, payment, tax, KYC, or recovery data.",
    ]
    tags = set(prize.tags)
    if "cloud_deployment" in tags or any("cloud" in blocker.lower() for blocker in opportunity.human_blockers):
        checkpoints.append("Capture live cloud deployment proof only after the deployment exists and can be public.")
    if "blog" in tags:
        checkpoints.append("Publish the blog/social post only after the user approves the public URL and wording.")
    if "public_pr" in tags:
        checkpoints.append("Open a public PR only after the user approves the GitHub account and branch.")
    if "product_analytics_required" in tags:
        checkpoints.append("Install or connect product analytics only after the official account is verified, and record the public proof without storing credentials.")
    return checkpoints


def strategy_for(opportunity: Opportunity, prize: Prize) -> str:
    tags = set(prize.tags)
    if "feedback" in tags:
        return "Submit concise, evidence-backed product or documentation feedback with reproduction details."
    if "blog" in tags:
        return "Prepare a qualified project submission, then use a public blog post to target the multi-winner blog award."
    if "honorable_mention" in tags:
        return "Ship a clean working prototype with honest deployment proof and strong project narrative."
    if "public_pr" in tags:
        return "Treat this as a backup bounty: prepare a focused patch, then wait for user-approved public PR and payout setup."
    if "product_analytics_required" in tags:
        return "Ship a narrow product workflow, instrument it with the required analytics tool, and use the data trail as judging evidence."
    return "Build the smallest credible artifact that satisfies the rules and can be verified publicly."


def plan_locally(opportunity: Opportunity) -> Dict[str, Any]:
    prize = choose_prize(opportunity)
    return {
        "opportunity": opportunity.to_dict(),
        "target_prize": prize.to_dict(),
        "score": _route_score(opportunity, prize),
        "strategy": strategy_for(opportunity, prize),
        "approval_checkpoints": approval_checkpoints(opportunity, prize),
        "human_actions": opportunity.human_blockers,
        "notes": opportunity.notes,
    }


def plan_portfolio(opportunities: Iterable[Opportunity]) -> Dict[str, Any]:
    ranked = [plan_locally(opportunity) for opportunity in opportunities]
    ranked.sort(key=lambda item: item["score"], reverse=True)
    return {
        "ranked": ranked,
        "recommendation": ranked[0]["opportunity"]["name"] if ranked else None,
    }
