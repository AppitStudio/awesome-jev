# JevDK and jev-serve (Mac tools to design decision questions and serve a Jev-style API locally)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Two free Mac tools: JevDK lets you design and test typed decision questions on a local MLX model and on hosted backends side by side (including TypeSafe Jev through OpenRouter), mark right answers and calibrate; jev-serve answers a hosted-Jev-style HTTP API on your Mac.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ancientcomputing/jevdk) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/ancientcomputing/jevdk#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (Apache-2.0); free download. Hosted Jev calls go through your own OpenRouter key; local models are free to run. Checked 2026-10-24. |
| Jev evidence | [`jevdk/Sources/JevDK/HostedBackends.swift`](https://github.com/ancientcomputing/jevdk/blob/5190119def442c3f7f3009ee3f4d98b4fe3ab438/jevdk/Sources/JevDK/HostedBackends.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ancientcomputing](https://github.com/ancientcomputing). Independently curated. |
| Format | macOS app and CLI (Swift) |
| Platform and availability | macOS on Apple silicon; signed and notarized DMG from GitHub Releases (v0.2.2 at review). |
| Jev's role | Optional hosted comparison backend: Jev (typesafe/jev-1.13 via OpenRouter) runs next to local models so you can compare answers before shipping questions. |
| Requirements | Apple-silicon Mac with macOS 27; an OpenRouter key for the hosted Jev backend (optional). |
| License | [Apache-2.0](https://github.com/ancientcomputing/jevdk/blob/5190119def442c3f7f3009ee3f4d98b4fe3ab438/LICENSE) |

## When to use

- Design and test the questions you plan to send to a decision model before writing app code.
- Compare a local model with hosted Jev on the same samples and mark the right answers.
- Mismatch: Jev here is reached through OpenRouter only; local models are not Jev.

## How it works

`HostedBackends.swift` defines the hosted backends: an OpenRouter route that passes requests to TypeSafe's `typesafe/jev-1.13`, plus Featherless's own classifier (a different model) with a free demo. jev-serve exposes a hosted-Jev-style API backed by local MLX models. Integration evidence: [`jevdk/Sources/JevDK/HostedBackends.swift`](https://github.com/ancientcomputing/jevdk/blob/5190119def442c3f7f3009ee3f4d98b4fe3ab438/jevdk/Sources/JevDK/HostedBackends.swift).

## Get started

From the upstream README (not run on the review host): download JevDK-x.y.z-arm64.dmg from the latest release, drag JevDK to Applications, then optionally install jev-serve from the JevDK menu:

```sh
jev-serve --model mlx-community/Qwen3-4B-4bit
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/ancientcomputing/jevdk/releases/latest](https://github.com/ancientcomputing/jevdk/releases/latest)
- Guide: [thisbrain.ai/locallm/jdk-guide.html](https://thisbrain.ai/locallm/jdk-guide.html)

## Limits and data handling

Samples you test against a hosted backend are sent to that provider (OpenRouter/TypeSafe or Featherless). Local models stay on your Mac.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 5190119def44](https://github.com/ancientcomputing/jevdk/tree/5190119def442c3f7f3009ee3f4d98b4fe3ab438). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
