# Pi Browser by Matt Riley (DOM-first Chrome companion for the Pi agent, where Jev chooses links from shared tabs)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome MV3 extension plus Pi extension that gives the Pi coding agent a persistent, paired connection to only the tabs you share; Pi owns the goal, Jev chooses among DOM-derived link candidates, and every click asks you first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/matt-riley/pi-browser) |
| Maintainer | [matt-riley](https://github.com/matt-riley). Independently curated. |
| Format | JavaScript / TypeScript Pi extension + Chrome extension |
| Requirements | Node 22.18+, Pi (tested with 1.5.0), Chrome 116+ and a `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/selection.ts`](https://github.com/matt-riley/pi-browser/blob/845a1189cf5e03db014ddb2522ca00cece3b151b/src/selection.ts) at the pinned commit. |

## When to use

- Let a Pi agent read and navigate tabs you explicitly share, with per-click approval and no cloud relay.
- Mismatch: other agents than Pi, or unattended browsing; there is no license file.

## How it works

`src/selection.ts` creates a `TypeSafeClient` (`jev-latest` by default) and asks a `choice` over a trimmed set of candidate links from the shared tab, validating the confidence and probabilities before any action; no screenshots or debugger permission are used. Integration evidence: [`src/selection.ts`](https://github.com/matt-riley/pi-browser/blob/845a1189cf5e03db014ddb2522ca00cece3b151b/src/selection.ts).

## Get started

Load the extension, start Pi with the plugin and pair.

```sh
git clone https://github.com/matt-riley/pi-browser
cd pi-browser
npm ci --legacy-peer-deps
export TYPESAFE_API_KEY=...
pi -e ./src/index.js
# Chrome: load unpacked ./chrome, then /browser in Pi to pair
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/matt-riley/pi-browser/blob/845a1189cf5e03db014ddb2522ca00cece3b151b/README.md](https://github.com/matt-riley/pi-browser/blob/845a1189cf5e03db014ddb2522ca00cece3b151b/README.md)
- Changelog: [github.com/matt-riley/pi-browser/blob/845a1189cf5e03db014ddb2522ca00cece3b151b/CHANGELOG.md](https://github.com/matt-riley/pi-browser/blob/845a1189cf5e03db014ddb2522ca00cece3b151b/CHANGELOG.md)

## Limits and data handling

Text from shared tabs and candidate links is sent to TypeSafe. Pairing uses a loopback WebSocket with a token. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 845a1189cf5e](https://github.com/matt-riley/pi-browser/tree/845a1189cf5e03db014ddb2522ca00cece3b151b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
