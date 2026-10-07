# Jev Slop Detector

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Unofficial Chrome extension (with a local Node relay holding your key) that labels posts on your X feed with a TypeSafe Jev classification probability such as `● Slop | 83%`; it never hides or edits posts. The repo also holds SylphAI's class material for teaching Jev and the demo-recording scripts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SylphAI-Inc/jev-slop-detector) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/SylphAI-Inc/jev-slop-detector#readme) (source-built app; no separate website verified). |
| Pricing and access | No app fee for the source build (load unpacked); requires your own TypeSafe key in the local relay (usage billed by TypeSafe). Checked 2026-10-07. |
| Jev evidence | [`relay/typesafe.js`](https://github.com/SylphAI-Inc/jev-slop-detector/blob/66881974c64c28532416ec1dfcc647ad4efbce4a/relay/typesafe.js) calls the TypeSafe API from the local relay; [`extension/content.js`](https://github.com/SylphAI-Inc/jev-slop-detector/blob/66881974c64c28532416ec1dfcc647ad4efbce4a/extension/content.js) sends post text and renders the label; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [SylphAI-Inc](https://github.com/SylphAI-Inc). Independently curated. |
| Format | Chrome Manifest V3 extension + local Node relay (`127.0.0.1:8790`) |
| Platform and availability | Chrome (load unpacked) with a Node 20+ relay on the same machine; source build only. |
| Jev's role | Jev answers one question per post (hype over substance) and returns the probability shown on the label; code applies the 0.70/0.50 display thresholds and caching. |
| Requirements | Node 20+, Chrome, a TypeSafe API key in `relay/.env`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |

## When to use

- Add a quick, explicitly probabilistic hype-vs-substance label to posts while reading X.
- Teach or study a small Jev classification project end to end (class material included).
- Mismatch: upstream tested on about 10 live posts; thresholds are uncalibrated and the label is not an AI-writing detector.

## How it works

The content script reads the main post text (posts under 15 characters or link-only are skipped) and asks the relay; the relay keeps `TYPESAFE_API_KEY` so the extension never sees it, calls Jev, and returns the probability. Class material: [`class-material/`](https://github.com/SylphAI-Inc/jev-slop-detector/tree/66881974c64c28532416ec1dfcc647ad4efbce4a/class-material).

## Get started

Quick start from the README:

```sh
git clone https://github.com/SylphAI-Inc/jev-slop-detector.git && cd jev-slop-detector
cp relay/.env.example relay/.env    # add TYPESAFE_API_KEY
npm run relay                        # listens on 127.0.0.1:8790
# chrome://extensions → Load unpacked → extension/
```

One Jev request per uncached post, billed to your TypeSafe key.

## Examples and demos

- README screenshots of the extension on a live X feed.
- Class page and runnable Jev examples: [`class-material/README.md`](https://github.com/SylphAI-Inc/jev-slop-detector/blob/66881974c64c28532416ec1dfcc647ad4efbce4a/class-material/README.md).

## Limits and data handling

Post text from your feed is sent to TypeSafe through your relay. Relies on X's `data-testid` markup, which can change. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 66881974c64c](https://github.com/SylphAI-Inc/jev-slop-detector/tree/66881974c64c28532416ec1dfcc647ad4efbce4a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
