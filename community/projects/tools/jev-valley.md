# Jev Valley (simulated valley where rabbits, deer and wolves decide with Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Small ecosystem simulation where every animal picks its next action once per valley hour with one Choice question and a few Score and Noul questions, watched live in a 3D browser viewer, with replays and month-long result notes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sarthak8696/jev-valley) |
| Maintainer | [Sarthak8696](https://github.com/Sarthak8696). Independently curated. |
| Format | Python simulation with WebGL viewer |
| Requirements | Python 3.11+ and a WebGL browser; a TypeSafe API key (there is no offline mode). |
| License | [MIT](https://github.com/Sarthak8696/jev-valley/blob/64ee8e6f1474bc666c63ad18056c09e9fa3ce771/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`valley/brains/system_one.py`](https://github.com/Sarthak8696/jev-valley/blob/64ee8e6f1474bc666c63ad18056c09e9fa3ce771/valley/brains/system_one.py) at the pinned commit. |

## When to use

- Watch typed decisions drive emergent behaviour without any scripted moves.
- Replay a finished run for free in the browser.
- Mismatch: needs a key to run at all; balance is still being tuned.

## How it works

`valley/brains/system_one.py` posts each animal's situation to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default; `TYPESAFE_BASE_URL` can point elsewhere) and applies the chosen action. Integration evidence: [`valley/brains/system_one.py`](https://github.com/Sarthak8696/jev-valley/blob/64ee8e6f1474bc666c63ad18056c09e9fa3ce771/valley/brains/system_one.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Sarthak8696/jev-valley.git && cd jev-valley
python3 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev,charts]"
export TYPESAFE_API_KEY=...
python -m valley live --seed 7 --days 2 --open
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/Sarthak8696/jev-valley#readme](https://github.com/Sarthak8696/jev-valley#readme)

## Limits and data handling

Simulation state goes to TypeSafe; long runs make many calls. Results are the author's own.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 64ee8e6f1474](https://github.com/Sarthak8696/jev-valley/tree/64ee8e6f1474bc666c63ad18056c09e9fa3ce771). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
