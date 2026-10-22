# webular (web research CLI with Jev decisions)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Web research CLI that covers search, scrape, crawl, map, extract, summarize, answer and multi-step research with free, open-source parts, and uses Jev for its judgment calls, with a deterministic fallback for every decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/srinitude/webular) |
| Maintainer | [srinitude](https://github.com/srinitude). Independently curated. |
| Format | CLI and MCP server (Bun, npm `webular`) |
| Requirements | Node for the npm launcher (or Bun/Homebrew/Scoop/winget builds); optional `TYPESAFE_API_KEY` for Jev decisions. |
| License | [Apache-2.0](https://github.com/srinitude/webular/blob/f5d0be4887e18ce0c65f138107d97d839bb7a529/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/jev/client.ts`](https://github.com/srinitude/webular/blob/f5d0be4887e18ce0c65f138107d97d839bb7a529/src/lib/jev/client.ts) at the pinned commit. |

## When to use

- Run Firecrawl- or Tavily-style research without a paid web-data API.
- Let Jev decide crawl, extraction and citation steps with typed answers.
- Mismatch: without a key, decisions fall back to deterministic code.

## How it works

`src/lib/jev/client.ts` is a typed System One client pinned to `jev-1.13.0`; decision modules under `src/lib/jev/decisions/` (crawl, extract, answer evidence and citations) call it, and every caller keeps a deterministic fallback so failures never block a workflow. Integration evidence: [`src/lib/jev/client.ts`](https://github.com/srinitude/webular/blob/f5d0be4887e18ce0c65f138107d97d839bb7a529/src/lib/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm i -g webular
webular doctor
webular research "your question"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Commands table in the README: [github.com/srinitude/webular#readme](https://github.com/srinitude/webular#readme)
- npm package: [www.npmjs.com/package/webular](https://www.npmjs.com/package/webular)

## Limits and data handling

With a key, page text and questions for decision steps go to TypeSafe. Respect site terms when crawling.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit f5d0be4887e1](https://github.com/srinitude/webular/tree/f5d0be4887e18ce0c65f138107d97d839bb7a529). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
