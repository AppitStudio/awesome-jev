# jev-align

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental CLI (`jeva` / `jev-align`) that builds calibrated AI Functions with TypeSafe Jev evaluations plus GEPA optimization from human labels—binary, multiclass, multilabel, or score tasks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sutro-sh/jev-align) |
| Maintainer | [Sutro / sutro-sh](https://github.com/sutro-sh). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **jev-align 0.1.2** on PyPI (`uv tool install jev-align` / `pip install jev-align`; entry points `jeva`, `jev-align`). |
| Requirements | Python ≥ 3.11; Jev via `TYPESAFE_API_KEY` (direct), or Vercel `AI_GATEWAY_API_KEY` / Cloudflare Workers AI credentials; a separate reflection-model key for GEPA (OpenAI/Anthropic/Gemini/LiteLLM). Depends on `typesafe-sdk` and `gepa`. |
| License | [Apache-2.0](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/LICENSE). |

## When to use

Use it to iterate classifiers from CSV/Parquet/JSONL with active labeling rounds, then export an AI Function for application use. Prefer raw SDK/`typesafe-cli` asks when you only need one-off judgments without GEPA loops. Human labels always gate acceptance—training score alone never auto-accepts a proposal.

## How it works

[`src/jev_align/backends.py`](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/src/jev_align/backends.py) constructs TypeSafe / Cloudflare / Vercel evaluators (default TypeSafe model `jev-1.13.0`). [`src/jev_align/jev.py`](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/src/jev_align/jev.py) uses `typesafe_sdk.AsyncTypeSafeClient` with Choice/Noul/Score. GEPA reflection is a separate LLM. Session state and accepted functions persist under `.jev-align/`.

## Get started

```sh
uv tool install jev-align
export TYPESAFE_API_KEY=…          # or Vercel/Cloudflare per README
export OPENAI_API_KEY=…            # reflection model (or Anthropic/Gemini)
jeva
# guided setup discovers local datasets and sample files
# or inspect:
git clone https://github.com/sutro-sh/jev-align.git
cd jev-align
git checkout 49753df924d30c0d3642b58e0b9b1e89921dc102
```

Optimization and evaluation send dataset rows to the configured Jev provider and reflection model. This listing did not run `jeva` or call TypeSafe.

## Examples and demos

- README demo video and `jeva optimize posts.csv …` flag examples.
- Sample datasets under `src/jev_align/sample_data/`.
- Offline tests: `tests/test_jev.py`, `tests/test_jev_gateways.py`, and related suite.

## Limits and data handling

Labeled and unlabeled row text leave the host for Jev and the reflection provider. Experimental Alpha software. Upstream demo quality claims were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 49753df9](https://github.com/sutro-sh/jev-align/tree/49753df924d30c0d3642b58e0b9b1e89921dc102): **0.1.2**, Apache-2.0. AI-assisted source review of README, `backends.py`, `jev.py`, `pyproject.toml`, and license. pytest / live TypeSafe / GEPA runs were not executed on the review host.

Related: [Advocaat](advocaat.md), [typesafe-cli](typesafe-cli.md), [JevScope](jevscope.md).
