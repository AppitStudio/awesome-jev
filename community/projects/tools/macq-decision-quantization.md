# MACQ by Yuanming Chen (4-bit weight and activation quantization for open Jev-like decision models such as Kev and Laya, with reproducible evaluations)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Post-training quantization method for open Jev-like System One models. It keeps each model's native question compiler and decision readout, samples calibration tokens by the model's top-two decision margins, and folds bounded activation-error corrections into low-bit weights. The repo (formerly S1Q) ships the method, a CLI and reproducible paired evaluations across Kev, Intern-Decision, StartLux-Decision and Laya.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CYMCharming/MACQ) |
| Maintainer | [Yuanming Chen](https://github.com/CYMCharming). Independently curated. |
| Format | Python package and CLI (research code) |
| Requirements | Python 3.12 and a CUDA PyTorch build; the upstream model sources and weights fetched by the setup scripts. |
| License | [Apache-2.0](https://github.com/CYMCharming/MACQ/blob/f4f5b1aeb00718a6d165f38d596ed1515258614d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/s1q/macq_runner.py`](https://github.com/CYMCharming/MACQ/blob/f4f5b1aeb00718a6d165f38d596ed1515258614d/src/s1q/macq_runner.py) at the pinned commit. |

## When to use

- Running an open decision model such as Kev on smaller hardware, or researching low-bit quantization that keeps decision accuracy.
- Mismatch: anything that uses TypeSafe's hosted Jev; there are no Jev weights to quantize.

## How it works

`macq optimize` fits and saves a W4A4 profile from 128 calibration requests (16,384 sampled token rows per quantized layer); the evaluation scripts run the frozen suites with floating-point quantize–dequantize execution. It works on open decision models, not TypeSafe's hosted Jev. Integration evidence: [`src/s1q/macq_runner.py`](https://github.com/CYMCharming/MACQ/blob/f4f5b1aeb00718a6d165f38d596ed1515258614d/src/s1q/macq_runner.py).

## Get started

Install the package, fetch model sources, prepare calibration data and optimise a model.

```sh
python -m pip install -e '.[models]'
python scripts/setup_sources.py --families kev rotation
python scripts/prepare_data.py shared --source-root work/upstream/kev --output work/data/shared
macq optimize --model kev-4b --data-dir work/data/shared --output-dir work/kev4-macq
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/CYMCharming/MACQ/blob/f4f5b1aeb00718a6d165f38d596ed1515258614d/docs/results.md](https://github.com/CYMCharming/MACQ/blob/f4f5b1aeb00718a6d165f38d596ed1515258614d/docs/results.md)
- Method: [github.com/CYMCharming/MACQ/blob/f4f5b1aeb00718a6d165f38d596ed1515258614d/docs/method.md](https://github.com/CYMCharming/MACQ/blob/f4f5b1aeb00718a6d165f38d596ed1515258614d/docs/method.md)

## Limits and data handling

Research code. The headline numbers (77.44% native BF16, 35.12% plain round-to-nearest W4A4, 74.82% MACQ W4A4, averaged over 22 suites and 11 models) are the author's own and use simulated quantize–dequantize, not packed-kernel speed. Each upstream model keeps its own licence (see `licenses/`).

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit f4f5b1aeb007](https://github.com/CYMCharming/MACQ/tree/f4f5b1aeb00718a6d165f38d596ed1515258614d). Inspected the README, LICENSE, NOTICE and the `src/s1q` package at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
