# JevPDF

[All projects](../README.md) · [Web apps](README.md#web-apps)

Search a PDF in your own words: TypeSafe Jev asks one yes/no question per line and the matching lines light up on the page, ranked by probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kylemclaren/jevpdf) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Hosted app](https://jevpdf.fly.dev) with a "Try the sample report" button; the project README documents self-hosting. |
| Pricing and access | No account or app fee, checked **2026-09-23**. On that date the hosted app's `/api/jev/config` reported no server-held key, so meaning search there needs your own TypeSafe key (entered in the app, kept in browser storage, and forwarded per request by the app's proxy). Exact-text search needs no key. A self-hosted deployment can set a server key so visitors need none. TypeSafe usage is billed to the key's owner. |
| Jev evidence | [`src/lib/jev.ts`](https://github.com/kylemclaren/jevpdf/blob/7f230370961c4a8e2f8b19c1729085b852124448/src/lib/jev.ts) (batching and requests), [`src/lib/jev-config.ts`](https://github.com/kylemclaren/jevpdf/blob/7f230370961c4a8e2f8b19c1729085b852124448/src/lib/jev-config.ts) (question wording, threshold, batch sizes), and [`server/typesafe-proxy.ts`](https://github.com/kylemclaren/jevpdf/blob/7f230370961c4a8e2f8b19c1729085b852124448/server/typesafe-proxy.ts) (key-holding proxy). |
| Disclosure | Submitted by the author with AI assistance (Claude Code). Not a commercial product. Listing is not an endorsement. |
| Maintainer | [kylemclaren](https://github.com/kylemclaren). Self-submission by the maintainer. |
| Format | Web app: React 19, Vite, Tailwind 4, and pdf.js in the browser, with a small Bun server that serves the build and proxies `/api/jev` to TypeSafe. |
| Platform and availability | Web · [hosted app](https://jevpdf.fly.dev) (HTTP 200 checked) or self-host from source (Dockerfile and `fly.toml` included). Early release. |
| Jev's role | Judges, for each extracted line, whether it answers the query (one Noul per line); the app ranks and highlights by that probability. pdf.js extraction, exact-text matching, caching, and ranking are local code. No other model is used. |
| Requirements | Hosted: a browser and a TypeSafe API key for meaning search. Self-host: Bun and `TYPESAFE_API_KEY` (optional if users bring their own key). |
| License | [MIT](https://github.com/kylemclaren/jevpdf/blob/7f230370961c4a8e2f8b19c1729085b852124448/LICENSE). |

## When to use

Use it to find passages in a report, paper, or contract when you do not know the exact wording, for example asking what drove costs up without guessing the words the report uses. Use the exact-text mode for literal matches. It highlights lines; it does not write answers or summaries.

## How it works

pdf.js extracts each page's text runs and groups them into lines with positions, in the browser ([`src/lib/extract.ts`](https://github.com/kylemclaren/jevpdf/blob/7f230370961c4a8e2f8b19c1729085b852124448/src/lib/extract.ts)). The extraction is cached in IndexedDB by the file's SHA-256. In meaning mode each line gets one Jev Noul, "does this line answer the query?". Up to 16 lines share one request whose state holds the query and the page text as context, and up to 16 requests run at once, so highlights stream in page by page. Lines at or above 0.55 are hits, ranked by probability; if none clears the threshold, the closest lines are shown. Requests back off on 429/529/5xx. Jev receives text only, never PDF bytes. The proxy pins the model, caps request size, accepts only same-origin POSTs, and rate-limits per IP.

## Get started

Open [jevpdf.fly.dev](https://jevpdf.fly.dev), click **Try the sample report** (a fictional four-page annual report), add a TypeSafe key when prompted, and ask one of the suggested questions. To run it yourself:

```sh
git clone https://github.com/kylemclaren/jevpdf.git
cd jevpdf
bun install
cp .env.example .env.local   # add TYPESAFE_API_KEY
bun run dev                  # http://localhost:5173
```

A meaning search sends the page text and the query to TypeSafe and may incur charges. The README estimates that checking every line of a 15-page paper costs well under a cent (author's estimate).

## Examples and demos

- [Hosted app](https://jevpdf.fly.dev) with the bundled sample report.
- Demo video in the upstream README.

## Limits and data handling

PDF bytes stay in the browser; extracted page text and the query go through the app's server proxy to TypeSafe. A key you enter is stored in `localStorage` or `sessionStorage` and sent to the app's server with each request, which forwards it without storing it, per the source. Scanned PDFs without a text layer have nothing to extract. Large documents mean many requests; the concurrency and budgets are set in `src/lib/jev-config.ts`. There is no published accuracy benchmark.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 7f23037](https://github.com/kylemclaren/jevpdf/tree/7f230370961c4a8e2f8b19c1729085b852124448) by the maintainer. In a fresh clone, `bun install && bun run build` (`tsc -b && vite build`) passed; the build makes no TypeSafe calls. The hosted app returned HTTP 200 and its config endpoint was checked. No live TypeSafe searches were run for this review, and it makes no independent quality or accuracy claims.

Related: [Jev Search](jev-search.md), [doc-router](../tools/doc-router.md), [DocJev](../tools/docjev.md).
