# JevSheet: Spreadsheet Enricher

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Handsontable demo that adds a Jev-classified column to a CSV or Excel sheet: describe the column in plain English (yes/no, score or choice), and every row gets an answer plus a confidence you can sort to review only the uncertain rows.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/handsontable-sandbox/jev-sheet) |
| Maintainer | [handsontable-sandbox](https://github.com/handsontable-sandbox). Independently curated. |
| Format | Web app (Vite) + Cloudflare Worker |
| Requirements | Node 22; a Jev API key; a Cloudflare account to deploy your own copy. |
| License | [MIT](https://github.com/handsontable-sandbox/jev-sheet/blob/6062486a5ae81c010124be14e4d8273df67dc087/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/worker.js`](https://github.com/handsontable-sandbox/jev-sheet/blob/6062486a5ae81c010124be14e4d8273df67dc087/src/worker.js) at the pinned commit. |

## When to use

- Triage product reviews, tickets or survey answers in a spreadsheet and check only low-confidence rows.
- Try it free in the hosted demo (up to 50 rows per column) before running your own copy.
- Mismatch: a demo/recipe from Handsontable; the hosted demo caps rows and rate-limits requests.

## How it works

The browser sends one request per row (eight at a time) to the Worker's `POST /api/classify`, which validates sizes and asks `https://api.typesafe.ai/v1/systemone` (`jev-latest`) one question, returning `{ value, confidence }`; the key is a Worker secret and hidden columns never leave the browser. Integration evidence: [`src/worker.js`](https://github.com/handsontable-sandbox/jev-sheet/blob/6062486a5ae81c010124be14e4d8273df67dc087/src/worker.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/handsontable-sandbox/jev-sheet.git && cd jev-sheet
cp .env.example .env   # JEV_API_KEY=...
npx wrangler dev --port 8787 --var ALLOWED_ORIGINS:http://localhost:8080
npm --prefix demo ci && npm --prefix demo run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [demos.handsontable.com/d/2g6f4hc3b2/](https://demos.handsontable.com/d/2g6f4hc3b2/)
- Step-by-step recipe: [handsontable.com/docs/javascript-data-grid/recipes/real-time/ai-columns-jev/](https://handsontable.com/docs/javascript-data-grid/recipes/real-time/ai-columns-jev/)

## Limits and data handling

Visible cell text for the classified column goes to TypeSafe; nothing is logged or stored by the Worker.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 6062486a5ae8](https://github.com/handsontable-sandbox/jev-sheet/tree/6062486a5ae81c010124be14e4d8273df67dc087). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
