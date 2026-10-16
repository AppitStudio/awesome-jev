# Jev Review Markers for Premiere

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Premiere UXP panel that turns typed Jev review findings on an SRT caption export into timeline markers: Jev flags issues and picks the exact caption, and every marker is added in one undoable transaction with the caption text copied byte for byte.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-premiere-markers) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Adobe Premiere UXP panel (source build) |
| Requirements | Node 22+, Premiere 25.6+, UXP Developer Tool 2.2+, a TypeSafe API key entered in the panel. |
| License | [MIT](https://github.com/gbesse/jev-premiere-markers/blob/e877507ebe2a74f7d422c798474aff59f41aa0d1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.js`](https://github.com/gbesse/jev-premiere-markers/blob/e877507ebe2a74f7d422c798474aff59f41aa0d1/src/client.js) at the pinned commit. |

## When to use

- Review a cut's captions against a declared pack and jump to flagged spots on the timeline.
- Mismatch: the author notes the panel has not yet been loaded and validated inside Premiere; capped at 255 captions.

## How it works

Pass one asks finite Noul issue questions over the captions; pass two picks one submitted caption ID, and a guard rejects any ID that was not offered. Network access is restricted to `https://api.typesafe.ai`, and the key is held only in panel memory. Integration evidence: [`src/client.js`](https://github.com/gbesse/jev-premiere-markers/blob/e877507ebe2a74f7d422c798474aff59f41aa0d1/src/client.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gbesse/jev-premiere-markers.git && cd jev-premiere-markers
npm install && npm test && npm run build
# load manifest.json in UXP Developer Tool, then Window > UXP Plugins > Jev Review Markers
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Offline caption-ID guard demo: `npm run demo:guard`.
- Synthetic adoption check: `examples/adoption-check.md`.

## Limits and data handling

Caption text leaves Premiere only when you click Review; the key is never persisted.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit e877507ebe2a](https://github.com/gbesse/jev-premiere-markers/tree/e877507ebe2a74f7d422c798474aff59f41aa0d1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
