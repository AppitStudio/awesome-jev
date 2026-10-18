# SafeDecide

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Certified automate/escalate thresholds for System One decision models (Jev, Clef, d3, Laya, …): pick the lowest confidence line that keeps automated error rate under a bound on labeled data, plus a 140M on-device model and adapters for `/v1/systemone`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yotambraun/safedecide) |
| Maintainer | [yotambraun](https://github.com/yotambraun). Independently curated. |
| Format | Python library + 140M model + Hugging Face Spaces demo |
| Requirements | Python; labeled decisions for certification; optional remote System One endpoint. |
| License | [Apache-2.0](https://github.com/yotambraun/safedecide/blob/968eda1b6865bd9c27c76e7ca4938bf12502ef83/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/safedecide/adapters.py`](https://github.com/yotambraun/safedecide/blob/968eda1b6865bd9c27c76e7ca4938bf12502ef83/src/safedecide/adapters.py) at the pinned commit. |

## When to use

- Need a statistically certified act-vs-escalate cutoff instead of eyeballing confidence.
- Want the same guarantee on top of Jev or other System One servers.
- Mismatch: calibration library + small model; not a hosted Jev replacement.

## How it works

`adapters.py` speaks `POST /v1/systemone` for Jev-compatible servers. The library fits binomial-certified thresholds on labeled automate/escalate outcomes and can run its own 140M decision model locally or in-browser. Integration evidence: [`src/safedecide/adapters.py`](https://github.com/yotambraun/safedecide/blob/968eda1b6865bd9c27c76e7ca4938bf12502ef83/src/safedecide/adapters.py).

## Get started

pip install safedecide or open the Hugging Face Space demo.

```sh
pip install safedecide
# see README for certify() on labeled decisions; demo: https://huggingface.co/spaces/yotambr/safedecide
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [huggingface.co/spaces/yotambr/safedecide](https://huggingface.co/spaces/yotambr/safedecide)
- [huggingface.co/yotambr/safedecide-140m](https://huggingface.co/yotambr/safedecide-140m)

## Limits and data handling

Certification quality depends on label volume and i.i.d. assumptions. Remote adapters send state to the configured host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 968eda1b6865](https://github.com/yotambraun/safedecide/tree/968eda1b6865bd9c27c76e7ca4938bf12502ef83). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
