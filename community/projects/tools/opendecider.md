# OpenDecider

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open System One decision models (typed choice/score/yes-no) with calibrated probabilities; optional Jev-compatible `/v1/systemone` server—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/manjunathshiva/opendecider) |
| Maintainer | [manjunathshiva](https://github.com/manjunathshiva). Independently curated. |
| Format | Python package + HF weights (nano/small/…) with optional serve/MLX extras. |
| Requirements | Python ≥ 3.10; `pip install opendecider` (weights download on first use). |
| License | [Apache-2.0](https://github.com/manjunathshiva/opendecider/blob/9a51b05c50c2a1e1daba1b5752a7073bd6eb5075/LICENSE) (GitHub license API may show NOASSERTION; LICENSE file is Apache-2.0). Independent open weights—not TypeSafe-hosted Jev. |
| Disclosure | Independent of hosted TypeSafe Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream benchmark claims vs Jev/Laya not re-run on the review host. |

## When to use

Use when you want a local/open System One alternative or a drop-in `/v1/systemone` base URL. Prefer hosted TypeSafe Jev for the commercial API.

## How it works

`model.system_one(state, questions)` returns calibrated choice/score/noul answers. `opendecider serve` speaks TypeSafe’s `/v1/systemone` so existing SDK clients can point `TYPESAFE_BASE_URL` at localhost.

## Get started

```sh
pip install opendecider
# or clone:
git clone https://github.com/manjunathshiva/opendecider.git
cd opendecider
git checkout 9a51b05c50c2a1e1daba1b5752a7073bd6eb5075
```

## Examples and demos

- HF Space demo and Colab linked from upstream README.
- COMPARISON.md benchmarks (upstream-reported; not re-run here).

## Limits and data handling

Local inference keeps data on-device; serve mode is operator-hosted. Catalog checks did not download weights or run serve.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 9a51b05](https://github.com/manjunathshiva/opendecider/tree/9a51b05c50c2a1e1daba1b5752a7073bd6eb5075). AI-assisted README and LICENSE inspection; install/live paths not executed.
