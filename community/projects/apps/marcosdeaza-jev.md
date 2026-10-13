# JEV (marcosdeaza)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS voice-control exploration: TypeSafe Jev decides intent and target while an Anthropic planner runs continuous sessions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marcosdeaza/JEV) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/marcosdeaza/JEV#readme) (source-built; no separate commercial homepage verified). |
| Pricing and access | Free source build; uses your own TypeSafe (or documented provider) key. Checked 2026-10-14. |
| Jev evidence | [`Sources/JevCore/Decision.swift`](https://github.com/marcosdeaza/JEV/blob/6131e5a45829eeb6f690adb4cfaa391bafa2986b/Sources/JevCore/Decision.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [marcosdeaza](https://github.com/marcosdeaza). Independently curated. |
| Format | macOS app (Swift) |
| Platform and availability | macOS (source build) |
| Jev's role | Jev classifies voice intents and targets for desktop actions. |
| Requirements | macOS; TypeSafe API key; Anthropic for planning. |
| License | [MIT](https://github.com/marcosdeaza/JEV/blob/6131e5a45829eeb6f690adb4cfaa391bafa2986b/LICENSE) |

## When to use

- Use when you need: macOS voice-control exploration: TypeSafe Jev decides intent and target while an…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `Sources/JevCore/Decision.swift`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: Sources/JevCore/Decision.swift.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 6131e5a45829](https://github.com/marcosdeaza/JEV/tree/6131e5a45829eeb6f690adb4cfaa391bafa2986b). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
