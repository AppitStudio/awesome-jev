# iMessage Bridge (Mac menu bar app that gives AI agents approved access to your iMessages, with Jev screening incoming texts)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Menu bar app that lets agents such as Claude Code or Grok Bot read and, if you allow it, send iMessages through the app instead of touching the Messages database. Each agent is approved with a pairing code and gets its own rules, every send can require confirmation, and incoming texts that try to instruct your agent can be screened by a local model and, optionally, Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cmer/imessage-bridge) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://cmer.github.io/imessage-bridge/) |
| Pricing and access | Free download and source (MIT); Jev screening uses your own TypeSafe or OpenRouter key. Checked 2026-11-01. |
| Jev evidence | [`Sources/BridgeCore/JevClient.swift`](https://github.com/cmer/imessage-bridge/blob/9e575be29e85e10d3d52dbf17804f7841dd41710/Sources/BridgeCore/JevClient.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/cmercier/status/2116640171483619754)). |
| Maintainer | [cmer](https://github.com/cmer). Independently curated. |
| Format | Native macOS app (Swift), `.dmg` release or Homebrew cask |
| Platform and availability | macOS 14 or later (menu bar app). |
| Jev's role | Optional prompt-injection screening of incoming messages before an agent sees them. |
| Requirements | macOS 14+; Full Disk Access; an optional TypeSafe or OpenRouter key for Jev screening. |
| License | [MIT](https://github.com/cmer/imessage-bridge/blob/9e575be29e85e10d3d52dbf17804f7841dd41710/LICENSE) |

## When to use

- Give a coding or personal agent scoped, revocable iMessage access with send confirmation.
- Mismatch: Jev is an optional screening layer; the core bridge works with only the on-device model.

## How it works

`Sources/BridgeCore/JevClient.swift` calls TypeSafe `POST /v1/systemone` (or OpenRouter) and the prompt in `Sources/BridgeCore/JevPrompt.swift` asks Jev whether an incoming message is trying to give the agent instructions; flagged texts are hidden before the agent reads them, alongside an on-device screening model. Integration evidence: [`Sources/BridgeCore/JevClient.swift`](https://github.com/cmer/imessage-bridge/blob/9e575be29e85e10d3d52dbf17804f7841dd41710/Sources/BridgeCore/JevClient.swift).

## Get started

From the upstream README (not run on the review host):

```sh
brew install --cask cmer/tap/imessage-bridge
# then open iMessage Bridge, grant Full Disk Access, and add a TypeSafe key under Safety > Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [cmer.github.io/imessage-bridge/](https://cmer.github.io/imessage-bridge/)
- Announcement on X: [x.com/cmercier/status/2116640171483619754](https://x.com/cmercier/status/2116640171483619754)

## Limits and data handling

Message text you screen with Jev is sent to TypeSafe or OpenRouter; reading and sending otherwise stay on your Mac. Screening reduces but does not eliminate prompt-injection risk. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 9e575be29e85](https://github.com/cmer/imessage-bridge/tree/9e575be29e85e10d3d52dbf17804f7841dd41710). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
