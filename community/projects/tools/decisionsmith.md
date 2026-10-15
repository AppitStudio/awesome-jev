# decisionsmith

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Use and fine-tune System One models (Jev, Laya) on your own data with an LLM as teacher: declare decisions as Pydantic fields and get a harness that calls Jev or a trained local student.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/izam-mohammed/decisionsmith) |
| Maintainer | [izam-mohammed](https://github.com/izam-mohammed). Independently curated. |
| Format | Python library (`uv add decisionsmith[all]`) and notebooks |
| Requirements | Python; TypeSafe key for Jev; an LLM key for the teacher; GPU optional for local fine-tuning. |
| License | [Apache-2.0](https://github.com/izam-mohammed/decisionsmith/blob/8b407c5c8fa5317c5b315732bcdc45326cdcad1c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisionsmith/engines/systemone.py`](https://github.com/izam-mohammed/decisionsmith/blob/8b407c5c8fa5317c5b315732bcdc45326cdcad1c/src/decisionsmith/engines/systemone.py) at the pinned commit. |

## When to use

- Start with an LLM teacher and distill a fast local decision model for a typed task.
- Compare LLM, Jev and Laya on the same Pydantic-defined decisions.
- Mismatch: training quality depends on your data; benchmark notebooks are the author's.

## How it works

Pydantic `Literal`/`Enum`, `bool` and scale fields map to Choice, Noul and Score questions; the System One engine sends them to Jev (or a Jev-compatible Laya server), while the teacher LLM labels data for fine-tuning a student. Integration evidence: [`src/decisionsmith/engines/systemone.py`](https://github.com/izam-mohammed/decisionsmith/blob/8b407c5c8fa5317c5b315732bcdc45326cdcad1c/src/decisionsmith/engines/systemone.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv add "decisionsmith[all]"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark notebook: `notebooks/07_bench_llm_vs_jev_vs_laya.ipynb`.

## Limits and data handling

Inputs go to TypeSafe and to your teacher LLM provider on your keys; local students run on your hardware.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 8b407c5c8fa5](https://github.com/izam-mohammed/decisionsmith/tree/8b407c5c8fa5317c5b315732bcdc45326cdcad1c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
