# Jev Lucid Memory

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Research prototype of wake–sleep memory for AI agents: an LLM drafts lessons from task records, a decision model (TypeSafe Jev via the official SDK or OpenRouter, or local Clef-Flash) judges whether each lesson is supported enough to keep and whether its conditions fit a new task, and code enforces evidence hashes, scope and versioning.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JayYun98/jev-lucid-memory) |
| Maintainer | [JayYun98](https://github.com/JayYun98). Independently curated. |
| Format | Python package + CLI (`jev-memory`) |
| Requirements | Python 3.11+ and `uv`; a local chat model for lesson writing; for Jev, `TYPESAFE_API_KEY` (with `uv sync --extra jev`) or `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/JayYun98/jev-lucid-memory/blob/67d930bd822906c90bbc16127e78deae3a724ee7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Experiment with gating agent memory writes and reuse behind calibrated yes/no judgments.
- Mismatch: the author reports no learning advantage established yet; treat it as research code.

## How it works

[`src/jev_memory/providers.py`](https://github.com/JayYun98/jev-lucid-memory/blob/67d930bd822906c90bbc16127e78deae3a724ee7/src/jev_memory/providers.py) implements `TypeSafeGate` (official `typesafe_sdk`, `jev-1.13.0`) and `OpenRouterGate` (`typesafe/jev-1.13` via OpenRouter Decisions). The maintainer's task results and limitations are in [`docs/EVALUATION.md`](https://github.com/JayYun98/jev-lucid-memory/blob/67d930bd822906c90bbc16127e78deae3a724ee7/docs/EVALUATION.md) (their results; not reproduced here).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/JayYun98/jev-lucid-memory.git
cd jev-lucid-memory
uv sync --locked
uv sync --extra jev   # optional official TypeSafe SDK
uv run jev-memory --provider typesafe admit examples/admission.jsonl
```

## Limits and data handling

Choosing a cloud decision provider sends the relevant task and observations to TypeSafe or OpenRouter; keys come from the environment and are not stored in SQLite. Lesson writing stays local unless a cloud writer is requested. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 67d930bd8229](https://github.com/JayYun98/jev-lucid-memory/tree/67d930bd822906c90bbc16127e78deae3a724ee7). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
