# Railroad Route

[All projects](../README.md) · [Web apps](README.md#web-apps)

Mine-cart track puzzle: lay and turn track pieces, then write the cart a one-sentence note; TypeSafe Jev-operated switches read the sentence and decide which way to send it, and each level forbids the obvious words, so you must describe the goal indirectly (English or Portuguese).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vinicius-francozo/railroad-route) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/vinicius-francozo/railroad-route#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the MIT source build; requires a TypeSafe key (server key or your own, per README *Keys, quota and privacy*), billed by TypeSafe. Checked 2026-10-08. |
| Jev evidence | [`backend/railroad/jev.py`](https://github.com/vinicius-francozo/railroad-route/blob/8cfbad52c56839fc7173abfaa838de53a4ee16f0/backend/railroad/jev.py) asks the switch questions; recorded Jev fixtures live in [`backend/tests/fixtures/jev/`](https://github.com/vinicius-francozo/railroad-route/tree/8cfbad52c56839fc7173abfaa838de53a4ee16f0/backend/tests/fixtures/jev). Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [vinicius-francozo](https://github.com/vinicius-francozo). Independently curated. |
| Format | Web game (Vite front end + Python FastAPI backend) |
| Platform and availability | Web browser via local dev servers or your own deployment. |
| Jev's role | Each switch is a Jev decision on the player's sentence; board, rules and scoring are code. |
| Requirements | Python 3.12, Node `^20.19` or `>=22.12`, and a TypeSafe API key. |
| License | [MIT](https://github.com/vinicius-francozo/railroad-route/blob/8cfbad52c56839fc7173abfaa838de53a4ee16f0/LICENSE). |

## When to use

- Play a word puzzle built around how a decision model reads indirect descriptions.
- See a small, tested example of Jev choices driving game state.
- Mismatch: puzzle game, not a general tool.

## How it works

The backend simulates the cart square by square; at each switch it sends the note and the switch's options to Jev, and the answer chooses the branch. Forbidden-word checks run in code before any request.

## Get started

Run locally (README *Running it locally*):

```sh
git clone https://github.com/vinicius-francozo/railroad-route && cd railroad-route
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt && npm ci
export TYPESAFE_API_KEY=...
.venv/bin/uvicorn railroad.app:app --app-dir backend --port 8000 &
npm run dev
```

Each run sends one Jev request per switch on the path, billed by TypeSafe.

## Examples and demos

- README *How a level works* and *What was measured*.

## Limits and data handling

Your note goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 8cfbad52c568](https://github.com/vinicius-francozo/railroad-route/tree/8cfbad52c56839fc7173abfaa838de53a4ee16f0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
