# Search Gateway

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Self-hostable gateway and SDK for 13 AI search providers (Exa, Perplexity, Tavily, Brave and more) with Jev-first auto routing that picks the provider and search breadth, falling back to OpenAI Decisions and then rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alvarovillalbaa/search-gateway) |
| Maintainer | [alvarovillalbaa](https://github.com/alvarovillalbaa). Independently curated. |
| Format | TypeScript gateway + TS/Python SDKs, React, CLI and MCP |
| Requirements | Node.js 22+ (Python 3.11+ for the client); provider keys; `TYPESAFE_API_KEY` for Jev routing. |
| License | [MIT](https://github.com/alvarovillalbaa/search-gateway/blob/f891c1378ca20fb90e007d9dc9610aa4740dfc45/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/search-gateway/src/routing.ts`](https://github.com/alvarovillalbaa/search-gateway/blob/f891c1378ca20fb90e007d9dc9610aa4740dfc45/packages/search-gateway/src/routing.ts) at the pinned commit. |

## When to use

- Use several search APIs behind one interface and let a fast model choose per query.
- Give agents one search tool over MCP.
- Mismatch: you still need keys for each search provider you enable.

## How it works

In `auto` mode `routing.ts` sends the query to TypeSafe's `/v1/systemone` with a provider Choice and a breadth Noul. A failed, invalid or low-confidence Jev answer falls back to OpenAI `/v1/decisions`, then built-in capability rules, and choices are validated before dispatch. Integration evidence: [`packages/search-gateway/src/routing.ts`](https://github.com/alvarovillalbaa/search-gateway/blob/f891c1378ca20fb90e007d9dc9610aa4740dfc45/packages/search-gateway/src/routing.ts).

## Get started

From the upstream README: install the release tarball or build from source, set provider keys from `.env.example`, and create a gateway in your backend.

```sh
git clone https://github.com/alvarovillalbaa/search-gateway.git && cd search-gateway
npm ci && npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- PROVIDERS.md (capabilities and sources)
- README routing modes table

## Limits and data handling

Queries go to the routing model and the selected search providers. Release artifacts are on GitHub Releases; registry packages were not verified.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit f891c1378ca2](https://github.com/alvarovillalbaa/search-gateway/tree/f891c1378ca20fb90e007d9dc9610aa4740dfc45). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
