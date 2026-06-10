# Architecture

PrizePilot has three layers:

1. `agent.py` loads structured opportunity data, scores prize routes, and emits approval checkpoints.
2. `qwen_client.py` optionally refines a local plan through Qwen Cloud's OpenAI-compatible chat endpoint.
3. `webapp.py` exposes the same deterministic planning payload through a small standard-library HTTP service for deployment proof.

External actions are intentionally separated from planning. Account creation, API keys, cloud deployment, public posts, public repositories, and final submissions require user confirmation at action time.
