# Decision Bench by Atlan (open benchmark of how accurately, quickly and cheaply decision models and LLMs make bounded choices)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open benchmark with 1,071 rows across 35 tasks from 36 public datasets (route a complaint, identify a clause, select a tool, pick a receipt total), scoring Jev, other decision models and LLMs on accuracy, latency and cost, with a public leaderboard at decisionbench.ai.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atlanai/decision-bench) |
| Maintainer | [atlanai](https://github.com/atlanai). Independently curated. |
| Format | Python benchmark runner with committed corpus and web leaderboard (MIT code) |
| Requirements | Python 3.11+ and a key for each provider you run, e.g. `TYPESAFE_API_KEY` for Jev direct or an OpenRouter key. |
| License | [MIT](https://github.com/atlanai/decision-bench/blob/412d13b19adaf75e09c017afabb893c4828fe080/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Leaderboard: [decisionbench.ai](https://decisionbench.ai/). Discovered via X ([post](https://x.com/surendranb/status/2121206693568626920)). |
| Jev evidence | [`decision_bench/adapters.py`](https://github.com/atlanai/decision-bench/blob/412d13b19adaf75e09c017afabb893c4828fe080/decision_bench/adapters.py) at the pinned commit. |

## When to use

- Compare Jev with other decision models and LLMs on realistic bounded choices before picking one.
- Mismatch: open-ended generation quality; every row is a single choice question.

## How it works

`decision_bench/adapters.py` posts to `https://api.typesafe.ai/v1/systemone` for the `typesafe` provider; `config/models.json` lists `jev-1.13` (TypeSafe direct) and `jev-1.14` (OpenRouter Decisions) next to other providers. Each row has one choice question; the model returns a probability per option and invalid responses count as incorrect. Results are the maintainers' published runs. Integration evidence: [`decision_bench/adapters.py`](https://github.com/atlanai/decision-bench/blob/412d13b19adaf75e09c017afabb893c4828fe080/decision_bench/adapters.py).

## Get started

Validate the committed corpus, copy `.env.example`, set the provider settings, and run a five-row smoke test.

```sh
python3 -m decision_bench validate
cp .env.example .env
python3 -m decision_bench run --model jev-1.13 --limit 5
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Leaderboard: [decisionbench.ai/](https://decisionbench.ai/)
- Protocol: [github.com/atlanai/decision-bench/blob/412d13b19adaf75e09c017afabb893c4828fe080/docs/protocol.md](https://github.com/atlanai/decision-bench/blob/412d13b19adaf75e09c017afabb893c4828fe080/docs/protocol.md)

## Limits and data handling

Benchmark rows (from public datasets) go to the providers you configure on your keys. Leaderboard numbers are maintainer-reported.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 412d13b19ada](https://github.com/atlanai/decision-bench/tree/412d13b19adaf75e09c017afabb893c4828fe080). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
