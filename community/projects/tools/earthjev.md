# EarthJev by IKNOS Lab, University of Naples Federico II (calibrated typed answers about 12-band Sentinel-2 satellite images)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research code, results and weights for a 0.8B multispectral model (Qwen3.5-0.8B on the open OneJev recipe) that answers yes/no, multiple-choice and ordinal questions about a 12-band Sentinel-2 patch with one probability per option instead of generated text, reported at 19.9 ms per question on one H100 with low calibration error. It does not call TypeSafe's Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CosmoIknosLab/EarthJev) |
| Maintainer | [CosmoIknosLab](https://github.com/CosmoIknosLab). Independently curated. |
| Format | Python research repo + Hugging Face weights |
| Requirements | A CUDA GPU and conda (the env script installs PyTorch, transformers and OneJev); the Slurm scripts assume a cluster. Weights: huggingface.co/dBenf/EarthJev. |
| License | [Apache-2.0](https://github.com/CosmoIknosLab/EarthJev/blob/b0a4c1907ad790caa3b1bf9e54064c5ca13d8303/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/s1geo/bench_latency.py`](https://github.com/CosmoIknosLab/EarthJev/blob/b0a4c1907ad790caa3b1bf9e54064c5ca13d8303/src/s1geo/bench_latency.py) at the pinned commit. |

## When to use

- Study calibrated, non-generative typed answers for remote-sensing imagery, with a paper, weights and baselines.
- Mismatch: a hosted Jev feature; this is an independent research model, not TypeSafe's Jev, and the authors note a new version is coming.

## How it works

`src/s1geo/bench_latency.py` builds System One-style requests (`SystemOneRequest` with a state and typed questions) for the OneJev multimodal engine and times them against generative baselines; training adds a Brier term and per-type temperature scaling. Integration evidence: [`src/s1geo/bench_latency.py`](https://github.com/CosmoIknosLab/EarthJev/blob/b0a4c1907ad790caa3b1bf9e54064c5ca13d8303/src/s1geo/bench_latency.py).

## Get started

Clone with submodules, build the environment and run the tests; data and training scripts are in `scripts/`.

```sh
git clone --recursive https://github.com/CosmoIknosLab/EarthJev && cd EarthJev
bash env/build_env.sh
source env/activate.sh
pytest tests/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/CosmoIknosLab/EarthJev/blob/b0a4c1907ad790caa3b1bf9e54064c5ca13d8303/README.md](https://github.com/CosmoIknosLab/EarthJev/blob/b0a4c1907ad790caa3b1bf9e54064c5ca13d8303/README.md)
- Preprint: [arxiv.org/abs/2611.02096](https://arxiv.org/abs/2611.02096)
- Weights: [huggingface.co/dBenf/EarthJev](https://huggingface.co/dBenf/EarthJev)

## Limits and data handling

Independent research implementation; benchmark numbers are the authors' and were not re-run here. Model weights and datasets carry their own terms.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit b0a4c1907ad7](https://github.com/CosmoIknosLab/EarthJev/tree/b0a4c1907ad790caa3b1bf9e54064c5ca13d8303). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
