# A2E (agent auditing engine with Jev as an extra judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source platform for auditing agent harnesses end to end (build experiments, capture trajectories, score process and outcome); a full evaluation can add four companion Jev scores next to the original LLM-judge annotations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/datamllab/A2E) |
| Maintainer | [datamllab](https://github.com/datamllab). Independently curated. |
| Format | Evaluation platform and CLI (Python, MIT) |
| Requirements | Python, the benchmarks and harnesses you pair, an LLM judge key, and `OPENROUTER_API_KEY` or `A2E_JEV_API_KEY` for the `*_jev` scores. |
| License | [MIT](https://github.com/datamllab/A2E/blob/ef86ec507f66a8fd6a2223b351b95444ab701f6b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`eval/core/jev_judge.py`](https://github.com/datamllab/A2E/blob/ef86ec507f66a8fd6a2223b351b95444ab701f6b/eval/core/jev_judge.py) at the pinned commit. |

## When to use

- Compare an LLM judge with a typed Jev judge on the same agent trajectories.
- Audit coding or terminal agents with full trace visibility.
- Mismatch: research platform; Jev covers four metrics only and defaults to OpenRouter.

## How it works

`eval/core/jev_judge.py` calls `https://openrouter.ai/api/v1/systemone` with `jev-latest` by default; per `eval/README.md`, Jev is an extra score that does not replace the LLM judge, and `--part all` writes the `*_jev` annotations. Integration evidence: [`eval/core/jev_judge.py`](https://github.com/datamllab/A2E/blob/ef86ec507f66a8fd6a2223b351b95444ab701f6b/eval/core/jev_judge.py).

## Get started

Follow the quick start, export a Jev key, then run the usual `run_eval.py` command.

```sh
git clone https://github.com/datamllab/A2E.git && cd A2E
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev as judge: [github.com/datamllab/A2E/blob/ef86ec507f66a8fd6a2223b351b95444ab701f6b/eval/README.md#jev-as-judge](https://github.com/datamllab/A2E/blob/ef86ec507f66a8fd6a2223b351b95444ab701f6b/eval/README.md#jev-as-judge)
- Paper: [arxiv.org/abs/2608.07346](https://arxiv.org/abs/2608.07346)

## Limits and data handling

Trajectory text for the four Jev metrics goes to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit ef86ec507f66](https://github.com/datamllab/A2E/tree/ef86ec507f66a8fd6a2223b351b95444ab701f6b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
