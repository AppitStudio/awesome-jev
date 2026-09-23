# jevper

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Jev-shaped System One client over any OpenAI-compatible model: `noul` / `choice` / `score` with probabilities and confidence—without calling the hosted TypeSafe API. Independent of `typesafe-sdk`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zhulinchng/jevper) |
| Maintainer | [zhulinchng](https://github.com/zhulinchng). Independently curated; this entry is not an upstream submission or endorsement. Not affiliated with TypeSafe AI. |
| Format | Python package **`jevper` 0.1.2** on PyPI (`pydantic` only at runtime; duck-typed OpenAI-like client). |
| Requirements | Python ≥ 3.10; an object exposing `responses.create` or `chat.completions.create` (e.g. OpenAI SDK or llama.cpp server). |
| License | [Apache-2.0](https://github.com/zhulinchng/jevper/blob/c95c140cc7604f2bfb97064030d06d61ab0c9298/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, pyproject). Live LLM calls were **not** executed on the review host. Behavior is not validated against official Jev. |

## When to use

Use it when application code expects System One-shaped answers but you want to back them with your own OpenAI-compatible model. Prefer the official TypeSafe SDK/API for hosted Jev; prefer [nokia AnyJev](nokia-anyjev.md) for local logit/head research on open weights.

## How it works

`SystemOneClient.system_one(state, questions=…)` builds messages and uses `logprobs` (or structured-output methods documented upstream) to fill Choice/Noul/Score answers with probabilities and confidence. No dependency on `typesafe-sdk` or `openai` at runtime beyond the duck-typed client you pass in.

## Get started

```sh
pip install jevper
# or:
git clone https://github.com/zhulinchng/jevper.git
cd jevper
git checkout c95c140cc7604f2bfb97064030d06d61ab0c9298
uv venv && uv pip install -e '.[test]'
pytest -q
```

## Examples and demos

- README `Choice` example with `SystemOneClient`.
- Test suite under the repo (offline where fixtures allow).

## Limits and data handling

Requests go to whatever backend your client targets—not TypeSafe. Calibration and option-order robustness depend on that model; this is not official Jev. This listing did not call live models.

## Review and maintenance

Reviewed on **2026-09-23** at [commit c95c140](https://github.com/zhulinchng/jevper/tree/c95c140cc7604f2bfb97064030d06d61ab0c9298) (**0.1.2**, Apache-2.0). AI-assisted source review of README, LICENSE, pyproject. No live model spend.

Related: [AnyJev (Nokia Applied Research)](nokia-anyjev.md), [hunch](hunch.md), [Advocaat](advocaat.md).
