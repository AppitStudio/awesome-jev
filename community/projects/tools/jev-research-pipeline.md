# jev-research-pipeline

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pilot daily research monitor: deterministic Python harvests papers/repos, TypeSafe Jev screens each (source, question) pair, and a writing model drafts Obsidian notes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shimo4228/jev-research-pipeline) |
| Maintainer | [shimo4228](https://github.com/shimo4228). Independently curated. |
| Format | Python package/CLI (macOS launchd; manual runs elsewhere). |
| Requirements | Python 3.12; paid TypeSafe API key; ChatGPT/Codex subscription (default prose) or DashScope for Qwen. |
| License | [MIT](https://github.com/shimo4228/jev-research-pipeline/blob/16a5b27ceccebe0e4bcd1ce868f9f3e2f54a3660/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Pilot status. |

## When to use

Use when you want **standing research questions** judged cheaply with typed Jev gates while an LLM only writes prose.

## How it works

Jev modules under [`src/jev_research_pipeline/jev/`](https://github.com/shimo4228/jev-research-pipeline/tree/16a5b27ceccebe0e4bcd1ce868f9f3e2f54a3660/src/jev_research_pipeline/jev) answer on-topic/gates/scores/claim picks via Pydantic AI `typesafe:` models. Code owns source nets, thresholds, and vault writes.

## Get started

```sh
git clone https://github.com/shimo4228/jev-research-pipeline.git
cd jev-research-pipeline
git checkout 16a5b27ceccebe0e4bcd1ce868f9f3e2f54a3660
# follow upstream README for uv/venv, keys, Obsidian vault path, and launchd
```

## Examples and demos

- Upstream overview SVG and pilot log under `docs/`.
- [https://dev.to/shimo4228/moving-my-research-pipelines-judgment-calls-from-an-llm-to-jev-a-judgment-only-model-4ncj](https://dev.to/shimo4228/moving-my-research-pipelines-judgment-calls-from-an-llm-to-jev-a-judgment-only-model-4ncj)

## Limits and data handling

Source abstracts/question context go to TypeSafe; prose goes to the writing model. Pilot: Japanese-oriented note strings; evaluation claims are author-reported.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 16a5b27](https://github.com/shimo4228/jev-research-pipeline/tree/16a5b27ceccebe0e4bcd1ce868f9f3e2f54a3660). AI-assisted README and LICENSE inspection of Jev package layout; install/live paths not executed.
