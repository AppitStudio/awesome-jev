# Astra + Jev: Fallout: New Vegas (source of a supervised main-story run where Jev made the gameplay choices)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Python agent controller behind a recorded, supervised Fallout: New Vegas main-story run: Jev made frequent bounded gameplay choices through normal keyboard and mouse controls while the controller handled recording gates, watchdogs and recovery. Includes a budget-reserving decision client and 147 regression tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0mis/astra-jev-new-vegas) |
| Maintainer | [0mis](https://github.com/0mis). Independently curated. |
| Format | Python controller (Windows) |
| Requirements | Windows, Python 3.12, an owned Steam copy of Fallout: New Vegas 1.4.0.525, `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/0mis/astra-jev-new-vegas/blob/bb9cfcd82d2dc275f8563d74d8f8fe415640addf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_bridge.py`](https://github.com/0mis/astra-jev-new-vegas/blob/bb9cfcd82d2dc275f8563d74d8f8fe415640addf/jev_bridge.py) at the pinned commit. |

## When to use

- Study how a supervised agent controller bounds and audits many small Jev decisions in a long game run.
- Mismatch: it is not a one-command unattended game player; the run needed substantial development and intervention.

## How it works

`jev_bridge.py` is a bounded Jev client that reads `TYPESAFE_API_KEY` from the environment and reserves budget in a usage ledger before each call; the controller turns game telemetry into typed questions and acts on the answers, with an independent watchdog that stops repeated failed plans. Integration evidence: [`jev_bridge.py`](https://github.com/0mis/astra-jev-new-vegas/blob/bb9cfcd82d2dc275f8563d74d8f8fe415640addf/jev_bridge.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -p 'test_*.py' -q
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Recorded main-story run: [youtu.be/tBVq09mDq6g](https://youtu.be/tBVq09mDq6g)
- Presentation on X: [x.com/imjustnewatai/status/2102934229180875054](https://x.com/imjustnewatai/status/2102934229180875054)

## Limits and data handling

Game state summaries are sent to TypeSafe. Back up saves and settings first; the README warns that the capture is not gap-free and the tests cover observed failure modes only. Independent project; not affiliated with TypeSafe or the game's publishers.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit bb9cfcd82d2d](https://github.com/0mis/astra-jev-new-vegas/tree/bb9cfcd82d2dc275f8563d74d8f8fe415640addf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
