# deslop

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill and stdlib Python CLI that scores fetched page bodies with TypeSafe Jev: four calibrated probabilities (`ad`, `slop`, `seo`, `derivative`) and no baked-in verdict.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yoichiojima-2/deslop) |
| Maintainer | [yoichiojima-2](https://github.com/yoichiojima-2). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code / agent-skills layout under `skills/deslop/` plus `eval/` harness; Python 3.9+ stdlib only. |
| Requirements | Python 3.9+; `TYPESAFE_API_KEY` (or a proxy that injects it for `api.typesafe.ai`). Default minimum body length 250 characters. |
| License | [MIT](https://github.com/yoichiojima-2/deslop/blob/69ce1b59b1ebe057de899ae8748eedc4be563a6c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source and `py_compile` inspected; live eval/`TYPESAFE_API_KEY` scoring not run on the review host. Upstream README eval table is author-reported on a hand-labelled set. |

## When to use

Use it when a research agent should **rank or filter pages** for promotional, machine-filler, SEO-shaped, or derivative content using TypeSafe Jev probabilities, while your code owns thresholds. Prefer [JevSlop](../apps/jevslop.md) for article-level AI-slop scoring UIs, or [Prompt Rejector](prompt-rejector.md) for prompt/skill screening rather than web-page bodies.

## How it works

[`jev.py`](https://github.com/yoichiojima-2/deslop/blob/69ce1b59b1ebe057de899ae8748eedc4be563a6c/skills/deslop/jev.py) batches TypeSafe System One requests to `https://api.typesafe.ai/v1/systemone` (model `jev-latest`) from `questions.json`. `deslop.py` enforces the JSONL input contract (`id`, `url`, `text`) and maps answers into the four score keys. Callers set cutoffs; the skill does not emit a single pass/fail.

## Get started

```sh
git clone https://github.com/yoichiojima-2/deslop.git
cd deslop
git checkout 69ce1b59b1ebe057de899ae8748eedc4be563a6c
python3 -m py_compile skills/deslop/deslop.py skills/deslop/jev.py eval/run.py
# Live: export TYPESAFE_API_KEY=...
# skills/deslop/deslop.py < skills/deslop/examples/pages.jsonl
```

Live scoring sends page text to TypeSafe and may incur charges. This listing did not call live APIs. Upstream `eval/run.py` also needs a key and was not executed here.

## Examples and demos

- Offline on the review host: `python3 -m py_compile` on `deslop.py`, `jev.py`, and `eval/run.py` succeeded; example `pages.jsonl` and `questions.json` present.
- Upstream documents a labelled eval set and CI workflow that requires `TYPESAFE_API_KEY`; those live numbers were not reproduced on the review host.

## Limits and data handling

Scores reflect the model's reading of the shipped questions, not an external ground truth. Short snippets are refused by the character floor. Experimental dimensions (for example `clickbait`) are opt-in. Page text leaves the machine on live runs.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 69ce1b5](https://github.com/yoichiojima-2/deslop/tree/69ce1b59b1ebe057de899ae8748eedc4be563a6c): MIT. AI-assisted source review of README, LICENSE, `skills/deslop/`, `eval/`. Offline `py_compile` OK. No live TypeSafe eval on the review host.

Related: [JevSlop](../apps/jevslop.md), [Prompt Rejector](prompt-rejector.md), [decision-first](decision-first.md).
