# skil.li

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS launcher and assistant (apps, files, clipboard, snippets, windows, Hyper Key) that can also act on requests; its Ask router uses a fast decision model such as TypeSafe Jev to route what you typed before a larger model runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nomdelasociete/skilli) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://skil.li) |
| Pricing and access | Free download (GPL-3.0); you bring your own AI keys and pay those providers. Checked 2026-10-19. |
| Jev evidence | [`Sources/Skilli/AI/AskRouter.swift`](https://github.com/nomdelasociete/skilli/blob/bb767bb91ebc2b75eb481e8321012f47754c1ccb/Sources/Skilli/AI/AskRouter.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [nomdelasociete](https://github.com/nomdelasociete). Independently curated. |
| Format | Native macOS app (Swift) |
| Platform and availability | macOS 26+ (signed, notarised download or Homebrew cask). |
| Jev's role | Optional fast router: Jev decides how an Ask request should be handled before the main model is called. |
| Requirements | macOS 26+; your own AI connection (Codex or an API key) and optionally a decision-model key such as TypeSafe Jev. |
| License | [GPL-3.0](https://github.com/nomdelasociete/skilli/blob/bb767bb91ebc2b75eb481e8321012f47754c1ccb/LICENSE) |

## When to use

- Want a keyboard-first launcher that also answers and acts, with your own AI keys.
- Like a cheap decision model deciding routing before a chat model runs.
- Mismatch: Jev is one optional piece of a large launcher; macOS 26+ only.

## How it works

`Sources/Skilli/AI/AskRouter.swift` uses a configured decision key (TypeSafe Jev first, then an OpenAI decision model) to classify each Ask request and route it. Integration evidence: [`Sources/Skilli/AI/AskRouter.swift`](https://github.com/nomdelasociete/skilli/blob/bb767bb91ebc2b75eb481e8321012f47754c1ccb/Sources/Skilli/AI/AskRouter.swift).

## Get started

Download from skil.li or install with Homebrew, allow Accessibility, and connect your AI keys in settings.

```sh
brew install --cask nomdelasociete/tap/skilli
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [skil.li](https://skil.li)
- Sources/Skilli/AI/AskRouter.swift

## Limits and data handling

Requests routed through Jev go to TypeSafe with your key. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit bb767bb91ebc](https://github.com/nomdelasociete/skilli/tree/bb767bb91ebc2b75eb481e8321012f47754c1ccb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
