# article-quality-gate (build-blocking quality gate for articles with deterministic checks and a Jev judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Quality gate for a site's articles: deterministic structural checks plus a 12-question judge, a hash ledger that forces re-scoring after edits, calibration against golden samples, and a build step that blocks publishing below the bar. The judge can be a mock or Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/s0yabean/article-quality-gate) |
| Maintainer | [s0yabean](https://github.com/s0yabean). Independently curated. |
| Format | Node.js CLI (TypeScript) |
| Requirements | Node.js; a TypeSafe or Vercel AI Gateway key for `JUDGE=jev`. |
| License | [MIT](https://github.com/s0yabean/article-quality-gate/blob/19d57363ead2f827d98d34380ba3818a6fade02e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judges/jev.ts`](https://github.com/s0yabean/article-quality-gate/blob/19d57363ead2f827d98d34380ba3818a6fade02e/src/judges/jev.ts) at the pinned commit. |

## When to use

- Stop low-quality or edited-but-unscored articles from shipping in a static site build.
- Mismatch: rubric is tuned to the author's site; recalibrate for yours.

## How it works

`src/judges/jev.ts` uses `@typesafe-ai/sdk` (`noul`, `score`) to ask all rubric questions in one request, pinned to `jev-1.13.0` with a direct key or via Vercel AI Gateway; answers are cached by text and rubric hash. Integration evidence: [`src/judges/jev.ts`](https://github.com/s0yabean/article-quality-gate/blob/19d57363ead2f827d98d34380ba3818a6fade02e/src/judges/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run quickstart   # mock judge
cp .env.example .env   # JUDGE=jev, TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/s0yabean/article-quality-gate#readme](https://github.com/s0yabean/article-quality-gate#readme)

## Limits and data handling

Article text is sent to TypeSafe when `JUDGE=jev`. Reported numbers are from the author's site. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 19d57363ead2](https://github.com/s0yabean/article-quality-gate/tree/19d57363ead2f827d98d34380ba3818a6fade02e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
