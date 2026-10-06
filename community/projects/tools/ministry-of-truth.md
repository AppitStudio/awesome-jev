# Ministry of Truth

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Spin-doctor web game: over a 15-day campaign you write cover stories in free text and five literal-minded Jev factions score every word — affect, credibility, salience, compliance, narrative fit — fully playable offline with a mock ensemble or live through a local key-holding proxy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LukasPodhorny/ministry-of-truth) |
| Maintainer | [LukasPodhorny](https://github.com/LukasPodhorny). Independently curated. |
| Format | Browser game + zero-dependency Node server (`npm start`) |
| Requirements | Node.js; optional `TYPESAFE_API_KEY` in `.env` for live Jev (kept server-side). |
| License | **No LICENSE file** in the reviewed tree — publicly readable source with unspecified reuse terms (source available, not Open source). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Explore how score, noul best-of-3 and choice questions can stand in for a panel of reactions to free text.
- Play offline with the built-in mock ensemble, then compare live Jev judgments.
- Mismatch: entertainment; no LICENSE, so reuse terms are unspecified.

## How it works

[`src/jev.js`](https://github.com/LukasPodhorny/ministry-of-truth/blob/abf2f5ed84f2d90fa21d666baa103641811ce3d7/src/jev.js) holds text features, strategy detection, the mock ensemble and the Jev client; [`server.mjs`](https://github.com/LukasPodhorny/ministry-of-truth/blob/abf2f5ed84f2d90fa21d666baa103641811ce3d7/server.mjs) proxies live requests to `api.typesafe.ai/v1/systemone` (`jev-latest`). Any failure falls back to the offline “Standby Tribunal” with an on-screen banner.

## Get started

Run the game (offline by default):

```sh
git clone https://github.com/LukasPodhorny/ministry-of-truth.git && cd ministry-of-truth
npm start            # http://localhost:8077
# live mode: put TYPESAFE_API_KEY in .env, then Settings → Jev Evaluator → Live Jev → Test live connection
```

Live mode makes one batched Jev request per briefing, billed to your key; offline mode is free.

## Examples and demos

- In-game *How to Play* primer; `npm run calibrate` sends 12 fixtures to the live API (opt-in).
- README *Jev integration* contract.

## Limits and data handling

Your drafts are sent to TypeSafe in live mode. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit abf2f5ed84f2](https://github.com/LukasPodhorny/ministry-of-truth/tree/abf2f5ed84f2d90fa21d666baa103641811ce3d7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
