# Jev Model Router by zerone-agents (OpenAI- and Anthropic-compatible gateway where Jev picks the model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go model-routing gateway for agents: OpenAI Chat Completions and Anthropic Messages clients connect to it, and either name a model or let Jev choose from editable model cards; it streams text and tool calls, stores configuration in SQLite and ships a CLI, bilingual dashboard, Docker Compose quickstart and an agent skill. Distinct from the separately listed Claude Code and Codex routers of the same name.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zerone-agents/jev-model-router) |
| Maintainer | [zerone-agents](https://github.com/zerone-agents). Independently curated. |
| Format | Go service with SQLite, CLI and web dashboard (Docker image) |
| Requirements | Docker Compose (or the Go binary); a TypeSafe API key for routing; keys for the upstream generation providers. |
| License | [Apache-2.0](https://github.com/zerone-agents/jev-model-router/blob/02839455d7f024d3b432ace588cc935731ffcc01/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/decision/jev.go`](https://github.com/zerone-agents/jev-model-router/blob/02839455d7f024d3b432ace588cc935731ffcc01/internal/decision/jev.go) at the pinned commit. |

## When to use

- Put one endpoint in front of several models and let Jev pick per request.
- Manage providers and model cards from a dashboard or CLI.
- Mismatch: benchmark savings are the maintainers' own, on their model pool.

## How it works

`internal/decision/jev.go` posts the request summary and model-card choices to `{base_url}/v1/systemone`; the documented official configuration uses `https://api.typesafe.ai` with pinned `jev-1.13.0` and `TYPESAFE_API_KEY`. Integration evidence: [`internal/decision/jev.go`](https://github.com/zerone-agents/jev-model-router/blob/02839455d7f024d3b432ace588cc935731ffcc01/internal/decision/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/zerone-agents/jev-model-router && cd jev-model-router/quickstart
docker compose up -d
docker compose ps
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/zerone-agents/jev-model-router#readme](https://github.com/zerone-agents/jev-model-router#readme)
- Configuration: [github.com/zerone-agents/jev-model-router/blob/main/docs/configuration.md](https://github.com/zerone-agents/jev-model-router/blob/main/docs/configuration.md)

## Limits and data handling

Request summaries used for routing go to TypeSafe; prompts go to the upstream provider that serves them. Benchmark figures are author-claimed.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 02839455d7f0](https://github.com/zerone-agents/jev-model-router/tree/02839455d7f024d3b432ace588cc935731ffcc01). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
