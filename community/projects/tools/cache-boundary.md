# cache-boundary by Hamza Ahmad Aslam (CLI that decides route by route whether a page cache may share a page, with Jev for what code cannot judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI for WordPress, WooCommerce and other sites behind a full-page cache: it fetches each route as an anonymous visitor (or reads saved responses), blocks in code on session cookies, private cache headers and WordPress/WooCommerce markers, and asks Jev only what code cannot judge, such as whether "Welcome back, Robin" belongs to one visitor. Unsure routes go to a review list instead of into a cache rule.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/cache-boundary) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam) (hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (`@hamzaahmadaslam/cache-boundary`, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (`--dry-run` runs the code checks only). |
| License | [MIT](https://github.com/hamzaahmadaslam/cache-boundary/blob/6a434dfead62d9a8f43b377ddb84c8e16ffc54a0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/cache-boundary/blob/6a434dfead62d9a8f43b377ddb84c8e16ffc54a0/src/jev.mjs) at the pinned commit. |

## When to use

- Site owners and agencies setting page-cache exclusions for WordPress or WooCommerce sites.
- Mismatch: logged-in or personalised caching strategies beyond share / do not share.

## How it works

`src/jev.mjs` posts page excerpts and questions to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`, override with `TYPESAFE_MODEL`); answers below the `--threshold` confidence (0.8 by default) are not acted on. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/cache-boundary/blob/6a434dfead62d9a8f43b377ddb84c8e16ffc54a0/src/jev.mjs).

## Get started

Install from npm and check a few routes.

```sh
npm install -g @hamzaahmadaslam/cache-boundary
export TYPESAFE_API_KEY=...
cache-boundary https://example.com/ https://example.com/shop/ https://example.com/cart/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Dry-run sample: [github.com/hamzaahmadaslam/cache-boundary/blob/main/examples/dry-run.txt](https://github.com/hamzaahmadaslam/cache-boundary/blob/main/examples/dry-run.txt)
- Example script: [github.com/hamzaahmadaslam/cache-boundary/blob/main/examples/run.mjs](https://github.com/hamzaahmadaslam/cache-boundary/blob/main/examples/run.mjs)

## Limits and data handling

Routes blocked in code send nothing to TypeSafe; for the rest, page excerpts are sent (see the README's "What leaves your machine"). Fetch only sites you are allowed to test.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 6a434dfead62](https://github.com/hamzaahmadaslam/cache-boundary/tree/6a434dfead62d9a8f43b377ddb84c8e16ffc54a0). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit and confirmed version 1.0.0 on npm; nothing was installed or run on the review host. Carried over from the 2026-11-28 00:36 run. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
