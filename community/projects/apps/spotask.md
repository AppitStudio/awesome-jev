# SpotAsk

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS menu-bar assistant: summon it with a hotkey to ask your own model (BYOK), act on selected text in any app, or route a question to web AI, desktop apps or local CLI agents, with an optional Jev decision that picks the destination and shows its confidence before sending.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shiquda/SpotAsk) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://shiquda.github.io/SpotAsk/) |
| Pricing and access | Free AGPL-3.0 app; you pay your own model provider and Jev calls. Checked 2026-10-20. |
| Jev evidence | [`Sources/SpotAsk/Decision/DecisionRouting.swift`](https://github.com/shiquda/SpotAsk/blob/df1b14bd6efcc5b7fc143595b6ea316a58fbf431/Sources/SpotAsk/Decision/DecisionRouting.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [shiquda](https://github.com/shiquda). Independently curated. |
| Format | macOS app (Swift and AppKit; signed DMG and Homebrew cask) |
| Platform and availability | macOS 15+ (Apple Silicon and Intel); DMG releases (v0.3.1 on 2026-10-19) and Homebrew cask. |
| Jev's role | Optional: Jev picks which destination (web AI, desktop app or CLI agent) a question should go to, with a confidence shown before sending. |
| Requirements | macOS 15+ on Apple Silicon or Intel; your own model provider key for in-app answers; a TypeSafe key for decision routing. |
| License | [AGPL-3.0](https://github.com/shiquda/SpotAsk/blob/df1b14bd6efcc5b7fc143595b6ea316a58fbf431/LICENSE) |

## When to use

- Keep one hotkey for every question and let a decision model send it to ChatGPT, Perplexity, a terminal agent or a notes app.
- Translate, explain or polish selected text in place.
- Mismatch: routing to web AI opens those sites; it does not answer for them.

## How it works

With automatic routing on, SpotAsk sends the question and the list of configured destinations to a System One endpoint (default `https://api.typesafe.ai`, see `Sources/SpotAsk/Decision/DecisionRouting.swift`) and shows the recommended destination with its confidence. Enter continues, Tab switches channel, Esc cancels, or a confidence threshold auto-sends. Keys are kept in the macOS Keychain. Integration evidence: [`Sources/SpotAsk/Decision/DecisionRouting.swift`](https://github.com/shiquda/SpotAsk/blob/df1b14bd6efcc5b7fc143595b6ea316a58fbf431/Sources/SpotAsk/Decision/DecisionRouting.swift).

## Get started

From the upstream README (not run on the review host):

```sh
brew tap shiquda/spotask https://github.com/shiquda/SpotAsk
brew install --cask shiquda/spotask/spotask
# Settings (Cmd+,) > Services: add a provider; enable decision routing with a TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [shiquda.github.io/SpotAsk/](https://shiquda.github.io/SpotAsk/)
- Demo video linked in the README (decision routing to three destinations)

## Limits and data handling

Questions sent for routing go to TypeSafe; in-app answers go to the provider you configure. No telemetry, per the README.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit df1b14bd6efc](https://github.com/shiquda/SpotAsk/tree/df1b14bd6efcc5b7fc143595b6ea316a58fbf431). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
