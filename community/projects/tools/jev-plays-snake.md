# jev plays snake

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Browser Snake where code computes legal moves and exact facts (food distance, flood-fill reachable cells, dead ends) and TypeSafe Jev picks one move per tick with a single `choice` question through a small Hono proxy; misses the deadline → the snake goes straight.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hoanganh25991/typesafe-jev) |
| Maintainer | [hoanganh25991](https://github.com/hoanganh25991). Independently curated. |
| Format | Local web demo (pnpm dev: UI + proxy) |
| Requirements | Node.js with pnpm; `TYPESAFE_API_KEY` in `.env` (held by the proxy, never in the browser). |
| License | **No LICENSE file** in the reviewed tree — publicly readable source with unspecified reuse terms (source available, not Open source). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Demo real-time decisions with a fixed tick clock and a safe fallback move.
- Copy the pattern: code enumerates legal options and fact strings; Jev chooses.
- Mismatch: a demo game; no LICENSE, so reuse terms are unspecified.

## How it works

The browser posts the board to `POST /api/decide`; the proxy ([`server/index.ts`](https://github.com/hoanganh25991/typesafe-jev/blob/3dba24ad048d38e44994434cdaab247e4f6c2871/server/index.ts)) builds state plus one choice question with per-move facts ([`src/jev/prompt.ts`](https://github.com/hoanganh25991/typesafe-jev/blob/3dba24ad048d38e44994434cdaab247e4f6c2871/src/jev/prompt.ts)) and calls Jev; the controller plays whatever arrived by the end of the tick.

## Get started

Run locally with your key:

```sh
git clone https://github.com/hoanganh25991/typesafe-jev.git && cd typesafe-jev
cp .env.example .env   # set TYPESAFE_API_KEY
pnpm install
pnpm dev               # web http://localhost:5188, proxy http://127.0.0.1:8787
```

Every tick is a Jev request billed to your key.

## Examples and demos

- README *One tick* walkthrough showing the exact request and response.
- `pnpm test` engine/controller tests.

## Limits and data handling

No published performance claims checked. Board state goes to TypeSafe. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 3dba24ad048d](https://github.com/hoanganh25991/typesafe-jev/tree/3dba24ad048d38e44994434cdaab247e4f6c2871). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
