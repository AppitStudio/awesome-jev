# SplitSeek

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS desktop app that searches a folder of grey, flat LOG video footage by describing a moment in plain words: it samples a frame every 2 seconds, asks Jev a yes/no question about each frame, and ranks matching moments with timestamps, confidence and a preview from the best frame.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/okoryem/split-seek) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/okoryem/split-seek#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source build; you pay for your own Jev calls (image access required). Checked 2026-10-20. |
| Jev evidence | [`src-tauri/src/jev.rs`](https://github.com/okoryem/split-seek/blob/7f587258a6abe5d86d171c77be0af04ebaa45dcc/src-tauri/src/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [okoryem](https://github.com/okoryem). Independently curated. |
| Format | macOS desktop app (Tauri, Rust; build from source) |
| Platform and availability | macOS on Apple Silicon (tested on macOS 15); build from source, no signed release. |
| Jev's role | Jev answers one yes/no question per sampled frame; the app ranks and groups frames by the returned probability. |
| Requirements | macOS on Apple Silicon, Node.js and npm, Rust (rustup), ffmpeg/ffprobe, and a TypeSafe key with image access. |
| License | [MIT](https://github.com/okoryem/split-seek/blob/7f587258a6abe5d86d171c77be0af04ebaa45dcc/LICENSE) |

## When to use

- Find 'the waterfall shot' across dozens of near-identical LOG clips without scrubbing.
- Keep a search window next to any video editor; it does not connect to one.
- Mismatch: hackathon proof of concept, macOS only, build from source.

## How it works

ffmpeg pulls one frame every 2 seconds into a local cache. For each search, `src-tauri/src/jev.rs` sends frames to `https://api.typesafe.ai/v1/systemone` 64 questions at a time, asking 'Does this frame show: <your phrase>?'. Back-to-back matching frames become one row ranked by confidence; matches under 60% wait behind Show more. Original clips are only read. Integration evidence: [`src-tauri/src/jev.rs`](https://github.com/okoryem/split-seek/blob/7f587258a6abe5d86d171c77be0af04ebaa45dcc/src-tauri/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/okoryem/split-seek.git splitseek && cd splitseek
npm install
cp .env.example .env   # paste JEV_API_KEY=
npm run tauri dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- devpost/ (hackathon PRD, spec and scope)
- src-tauri/examples/jev_probe.rs and search_cli.rs

## Limits and data handling

Searches send low-resolution stills of your footage to TypeSafe. Frames are cached under ~/Library/Caches/com.splitseek.app and can be cleared in the app.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 7f587258a6ab](https://github.com/okoryem/split-seek/tree/7f587258a6abe5d86d171c77be0af04ebaa45dcc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
