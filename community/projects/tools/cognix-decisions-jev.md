# cognix-decisions-jev (COGNIX[WS] helper that answers fast browser decisions with TypeSafe Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Tiny Node helper for COGNIX[WS] that forwards the agent's fast browser decisions—which DOM element matches a description, and yes/no page questions—to TypeSafe Jev so the browser agent can act without re-reading the whole page each step.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cognixws/cognix-decisions-jev) |
| Maintainer | [cognixws](https://github.com/cognixws). Independently curated. |
| Format | Node.js COGNIX[WS] helper (Apache-2.0) |
| Requirements | COGNIX[WS] manifest v11+, Node.js, and a TypeSafe API key (`JEV_API_KEY` / model). |
| License | [Apache-2.0](https://github.com/cognixws/cognix-decisions-jev/blob/90c55e3e7a3bd02972b987be419b5d45b805d3bb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.mjs`](https://github.com/cognixws/cognix-decisions-jev/blob/90c55e3e7a3bd02972b987be419b5d45b805d3bb/server.mjs) at the pinned commit. |

## When to use

- Speed up COGNIX[WS] browser agents with typed Jev judgments.
- Answer element-match and yes/no page questions.
- Mismatch: COGNIX[WS]-specific helper; not a general browser MCP.

## How it works

`server.mjs` POSTs to `https://api.typesafe.ai/v1/systemone` (overridable via `JEV_API_URL`) with the owner's TypeSafe key and model (`jev-latest` by default) and returns typed answers to COGNIX[WS]. Integration evidence: [`server.mjs`](https://github.com/cognixws/cognix-decisions-jev/blob/90c55e3e7a3bd02972b987be419b5d45b805d3bb/server.mjs).

## Get started

Point COGNIX[WS] Settings ▸ Helper model at this server and set `JEV_API_KEY` (and optional `JEV_MODEL`).

```sh
git clone https://github.com/cognixws/cognix-decisions-jev.git && cd cognix-decisions-jev
export JEV_API_KEY=...
node server.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/cognixws/cognix-decisions-jev/blob/90c55e3e7a3bd02972b987be419b5d45b805d3bb/README.md](https://github.com/cognixws/cognix-decisions-jev/blob/90c55e3e7a3bd02972b987be419b5d45b805d3bb/README.md)

## Limits and data handling

Page snippets and agent questions under review are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 90c55e3e7a3b](https://github.com/cognixws/cognix-decisions-jev/tree/90c55e3e7a3bd02972b987be419b5d45b805d3bb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
