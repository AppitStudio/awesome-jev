# jev-adaptive-granularity-WM (Jev-routed temporal granularity for causal video generation)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Official code, locked protocols and audit artifacts for a paper that routes causal video generation's temporal granularity with TypeSafe Jev (System One) plus recovery and hysteresis, instead of a fixed warp threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/j1s4nn/jev-adaptive-granularity-WM) |
| Maintainer | [j1s4nn](https://github.com/j1s4nn). Independently curated. |
| Format | Research code + Colab/Kaggle notebooks (Python, MIT) |
| Requirements | GPU notebook environment (Colab/Kaggle) and a TypeSafe API key for the online Jev routing experiments. |
| License | [MIT](https://github.com/j1s4nn/jev-adaptive-granularity-WM/blob/9895e95c12c7fa6cc26b5d568bc5b9009052c0de/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`colab/a100_online_jev.py`](https://github.com/j1s4nn/jev-adaptive-granularity-WM/blob/9895e95c12c7fa6cc26b5d568bc5b9009052c0de/colab/a100_online_jev.py) at the pinned commit. |

## When to use

- Reproduce the paper's Jev-routed temporal granularity protocol.
- Compare Jev routing against warp-threshold baselines.
- Mismatch: research artifact; not a drop-in video product.

## How it works

`colab/a100_online_jev.py` POSTs to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY` and uses typed answers as the routing signal. Integration evidence: [`colab/a100_online_jev.py`](https://github.com/j1s4nn/jev-adaptive-granularity-WM/blob/9895e95c12c7fa6cc26b5d568bc5b9009052c0de/colab/a100_online_jev.py).

## Get started

Follow the README DOI/protocol docs and run the Colab/Kaggle notebooks with your TypeSafe key.

```sh
git clone https://github.com/j1s4nn/jev-adaptive-granularity-WM.git && cd jev-adaptive-granularity-WM
export TYPESAFE_API_KEY=...
# follow README / colab notebooks
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/j1s4nn/jev-adaptive-granularity-WM/blob/9895e95c12c7fa6cc26b5d568bc5b9009052c0de/README.md](https://github.com/j1s4nn/jev-adaptive-granularity-WM/blob/9895e95c12c7fa6cc26b5d568bc5b9009052c0de/README.md)

## Limits and data handling

Experiment prompts/state under review are sent to TypeSafe on your key. Large GPU runs incur separate cloud costs.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 9895e95c12c7](https://github.com/j1s4nn/jev-adaptive-granularity-WM/tree/9895e95c12c7fa6cc26b5d568bc5b9009052c0de). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
