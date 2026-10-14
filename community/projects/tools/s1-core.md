# S1-Core

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Python harness for System 1 decision models like Jev: choice/score/noul specs, fail-closed calibration gates, wave-parallel fan-out and a replayable audit ledger.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/acbcore-labs/s1-core) |
| Maintainer | [acbcore-labs](https://github.com/acbcore-labs). Independently curated. |
| Format | Python library |
| Requirements | Python 3.14+; TypeSafe API key for the Jev driver. |
| License | [MIT](https://github.com/acbcore-labs/s1-core/blob/a42288c78a8d34d04b7cfa4edb524b415270bdfd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/s1core/config.py`](https://github.com/acbcore-labs/s1-core/blob/a42288c78a8d34d04b7cfa4edb524b415270bdfd/src/s1core/config.py) at the pinned commit. |

## When to use

- Wrap Jev (or local decision models) in a deterministic control loop with calibration gates.
- Keep a hash-chained, replayable record of every decision.
- Mismatch: harness only; you bring the backend.

## How it works

A driver configured from `TYPESAFE_API_KEY` sends compiled questions to Jev; verdicts carry probabilities, confidence, margin and a replay digest, and only ratified values pass the gate. Integration evidence: [`src/s1core/config.py`](https://github.com/acbcore-labs/s1-core/blob/a42288c78a8d34d04b7cfa4edb524b415270bdfd/src/s1core/config.py).

## Get started

From a clone of the repository (not run on the review host):

```sh
pip install -e .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Examples: `examples/refund_triage.py`, `examples/orthogonal_pr_gate.py`.

## Limits and data handling

State goes to TypeSafe when the Jev driver is used and is billed to your key; the ledger is stored locally.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit a42288c78a8d](https://github.com/acbcore-labs/s1-core/tree/a42288c78a8d34d04b7cfa4edb524b415270bdfd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
