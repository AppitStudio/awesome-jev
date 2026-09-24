# Find the Right API (Orthogonal × Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted discovery UI where you describe a goal in natural language; product copy states that **Jev** searches about 1,000 [Orthogonal](https://orthogonal.com) API endpoints and returns priced matches with `curl` snippets to run via Orthogonal.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://www.findtherightapi.com/) |
| Tags | `Closed source` · `Freemium` · `Commercial` |
| Product homepage | [findtherightapi.com](https://www.findtherightapi.com/) (branded Orthogonal × Jev) |
| Pricing and access | Natural-language search on the public site needed no signup during review. Running a matched endpoint uses Orthogonal’s pay-per-call gateway; [Orthogonal pricing](https://docs.orthogonal.com/concepts/pricing) documents per-call prices in the catalog/search results, prepaid credits, and **$5 free credits** for new accounts (no card required for that trial credit). Checked **2026-09-24**. Exact findtherightapi.com rate limits and any future signup walls were not exhaustively verified. |
| Jev evidence | Live homepage copy: “Jev searches about 1,000 Orthogonal endpoints to find the right fit.” Title: “Find the right APIs \| Jev x Orthogonal.” Launch demo on X ([@chrisspickett](https://x.com/chrisspickett/status/2102855582969725198), 2026-09-23) shows the same Orthogonal × Jev UI with “JEV MATCH” cards and Orthogonal `POST https://api.orthogonal.com/v1/run` snippets. Implementation was **not** inspected (no public app source); TypeSafe API traffic was **not** captured on the review host. |
| Disclosure | Closed source. The findtherightapi.com implementation was not inspected; Jev use is a vendor/product claim from the live site and the linked X launch post, not independently observed System One API calls. Commercial Freemium access: natural-language search was free without signup during review; executing matched endpoints is Orthogonal pay-per-call (see pricing docs; new accounts get trial credits). Orthogonal’s open SDKs/CLI are separate MIT-licensed clients for the gateway, not the Jev search UI. Independently curated for Awesome Jev; no affiliation with Orthogonal. Listing is not an endorsement or purchase recommendation. |
| Maintainer | Orthogonal ([orthogonal.com](https://orthogonal.com)); launch attributed to [Christian Pickett (@chrisspickett)](https://x.com/chrisspickett) (building [@orthogonal_sh](https://x.com/orthogonal_sh)). |
| Format | Hosted web application (Vercel). |
| Platform and availability | Public web app at [www.findtherightapi.com](https://www.findtherightapi.com/) (HTTP 200 on review). Related Orthogonal surfaces: [orthogonal.com](https://orthogonal.com), [docs](https://docs.orthogonal.com), [MCP](https://mcp.orthogonal.com), catalog browse via site “Browse all APIs” → Orthogonal discover. |
| Jev's role | Vendor/product claim: Jev ranks/selects which Orthogonal catalog endpoints fit a natural-language goal; the UI compares prices and shows run snippets. Orthogonal executes calls after you use an Orthogonal API key. Whether every search path always calls TypeSafe Jev (vs other rankers) was not verified. |
| Requirements | Modern browser. Optional Orthogonal account/`ORTHOGONAL_API_KEY` to execute endpoints (not required only to view the public search UI as reviewed). |
| License | Proprietary hosted product. Orthogonal TypeScript SDK and CLI are MIT ([orthogonal-sh/typescript](https://github.com/orthogonal-sh/typescript) @ `7da7967bf7b6a3c0cd5aa96c20a9907f7da8b8e1`, [orthogonal-sh/cli](https://github.com/orthogonal-sh/cli) @ `1734dfdaa60436fd9e61b5d9d8acd87ad4cdfe72` on review) but do not cover this UI. |

## When to use

Use Find the Right API when you want a Jev-branded natural-language front door into Orthogonal’s multi-provider API catalog (enrichment, search, scrape, media, and similar) with prices and copy-paste `curl` against `api.orthogonal.com`. Prefer Orthogonal’s own docs/CLI/MCP when you already know the slug/path, or open-source Jev examples when you need inspectable System One integration code.

## How it works

Vendor materials describe this loop:

1. Enter a goal (for example “find creators for my product” or “scrape Instagram”).
2. The UI presents matched providers/endpoints (demo cards labeled “JEV MATCH”) with path and price.
3. “Access via Orthogonal” / run snippets call `POST https://api.orthogonal.com/v1/run` with an Orthogonal API key.

This catalogue entry does not claim to have inspected TypeSafe question schemas, confidence thresholds, or backend routing.

## Get started

Reviewed path (search UI only; no Orthogonal signup or paid call was completed by the curator):

1. Open [https://www.findtherightapi.com/](https://www.findtherightapi.com/).
2. Describe a goal in the search field and submit.
3. Compare matched endpoints and prices; use an Orthogonal key only if you choose to run a call (see [Orthogonal quickstart](https://docs.orthogonal.com/quickstart)).

Live Orthogonal execution can spend credits or crypto per call; review prices before running.

## Examples and demos

- Live product: [findtherightapi.com](https://www.findtherightapi.com/)
- Launch post + demo video: [x.com/chrisspickett/status/2102855582969725198](https://x.com/chrisspickett/status/2102855582969725198)
- Orthogonal docs / MCP / CLI: [docs.orthogonal.com](https://docs.orthogonal.com/), [skill.md](https://orthogonal.com/skill.md)

## Limits and data handling

Closed source: prompts, Jev questions, logging, and retention for findtherightapi.com were not inspected. Assume goal text and selections may be processed by Orthogonal (and any AI providers they use). Orthogonal API calls send request parameters to Orthogonal and upstream providers under Orthogonal’s terms. No public LICENSE for the discovery UI.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia). Primary sources: live site title/subhead (HTTP 200), X launch [2102855582969725198](https://x.com/chrisspickett/status/2102855582969725198) (demo frames: Orthogonal × Jev branding, JEV MATCH cards, `api.orthogonal.com` curl), Orthogonal pricing docs, MIT SDK/CLI repos pinned above. AI-assisted curation; no TypeSafe or Orthogonal live keys used for end-to-end search/run by the curator. De-dupe: no existing Awesome Jev listing for findtherightapi, Orthogonal × Jev, or orthogonal.com as a Jev app.

**X attribution:** `https://x.com/chrisspickett/status/2102855582969725198`
