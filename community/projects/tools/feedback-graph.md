# Feedback Graph (local memory of corrections for coding agents, optional Jev classifier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Docker app that reads Claude Code and Codex sessions, finds the moments you pushed back, and turns them into confirmed lessons your agents get through MCP; Jev is one of the selectable models for classification jobs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ChaosDeSelva/Feedback-Graph) |
| Maintainer | [ChaosDeSelva](https://github.com/ChaosDeSelva). Independently curated. |
| Format | Self-hosted app (Docker) with MCP server |
| Requirements | Docker, git and Ollama by default; optional TypeSafe API key. |
| License | [Apache-2.0](https://github.com/ChaosDeSelva/Feedback-Graph/blob/789ac9cb7cacdc4b2212dba92b329e3fb651ba50/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/core/src/llm/providers.ts`](https://github.com/ChaosDeSelva/Feedback-Graph/blob/789ac9cb7cacdc4b2212dba92b329e3fb651ba50/packages/core/src/llm/providers.ts) at the pinned commit. |

## When to use

- Stop coding agents repeating mistakes you already corrected.
- Keep everything local by default, with optional cloud providers.
- Mismatch: Jev answers only enum-style classification jobs, not free-text jobs.

## How it works

`providers.ts` adds a `jev` provider that turns enum schema fields into choice questions posted to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); set e.g. `CLASSIFY_LLM=jev`. Integration evidence: [`packages/core/src/llm/providers.ts`](https://github.com/ChaosDeSelva/Feedback-Graph/blob/789ac9cb7cacdc4b2212dba92b329e3fb651ba50/packages/core/src/llm/providers.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ChaosDeSelva/Feedback-Graph.git feedback-graph
cd feedback-graph && ./scripts/setup.sh
docker compose up -d --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ChaosDeSelva/Feedback-Graph#readme](https://github.com/ChaosDeSelva/Feedback-Graph#readme)

## Limits and data handling

Local Ollama by default; session excerpts go to TypeSafe only when Jev is configured.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 789ac9cb7cac](https://github.com/ChaosDeSelva/Feedback-Graph/tree/789ac9cb7cacdc4b2212dba92b329e3fb651ba50). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
