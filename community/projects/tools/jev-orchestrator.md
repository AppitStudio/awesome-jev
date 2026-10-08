# Jev Orchestrator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Node/TypeScript experiment testing whether Jev can make useful next-step decisions around a coding agent: decision-only by default (inspect the repo, send compact state to Jev via TypeSafe, Vercel or OpenRouter, apply deterministic thresholds, record a JSONL trace), with an explicit `--orchestrate` mode for a bounded, manually approved loop of safe searches, reads, read-only git, validation scripts and delegation to Codex CLI or Claude Code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/petercr/jev-orchestrator) |
| Maintainer | [petercr](https://github.com/petercr). Independently curated. |
| Format | Node CLI (pnpm + tsx) |
| Requirements | Node, pnpm; one provider key: `TYPESAFE_API_KEY` (`jev-latest`), `AI_GATEWAY_API_KEY` (`typesafe-ai/jev`) or `OPENROUTER_API_KEY` (`typesafe/jev-1.13`). |
| License | [MIT](https://github.com/petercr/jev-orchestrator/blob/933c4ecc888370003f0f8f13c20b06a223523600/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Measure whether a decision model chooses sensible next actions for an agent.
- Run a tightly bounded, approve-each-step orchestration loop.
- Mismatch: an experiment; it cannot run arbitrary shell commands by design.

## How it works

The CLI builds a compact repo state, asks Jev via the selected provider (`JEV_PROVIDER`), applies policy thresholds and appends a JSONL trace; [`scripts/verify-jev.mjs`](https://github.com/petercr/jev-orchestrator/blob/933c4ecc888370003f0f8f13c20b06a223523600/scripts/verify-jev.mjs) checks provider wiring.

## Get started

Install and run decision-only mode (README):

```sh
git clone https://github.com/petercr/jev-orchestrator.git && cd jev-orchestrator
pnpm install
cp .env.example .env
pnpm exec node --env-file=.env --import tsx src/cli.ts -- . "Inspect this repo and choose the safest useful first action"
```

Jev calls billed by the selected provider; delegated agents bill separately.

## Examples and demos

- README provider table and `--orchestrate` safety notes.

## Limits and data handling

Repository state summaries go to the selected provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 933c4ecc8883](https://github.com/petercr/jev-orchestrator/tree/933c4ecc888370003f0f8f13c20b06a223523600). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
