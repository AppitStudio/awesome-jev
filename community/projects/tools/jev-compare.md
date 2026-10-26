# jev-compare (Jev image comparison: similarity score, differing regions and fix suggestions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

npm package that compares a candidate image with a reference using Jev and returns a 1–10 similarity score, the differing regions as boxes in both images, and each difference's type, element and fix suggestion in English or Chinese, with optional SVG outlines, saved JSON and HTML reports and request caching; built for design-vs-implementation UI review and visual regression checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sixdjango/jev-compare) |
| Maintainer | [sixdjango](https://github.com/sixdjango). Independently curated. |
| Format | Node.js library (npm `jev-compare`) |
| Requirements | Node.js 22+; a TypeSafe API key in `JEV_KEY` or `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/sixdjango/jev-compare/blob/d7d9bd0c45df711fdb28717813a7e097b1eb5cde/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/compare.ts`](https://github.com/sixdjango/jev-compare/blob/d7d9bd0c45df711fdb28717813a7e097b1eb5cde/src/compare.ts) at the pinned commit. |

## When to use

- Check an implementation screenshot against a design mockup in CI or review.
- Get located, explained differences rather than a pixel diff.
- Mismatch: default locale is Chinese; set `locale: "en"` for English.

## How it works

`src/compare.ts` uses `@typesafe-ai/sdk` to send both images as assets (downscaled to the API's 1568 px limit) with score, box and choice questions, then maps boxes back to original pixels; identical requests are served from cache. Integration evidence: [`src/compare.ts`](https://github.com/sixdjango/jev-compare/blob/d7d9bd0c45df711fdb28717813a7e097b1eb5cde/src/compare.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install jev-compare
export TYPESAFE_API_KEY=...
# compareImages("design.png", "screenshot.png", { locale: "en" })
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- npm: [www.npmjs.com/package/jev-compare](https://www.npmjs.com/package/jev-compare)
- README: [github.com/sixdjango/jev-compare#readme](https://github.com/sixdjango/jev-compare#readme)

## Limits and data handling

Both images go to TypeSafe on cache misses. Reports and the disk cache stay local.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit d7d9bd0c45df](https://github.com/sixdjango/jev-compare/tree/d7d9bd0c45df711fdb28717813a7e097b1eb5cde). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
