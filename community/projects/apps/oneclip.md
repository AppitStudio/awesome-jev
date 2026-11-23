# OneClip by Jan M. (local AI video clipper where Jev scores candidate clips for hook strength before rendering vertical shorts)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Transcribes a long video locally, cuts sentence-aligned candidate clips, asks Jev for six scores, a context check and a hook type per clip, ranks them, has an AI planner (or a template) plan the edit, and renders 1080x1920 MP4s with word-by-word captions via Remotion or FFmpeg.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/janmm97/oneclip) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/janmm97/oneclip#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source build that runs locally; requires a free One account (withone.ai) plus your own TypeSafe account, billed at about 34k Jev tokens per video by the author's estimate; OpenRouter edit plans optional. Checked 2026-11-24. |
| Jev evidence | [`packages/core/src/jev/evaluator.ts`](https://github.com/janmm97/oneclip/blob/c983bb2b80e3d90423ffdd7c71c321fc81c6261d/packages/core/src/jev/evaluator.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [janmm97](https://github.com/janmm97). Independently curated. |
| Format | TypeScript monorepo (Next.js app, worker, Remotion templates) with optional Python transcription |
| Platform and availability | Local web app (Next.js) and media worker; tested on Windows 11, macOS/Linux untested end to end per the README. |
| Jev's role | Jev scores each candidate clip (six dimensions, context, hook type); OneClip ranks, penalises and de-duplicates from those answers. |
| Requirements | Node.js 22.13+, pnpm 10, FFmpeg 6+; One CLI 2.x with a TypeSafe connection; Python 3.10-3.12 optional. |
| License | [MIT](https://github.com/janmm97/oneclip/blob/c983bb2b80e3d90423ffdd7c71c321fc81c6261d/LICENSE) |

## When to use

- Find and render the strongest short clips from your own long videos on your own machine.
- Mismatch: fully offline use; clip text goes to Jev.

## How it works

`packages/core/src/jev/evaluator.ts` sends one Jev request per candidate through the One CLI, which holds the TypeSafe connection, with bounded concurrency; questions live in `jev/questions.ts`. Integration evidence: [`packages/core/src/jev/evaluator.ts`](https://github.com/janmm97/oneclip/blob/c983bb2b80e3d90423ffdd7c71c321fc81c6261d/packages/core/src/jev/evaluator.ts).

## Get started

Install, connect TypeSafe through One, run setup and start the app.

```sh
git clone https://github.com/janmm97/oneclip.git && cd oneclip
corepack enable && pnpm install
npm i -g @withone/cli && one init && one add typesafe
pnpm run setup && pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/janmm97/oneclip/blob/c983bb2b80e3d90423ffdd7c71c321fc81c6261d/README.md](https://github.com/janmm97/oneclip/blob/c983bb2b80e3d90423ffdd7c71c321fc81c6261d/README.md)

## Limits and data handling

Clip text (not video) is sent to TypeSafe via One, and by default to an AI planner. Remotion needs a company licence for larger companies.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit c983bb2b80e3](https://github.com/janmm97/oneclip/tree/c983bb2b80e3d90423ffdd7c71c321fc81c6261d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
