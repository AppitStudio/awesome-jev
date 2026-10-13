# Stillwatch

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Notification guardian that saves every notification locally and, in AI mode, uses TypeSafe Jev (via NanoGPT's Decisions API) to decide what needs you now with persistent modals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/difflabai/stillwatch) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/difflabai/stillwatch#readme](https://github.com/difflabai/stillwatch#readme) |
| Pricing and access | Free MIT source; AI mode bills NanoGPT/TypeSafe usage to your key. |
| Jev evidence | [`src/stillwatch/decision.py`](https://github.com/difflabai/stillwatch/blob/73e796a2620c34c76d8eb479d91f32c32d0e216c/src/stillwatch/decision.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [difflabai](https://github.com/difflabai). Independently curated. |
| Format | Linux desktop app (Python) |
| Platform and availability | Linux desktop (Python, GTK 4/libadwaita) · Android companion (early alpha) |
| Jev's role | Typed Jev choices classify each new notification's importance and severity; code handles cooldowns, history and cross-device sync. |
| Requirements | Linux with GTK 4, libadwaita, D-Bus; Python 3.10+; NanoGPT API key for AI mode. |
| License | [MIT](https://github.com/difflabai/stillwatch/blob/73e796a2620c34c76d8eb479d91f32c32d0e216c/LICENSE) |

## When to use

- Stay heads-down while urgent incidents still break through.
- Mismatch: Calls Jev through NanoGPT rather than TypeSafe directly.

## How it works

Notifications are stored with seven-day history; in AI mode each new one goes to the pinned `typesafe/jev-1.13` model for importance; severe items raise red modals with per-issue cooldown. (Summarized from the upstream [README](https://github.com/difflabai/stillwatch/blob/73e796a2620c34c76d8eb479d91f32c32d0e216c/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install per the README and enable AI mode with your NanoGPT key.

## Limits and data handling

App name, title and up to 3,000 body characters per new notification go to NanoGPT. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 73e796a2620c](https://github.com/difflabai/stillwatch/tree/73e796a2620c34c76d8eb479d91f32c32d0e216c). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
