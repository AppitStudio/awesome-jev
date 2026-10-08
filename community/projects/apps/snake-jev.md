# Snake × Jev

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser Snake played by TypeSafe Jev with a live panel of every call — the state sent, the one choice question asked and Jev's probabilities; code only describes what the snake sees and where the food is, shuffles option order each turn and never overrides Jev's move. Distinct from the listed *jev plays snake*.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/michaelmld/snake-jev) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/michaelmld/snake-jev#readme) (source-built app; no hosted version verified). |
| Pricing and access | No app fee; requires your own `TYPESAFE_API_KEY` in `.env` (usage billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`server.js`](https://github.com/michaelmld/snake-jev/blob/3fc6682fe9c3a95b60da39a7f36ace640e171371/server.js) proxies calls to `https://api.typesafe.ai/v1/systemone` and [`public/game.js`](https://github.com/michaelmld/snake-jev/blob/3fc6682fe9c3a95b60da39a7f36ace640e171371/public/game.js) builds the per-turn state and question. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [michaelmld](https://github.com/michaelmld). Independently curated. |
| Format | Node web app (no dependencies) |
| Platform and availability | Web browser via a local Node 18+ server. |
| Jev's role | Chooses every move from what the snake observes; code applies it as-is. |
| Requirements | Node 18+ and `TYPESAFE_API_KEY` in `.env`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |

## When to use

- Demo how a decision model behaves with minimal, unhinted state.
- Download exact request/response JSON for each turn to study question design.
- Mismatch: a toy; Jev is not given which moves are safe, so it can lose.

## How it works

Each turn the server sends two state fields (what lies in each allowed direction, food position) and one choice question; retries handle `model_unavailable`, 429 and 5xx. You can let Jev drive or steer yourself, step one decision at a time, and pause after each move.

## Get started

Copy the env file, add your key and start (README *Run it*):

```sh
git clone https://github.com/michaelmld/snake-jev.git && cd snake-jev
cp .env.example .env   # set TYPESAFE_API_KEY
npm start              # http://localhost:3000
```

One Jev request per move, billed to your TypeSafe key.

## Examples and demos

- README *How Jev plays* and *Controls* (Download JSON of every call).

## Limits and data handling

Game state goes to TypeSafe; the key stays server-side. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 3fc6682fe9c3](https://github.com/michaelmld/snake-jev/tree/3fc6682fe9c3a95b60da39a7f36ace640e171371). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
