# JEV Trading Command Center

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper-trading research app (README in Traditional Chinese) where Jev decisions pass validation and risk checks before a simulated broker acts, shown in an animated 3D command center with model 'pets' and an offline demo that uses only synthetic data.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mars-tw/jev-trading-command-center) |
| Maintainer | [mars-tw](https://github.com/mars-tw). Independently curated. |
| Format | Local Python web app with a Three.js 3D front end |
| Requirements | Python 3.11+ and a WebGL browser; the offline demo needs no packages or keys; live paper mode needs `requirements.txt` and a TypeSafe key. |
| License | [MIT](https://github.com/mars-tw/jev-trading-command-center/blob/75f9c79eb08a3f2cb6a9724ea5ac1c7935e3df78/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scanner/jev_decision.py`](https://github.com/mars-tw/jev-trading-command-center/blob/75f9c79eb08a3f2cb6a9724ea5ac1c7935e3df78/scanner/jev_decision.py) at the pinned commit. |

## When to use

- Watch a decision model drive a paper-trading loop with every receipt, wait and risk rejection shown.
- Study how to validate a Jev Choice answer (known option, matches the top probability) before acting on it.
- Mismatch: paper trading only; no exchange order placement; not financial advice.

## How it works

The scanner gathers public market data and `scanner/jev_client.py` asks Jev at `https://api.typesafe.ai/v1/systemone` for a decision. `scanner/jev_decision.py` rejects answers whose choice is unknown or is not the highest-probability option, and risk controls can still refuse. Only an executed receipt shows as a pass; the in-app PaperBroker simulates fills. Integration evidence: [`scanner/jev_decision.py`](https://github.com/mars-tw/jev-trading-command-center/blob/75f9c79eb08a3f2cb6a9724ea5ac1c7935e3df78/scanner/jev_decision.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -B run_app.py --demo --port 8775        # offline synthetic demo
python -m venv .venv && .venv/bin/python -m pip install -r requirements.txt
export TYPESAFE_API_KEY=...
.venv/bin/python -B run_app.py --real-paper --port 8765
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- 70-second showcase video: [github.com/mars-tw/jev-trading-command-center/releases/tag/v0.1.0](https://github.com/mars-tw/jev-trading-command-center/releases/tag/v0.1.0)
- tests/test_jev_decision.py

## Limits and data handling

Live paper mode contacts public market data and TypeSafe on your key. Model confidence is not a win rate, per the README. Simulated trades only.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 75f9c79eb08a](https://github.com/mars-tw/jev-trading-command-center/tree/75f9c79eb08a3f2cb6a9724ea5ac1c7935e3df78). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
