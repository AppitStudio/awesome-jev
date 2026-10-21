# UIScore (UI design score from a screenshot)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Mac menu-bar app that scores a screenshot's UI design on contrast, grouping, hierarchy, clarity, trust, reading grade and feeling, combining yes/no checks from design research answered by Jev with Claude, into one 0 to 100 score.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/itsdimachka/uiscore) |
| Maintainer | [itsdimachka](https://github.com/itsdimachka). Independently curated. |
| Format | macOS menu-bar app and CLI (Swift) |
| Requirements | macOS 13+; a TypeSafe Jev key and an Anthropic API key, stored in Keychain. |
| License | [MIT](https://github.com/itsdimachka/uiscore/blob/d55d17cd8d23d32e9c6b5be6829223a43f364497/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Sources/ScreenCheckCore/Clients.swift`](https://github.com/itsdimachka/uiscore/blob/d55d17cd8d23d32e9c6b5be6829223a43f364497/Sources/ScreenCheckCore/Clients.swift) at the pinned commit. |

## When to use

- Get a quick design read on a screen you just captured.
- Compare iterations of a page by score.
- Mismatch: needs both a Jev and a Claude key.

## How it works

UIScore detects the page type, skips checks that don't apply, and sends the screenshot with yes/no design checks to `https://api.typesafe.ai/v1/systemone` (`Clients.swift`), alongside Claude and local code measures. Integration evidence: [`Sources/ScreenCheckCore/Clients.swift`](https://github.com/itsdimachka/uiscore/blob/d55d17cd8d23d32e9c6b5be6829223a43f364497/Sources/ScreenCheckCore/Clients.swift).

## Get started

From the upstream README (not run on the review host):

```sh
# download UIScore.zip from the latest release, or build:
swift build && swift test
scripts/make-app.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install guide: [github.com/itsdimachka/uiscore/blob/main/docs/INSTALL.md](https://github.com/itsdimachka/uiscore/blob/main/docs/INSTALL.md)
- Releases: [github.com/itsdimachka/uiscore/releases/latest](https://github.com/itsdimachka/uiscore/releases/latest)

## Limits and data handling

Screenshots you score are sent to Anthropic and TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit d55d17cd8d23](https://github.com/itsdimachka/uiscore/tree/d55d17cd8d23d32e9c6b5be6829223a43f364497). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
