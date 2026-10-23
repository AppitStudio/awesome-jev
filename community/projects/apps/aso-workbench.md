# ASO Workbench (App Store Optimization on your Mac, with Jev keyword clues)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Mac app for App Store Optimization that tracks keyword ranks per country, estimates popularity and difficulty with labelled sources, writes and publishes store listings in every language, and measures what each change did; Jev answers narrow keyword questions that feed its popularity estimate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mustafakendiguzel/aso-workbench) |
| Tags | `Source available` · `Free` |
| Product homepage | [Repository README](https://github.com/mustafakendiguzel/aso-workbench#readme) (source-built; no separate product site verified). |
| Pricing and access | Free download (MIT with Commons Clause: free to use, including for your own apps, but not to sell). OpenRouter usage for Jev and the AI writer is pay per use on your key. Checked 2026-10-23. |
| Jev evidence | [`Sources/ASOProviders/OpenRouter/JevClient.swift`](https://github.com/mustafakendiguzel/aso-workbench/blob/037bfb68b7c6c9dc7f844ee63704c46a0277b65c/Sources/ASOProviders/OpenRouter/JevClient.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/mustafakndgzl/status/2113582230799065514)). |
| Maintainer | [mustafakendiguzel](https://github.com/mustafakendiguzel). Independently curated. |
| Format | macOS app (Swift 6.2, SwiftUI) |
| Platform and availability | macOS 15+; free unnotarized DMG from GitHub releases, or build from source with Xcode 26. |
| Jev's role | Optional: through OpenRouter, Jev answers probability questions about each keyword (is it a brand, is it relevant) that the app uses as clues for its popularity estimate. |
| Requirements | macOS 15+; optional OpenRouter key for Jev clues and the AI writer; optional Apple Ads, App Store Connect and RevenueCat keys. |
| License | [MIT with Commons Clause (source available)](https://github.com/mustafakendiguzel/aso-workbench/blob/037bfb68b7c6c9dc7f844ee63704c46a0277b65c/LICENSE) |

## When to use

- Track App Store keyword ranks and see where each number comes from.
- Estimate popularity for terms Apple does not report.
- Mismatch: the Commons Clause forbids selling the app or a paid service built on it.

## How it works

`Sources/ASOProviders/OpenRouter/JevClient.swift` calls OpenRouter's decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with `typesafe/jev-1.13`; the author reports a 0.74 rank correlation with Apple's popularity on unseen terms. Integration evidence: [`Sources/ASOProviders/OpenRouter/JevClient.swift`](https://github.com/mustafakendiguzel/aso-workbench/blob/037bfb68b7c6c9dc7f844ee63704c46a0277b65c/Sources/ASOProviders/OpenRouter/JevClient.swift).

## Get started

Download the DMG from the [latest release](https://github.com/mustafakendiguzel/aso-workbench/releases/latest), or build from source (not run on the review host):

```sh
git clone https://github.com/mustafakendiguzel/aso-workbench
cd aso-workbench && make install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How the numbers work, in the README: [github.com/mustafakendiguzel/aso-workbench#how-the-numbers-work](https://github.com/mustafakendiguzel/aso-workbench#how-the-numbers-work)

## Limits and data handling

Keywords are sent to OpenRouter when Jev clues are on. An advanced option uses an undocumented Apple Ads website session at your own risk.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 037bfb68b7c6](https://github.com/mustafakendiguzel/aso-workbench/tree/037bfb68b7c6c9dc7f844ee63704c46a0277b65c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
