# jev · youtube by Luca Baeyens (filters your YouTube home feed by sending titles and thumbnails to Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

A Chrome/Safari extension that sends the title, channel and thumbnail of each long video in your YouTube home feed to Jev and hides whatever scores below your threshold; shorts, lives and similar cards are hidden without a call, and decisions are cached, capped per load and logged so you can mark them right or wrong.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lucabae/jev-youtube) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/lucabae/jev-youtube#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source, loaded unpacked; Jev calls are billed to your own OpenRouter key, with a per-load cap and an hourly call limit. Checked 2026-11-21. |
| Jev evidence | [`src/background.js`](https://github.com/lucabae/jev-youtube/blob/20c1a119cbc466a716f414fa4ed87dd542846ddf/src/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [lucabae](https://github.com/lucabae). Independently curated. |
| Format | Browser extension (no build step) |
| Platform and availability | Chrome or Safari (Manifest V3), loaded unpacked. UI in Spanish; code and docs in English. |
| Jev's role | Scores each home-feed video against your stated taste from its title and thumbnail; the score is compared with your threshold. |
| Requirements | An OpenRouter API key with access to `typesafe/jev-1.14`. |
| License | [MIT](https://github.com/lucabae/jev-youtube/blob/20c1a119cbc466a716f414fa4ed87dd542846ddf/LICENSE) |

## When to use

- Cut low-value videos out of your YouTube home feed by describing your taste once.
- Mismatch: search results or watch pages; it only filters the home feed.

## How it works

`src/background.js` calls OpenRouter's Decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with `typesafe/jev-1.14` for each card, caches each video's decision, and enforces `maxPerLoad` (20 by default) and an hourly limit; a separate OpenRouter chat-completions call rewrites your taste description from the decisions you mark right or wrong. Integration evidence: [`src/background.js`](https://github.com/lucabae/jev-youtube/blob/20c1a119cbc466a716f414fa4ed87dd542846ddf/src/background.js).

## Get started

Load the extension unpacked and paste your OpenRouter key in its settings.

```sh
git clone https://github.com/lucabae/jev-youtube
# chrome://extensions -> Developer mode -> Load unpacked -> select the folder
# open the extension settings and add your OpenRouter key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lucabae/jev-youtube/blob/20c1a119cbc466a716f414fa4ed87dd542846ddf/README.md](https://github.com/lucabae/jev-youtube/blob/20c1a119cbc466a716f414fa4ed87dd542846ddf/README.md)

## Limits and data handling

Video titles, channel names and thumbnails from your feed are sent to OpenRouter/TypeSafe, with per-call cost (capped); the taste-refinement feature also sends your marked decisions to an OpenRouter chat model. Unfiltered cards past the cap are hidden rather than shown.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 20c1a119cbc4](https://github.com/lucabae/jev-youtube/tree/20c1a119cbc466a716f414fa4ed87dd542846ddf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
