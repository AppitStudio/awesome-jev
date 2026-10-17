# Scene Finder

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Desktop app for finding a moment in a movie you can only describe: it samples frames from your MKV or MP4, asks Jev which ones match, lets you play the hits, then trim and save an MP4 clip.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EmmyMay/scene-finder) |
| Tags | `Free` · `Source available` · `BYOK` |
| Product homepage | [Product homepage](https://github.com/EmmyMay/scene-finder/releases) |
| Pricing and access | Free beta downloads; you pay your own Jev/TypeSafe usage. No open-source license on the reviewed commit. Checked 2026-10-17. |
| Jev evidence | [`src/jev-client.ts`](https://github.com/EmmyMay/scene-finder/blob/983169839e8131ed9ba5e1d3eef3c66130c0cb76/src/jev-client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/techemmyleke/status/2111256290013896949)). |
| Maintainer | [EmmyMay](https://github.com/EmmyMay). Independently curated. |
| Format | Electron desktop app (DMG for Apple silicon, Windows setup EXE, Linux portable archive) |
| Platform and availability | macOS (Apple silicon), Windows x64, Linux x64 |
| Jev's role | Jev judges which sampled frames match your scene description. |
| Requirements | macOS 13+ on Apple silicon, Windows 10/11 x64 or Linux x64; your own Jev (TypeSafe) API key and an internet connection for search. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Find the timestamp of a scene you remember visually but not by time, and export just that clip.
- See how Jev handles visual yes/no questions over sampled video frames.
- Mismatch: results are approximate sampled matches; it searches what is visible, not dialogue or audio.

## How it works

The app samples frames locally with bundled FFmpeg and sends them with your description to TypeSafe's API through `src/jev-client.ts`; matching moments stream in as the search runs and can be resumed if interrupted. Movies and exported clips stay on your device, and the key is kept in OS-encrypted storage. Integration evidence: [`src/jev-client.ts`](https://github.com/EmmyMay/scene-finder/blob/983169839e8131ed9ba5e1d3eef3c66130c0cb76/src/jev-client.ts).

## Get started

From the upstream README (not run on the review host). Beta installers are on GitHub Releases; the source build needs a native toolchain:

```sh
# Users: download a beta from https://github.com/EmmyMay/scene-finder/releases
# Developers (Node.js 22):
npm ci
npm run media:prepare
npm run desktop
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video in the author's X post: [x.com/techemmyleke/status/2111256290013896949](https://x.com/techemmyleke/status/2111256290013896949)
- Beta downloads: [github.com/EmmyMay/scene-finder/releases](https://github.com/EmmyMay/scene-finder/releases)

## Limits and data handling

Sampled frames and your query go to TypeSafe on your key; no API credits are included. Windows installers are unsigned. The repository has no LICENSE file on the reviewed commit, so the source is viewable but not licensed for reuse.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 983169839e81](https://github.com/EmmyMay/scene-finder/tree/983169839e8131ed9ba5e1d3eef3c66130c0cb76). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
