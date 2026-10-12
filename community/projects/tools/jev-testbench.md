# jev-testbench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Lightweight, auditable testbench that probes Jev as a typed probabilistic decision primitive, logs every call to append-only JSONL, labels every claim by evidence type, and reports a negative headline result (`NO_STRONG_JEV_SPECIFIC_NOVEL_FINDING_YET`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Charlie-Wang-03/jev-testbench) |
| Maintainer | [Charlie-Wang-03](https://github.com/Charlie-Wang-03). Independently curated. |
| Format | Python research harness (uv) |
| Requirements | Python 3.13+, uv; a TypeSafe account only for live reproduction. |
| License | [MIT](https://github.com/Charlie-Wang-03/jev-testbench/blob/44463f065f3cfb4ec4ae3001707385d24e09733d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Reproduce small, budget-capped Jev capability probes with explicit call ceilings.
- Read an evidence-labelled example of what you cannot conclude from small samples.
- Mismatch: Small sample (42 core + 12 P3 records); not a benchmark of model quality.

## How it works

Experiments send typed questions through a client with credential hygiene; offline tests block sockets; reports and an evidence freeze are generated from the recorded logs. Jev integration: [`src/jev_lab/client.py`](https://github.com/Charlie-Wang-03/jev-testbench/blob/44463f065f3cfb4ec4ae3001707385d24e09733d/src/jev_lab/client.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Charlie-Wang-03/jev-testbench.git
cd jev-testbench
uv run pytest
uv run python -m jev_lab report
```

## Limits and data handling

Live runs need a TypeSafe key and an explicit budget. Results are the maintainer's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 44463f065f3c](https://github.com/Charlie-Wang-03/jev-testbench/tree/44463f065f3cfb4ec4ae3001707385d24e09733d). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
