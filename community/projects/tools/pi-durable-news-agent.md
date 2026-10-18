# Pi Durable News Agent

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Proactive pi-durable news agent: a cron tick sweeps about 28 feeds plus topic searches, Jev throws out off-topic or low-value items and sorts the rest into Hype, Facts, and Signal, and research subagents dig into the strongest stories.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/disler/pi-durable-news-agent) |
| Maintainer | [disler](https://github.com/disler). Independently curated. |
| Format | TypeScript workspace (pi-durable agent + apps) |
| Requirements | Node 24, `just`, and keys for OpenRouter (agents) and TypeSafe or OpenRouter (Jev). |
| License | [MIT](https://github.com/disler/pi-durable-news-agent/blob/273b79bb8d3d8907cae9fbd6abd3da163ee2a343/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/shared/packages/jev/src/client.ts`](https://github.com/disler/pi-durable-news-agent/blob/273b79bb8d3d8907cae9fbd6abd3da163ee2a343/apps/shared/packages/jev/src/client.ts) at the pinned commit. |

## When to use

- Run an always-on agent that filters tech news before you read it.
- Learn a durable proactive-agent pattern with Jev as the cheap filter.
- Mismatch: reference codebase from a video, not a hosted product.

## How it works

`apps/shared/packages/jev/src/client.ts` wraps Jev, preferring TypeSafe and then OpenRouter. Each tick, Jev filters and labels candidate stories, repeated coverage is folded, the top items are ranked, and subagents research them. Walkthrough video: youtu.be/OLqP8jxJ0Wc. Integration evidence: [`apps/shared/packages/jev/src/client.ts`](https://github.com/disler/pi-durable-news-agent/blob/273b79bb8d3d8907cae9fbd6abd3da163ee2a343/apps/shared/packages/jev/src/client.ts).

## Get started

From the upstream README: run the agentic `/install` command in Claude Code (or Pi), which checks Node 24 and `just`, installs workspaces, and confirms your keys.

```sh
git clone https://github.com/disler/pi-durable-news-agent && cd pi-durable-news-agent
claude "/install"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [youtu.be/OLqP8jxJ0Wc](https://youtu.be/OLqP8jxJ0Wc)
- apps/shared/packages/jev/src/client.ts

## Limits and data handling

Story titles and text go to TypeSafe or OpenRouter; agents call OpenRouter models. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 273b79bb8d3d](https://github.com/disler/pi-durable-news-agent/tree/273b79bb8d3d8907cae9fbd6abd3da163ee2a343). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
