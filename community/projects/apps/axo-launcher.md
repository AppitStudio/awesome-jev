# axo-launcher

[All projects](../README.md) · [Android apps](README.md#android-apps)

Minimalist Android launcher (Portuguese docs): text-only home, grayscale screen and delays for distracting apps; quick-capture phrases are classified offline, with TypeSafe Jev deciding the ambiguous ones.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/axolutions/axo-launcher) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/axolutions/axo-launcher#readme](https://github.com/axolutions/axo-launcher#readme) |
| Pricing and access | Free MIT source; optional OpenRouter key for Jev (reported ~US$0.000018 per phrase). |
| Jev evidence | [`src/com/axolutions/launcher/Jev.java`](https://github.com/axolutions/axo-launcher/blob/e6f78038521ebc35c25c2b2547930342b7e8bff3/src/com/axolutions/launcher/Jev.java) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [axolutions](https://github.com/axolutions). Independently curated. |
| Format | Android app (Java) |
| Platform and availability | Android 8+ (build from source; tuned for Xiaomi HyperOS) |
| Jev's role | When the offline keyword classifier is unsure what kind of item a phrase is, Jev (`typesafe/jev-1.13` via OpenRouter) chooses among the offered types; cached, capped at 300 calls/day. |
| Requirements | Android build toolchain; optional OpenRouter key in `secrets.properties`. |
| License | [MIT](https://github.com/axolutions/axo-launcher/blob/e6f78038521ebc35c25c2b2547930342b7e8bff3/LICENSE) |

## When to use

- Reduce phone distraction while capturing reminders and appointments by typing a phrase.
- Mismatch: Jev is optional; some features target Xiaomi behavior.

## How it works

Each keystroke runs an offline classifier; on doubt, one Jev choice picks the item type; time, date, amount and person are extracted locally. (Summarized from the upstream [README](https://github.com/axolutions/axo-launcher/blob/e6f78038521ebc35c25c2b2547930342b7e8bff3/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): copy `secrets.properties.example`, optionally add the key, and build/install the APK.

## Limits and data handling

Only the ambiguous phrase is sent to Jev via OpenRouter. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit e6f78038521e](https://github.com/axolutions/axo-launcher/tree/e6f78038521ebc35c25c2b2547930342b7e8bff3). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
