# agent-evals

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Deterministic LLM-agent eval harness: rule scorers for tool/latency/cost failures, plus an optional calibrated TypeSafe Jev judge you can gate CI deploys on.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marianoberton/agent-evals) |
| Maintainer | [marianoberton](https://github.com/marianoberton) (Mariano Berton). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm CLI/library **agent-evals 0.1.0** (`agent-evals run …`) with Vitest helpers. |
| Requirements | Node.js **≥ 20.10**. Mechanical scorers need no key. `jevJudge` / live Jev needs `TYPESAFE_API_KEY` (or the transport the suite configures). |
| License | [MIT](https://github.com/marianoberton/agent-evals/blob/a703251f7a7a14c9212d357b00b72c8e52e12266/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (`src/scorers/jevJudge.ts`, `src/jev/`, README, LICENSE, docs/JEV_JUDGE.md). Package install and live Jev runs were **not** executed on the review host. |

## When to use

Use it when agent failures you care about are **checkable** (wrong tool, forbidden phrase, latency/cost, missing escalation) and you still want a typed probability for the few semantic judgments. Prefer Likert LLM-as-judge benches only when you accept non-gatable prose scores.

## How it works

Suites combine deterministic scorers with optional [`jevJudge`](https://github.com/marianoberton/agent-evals/blob/a703251f7a7a14c9212d357b00b72c8e52e12266/src/scorers/jevJudge.ts) over TypeSafe System One (Noul/Choice/Score via [`src/jev/`](https://github.com/marianoberton/agent-evals/tree/a703251f7a7a14c9212d357b00b72c8e52e12266/src/jev)). `--fail-under` turns the aggregate into a CI exit code. Upstream contrasts this with slow, non-repeatable 1–5 LLM judges.

## Get started

```sh
npm i -D agent-evals
# See upstream README for defineSuite / defineCase examples
# agent-evals run evals/buggy.suite.ts --fail-under
```

Pin for review: [commit a703251](https://github.com/marianoberton/agent-evals/tree/a703251f7a7a14c9212d357b00b72c8e52e12266). Offline unit tests and live Jev were not run here.

## Examples and demos

- README buggy dealership-sales suite (planted tool/latency/cost failures).
- [`docs/JEV_JUDGE.md`](https://github.com/marianoberton/agent-evals/blob/a703251f7a7a14c9212d357b00b72c8e52e12266/docs/JEV_JUDGE.md).

## Limits and data handling

Live Jev sends case text/state to TypeSafe. Mechanical scorers stay local. This listing did not install the package or call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit a703251](https://github.com/marianoberton/agent-evals/tree/a703251f7a7a14c9212d357b00b72c8e52e12266) (`agent-evals` **0.1.0**, MIT). AI-assisted review of README, LICENSE, Jev modules. No live TypeSafe spend.

Related: [DecideKit](decidekit.md), [chinese-workflow-decision-bench](chinese-workflow-decision-bench.md), [TypeSafe-as-a-Judge](typesafe-as-a-judge.md).
