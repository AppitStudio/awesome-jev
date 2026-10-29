# Jev Workspace (give Jev a mission and some links; it judges every item live and hands you a results page)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local app: type a goal, paste links or drop files (sites, sitemaps, feeds, CSV or Google Sheets, PDFs, Instagram exports), let Claude draft a yes/no gate plus breakdown questions, and watch Jev judge every item live with counters, throughput and cost. Matches, rejects and an uncertain band that Claude reviews; filters, CSV/JSON export and an optional Mac app wrapper.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/freakngenius/jev-workspace) |
| Maintainer | [freakngenius](https://github.com/freakngenius). Independently curated. |
| Format | Next.js app (TypeScript) with optional macOS app wrapper |
| Requirements | Node.js 22+ and a TypeSafe or OpenRouter key; optionally an Anthropic key or a logged-in Claude Code for planning and review. |
| License | [MIT](https://github.com/freakngenius/jev-workspace/blob/cedff5611df40f003044dc67f18f52907eaaf721/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev.ts`](https://github.com/freakngenius/jev-workspace/blob/cedff5611df40f003044dc67f18f52907eaaf721/lib/jev.ts) at the pinned commit. |

## When to use

- Sort hundreds of links or rows against one goal quickly, with a reviewable results page.
- Mismatch: runs on your machine only; crawl targets see normal requests.

## How it works

`lib/jev.ts` sends each item with all questions in one call to `https://api.typesafe.ai/v1/systemone` (or OpenRouter's System One endpoint for `sk-or-` keys), `jev-latest` by default, capped at the key's rate limit. Integration evidence: [`lib/jev.ts`](https://github.com/freakngenius/jev-workspace/blob/cedff5611df40f003044dc67f18f52907eaaf721/lib/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/freakngenius/jev-workspace.git && cd jev-workspace
npm install
npm run setup   # saves keys to .env.local
npm run app     # http://127.0.0.1:3131
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/freakngenius/jev-workspace#readme](https://github.com/freakngenius/jev-workspace#readme)

## Limits and data handling

Items go to TypeSafe or OpenRouter, plans and uncertain items to Claude; runs and keys stay in the local folder.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit cedff5611df4](https://github.com/freakngenius/jev-workspace/tree/cedff5611df40f003044dc67f18f52907eaaf721). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
