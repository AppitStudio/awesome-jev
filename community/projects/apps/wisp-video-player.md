# Wisp (content-aware video player that fades video edges into the page, keeping Jev-tracked people sharp)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local web video player that softly fades a video's edges into the page; optional focus tracks built with Jev's image questions mark people, animals and faces ahead of time so the fade opens around them, and a QA tool asks Jev whether subjects stayed visible.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nomanjack/wisp) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/nomanjack/wisp#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source build; an optional TypeSafe key is billed by TypeSafe when you build focus tracks. Checked 2026-11-13. |
| Jev evidence | [`jev.mjs`](https://github.com/nomanjack/wisp/blob/ce02d170888e69c0cd0efcf2372a31e9ccccd020/jev.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Creator's X account @Nomandsign is linked from the maintainer's site iamnoman.com (GitHub nomanjack). Discovered via X ([post](https://x.com/Nomandsign/status/2120970644255121433)). |
| Maintainer | [nomanjack](https://github.com/nomanjack). Independently curated. |
| Format | Local Node.js web app (JavaScript, WebGL, MIT) |
| Platform and availability | Web (local Node.js server, any modern browser with WebGL); source build only, no hosted product verified |
| Jev's role | Optional: Jev box questions build per-clip focus tracks of people, animals and faces, and judge QA frames; playback works without Jev. |
| Requirements | Node.js with `npm`; a TypeSafe key (`TYPESAFE_API_KEY`) only to build new focus tracks or run the QA judge. |
| License | [MIT](https://github.com/nomanjack/wisp/blob/ce02d170888e69c0cd0efcf2372a31e9ccccd020/LICENSE) |

## When to use

- Embed a dreamy, edge-faded video on a page without cutting off people near the frame edge.
- Precompute subject tracks once with Jev instead of running detection on every viewer's device.
- Mismatch: a hosted player or CDN service; this is a local source build.

## How it works

`jev.mjs` is a local-only API used by `tools/focus-track.html`: it sends JPEG frames to `https://api.typesafe.ai/v1/systemone` with model pinned to `jev-1.14.0` and a box question for the main subject, and saves the result as `assets/<scene>.focus.json`. The key is read on the local server and never sent to the browser. Playback itself needs no key; clips without a track fall back to on-device MediaPipe face detection. Integration evidence: [`jev.mjs`](https://github.com/nomanjack/wisp/blob/ce02d170888e69c0cd0efcf2372a31e9ccccd020/jev.mjs).

## Get started

Install and start the local server, open `http://127.0.0.1:4173` and drop in a clip; add a key in `.env.local` only to build Jev focus tracks.

```sh
npm install
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with preview: [github.com/nomanjack/wisp/blob/ce02d170888e69c0cd0efcf2372a31e9ccccd020/README.md](https://github.com/nomanjack/wisp/blob/ce02d170888e69c0cd0efcf2372a31e9ccccd020/README.md)
- Focus-track builder: [github.com/nomanjack/wisp/blob/ce02d170888e69c0cd0efcf2372a31e9ccccd020/tools/focus-track.html](https://github.com/nomanjack/wisp/blob/ce02d170888e69c0cd0efcf2372a31e9ccccd020/tools/focus-track.html)

## Limits and data handling

Only when you build focus tracks or run QA are video frames sent to TypeSafe on your key; normal playback runs in the browser.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit ce02d170888e](https://github.com/nomanjack/wisp/tree/ce02d170888e69c0cd0efcf2372a31e9ccccd020). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
