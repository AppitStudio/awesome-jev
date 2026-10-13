# JEV MLX

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Typed decisions from existing MLX-LM and MLX-VLM models on Apple Silicon without fine-tuning or extra decision weights.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/itsodeleo/jev-mlx) |
| Maintainer | [itsodeleo](https://github.com/itsodeleo). Independently curated. |
| Format | Python library (Apple Silicon MLX) |
| Requirements | Apple Silicon; MLX; no TypeSafe key required for local mode. |
| License | [MIT](https://github.com/itsodeleo/jev-mlx/blob/f5440131e3b26cc93b34ff811f015a81fffe6c13/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`src/jev_mlx/backends/mlx_lm.py`](https://github.com/itsodeleo/jev-mlx/blob/f5440131e3b26cc93b34ff811f015a81fffe6c13/src/jev_mlx/backends/mlx_lm.py) at the pinned commit. |

## When to use

- Use when you need: Typed decisions from existing MLX-LM and MLX-VLM models on Apple Silicon without…
- Mismatch: See upstream README for setup limits.

## How it works

MLX backends under src/jev_mlx produce choice/score-style outputs from existing LM/VLM weights. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- src/jev_mlx/backends/mlx_lm.py and mlx_vlm backends.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit f5440131e3b2](https://github.com/itsodeleo/jev-mlx/tree/f5440131e3b26cc93b34ff811f015a81fffe6c13). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
