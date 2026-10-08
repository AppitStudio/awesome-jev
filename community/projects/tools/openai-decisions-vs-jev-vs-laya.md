# openai-decisions-vs-jev-vs-laya

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent Portuguese-language benchmark of decision models — OpenAI Decisions API (`gpt-6-luna`), TypeSafe Jev (`jev-1.13.0`) and local Laya (with option rotation) — on agent tool routing, prompt-injection detection and LLM-as-judge in PT-BR: 450 cases per provider (2026-10-07), with accuracy, macro-F1, ECE, latency with and without network, and cost per 1k.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mateusfonsek/openai-decisions-vs-jev-vs-laya) |
| Maintainer | [mateusfonsek](https://github.com/mateusfonsek). Independently curated. |
| Format | Python benchmark (`uv run bench validate / run / report`) with recorded results |
| Requirements | Python + uv; `OPENAI_API_KEY` and `TYPESAFE_API_KEY` (Laya runs locally with `--extra laya`). |
| License | [MIT](https://github.com/mateusfonsek/openai-decisions-vs-jev-vs-laya/blob/b9d296e97b4ed382cbad65248800ec63096225f4/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Choose a decision model for Portuguese-language agents.
- Reuse the dataset and adapters for your own provider comparison.
- Mismatch: zero-shot Laya scored poorly in Portuguese here; results are one dated run.

## How it works

Adapters such as [`bench/adapters/jev.py`](https://github.com/mateusfonsek/openai-decisions-vs-jev-vs-laya/blob/b9d296e97b4ed382cbad65248800ec63096225f4/bench/adapters/jev.py) send the same cases to each provider; raw responses and RTT are stored under [`results/2026-10-07/`](https://github.com/mateusfonsek/openai-decisions-vs-jev-vs-laya/tree/b9d296e97b4ed382cbad65248800ec63096225f4/results/2026-10-07) and `bench report` renders tables and charts.

## Get started

Install, add keys and run one provider (README):

```sh
git clone https://github.com/mateusfonsek/openai-decisions-vs-jev-vs-laya.git && cd openai-decisions-vs-jev-vs-laya
uv sync --extra laya
cp .env.example .env   # OPENAI_API_KEY, TYPESAFE_API_KEY
uv run bench validate
uv run bench run --provider jev
```

Runs bill OpenAI and TypeSafe; Laya is local.

## Examples and demos

- README *Resumo*: Jev ahead on routing (88.0% vs 86.7%) and judge exact score (80.7% vs 72.0%) at 17–35% lower cost (author-reported).

## Limits and data handling

Synthetic/curated PT-BR cases go to the hosted providers. Results are the author's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit b9d296e97b4e](https://github.com/mateusfonsek/openai-decisions-vs-jev-vs-laya/tree/b9d296e97b4ed382cbad65248800ec63096225f4). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
