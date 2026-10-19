# jevelin

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reference design for fast, low-cost real-time voice agents: small per-turn decisions (card number read-out, wants a human, risky draft) go to a System One classifier such as Jev off the critical path, scheduled as a dependency graph, with a browser demo running the same engine.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/henryzhangpku/jevelin) |
| Maintainer | [henryzhangpku](https://github.com/henryzhangpku). Independently curated. |
| Format | Python reference design + Pyodide browser demo |
| Requirements | Python 3.10+; no keys for the simulated runs; a hosted classifier key (`CLASSIFIER_API_KEY` or `TYPESAFE_API_KEY`) for live runs. |
| License | [MIT](https://github.com/henryzhangpku/jevelin/blob/afc1ffbcbb39ccd80bbe412755cafba8c1c72aca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevelin/backends.py`](https://github.com/henryzhangpku/jevelin/blob/afc1ffbcbb39ccd80bbe412755cafba8c1c72aca/jevelin/backends.py) at the pinned commit. |

## When to use

- Cut time to first audio by taking classification off a voice agent's critical path.
- Compare baseline and fast-path pipelines on your own latency and price profile.
- Mismatch: headline numbers are simulated from an illustrative profile, not production traffic.

## How it works

Each turn is scheduled as a dependency graph, so the classifier runs alongside the conversation instead of in front of it. `jevelin/backends.py` connects the hosted classifier (reading `CLASSIFIER_API_KEY` or `TYPESAFE_API_KEY`), a mock, and Laya as interchangeable backends; risky drafts are blocked and failures close safely. Integration evidence: [`jevelin/backends.py`](https://github.com/henryzhangpku/jevelin/blob/afc1ffbcbb39ccd80bbe412755cafba8c1c72aca/jevelin/backends.py).

## Get started

From the upstream README: run the simulated comparison with no dependencies, or install the hosted extra for live classifier calls.

```sh
python -m jevelin compare
python -m jevelin trace --call 0
pip install -e ".[hosted]"
python -m jevelin compare --classifier hosted --calls 20
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [henryzhangpku.github.io/jevelin/](https://henryzhangpku.github.io/jevelin/)

## Limits and data handling

Simulated numbers depend on the bundled latency and price profile; replace it with your own measurements. Live runs send turn text to the classifier provider.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit afc1ffbcbb39](https://github.com/henryzhangpku/jevelin/tree/afc1ffbcbb39ccd80bbe412755cafba8c1c72aca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
