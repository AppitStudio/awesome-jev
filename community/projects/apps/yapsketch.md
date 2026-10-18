# YapSketch

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS app for explaining bugs by talking and pointing: record your screen and voice, and Jev splits what you said into points, matches each to what you showed, and picks the clearest screenshot, then puts numbered text plus images on your clipboard for a coding agent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/farouqaldori/yapsketch) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/farouqaldori/yapsketch#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; Jev calls are billed by TypeSafe, Opper, or OpenRouter. Speech-to-text runs locally by default. |
| Jev evidence | [`Sources/YapSketch/Providers/Jev.swift`](https://github.com/farouqaldori/yapsketch/blob/4b4b9c54c30805dc72cc3509ef16d9e027900e1c/Sources/YapSketch/Providers/Jev.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [farouqaldori](https://github.com/farouqaldori). Independently curated. |
| Format | Native macOS app + `yapsketch` CLI |
| Platform and availability | macOS 15+ (build from source with `./scripts/build-app.sh`). |
| Jev's role | Jev aligns transcript segments with on-screen gestures and picks the best frame for each point. |
| Requirements | macOS 15+; Screen Recording, Microphone, Accessibility and Input Monitoring permissions; Jev via TypeSafe key or Opper/OpenRouter sign-in. |
| License | [Apache-2.0](https://github.com/farouqaldori/yapsketch/blob/4b4b9c54c30805dc72cc3509ef16d9e027900e1c/LICENSE) |

## When to use

- Hand a coding agent a precise, illustrated bug report from a short recording.
- Prefer local speech-to-text with an optional Jev step.
- Mismatch: build from source; macOS only.

## How it works

`Sources/YapSketch/Providers/Jev.swift` sends transcript and gesture context to Jev, which returns typed choices for which words go with which moment; the app assembles numbered text and screenshots. Integration evidence: [`Sources/YapSketch/Providers/Jev.swift`](https://github.com/farouqaldori/yapsketch/blob/4b4b9c54c30805dc72cc3509ef16d9e027900e1c/Sources/YapSketch/Providers/Jev.swift).

## Get started

From the upstream README: build the app, grant permissions, connect TypeSafe (or Opper/OpenRouter) in Settings > Models, then press the record shortcut.

```sh
git clone https://github.com/farouqaldori/yapsketch && cd yapsketch
./scripts/build-app.sh   # builds build/YapSketch.app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README clipboard example
- Sources/YapSketch/Providers/Jev.swift

## Limits and data handling

Words and pictures leave the Mac only when Jev or a cloud speech model is on, and only to the chosen provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 4b4b9c54c308](https://github.com/farouqaldori/yapsketch/tree/4b4b9c54c30805dc72cc3509ef16d9e027900e1c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
