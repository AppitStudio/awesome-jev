# jev-scout by Kieran (MCP research tools where Jev scores every query, result and fetched page, with a live dashboard)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

An MCP stdio server exposing `guarded_search`, `guarded_fetch` and `research_report`: one Jev call per search result (relevance, credibility, worth fetching) and one per fetched page (answered, content class, steering risk), every decision written to a JSONL ledger and streamed to a local dashboard, with budgets and optional gating.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kierandotai/jev-scout) |
| Maintainer | [kierandotai](https://github.com/kierandotai). Independently curated. |
| Format | TypeScript MCP server |
| Requirements | Node.js, the sibling `jev-client` library (cloned by the install script), a search backend (SearXNG by default), and an OpenRouter or TypeSafe key. |
| License | no license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judge.ts`](https://github.com/kierandotai/jev-scout/blob/99b530214215b7b597f6e8a56418bfd58f012b95/src/judge.ts) at the pinned commit. |

## When to use

- See (and optionally gate) which sources an agent trusts during web research, with a cheap Jev judgment on every step.
- Mismatch: a research agent that writes reports for you; jev-scout is a thin decision layer.

## How it works

`src/judge.ts` is the small `Judge` interface over `kierandotai/jev-client`, which handles the OpenRouter/TypeSafe provider wiring; `src/pipeline.ts` asks Jev about each result and fetched page, and `src/ledger.ts` and `src/dashboard.ts` record and stream the decisions. It annotates or gates what the agent sees and does not plan or write answers. Integration evidence: [`src/judge.ts`](https://github.com/kierandotai/jev-scout/blob/99b530214215b7b597f6e8a56418bfd58f012b95/src/judge.ts).

## Get started

Start SearXNG with JSON output enabled, then run the install script (or the manual steps) and add your key.

```sh
git clone https://github.com/kierandotai/jev-client.git
git clone https://github.com/kierandotai/jev-scout.git
cd jev-client && npm install && npm run build && cd ../jev-scout
npm install
# then follow scripts/install.sh to register the MCP server and create .env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kierandotai/jev-scout/blob/99b530214215b7b597f6e8a56418bfd58f012b95/README.md](https://github.com/kierandotai/jev-scout/blob/99b530214215b7b597f6e8a56418bfd58f012b95/README.md)
- jev-client library: [github.com/kierandotai/jev-client](https://github.com/kierandotai/jev-client)

## Limits and data handling

Search results and fetched page text are sent to the Jev provider, one call per result and page. Depends on an unpinned sibling library. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 99b530214215](https://github.com/kierandotai/jev-scout/tree/99b530214215b7b597f6e8a56418bfd58f012b95). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
