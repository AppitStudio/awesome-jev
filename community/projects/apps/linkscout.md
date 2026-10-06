# LinkScout

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Browser extension plus your own Cloudflare Worker that scores Google, Bing and DuckDuckGo results before you click: pages are fetched as Markdown and TypeSafe Jev judges relevance, depth, SEO spam and category and picks a key passage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ianTPE/linkscout) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ianTPE/linkscout#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the source build. You deploy the Worker on your Cloudflare account (Browser Rendering), and bring `TYPESAFE_API_KEY` and optionally a Jina key; each provider bills separately. Checked 2026-10-07. |
| Jev evidence | Inspected [`worker/src/judge.ts`](https://github.com/ianTPE/linkscout/blob/02482b409e353a74e65a7dba696291579f7ec896/worker/src/judge.ts), which calls `client.systemOne` from `@typesafe-ai/sdk` with choice, noul and score questions per page. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [ianTPE](https://github.com/ianTPE). Independently curated. |
| Format | MV3 browser extension (plain JS) + Cloudflare Worker (TypeScript) |
| Platform and availability | Chromium browsers (load unpacked) with a self-deployed Cloudflare Worker; early open-source project. |
| Jev's role | Per (query, URL) pair the Worker fetches the page (Cloudflare Browser Run, Jina Reader fallback) and asks Jev for relevance, depth, SEO-spam and category judgments plus a key passage; the extension badges, reorders and ranks results. Results are cached 24 h. |
| Requirements | Cloudflare account with Browser Rendering (`CF_ACCOUNT_ID`, `CF_API_TOKEN`), `TYPESAFE_API_KEY`, optional `JINA_API_KEY`, and a random `LINKSCOUT_TOKEN` for production. |
| License | [MIT](https://github.com/ianTPE/linkscout/blob/02482b409e353a74e65a7dba696291579f7ec896/LICENSE). |

## When to use

- Skip SEO spam and thin pages on search results with a relevance score and key passage per link.
- Self-host a page-judging endpoint (`POST /score { query, urls[] }`) for other tools.
- Mismatch: requires deploying and securing your own Worker; visited URLs and page text go to Cloudflare and TypeSafe.

## How it works

The extension watches result pages and posts query + URLs to the Worker ([`worker/src/index.ts`](https://github.com/ianTPE/linkscout/blob/02482b409e353a74e65a7dba696291579f7ec896/worker/src/index.ts)); [`fetchPage.ts`](https://github.com/ianTPE/linkscout/blob/02482b409e353a74e65a7dba696291579f7ec896/worker/src/fetchPage.ts) renders Markdown and [`judge.ts`](https://github.com/ianTPE/linkscout/blob/02482b409e353a74e65a7dba696291579f7ec896/worker/src/judge.ts) asks Jev typed questions about the page against the query.

## Get started

Run the Worker locally, then load the extension:

```sh
git clone https://github.com/ianTPE/linkscout.git && cd linkscout
npm install
# root .env: CF_ACCOUNT_ID, CF_API_TOKEN, TYPESAFE_API_KEY (optional JINA_API_KEY)
npm run dev   # Worker on http://localhost:8787
# chrome://extensions → Developer mode → Load unpacked → extension/
```

Each scored link uses Cloudflare Browser Run and a Jev request billed to your accounts (cached 24 h).

## Examples and demos

- README screenshot and `curl` test of `POST /score`.
- `worker/scripts/compare.ts` and `timing.ts` for local comparisons.

## Limits and data handling

The production token is the only protection on the public Worker URL (upstream warning). Page content and queries go to Cloudflare and TypeSafe (and Jina on fallback). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 02482b409e35](https://github.com/ianTPE/linkscout/tree/02482b409e353a74e65a7dba696291579f7ec896). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
