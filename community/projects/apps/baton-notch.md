# Baton (notch app)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS notch app that pings you when a ChatGPT, Codex, Claude or Cursor chat finishes or needs you; TypeSafe Jev decides finished vs needs-you.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jeanlucandre-afk/baton) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/jeanlucandre-afk/baton/releases](https://github.com/jeanlucandre-afk/baton/releases) |
| Pricing and access | Free MIT app; Jev (and optional Gemini) calls use your own keys. |
| Jev evidence | [`Sources/BatonCore/Jev.swift`](https://github.com/jeanlucandre-afk/baton/blob/21a557b7f7e5d15f4b864cc089f716d0048a555d/Sources/BatonCore/Jev.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [jeanlucandre-afk](https://github.com/jeanlucandre-afk). Independently curated. |
| Format | macOS app (Swift) |
| Platform and availability | macOS (DMG, not notarized; Sparkle updates) |
| Jev's role | Jev reads each chat's latest reply and decides whether it is finished or needs your answer; without a Jev key Baton only lists chats. |
| Requirements | macOS with Accessibility permission; TypeSafe key. |
| License | [MIT](https://github.com/jeanlucandre-afk/baton/blob/21a557b7f7e5d15f4b864cc089f716d0048a555d/LICENSE) |

## When to use

- Run several AI chats in parallel and get notified only when one needs you.
- Mismatch: Distinct from the Baton agent orchestrator; reads chat UI text via Accessibility.

## How it works

Baton reads chat state from supported apps, sends the reply text to Jev for a finished / needs-you decision, and pops the notch. (Summarized from the upstream [README](https://github.com/jeanlucandre-afk/baton/blob/21a557b7f7e5d15f4b864cc089f716d0048a555d/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): download Baton.dmg from Releases, open it via Privacy & Security once, and add your keys in the welcome window.

## Limits and data handling

Chat reply text goes to Jev (and Gemini if configured). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 21a557b7f7e5](https://github.com/jeanlucandre-afk/baton/tree/21a557b7f7e5d15f4b864cc089f716d0048a555d). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
