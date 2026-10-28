# Dadvar (open training data, training and evaluation for System One decision models)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

36 public Hugging Face datasets converted into TypeSafe System One rows (state, questions, gold answers), code to fine-tune a calibrated decision model from a pretrained encoder, and a benchmark runner that scores any model, including TypeSafe's hosted Jev, on accuracy, calibration and latency over the same rows, with diagnostics for question reading, references into the state and option order.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ashaazami/dadvar) |
| Maintainer | [ashaazami](https://github.com/ashaazami). Independently curated. |
| Format | Python package (datasets, training, benchmarks) |
| Requirements | Python; a GPU for training; a TypeSafe API key only to benchmark Jev. |
| License | [Apache-2.0](https://github.com/ashaazami/dadvar/blob/5a3a7a8b1c8136b41653c55363c55ad8366aa893/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`benchmarks/models.py`](https://github.com/ashaazami/dadvar/blob/5a3a7a8b1c8136b41653c55363c55ad8366aa893/benchmarks/models.py) at the pinned commit. |

## When to use

- Train or compare your own Jev-style decision model on public data.
- Mismatch: research code; numbers depend on your runs.

## How it works

`benchmarks/models.py` defines the `system_one(state, questions)` interface; the `jev` backend calls TypeSafe through the official Python SDK (`--backend jev`, billed). Integration evidence: [`benchmarks/models.py`](https://github.com/ashaazami/dadvar/blob/5a3a7a8b1c8136b41653c55363c55ad8366aa893/benchmarks/models.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ashaazami/dadvar.git && cd dadvar
pip install -e '.[bench]'
TYPESAFE_API_KEY=... python -m benchmarks.run all --backend jev   # billed
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ashaazami/dadvar#readme](https://github.com/ashaazami/dadvar#readme)

## Limits and data handling

Benchmark rows go to TypeSafe only with the `jev` backend.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 5a3a7a8b1c81](https://github.com/ashaazami/dadvar/tree/5a3a7a8b1c8136b41653c55363c55ad8366aa893). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
