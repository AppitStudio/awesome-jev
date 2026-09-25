# TinyJev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Offline ~0.6B System One–compatible decision model (Choice/Noul/Score with calibrated probabilities) on MLX or PyTorch—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ankit-aglawe/tinyjev) |
| Maintainer | [ankit-aglawe](https://github.com/ankit-aglawe). Independently curated. |
| Format | Python package (`tinyjev`) + local HTTP/System One–compatible endpoint; weights on Hugging Face. |
| Requirements | Python 3.9+; MLX on Apple Silicon or PyTorch elsewhere; ~1.2 GB weights (`AnkitAI/tinyjev-0.6b`). |
| License | [MIT](https://github.com/ankit-aglawe/tinyjev/blob/0a6c9b1719f5ab15a5702e9b6edd08661cfce4dd/LICENSE). |
| Disclosure | Independent open model research—not TypeSafe-hosted Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live inference/benchmarks not re-run on the review host. |

## When to use

Use for **local typed decisions** (ticket triage, offline gatekeeping) without cloud Jev. Prefer hosted TypeSafe Jev when you need the official cloud model and SLA.

## How it works

TinyJev scores offered options in one forward pass and returns probabilities. It never generates free text. A local HTTP server can expose a System One–shaped API.

## Get started

```sh
pip install 'tinyjev[mlx,demo]'   # or tinyjev[torch,demo]
python -c "import tinyjev; print(tinyjev.__file__)"
# Weights: https://huggingface.co/AnkitAI/tinyjev-0.6b
# Pin: https://github.com/ankit-aglawe/tinyjev/tree/0a6c9b1719f5ab15a5702e9b6edd08661cfce4dd
```

## Examples and demos

- `demos/triage_desk.py` and recorded GIFs in the README.
- OpenDecision benchmark tables under `benchmarks/opendecision` (upstream-reported).

## Limits and data handling

Not official Jev. Upstream benchmark numbers are author-reported. Local inference uses your hardware only unless you point a remote client at your server.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 0a6c9b1](https://github.com/ankit-aglawe/tinyjev/tree/0a6c9b1719f5ab15a5702e9b6edd08661cfce4dd). AI-assisted README and LICENSE inspection; package install/inference not executed on the review host.

Related: [Malkuth](malkuth.md), [vLLM Jev](vllm-jev.md).
