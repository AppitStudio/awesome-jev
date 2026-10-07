# jev-claude-router (sergeiboikov)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server for Claude Code and Claude Desktop where TypeSafe Jev recommends which Claude model and effort level suit a task, comparing candidates by live OpenRouter prices, context sizes and output limits; it recommends only and never switches the model itself. Distinct from the separately listed jev-claude-router.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sergeiboikov/jev-claude-router) |
| Maintainer | [sergeiboikov](https://github.com/sergeiboikov). Independently curated. |
| Format | Python MCP server (`uv run jev-claude-router`, stdio) with a Claude Desktop config example |
| Requirements | Python with uv and a TypeSafe console API key in `JEV_API_KEY`; no OpenRouter or Anthropic key (the public OpenRouter catalog is read for prices). |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Get a model + effort recommendation at the start of a Claude task, then switch in the model picker.
- Limit candidates with `CLAUDE_MODELS` (OpenRouter ids).
- Mismatch: an MCP tool cannot change the running model, so you switch manually; see also [jev-claude-router](jev-claude-router.md), a different project.

## How it works

[`server.py`](https://github.com/sergeiboikov/jev-claude-router/blob/4f61b50951949f31fec02fb619d91f5f09cf2d95/src/jev_claude_router/server.py) exposes `pick_model`: Jev first picks a model from the candidates using live OpenRouter prices and limits, then is asked again for an effort level on that model; the tool returns the recommendation.

## Get started

Run from a checkout (README *Development*) and register it as an MCP server:

```sh
git clone https://github.com/sergeiboikov/jev-claude-router && cd jev-claude-router
uv sync
JEV_API_KEY=... uv run jev-claude-router
```

Each `pick_model` call makes two Jev requests billed to your TypeSafe key.

## Examples and demos

- README *How it works* and *Configuration*.
- Claude Desktop config: [`examples/claude_desktop_config.json`](https://github.com/sergeiboikov/jev-claude-router/blob/4f61b50951949f31fec02fb619d91f5f09cf2d95/examples/claude_desktop_config.json).

## Limits and data handling

Your task description goes to TypeSafe; the server fetches OpenRouter's public model catalog. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 4f61b5095194](https://github.com/sergeiboikov/jev-claude-router/tree/4f61b50951949f31fec02fb619d91f5f09cf2d95). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
