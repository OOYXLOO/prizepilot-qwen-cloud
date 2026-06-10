import unittest

from prizepilot.agent import Opportunity, Prize, plan_locally, plan_portfolio


class AgentTests(unittest.TestCase):
    def test_prioritizes_multi_winner_small_cash_prize(self) -> None:
        opportunity = Opportunity(
            name="Qwen",
            url="https://example.com",
            deadline="2026-07-10",
            participants=2500,
            human_blockers=["cloud deployment"],
            prizes=[
                Prize("Grand Prize", 7000, 1, ["single_winner", "cloud_deployment"]),
                Prize("Blog Post Award", 500, 10, ["blog", "cloud_deployment"]),
            ],
        )

        plan = plan_locally(opportunity)

        self.assertEqual(plan["target_prize"]["name"], "Blog Post Award")

    def test_product_usage_prize_is_marked_as_requiring_real_usage(self) -> None:
        opportunity = Opportunity(
            name="UiPath",
            url="https://example.com",
            deadline="2026-06-30",
            prizes=[Prize("Best Product Feedback", 1500, 1, ["feedback", "product_usage_required", "single_winner"])],
            human_blockers=["real product usage"],
        )

        plan = plan_locally(opportunity)

        self.assertIn("real product usage", plan["human_actions"])
        self.assertIn("Submit concise", plan["strategy"])

    def test_human_action_queue_flags_external_side_effects(self) -> None:
        opportunity = Opportunity(
            name="Blog route",
            url="https://example.com",
            deadline="2026-07-10",
            prizes=[Prize("Blog Post Award", 500, 10, ["blog"])],
        )

        plan = plan_locally(opportunity)

        self.assertTrue(any("Publish the blog" in item for item in plan["approval_checkpoints"]))
        self.assertTrue(any("Do not store passwords" in item for item in plan["approval_checkpoints"]))

    def test_single_winner_platform_prize_uses_evidence_strategy(self) -> None:
        opportunity = Opportunity(
            name="Arm",
            url="https://example.com",
            deadline="2026-08-15",
            prizes=[Prize("Best Cloud AI", 1000, 1, ["single_winner", "cloud_deployment"])],
        )

        plan = plan_locally(opportunity)

        self.assertIn("smallest credible artifact", plan["strategy"])

    def test_product_analytics_required_route_keeps_cash_target(self) -> None:
        opportunity = Opportunity(
            name="Mind the Product",
            url="https://example.com",
            deadline="2026-06-20",
            prizes=[
                Prize("First Place", 5000, 1, ["single_winner", "product_analytics_required"]),
                Prize("Product Bundle", 0, 10, ["non_cash", "product_analytics_required"]),
            ],
            human_blockers=["Novus email verification"],
        )

        plan = plan_locally(opportunity)

        self.assertEqual(plan["target_prize"]["name"], "First Place")
        self.assertIn("instrument it with the required analytics tool", plan["strategy"])
        self.assertTrue(any("Install or connect product analytics" in item for item in plan["approval_checkpoints"]))

    def test_portfolio_keeps_splunk_first(self) -> None:
        splunk = Opportunity(
            name="Splunk Agentic Ops Hackathon",
            url="https://splunk.devpost.com/",
            deadline="2026-06-16",
            status="primary",
            prizes=[Prize("Most Valuable Feedback", 200, 5, ["feedback"])],
        )
        qwen = Opportunity(
            name="Qwen Cloud",
            url="https://qwencloud-hackathon.devpost.com/",
            deadline="2026-07-10",
            participants=2500,
            prizes=[Prize("Blog Post Award", 500, 10, ["blog", "cloud_deployment"])],
            human_blockers=["cloud deployment", "public repo", "public video"],
        )

        portfolio = plan_portfolio([qwen, splunk])

        self.assertEqual(portfolio["ranked"][0]["opportunity"]["name"], "Splunk Agentic Ops Hackathon")


if __name__ == "__main__":
    unittest.main()
