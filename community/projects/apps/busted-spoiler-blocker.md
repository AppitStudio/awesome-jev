# Busted! (browser extension that blurs GTA VI spoilers on YouTube, X and Reddit, judged by Cloudflare Clef or Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Browser extension that asks a yes/no decision model whether each video, post or link preview spoils GTA VI and hides the ones that do behind a blurred "BUSTED!" stamp you can click through; Cloudflare Clef on your own account is the default, and TypeSafe Jev is a built-in alternative.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/canvural/busted) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://chromewebstore.google.com/detail/busted-%E2%80%94-spoiler-blocker/eggbgmgafnkeckpopfcmnnopcjgnbnfb) |
| Pricing and access | Free extension on the Chrome Web Store and Firefox Add-ons; Cloudflare Clef runs on your own (free-for-normal-use) account, TypeSafe mode is pay per use on your key. Checked 2026-11-13. |
| Jev evidence | [`src/lib/jev.ts`](https://github.com/canvural/busted/blob/69fc518c3568092965b42b7d52ffaceb979cac66/src/lib/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/can__vural/status/2121168276814237778)). |
| Maintainer | [canvural](https://github.com/canvural). Independently curated. |
| Format | Chrome/Edge/Firefox extension built with WXT (TypeScript, MIT) |
| Platform and availability | Desktop Chrome, Chromium and Edge (Chrome Web Store) and Firefox 142+ (Firefox Add-ons); store listings checked 2026-11-13 |
| Jev's role | Optional: in TypeSafe mode, Jev answers whether each item spoils GTA VI; the default judge is Cloudflare Clef. |
| Requirements | Desktop Chrome, Chromium, Edge or Firefox 142+, Node.js to build, and either a Cloudflare API token or your own TypeSafe key. |
| License | [MIT](https://github.com/canvural/busted/blob/69fc518c3568092965b42b7d52ffaceb979cac66/LICENSE) |

## When to use

- Avoid GTA VI spoilers on YouTube, X and Reddit without muting every post that mentions the game.
- Mismatch: spoilers for other games or shows; the questions are written for GTA VI.

## How it works

In TypeSafe mode, `src/lib/jev.ts` sends batched `noul` questions to `https://api.typesafe.ai/v1/systemone` with the pinned model `jev-1.14.0` (the author pins a version because `jev-latest` moves with releases). Only text is sent to Jev; thumbnails and X images are skipped because Jev rejects images under 280 pixels. The optional Cloudflare Worker proxy in `worker/` is only for sharing a Clef quota and is deployed to your own account. Integration evidence: [`src/lib/jev.ts`](https://github.com/canvural/busted/blob/69fc518c3568092965b42b7d52ffaceb979cac66/src/lib/jev.ts).

## Get started

Install from the Chrome Web Store or Firefox Add-ons (or build from source), then in settings choose **TypeSafe Jev**, paste your key and click **Test connection**.

```sh
# Chrome/Edge: https://chromewebstore.google.com/detail/eggbgmgafnkeckpopfcmnnopcjgnbnfb
# Firefox:     https://addons.mozilla.org/addon/busted-spoiler-blocker-gta-vi/
# Settings → TypeSafe Jev → paste key → Test connection
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/canvural/busted/blob/69fc518c3568092965b42b7d52ffaceb979cac66/README.md](https://github.com/canvural/busted/blob/69fc518c3568092965b42b7d52ffaceb979cac66/README.md)
- Privacy notes: [github.com/canvural/busted/blob/69fc518c3568092965b42b7d52ffaceb979cac66/PRIVACY.md](https://github.com/canvural/busted/blob/69fc518c3568092965b42b7d52ffaceb979cac66/PRIVACY.md)

## Limits and data handling

Titles and post text from pages you browse go to Cloudflare or TypeSafe on your own account; there is no Busted! server. TypeSafe has no free allowance (the README estimates about 150,000 checks per dollar).

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 69fc518c3568](https://github.com/canvural/busted/tree/69fc518c3568092965b42b7d52ffaceb979cac66). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
