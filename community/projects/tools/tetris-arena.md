# Tetris Arena (SAP-RPT-1 vs. Jev vs. LLMs vs. a heuristic on the same pieces, with live costs)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Browser Tetris tournament where SAP-RPT-1, Jev, any LLM and a 15-line El-Tetris heuristic play the same seeded pieces from the same candidate moves while cost and latency are tracked live; the write-up compares three briefings for Jev and finds a well-briefed cheap model and the heuristic play about as well as anything else.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arndth/tetrisarena) |
| Maintainer | [arndth](https://github.com/arndth). Independently curated. |
| Format | Browser app with a small Node.js server (no build step) |
| Requirements | Node.js 18+ and a modern browser; a TypeSafe or OpenRouter key for Jev, plus keys for any other backends you enable. |
| License | [MIT](https://github.com/arndth/tetrisarena/blob/25e67ab85369255f4aa31933eeebb378e1059ac7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`js/picker-jev.js`](https://github.com/arndth/tetrisarena/blob/25e67ab85369255f4aa31933eeebb378e1059ac7/js/picker-jev.js) at the pinned commit. |

## When to use

- Compare decision models, LLMs and a heuristic on one controlled game with real cost numbers.
- Study how changing a Jev briefing changes its play.
- Mismatch: a demo and write-up; results are the author's.

## How it works

`js/picker-jev.js` builds a Choice over the candidate placements and the local `server.mjs` forwards it to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) or OpenRouter's `/api/v1/systemone` (`~typesafe/jev-latest`), so the key stays on the server. Integration evidence: [`js/picker-jev.js`](https://github.com/arndth/tetrisarena/blob/25e67ab85369255f4aa31933eeebb378e1059ac7/js/picker-jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/arndth/tetrisarena.git && cd tetrisarena
cp .env.example .env   # add TYPESAFE_API_KEY or OPENROUTER_API_KEY
node server.mjs        # http://localhost:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README and race video: [github.com/arndth/tetrisarena#readme](https://github.com/arndth/tetrisarena#readme)

## Limits and data handling

Board summaries and candidate moves go to the providers you enable, via the local server. Cost and quality comparisons are the author's.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 25e67ab85369](https://github.com/arndth/tetrisarena/tree/25e67ab85369255f4aa31933eeebb378e1059ac7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
