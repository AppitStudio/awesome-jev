# Qiaomu Banbot (乔木净评)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension preview that uses TypeSafe Jev (or Magpie / OpenRouter / Vercel gateways) to fold suspected AI, low-signal, and promo replies on X, with optional natural-language rules and hot-post probability estimates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/joeseesun/qiaomu-ban-bot) |
| Tags | `Free` · `Source available` · `BYOK` |
| Product homepage | [Repository README](https://github.com/joeseesun/qiaomu-ban-bot#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source / preview build; you supply your own provider key and pay that provider. |
| Jev evidence | [`src/connection.js`](https://github.com/joeseesun/qiaomu-ban-bot/blob/642a0da7d900c143ba0fe28d1fca5dbb9a6c712a/src/connection.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [joeseesun](https://github.com/joeseesun). Independently curated. |
| Format | Chrome extension (MV3) preview build |
| Platform and availability | Chrome / Chromium (preview release; not yet on the Chrome Web Store). |
| Jev's role | Jev scores each reply (and optional hot-post questions) over the System One or Decisions wire format; the extension folds or marks based on thresholds you set. |
| Requirements | Chromium browser; a Jev-capable API key (TypeSafe, Magpie, OpenRouter, or Vercel AI Gateway). |
| License | [MIT](https://github.com/joeseesun/qiaomu-ban-bot/blob/642a0da7d900c143ba0fe28d1fca5dbb9a6c712a/LICENSE) |

## When to use

- Want typed Jev judgments to quiet AI-spam reply threads on X.
- Prefer fold-with-expand over hard deletes, with BYOK providers.
- Mismatch: preview (v0.1.x); full Chrome Web Store flow still pending per README.

## How it works

`src/connection.js` defines providers including TypeSafe (`https://api.typesafe.ai/v1` → `/systemone`). `src/jev.js` POSTs state/questions and parses typed answers for fold/mark UI. Integration evidence: [`src/connection.js`](https://github.com/joeseesun/qiaomu-ban-bot/blob/642a0da7d900c143ba0fe28d1fca5dbb9a6c712a/src/connection.js).

## Get started

Install a preview release from GitHub Releases, open settings, connect a provider key, then browse X.

```sh
# Download a preview .zip from https://github.com/joeseesun/qiaomu-ban-bot/releases
# Load unpacked in chrome://extensions (Developer mode)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README UI screenshots and QA notes
- GitHub Releases v0.1.3 preview

## Limits and data handling

Preview quality; reply text is sent to the chosen provider. Not affiliated with X/Twitter.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 642a0da7d900](https://github.com/joeseesun/qiaomu-ban-bot/tree/642a0da7d900c143ba0fe28d1fca5dbb9a6c712a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
