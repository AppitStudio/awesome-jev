# Usher (macOS menu bar app that sizes the focused window by the kind of work, classified by Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

When you switch windows, Usher sends the app name and window title to Jev on OpenRouter, sorts the window into Code, Reference, Media, Writing, Chat or Ambient, gives it that category's share of the screen (two-thirds for code, full for media) and arranges the other windows around it. Shares are adjustable from the menu bar, answers are cached per app and title, and with no network or key it guesses from the app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jabreeflor/usher) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jabreeflor/usher#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; bring your own OpenRouter key. Checked 2026-10-30. |
| Jev evidence | [`Sources/Usher/Classifier.swift`](https://github.com/jabreeflor/usher/blob/dbd96c2a7bead9858a0d453dd2fc809989fd265d/Sources/Usher/Classifier.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jabreeflor](https://github.com/jabreeflor). Independently curated. |
| Format | macOS menu bar app (Swift) |
| Platform and availability | macOS 13+; build from source with Swift (no release binary verified). |
| Jev's role | Classifies the focused window's kind of work so Usher can size it. |
| Requirements | macOS 13+, Swift 5.10+, Accessibility permission, and an OpenRouter key. |
| License | [MIT](https://github.com/jabreeflor/usher/blob/dbd96c2a7bead9858a0d453dd2fc809989fd265d/LICENSE) |

## When to use

- Automatic window sizing based on what you are doing, without writing per-app rules.
- Mismatch: source build only; sends window titles to OpenRouter.

## How it works

`Classifier.swift` asks `typesafe/jev-router` on OpenRouter to pick one of six categories from the app name and window title; the layout engine then tiles windows by category share. Integration evidence: [`Sources/Usher/Classifier.swift`](https://github.com/jabreeflor/usher/blob/dbd96c2a7bead9858a0d453dd2fc809989fd265d/Sources/Usher/Classifier.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jabreeflor/usher.git && cd usher
swift build
export OPENROUTER_API_KEY=sk-or-...
.build/debug/Usher
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Classify without moving windows: .build/debug/Usher --classify com.google.Chrome "YouTube - Some video"

## Limits and data handling

App names and window titles are sent to OpenRouter (and on to TypeSafe). Independent project; not affiliated with TypeSafe or Apple.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit dbd96c2a7bea](https://github.com/jabreeflor/usher/tree/dbd96c2a7bead9858a0d453dd2fc809989fd265d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
