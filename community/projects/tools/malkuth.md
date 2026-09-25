# Malkuth

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-weight multilingual System One–style decision models (2B/4B, Korean focus): Choice, Noul, and Score over `/v1/systemone` via Kev—adjacent to hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/newfull5/malkuth) |
| Maintainer | [newfull5](https://github.com/newfull5). Independently curated. |
| Format | Model cards + serve instructions (weights on Hugging Face `dhtocks/malkuth-*`; served with Kev). |
| Requirements | Kev (`jaredpalmer/kev`) with uv; HF download for `dhtocks/malkuth-4b` or `-2b`; local GPU/CPU suitable for serve. |
| License | [Apache-2.0](https://github.com/newfull5/malkuth/blob/af2e1c06ded5c448e78394f356319fc2e49f4c94/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **run a Korean-focused open decision model** compatible with System One question types without the hosted TypeSafe endpoint.

## How it works

Post-trained from Kev; serve with `python -m kev.serve --run dhtocks/malkuth-4b` and POST Choice/Noul/Score questions to `/v1/systemone`.

## Get started

```sh
git clone https://github.com/jaredpalmer/kev.git kev && cd kev
uv sync --extra serve
uv run --extra serve python -m kev.serve --run dhtocks/malkuth-4b --port 8009
# Model docs/pin: https://github.com/newfull5/malkuth/tree/af2e1c06ded5c448e78394f356319fc2e49f4c94
```

## Examples and demos

- README curl example for department Choice routing.
- HF model pages for 2B/4B.

## Limits and data handling

Not TypeSafe-hosted Jev—API-compatible shape via Kev. Eval scores on README are upstream-reported. First load downloads base + fine-tune weights.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit af2e1c0](https://github.com/newfull5/malkuth/tree/af2e1c06ded5c448e78394f356319fc2e49f4c94). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [vLLM Jev](vllm-jev.md), [Mechanical Jev](mechanical-jev.md).
