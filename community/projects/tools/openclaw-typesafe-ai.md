# openclaw-typesafe-ai

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenClaw plugin that registers one optional agent tool, `typesafe_decide`, for explicit TypeSafe Jev decisions over caller-supplied state—no hooks, model provider, or ambient conversation capture. Independent of the broader hook-based community OpenClaw TypeSafe plugin.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Olli0103/openclaw-typesafe-ai) |
| Maintainer | [Olli0103](https://github.com/Olli0103). Independently curated; this page is not an upstream submission or endorsement. Not an official TypeSafe or OpenClaw package. |
| Format | OpenClaw plugin **openclaw-typesafe-ai 0.1.3** (TypeScript; npm / ClawHub). Plugin ID `typesafe-ai` (conflicts with the other community plugin of the same ID). |
| Requirements | OpenClaw **2026.9.4** (pinned compatibility); Node **≥ 24.16** for upstream verify; `TYPESAFE_API_KEY` via OpenClaw SecretRef / env provider. |
| License | [MIT](https://github.com/Olli0103/openclaw-typesafe-ai/blob/985718448bf38a3a58d18389d376621b9bc54615/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Review host is Node 22—upstream `VERIFICATION.md` reports **102** mocked tests + host checks on Node 24.20 / OpenClaw 2026.9.4; this listing did not re-run that suite or install into a live Gateway. No live TypeSafe spend here. |

## When to use

Use it when an OpenClaw agent should opt in to typed Jev decisions over deliberately supplied JSON/text without automatic lifecycle interception. Prefer the other community OpenClaw TypeSafe plugin only when hook-based triage/guardrails are intended and its manifest installs on your OpenClaw version. Do not load both: they share plugin ID `typesafe-ai`.

## How it works

[`src/index.ts`](https://github.com/Olli0103/openclaw-typesafe-ai/blob/985718448bf38a3a58d18389d376621b9bc54615/src/index.ts) registers `typesafe_decide` only. The client posts to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) with validated Choice/Score/Noul questions, SecretRef-aware credentials, redirect rejection, and bounded retries on 429/529. No ambient key fallback.

## Get started

```sh
git clone https://github.com/Olli0103/openclaw-typesafe-ai.git
cd openclaw-typesafe-ai
git checkout 985718448bf38a3a58d18389d376621b9bc54615
# Upstream verify expects Node 24.20 + OpenClaw 2026.9.4:
# npm ci --ignore-scripts && npm test && npm run test:host
```

Install only when you intend to change OpenClaw (may restart Gateway):

```sh
openclaw plugins install npm:openclaw-typesafe-ai@0.1.3
# or: clawhub:openclaw-typesafe-ai
openclaw config set plugins.entries.typesafe-ai.config.apiKey \
  --ref-provider default --ref-source env --ref-id TYPESAFE_API_KEY
openclaw plugins enable typesafe-ai
```

Live tool calls bill TypeSafe; this listing did not install or call.

## Examples and demos

- Upstream [VERIFICATION.md](https://github.com/Olli0103/openclaw-typesafe-ai/blob/985718448bf38a3a58d18389d376621b9bc54615/VERIFICATION.md) documents mocked and host checks.
- README comparison table vs `jason-allen-oneal/openclaw-plugin-typesafe-ai`.

## Limits and data handling

Only caller-supplied `state` / questions / model reach TypeSafe. Shared plugin ID means mutual exclusion with the other community plugin. Compatibility claimed only for OpenClaw 2026.9.4.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9857184](https://github.com/Olli0103/openclaw-typesafe-ai/tree/985718448bf38a3a58d18389d376621b9bc54615): MIT **0.1.3**; AI-assisted source review of README, LICENSE, `src/`, tests, and upstream verification report. Catalog host did not re-run Node 24 suite. No live TypeSafe call.

Related: [typesafe-mcp](typesafe-mcp.md), [jev-mcp](jev-mcp.md).
