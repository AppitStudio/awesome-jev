# seo-jev-analyzer

[All projects](../README.md) · [Web apps](README.md#web-apps)

Measures how closely each page matches the search intent you set, using TypeSafe Jev with a calibrated noise band.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/matthelam/seo-jev-analyzer) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/matthelam/seo-jev-analyzer#readme](https://github.com/matthelam/seo-jev-analyzer#readme) |
| Pricing and access | Free MIT source; Jev calls use your TypeSafe key. Checked 2026-10-13. |
| Jev evidence | [`src/lib/server/jev.ts`](https://github.com/matthelam/seo-jev-analyzer/blob/00c6e7fae66b6bc531d6d5e6099d4e789dd4f499/src/lib/server/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [matthelam](https://github.com/matthelam). Independently curated. |
| Format | Web app (Next.js / TypeScript) |
| Platform and availability | Self-hosted web |
| Jev's role | Jev scores page content against declared search intent. |
| Requirements | Node; TypeSafe API key. |
| License | [MIT](https://github.com/matthelam/seo-jev-analyzer/blob/00c6e7fae66b6bc531d6d5e6099d4e789dd4f499/LICENSE) |

## When to use

- Audit whether pages still match the intent you assigned them.
- Mismatch: Self-hosted; not a hosted SaaS SEO product.

## How it works

Pages and intent text are sent to Jev; scores (with a noise band) drive the UI. (Summarized from the upstream [README](https://github.com/matthelam/seo-jev-analyzer/blob/00c6e7fae66b6bc531d6d5e6099d4e789dd4f499/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install deps, set `TYPESAFE_API_KEY`, and run the Next.js app.

## Limits and data handling

Page text and intents go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 00c6e7fae66b](https://github.com/matthelam/seo-jev-analyzer/tree/00c6e7fae66b6bc531d6d5e6099d4e789dd4f499). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
