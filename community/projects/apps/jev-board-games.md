# Jev 棋馆 (Jev board games)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser board-game hall (Gomoku, Go 9x9, Xiangqi, chess, checkers, Chinese checkers) where TypeSafe Jev chooses moves, with a deterministic safety layer and a Cloudflare Worker + D1 record book.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tripodxu/board-games) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/tripodxu/board-games#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`src/core/jev/client.ts`](https://github.com/tripodxu/board-games/blob/591e7220f66d2e70dc460588d2ee8db93b3a5381/src/core/jev/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tripodxu](https://github.com/tripodxu). Independently curated. |
| Format | Static web app (Vite + TypeScript) with a Cloudflare Worker backend |
| Platform and availability | Web (self-hosted or the author's deployment; source build) |
| Jev's role | Jev chooses each move from candidates; code enforces legality and safety checks. |
| Requirements | Node.js to build; your own TypeSafe key (BYOK, stored in your browser). |
| License | [MIT](https://github.com/tripodxu/board-games/blob/591e7220f66d2e70dc460588d2ee8db93b3a5381/LICENSE) |

## When to use

- Play board games against a decision model and inspect its move choices.
- Study how a deterministic safety layer combines with model choices (wins, draws and losses all reported).
- Mismatch: Chinese-language UI and docs.

## How it works

Each turn the client sends the board state and candidate moves to Jev as a choice question; deterministic rules guard illegal or blunder moves. A Worker + D1 backend stores game records, stats and a leaderboard, falling back to localStorage without a backend. Integration evidence: [`src/core/jev/client.ts`](https://github.com/tripodxu/board-games/blob/591e7220f66d2e70dc460588d2ee8db93b3a5381/src/core/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture notes: `docs/adr/` and `docs/plans/` in the repository.

## Limits and data handling

Board states go to TypeSafe with your key from the browser; game records can be stored in the operator's D1 database.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 591e7220f66d](https://github.com/tripodxu/board-games/tree/591e7220f66d2e70dc460588d2ee8db93b3a5381). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
