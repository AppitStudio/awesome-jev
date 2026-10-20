# L Ragebait

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that conservatively hides high-confidence ragebait, hostile threads and sensationalised tragedy commentary on X and YouTube, using three Jev noul scores per item in one request against a threshold you set (default 0.85).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davidherring123/l-ragebait) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/davidherring123/l-ragebait#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source; you pay for your own Jev calls. Checked 2026-10-20. |
| Jev evidence | [`src/classifier/jev-client.ts`](https://github.com/davidherring123/l-ragebait/blob/5aa14d198ae9a965a33aa2d840e2b00f558a1a53/src/classifier/jev-client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [davidherring123](https://github.com/davidherring123). Independently curated. |
| Format | Chrome extension (Manifest V3, WXT; load unpacked) |
| Platform and availability | Chrome or Chromium desktop; build from source and load unpacked. |
| Jev's role | Jev scores each visible item on three yes/no questions; the extension hides items above your threshold. |
| Requirements | Chrome or Chromium, Node.js 22+ and npm to build, and a TypeSafe key entered in the popup. |
| License | [MIT](https://github.com/davidherring123/l-ragebait/blob/5aa14d198ae9a965a33aa2d840e2b00f558a1a53/LICENSE) |

## When to use

- Clean up X timelines, replies and YouTube recommendations without blocking whole accounts.
- Restore recently hidden items in the active tab.
- Mismatch: visible text only; no media or transcripts; no store release yet.

## How it works

The extension watches visible items, and the background worker (`src/classifier/jev-client.ts`) sends their text to `https://api.typesafe.ai/v1/systemone` with `jev-1.13.0`, asking three yes/no questions. Items above the threshold are hidden; failures leave content visible. Scores are cached and in-flight requests deduplicated. Integration evidence: [`src/classifier/jev-client.ts`](https://github.com/davidherring123/l-ragebait/blob/5aa14d198ae9a965a33aa2d840e2b00f558a1a53/src/classifier/jev-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run build
# chrome://extensions > Developer mode > Load unpacked > .output/chrome-mv3
# paste your TypeSafe key in the popup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README quality gates (`npm run check`, Playwright e2e)
- tests/unit/jev-client.test.ts

## Limits and data handling

Visible post and video titles go to TypeSafe. Key kept in chrome.storage.local.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 5aa14d198ae9](https://github.com/davidherring123/l-ragebait/tree/5aa14d198ae9a965a33aa2d840e2b00f558a1a53). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
