# systemone-probe

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Conformance and behaviour test harness for System One endpoints (TypeSafe Jev or self-hosted Jev-like models): checks the answer contract, Python-computed accuracy, calibration, determinism, batching, robustness and limits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mokko/systemone-probe) |
| Maintainer | [mokko](https://github.com/mokko). Independently curated. |
| Format | Python CLI (stdlib runtime) with an offline mock endpoint |
| Requirements | Python with uv; a TypeSafe API key or any `POST /v1/systemone` endpoint; no key needed for the mock. |
| License | [MIT](https://github.com/mokko/systemone-probe/blob/4da11b2eef0c682e3a24233b79c326a6bdf2107b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone_probe/client.py`](https://github.com/mokko/systemone-probe/blob/4da11b2eef0c682e3a24233b79c326a6bdf2107b/src/systemone_probe/client.py) at the pinned commit. |

## When to use

- Check whether a self-hosted Jev-compatible model actually honours the documented contract before swapping it in.
- Measure calibration and determinism of an endpoint with labels computed in code rather than by a judge.
- Mismatch: probes synthetic task families; it says little about accuracy on your own domain.

## How it works

`client.py` posts typed questions to `<base-url>/v1/systemone` (default `https://api.typesafe.ai`). Suites verify probability sums, arg-max agreement, the documented score and confidence formulas, Brier and ECE calibration, repeat drift and batching behaviour, and write `report.md` and `report.json`. Integration evidence: [`src/systemone_probe/client.py`](https://github.com/mokko/systemone-probe/blob/4da11b2eef0c682e3a24233b79c326a6bdf2107b/src/systemone_probe/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv venv .venv && uv pip install -p .venv -e . pytest
source .venv/bin/activate
systemone-probe selfcheck
export TYPESAFE_API_KEY=sk-...
systemone-probe run --base-url https://api.typesafe.ai --model jev-latest --out runs/jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Offline reference endpoint: `systemone-probe mock`.
- Cost and egress notes in the README.

## Limits and data handling

Probe items go to the endpoint you point it at; a full run against TypeSafe spends credits on your key.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 4da11b2eef0c](https://github.com/mokko/systemone-probe/tree/4da11b2eef0c682e3a24233b79c326a6bdf2107b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
