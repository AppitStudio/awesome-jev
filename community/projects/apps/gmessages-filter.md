# gmessages-filter (Google Messages Web auto-filter with one-call multi-category Jev classification and KDE alerts)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

WebExtension plus local sync daemon for Google Messages Web: it blocks spam, cleans up messages by age, classifies non-contact messages against all your AI categories in one OpenRouter call to `typesafe/jev-router` with disk caching and per-category age thresholds, and raises KDE Plasma 6 alerts for VIP senders.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/russellmilliner/gmessages-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/russellmilliner/gmessages-filter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (Apache-2.0); you supply an OpenRouter key. Checked 2026-11-01. |
| Jev evidence | [`src/server.py`](https://github.com/russellmilliner/gmessages-filter/blob/9fb42de577b6f9279d0b67c2cf2c2bae11d3ae73/src/server.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [russellmilliner](https://github.com/russellmilliner). Independently curated. |
| Format | Browser extension (MV3) + local Python daemon and CLI |
| Platform and availability | Chromium browser on Linux (KDE Plasma 6 Wayland for alerts). |
| Jev's role | Classifies non-contact messages against your categories in one call. |
| Requirements | Chromium-based browser; Python; an OpenRouter key; KDE Plasma 6 on Wayland for VIP alerts. |
| License | [Apache-2.0](https://github.com/russellmilliner/gmessages-filter/blob/9fb42de577b6f9279d0b67c2cf2c2bae11d3ae73/LICENSE) |

## When to use

- Auto-triage SMS/RCS in Google Messages Web on a Linux desktop.
- Mismatch: built around KDE Plasma; deletion actions are destructive, so review settings.

## How it works

`src/server.py` sends each non-contact message with all active category definitions to OpenRouter with model `typesafe/jev-router` (default set in `extension/background.js`), caches results by SHA-256, and returns per-category verdicts to the extension. Integration evidence: [`src/server.py`](https://github.com/russellmilliner/gmessages-filter/blob/9fb42de577b6f9279d0b67c2cf2c2bae11d3ae73/src/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
# with the extension loaded and the local daemon running (see README):
gmessages-filter ai-add "login codes" --older-than 1d --delete
gmessages-filter ai-test "Your order will be ready at 7:15 PM."
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/russellmilliner/gmessages-filter#readme](https://github.com/russellmilliner/gmessages-filter#readme)

## Limits and data handling

Message text from non-contacts is sent to OpenRouter. The tool can delete messages automatically. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 9fb42de577b6](https://github.com/russellmilliner/gmessages-filter/tree/9fb42de577b6f9279d0b67c2cf2c2bae11d3ae73). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
