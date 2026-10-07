# Danmaku spoiler filter (JEV)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Zero-dependency Chrome extension (plus CLI) that has TypeSafe Jev judge whether Bilibili danmaku comments are spoilers and filters the hits, batching comments per request with a local cache; built to add other danmaku sites later. Docs in Chinese and English.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/meetchen/jev-danmaku-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/meetchen/jev-danmaku-filter#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the MIT extension (load unpacked or from Releases); requires your own TypeSafe key stored in extension storage (usage billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`apps/extension/background.js`](https://github.com/meetchen/jev-danmaku-filter/blob/d1d2681bef315ce0be465206cfb2bdf4a8dbc166/apps/extension/background.js) and [`vendor/core/jev.js`](https://github.com/meetchen/jev-danmaku-filter/blob/d1d2681bef315ce0be465206cfb2bdf4a8dbc166/apps/extension/vendor/core/jev.js) call `api.typesafe.ai`; README documents the architecture. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [meetchen](https://github.com/meetchen). Independently curated. |
| Format | Chrome MV3 extension + Node CLI |
| Platform and availability | Chrome (developer mode or Releases zip) on bilibili.com video pages. |
| Jev's role | Judges each danmaku line as spoiler or not; fetching, caching and hiding are code. |
| Requirements | Chrome, Node.js to build (`npm run build`), and a TypeSafe API key. |
| License | [MIT](https://github.com/meetchen/jev-danmaku-filter/blob/d1d2681bef315ce0be465206cfb2bdf4a8dbc166/LICENSE). |

## When to use

- Keep danmaku on while hiding spoilers on Bilibili videos.
- Adapt the batching and caching approach for other comment streams.
- Mismatch: Bilibili only for now; first visit to a video needs a few seconds of warm-up.

## How it works

`page.js` rewrites the player's danmaku segments in the page context, `content.js` gathers the full video's danmaku and hands it to the background worker, which alone calls Jev and caches answers locally.

## Get started

Build and load unpacked (README *快速开始*):

```sh
git clone https://github.com/meetchen/jev-danmaku-filter.git && cd jev-danmaku-filter
npm run build
# chrome://extensions → Developer mode → Load unpacked → apps/extension
```

Each video's danmaku is judged in batches billed to your TypeSafe key; later views use the local cache.

## Examples and demos

- [English README](https://github.com/meetchen/jev-danmaku-filter/blob/d1d2681bef315ce0be465206cfb2bdf4a8dbc166/README.en.md).
- [Releases](https://github.com/meetchen/jev-danmaku-filter/releases).

## Limits and data handling

Danmaku text from the videos you watch goes to TypeSafe; the key stays in local extension storage. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit d1d2681bef31](https://github.com/meetchen/jev-danmaku-filter/tree/d1d2681bef315ce0be465206cfb2bdf4a8dbc166). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
