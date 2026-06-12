# Blog Draft

Title: Building PrizePilot: an accountable Qwen-ready agent for hackathon execution

## The Problem

Online hackathons look like a fast path to income, but the real decision is not "which prize is biggest?" It is "which prize is most reachable with the time, accounts, evidence, and public actions available right now?"

PrizePilot was built around that practical question. It reads structured opportunity data, ranks cash-prize routes, and turns the best route into a concrete submission plan with human approval checkpoints. The goal is not to make an agent blindly submit forms. The goal is to make an agent useful before the risky steps: account creation, API keys, public repositories, videos, blog posts, payout setup, and final submission buttons.

## Why This Fits Track 4: Autopilot Agent

PrizePilot automates a real workflow: evaluating prize opportunities and preparing submission assets. That workflow has messy inputs and high-consequence edges. Prize pages often mix headline prize pools with small category prizes, eligibility rules, judging criteria, public artifact requirements, and deadlines in different time zones.

The agent's job is to convert that ambiguity into an execution queue:

- Which route should be attempted first?
- Which prizes have multiple winners?
- Which steps can be safely prepared offline?
- Which steps require the user's identity, account, API key, or final approval?
- What proof should be captured before making a public claim?

This makes the agent useful as an autopilot system while still preserving human control where external side effects matter.

## Current Planning Behavior

The local deterministic planner ranks opportunities by prize amount, number of winners, deadline pressure, and blockers. In the current sample portfolio, the agent keeps a near-deadline USD 200 Splunk feedback route first because it is a multi-winner, low-friction prize. The Qwen Cloud Blog Post Award is ranked as the second wave because it has higher upside, but it requires a qualified Devpost project, public repo, demo/video, blog/social URL, Qwen Cloud usage, and Alibaba Cloud deployment proof.

That distinction is the whole product thesis: the best agent should not chase the largest headline pool. It should help the builder choose the route that can actually be completed with honest evidence.

## Qwen Cloud Integration Plan

PrizePilot is Qwen-ready through an OpenAI-compatible DashScope client. The deterministic planner works locally so every recommendation can be audited. A live Qwen/DashScope smoke proof now shows that Qwen Cloud can refine the reasoning, rewrite submission narratives, and help turn raw opportunity data into sharper Devpost and blog materials without storing the runtime key.

The client supports:

- `DASHSCOPE_API_KEY` and `QWEN_API_KEY`
- OpenAI-compatible `/chat/completions` request shape
- configurable base URL and model
- safer error messages when no API key is present

This draft claims only the completed Qwen/DashScope smoke proof captured with a runtime-only key. It does not claim Alibaba Cloud endpoint deployment.

## Deployment Story

PrizePilot includes a deployable standard-library web/API service and Dockerfile. The dashboard exposes the same plan through:

- `/` for a browser-readable dashboard
- `/api/plan` for machine-readable planning output

The local dashboard already shows the project target, portfolio ranking, and integrity boundary. The Alibaba Cloud deployment runbook describes how to capture the final public endpoint, screenshot, API response, and deployment proof once the user authorizes cloud setup.

## Integrity Boundary

The agent intentionally separates preparation from external effects:

- It can write drafts, rank opportunities, generate checklists, and build local packages.
- It can truthfully claim one Qwen/DashScope live smoke proof, and future reruns still require action-time key entry.
- It cannot claim Alibaba Cloud deployment until a public deployment exists.
- It cannot publish a repo, video, blog post, or Devpost submission without user approval.
- It does not store passwords, OTPs, API keys, payout data, tax data, or KYC data.

That boundary is a product feature. Hackathon automation becomes more credible when the agent is explicit about what is proven and what still requires user action.

## What I Would Show in the Demo

The demo starts with a portfolio containing Splunk, Qwen Cloud, UiPath, Arm, and an engineering bounty. PrizePilot ranks the routes and explains why the Splunk feedback prize is the urgent first target while Qwen Cloud is the stronger second-wave project route.

Then the demo opens the Qwen project plan. The agent targets the Blog Post Award and Honorable Mention route instead of over-optimizing for a single-winner grand prize. It generates approval checkpoints for Devpost joining, Qwen/Alibaba account work, public repository creation, video/blog publication, and final submission.

Finally, the demo shows the dashboard and `/api/plan` output, proving that the planning result can be inspected by both people and tools.

## Next Steps Before Publication

Before this is published as a final Qwen Blog Post Award entry, the remaining proof should be captured:

1. Link the completed Qwen Cloud refinement proof.
2. Deploy the web/API service on Alibaba Cloud after account-owner approval.
3. Publish the source repository after user approval.
4. Record or publish the demo video.
5. Update this blog with the final public repo, deployment URL, and Qwen live-check result.
6. Submit the Devpost project and blog URL only after final confirmation.

## Closing

PrizePilot is a small agent, but it aims at a real pattern: using AI to make prize work accountable. The valuable part is not just drafting text. It is maintaining a clear distinction between preparation, evidence, and irreversible external action.

That is the kind of autopilot I want for hackathon execution: fast where it can be fast, cautious where it must be cautious, and always honest about what has actually happened.
