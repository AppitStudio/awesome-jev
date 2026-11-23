# Better Jev Pipeline by Aria (local node-graph workbench for chaining several Jev calls and inspecting every request and answer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Organise multi-step decisions as a DAG of Jev calls: edit each node's state and questions visually, inject upstream answers with templates such as `{{n1.urgent.noul}}`, add local logic steps that gate downstream edges, then run everything in topological order and see probabilities, confidence, raw JSON, tokens and cost per node. Four built-in scenarios; Chinese UI and README.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aria467/better-jev-pipeline) |
| Maintainer | [aria467](https://github.com/aria467). Independently curated. |
| Format | Local web app (Vite frontend + Node.js proxy server) |
| Requirements | Node.js 22+ and pnpm; a TypeSafe API key (an optional HTTP proxy can be set). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/index.ts`](https://github.com/aria467/better-jev-pipeline/blob/334d55aa33f59b70eb882192965cdb79ebe606b7/server/index.ts) at the pinned commit. |

## When to use

- Prototype and debug a multi-question Jev pipeline visually before writing it in code.
- Mismatch: production orchestration; scenarios live in browser storage.

## How it works

`server/index.ts` keeps the key server-side and proxies `/api/systemone` to `TYPESAFE_BASE_URL` (default `https://api.typesafe.ai`). Integration evidence: [`server/index.ts`](https://github.com/aria467/better-jev-pipeline/blob/334d55aa33f59b70eb882192965cdb79ebe606b7/server/index.ts).

## Get started

Install, add a key to `.env` and start the dev server.

```sh
git clone https://github.com/aria467/better-jev-pipeline && cd better-jev-pipeline
pnpm install
echo 'TYPESAFE_API_KEY=...' > .env
pnpm dev   # http://127.0.0.1:5173
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese) with screenshots: [github.com/aria467/better-jev-pipeline/blob/334d55aa33f59b70eb882192965cdb79ebe606b7/README.md](https://github.com/aria467/better-jev-pipeline/blob/334d55aa33f59b70eb882192965cdb79ebe606b7/README.md)

## Limits and data handling

Node state is sent to TypeSafe when you run a graph. Custom scenarios are kept in localStorage and lost if site data is cleared. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 334d55aa33f5](https://github.com/aria467/better-jev-pipeline/tree/334d55aa33f59b70eb882192965cdb79ebe606b7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
