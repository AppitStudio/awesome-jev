# Jev Studio

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

One-stop kit for experimenting with TypeSafe Jev: a `jev` CLI for verify/screen/classify/extract/match/route flows plus an MCP server that exposes Choice/Noul/Score tools and cookbook slash commands.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/utk2103/jev-studio) |
| Maintainer | [utk2103](https://github.com/utk2103). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **jev-studio 0.1.0** (Alpha) installing `jev` CLI and `jev-studio` MCP server. |
| Requirements | Python ≥ 3.10; credentials via `TYPESAFE_API_KEY` and/or OpenRouter / Cloudflare Workers AI per upstream auth cascade. |
| License | [MIT](https://github.com/utk2103/jev-studio/blob/af18274793a0c6e1be7394bbc77793f70cc7ec0c/LICENSE). |

## When to use

Use it when you want a single install for shell judgments and agent MCP tools while exploring TypeSafe cookbooks. Prefer [typesafeai-cli](typesafeai-cli.md) or [typesafe-cli](typesafe-cli.md) for a thinner CLI-only surface, or [jev-mcp](jev-mcp.md) for a focused TypeScript MCP judgment server without the combined studio packaging.

## How it works

[`jev_studio/cli/provider.py`](https://github.com/utk2103/jev-studio/blob/af18274793a0c6e1be7394bbc77793f70cc7ec0c/jev_studio/cli/provider.py) resolves TypeSafe (`https://api.typesafe.ai/v1/systemone`), OpenRouter Decisions, or Cloudflare Workers AI from available keys. The CLI wraps typed judgments (verify, screen, classify, extract, match, and more); `jev-studio` serves MCP tools and prompt libraries over stdio. Optional agent hooks live under `hooks/`.

## Get started

```sh
git clone https://github.com/utk2103/jev-studio.git
cd jev-studio
git checkout af18274793a0c6e1be7394bbc77793f70cc7ec0c
pip install -e .
jev auth status
# jev classify --help   # live calls need a provider key
```

Live commands send text to the selected provider and can incur charges. This listing did not run live inference or install the MCP server into an agent host.

## Examples and demos

- Upstream README command catalog (`jev verify|screen|classify|extract|match|…`).
- Package tests under `tests/` (instructions helpers); not fully re-run on the review host.

## Limits and data handling

Input text and judgment state leave the host for the chosen provider. Project is marked Under Development / Alpha (0.1.0)—APIs and packaging may change. Upstream timing/cost claims were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit af18274](https://github.com/utk2103/jev-studio/tree/af18274793a0c6e1be7394bbc77793f70cc7ec0c): **0.1.0**, MIT. AI-assisted source review of README, `pyproject.toml`, `jev_studio/cli/provider.py`, and license. No live TypeSafe/OpenRouter/Cloudflare calls were made.

Related: [jev-mcp](jev-mcp.md), [typesafeai-cli](typesafeai-cli.md), [typesafe-cli](typesafe-cli.md).
