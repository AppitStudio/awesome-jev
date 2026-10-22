# Agent Chess (Claude vs Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local chess board styled after chess.com where Claude models and Jev play each other, with per-side engine settings, Jev move probabilities in the live view, a per-run spend cap and server-side legality checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bakirgdev/agent-chess) |
| Maintainer | [bakirgdev](https://github.com/bakirgdev). Independently curated. |
| Format | Local web app (Node.js) |
| Requirements | Node.js 22.9+; `ANTHROPIC_API_KEY` and/or `TYPESAFE_API_KEY` (mock mode needs none). |
| License | [MIT](https://github.com/bakirgdev/agent-chess/blob/3b71996decd50fc673b54f81efd310a1177ca663/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.js`](https://github.com/bakirgdev/agent-chess/blob/3b71996decd50fc673b54f81efd310a1177ca663/jev.js) at the pinned commit. |

## When to use

- Compare Jev's move choices with Claude models on the same position.
- Show Jev choice probabilities in a fun, visual demo.
- Mismatch: a demo, not a chess engine; Jev picks among legal moves.

## How it works

The server rebuilds the position from the move history and `jev.js` asks Jev at `https://api.typesafe.ai/v1/systemone` to choose one of the legal moves; the returned move is checked before it is accepted. Integration evidence: [`jev.js`](https://github.com/bakirgdev/agent-chess/blob/3b71996decd50fc673b54f81efd310a1177ca663/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bakirgdev/agent-chess.git
cd agent-chess
npm install
cp .env.example .env   # add your keys
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quick start and env vars in the README: [github.com/bakirgdev/agent-chess#readme](https://github.com/bakirgdev/agent-chess#readme)

## Limits and data handling

Positions are sent to TypeSafe and Anthropic for the engines you pick; `BUDGET_USD` caps spend per server run.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 3b71996decd5](https://github.com/bakirgdev/agent-chess/tree/3b71996decd50fc673b54f81efd310a1177ca663). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
