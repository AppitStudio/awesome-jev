# Race Calls (timestamped F1 race predictions from TypeSafe Jev, scored after every race)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Public experiment: before each 2026 Grand Prix TypeSafe Jev makes timestamped calls, which are scored after the race against two simple baselines, with the full season record (hits and misses) on a React site.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/herambbbb/race-calls) |
| Maintainer | [herambbbb](https://github.com/herambbbb). Independently curated. |
| Format | Python pipeline + GitHub Actions + React site (MIT) |
| Requirements | Python 3.12 and a TypeSafe API key (or OpenRouter) for live calls; tests run offline. |
| License | [MIT](https://github.com/herambbbb/race-calls/blob/054272c144aea7250645195c21a5b47eafa33a2f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipeline/src/race_calls/jev.py`](https://github.com/herambbbb/race-calls/blob/054272c144aea7250645195c21a5b47eafa33a2f/pipeline/src/race_calls/jev.py) at the pinned commit. |

## When to use

- See how Jev's calibrated calls hold up on real sports outcomes.
- Reuse a predict-then-score pattern with baselines.
- Mismatch: one season of a single sport; not betting advice.

## How it works

`pipeline/src/race_calls/jev.py` posts typed questions to `https://api.typesafe.ai/v1/systemone` and records the dated model version so results are pinned; pre-race and post-race workflows commit predictions and scores. Integration evidence: [`pipeline/src/race_calls/jev.py`](https://github.com/herambbbb/race-calls/blob/054272c144aea7250645195c21a5b47eafa33a2f/pipeline/src/race_calls/jev.py).

## Get started

Clone, read the five-minute case study, and run the offline test suite; live calls need a key.

```sh
git clone https://github.com/herambbbb/race-calls.git && cd race-calls
export TYPESAFE_API_KEY=...
cd pipeline && pip install -e . && pytest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/herambbbb/race-calls/blob/054272c144aea7250645195c21a5b47eafa33a2f/README.md](https://github.com/herambbbb/race-calls/blob/054272c144aea7250645195c21a5b47eafa33a2f/README.md)

## Limits and data handling

Only public race data is sent to TypeSafe; predictions and scores are committed publicly.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 054272c144ae](https://github.com/herambbbb/race-calls/tree/054272c144aea7250645195c21a5b47eafa33a2f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
