# Gomoku × Jev

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Five-in-a-row against Jev on a Three.js 3D board (README in Chinese): local heuristics propose up to ten tactically labelled moves and Jev picks one with a Choice question, showing the pick and its confidence in the status bar.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fanweiya/gomoku-jev) |
| Maintainer | [fanweiya](https://github.com/fanweiya). Independently curated. |
| Format | Vite + Three.js web game with a server-side proxy for the key |
| Requirements | Node and npm; a TypeSafe key (or a compatible endpoint). |
| License | [MIT](https://github.com/fanweiya/gomoku-jev/blob/82947ddfd936972674e95061e0ea6ace9cae8515/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/game/JevClient.ts`](https://github.com/fanweiya/gomoku-jev/blob/82947ddfd936972674e95061e0ea6ace9cae8515/src/game/JevClient.ts) at the pinned commit. |

## When to use

- Play a quick game against a decision model and watch its confidence per move.
- Borrow the pattern: code generates and labels legal candidates, Jev only chooses among them.
- Mismatch: the heuristic candidates do much of the work; a demo, not a strong engine.

## How it works

The browser posts the board and labelled candidates (win, block an open four, make an open three) to a Vite server proxy, which calls Jev with `jev-latest` and a Choice question; the key never reaches the browser. Integration evidence: [`src/game/JevClient.ts`](https://github.com/fanweiya/gomoku-jev/blob/82947ddfd936972674e95061e0ea6ace9cae8515/src/game/JevClient.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
echo "JEV_API_KEY=your-key" > .env.local
npm run dev        # http://127.0.0.1:5188
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshots in `docs/screenshots/`.

## Limits and data handling

Board positions go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 82947ddfd936](https://github.com/fanweiya/gomoku-jev/tree/82947ddfd936972674e95061e0ea6ace9cae8515). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
