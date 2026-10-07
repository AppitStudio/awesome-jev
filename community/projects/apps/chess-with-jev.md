# Chess with Jev

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser chess where your opponent is TypeSafe Jev: every move is a short chain of choice questions (focus, piece, destination) whose options are the legal moves, so illegal moves cannot be expressed; you can read each answer chain and rewrite the questions in an in-app workflow editor.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vlaier/chessWithJev) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/vlaier/chessWithJev#readme) (source-built app; no hosted version verified). |
| Pricing and access | No app fee for the source build; requires your own TypeSafe key in `.env` (usage billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`src/ai/jevPlayer.ts`](https://github.com/vlaier/chessWithJev/blob/4a223dcf927b14b1b17beb467697cc6c8a25e7a1/src/ai/jevPlayer.ts) and [`jevWorkflow.ts`](https://github.com/vlaier/chessWithJev/blob/4a223dcf927b14b1b17beb467697cc6c8a25e7a1/src/ai/jevWorkflow.ts) send one `/v1/systemone` choice question per step; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [vlaier](https://github.com/vlaier). Independently curated. |
| Format | React 19 + Vite web app (dev/preview server) |
| Platform and availability | Web browser via the local Vite dev or preview server (a static build has no Jev proxy). |
| Jev's role | Chooses each move step (focus, piece, destination) and the post-move commentary; rules engine and legality are code. |
| Requirements | Node.js/npm and `JEV_API_KEY` in `.env`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |

## When to use

- Play against a typed-decision model and see why it moved.
- Experiment with question design by editing the workflow steps.
- Mismatch: not a strong engine; falls back to a random legal move if the API fails.

## How it works

A dependency-free rules engine in `src/engine/` generates legal moves; each workflow step is one Jev call with FEN and earlier answers as state and the legal options as choices. A Vite plugin (`vite-plugins/jevProxy.ts`) keeps the key server-side.

## Get started

Clone, add your key and start the dev server (README):

```sh
git clone https://github.com/vlaier/chessWithJev && cd chessWithJev
npm install
echo 'JEV_API_KEY=...' > .env
npm run dev
```

Each move makes several Jev requests billed to your TypeSafe key.

## Examples and demos

- README *How Jev plays* and *Editing the workflow*.

## Limits and data handling

Board positions and your workflow prompts go to TypeSafe. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 4a223dcf927b](https://github.com/vlaier/chessWithJev/tree/4a223dcf927b14b1b17beb467697cc6c8a25e7a1). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
