# YouTube Sponsor Skip (Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Browser extension for Chrome and Safari that finds spoken sponsor integrations inside Russian-language YouTube videos from subtitles and skips them, using TypeSafe Jev via OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Project README](https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip#readme) |
| Pricing and access | Free MIT source. Requires your own OpenRouter key for `typesafe/jev-1.13` (provider usage billed). Optional daily spend limit in the extension. Checked 2026-10-12. |
| Jev evidence | [`lib/jev.js`](https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip/blob/3bb5ff4eb6b04e3b7973397dd2a8cf14a72cdf86/lib/jev.js) calls Jev on subtitle windows; `tests/jev.test.js` covers it. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Extension not run on the review host. |
| Maintainer | [AnatoliyLikarchuk](https://github.com/AnatoliyLikarchuk). Independently curated. |
| Format | Browser extension (Chrome + Safari) |
| Platform and availability | Chrome; Safari on macOS. Manifest V3. |
| Jev's role | Jev classifies subtitle spans as sponsor vs content; the extension seeks/skips. Without a key it cannot classify. |
| Requirements | Browser; OpenRouter API key configured in extension settings. |
| License | [MIT](https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip/blob/3bb5ff4eb6b04e3b7973397dd2a8cf14a72cdf86/LICENSE) |

## When to use

- Skip mid-roll spoken ads on RU YouTube without crowd-sourced SponsorBlock segments.
- Mismatch: Tuned for Russian sponsorship phrasing; English coverage not claimed.

## How it works

Subtitles are chunked and sent to Jev; probabilities drive seek. Distinct from SponsorBlock community labels.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip.git
# load unpacked / Safari steps per README
```

## Limits and data handling

Subtitle text goes to OpenRouter/TypeSafe; billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 3bb5ff4eb6b0](https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip/tree/3bb5ff4eb6b04e3b7973397dd2a8cf14a72cdf86). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
