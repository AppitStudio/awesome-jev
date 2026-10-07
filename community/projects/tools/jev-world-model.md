# A Decision Model as a World Model

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, data, run logs and manuscript for a KIIS 2026 Fall Conference paper testing whether a frozen TypeSafe Jev decision model can serve as an LLM agent's world model in TextWorld, against zero-shot and LoRA-tuned Qwen3-4B in decision-style and generative set-ups; the author reports Jev near the oracle on task success without task training. English and Korean docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thddydgnl/jev-world-model) |
| Maintainer | [thddydgnl](https://github.com/thddydgnl). Independently curated. |
| Format | Python scripts, run artifacts and manuscript sources |
| Requirements | Python with the pinned `environment.lock` packages (TextWorld, httpx…), a TypeSafe key for Jev runs; a GPU for the Qwen3-4B / LoRA side. |
| License | [MIT](https://github.com/thddydgnl/jev-world-model/blob/ffaf9f6840468033aaddebecc867f1707ac0f074/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check evidence on using Jev to predict action outcomes before an agent acts.
- Reuse the 2 × 2 world-model comparison design.
- Mismatch: results are the author's (camera-ready due Oct 23, 2026); not verified here.

## How it works

[`src/wm/jev_forecaster.py`](https://github.com/thddydgnl/jev-world-model/blob/ffaf9f6840468033aaddebecc867f1707ac0f074/src/wm/jev_forecaster.py) asks Jev option questions about the next state; [`src/jev_client.py`](https://github.com/thddydgnl/jev-world-model/blob/ffaf9f6840468033aaddebecc867f1707ac0f074/src/jev_client.py) handles the API. Every agent shares the same Qwen3-4B policy and planner; only the world model differs.

## Get started

Set up the local side and confirm the API schema (README *Reproducing*):

```sh
git clone https://github.com/thddydgnl/jev-world-model && cd jev-world-model
python -m venv .venv && .venv/bin/pip install -r <(grep -v '^#' environment.lock)
.venv/bin/python scripts/phase0_api_check.py
```

Jev runs are billed by TypeSafe; the GPU side runs on your hardware.

## Examples and demos

- README *Overview* findings and *Paper* table.
- [Run artifacts](https://github.com/thddydgnl/jev-world-model/tree/ffaf9f6840468033aaddebecc867f1707ac0f074/artifacts).

## Limits and data handling

Game states go to TypeSafe on Jev runs. Reported success rates are upstream results; not rerun on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit ffaf9f684046](https://github.com/thddydgnl/jev-world-model/tree/ffaf9f6840468033aaddebecc867f1707ac0f074). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
