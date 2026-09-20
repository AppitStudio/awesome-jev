# jev-ci-selector

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that asks TypeSafe Jev whether each named CI task still applies to the current pull-request diff, then exports boolean job outputs so your existing workflow can skip irrelevant work.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/guilhem/jev-ci-selector) |
| Maintainer | [guilhem](https://github.com/guilhem). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js GitHub Action (`jev-ci-selector` 0.1.0) with TypeSafe SDK client and shadow/enforce modes. |
| Requirements | GitHub Actions runner; repository secret for the API key (`JEV_API_KEY` / TypeSafe). Offline unit tests need Node.js and no key. |
| License | [MIT](https://github.com/guilhem/jev-ci-selector/blob/c76225d74ed0bbab0d07e93881742c0ba28ebd68/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline tests inspected. Live TypeSafe and full CI pipelines were not run. Distinct from [Moongate](moongate.md) (rule annotations) and [Metis](metis.md) (issue triage). |

## When to use

Use it when a large workflow has many optional jobs and you want Jev to propose which described checks matter for this diff, while your YAML still owns runners, installs, and commands. Prefer classical `paths-filter` when selection is purely path-based. Prefer [Moongate](moongate.md) when the goal is semantic PR annotations rather than job selection.

## How it works

The Action loads task descriptions and a bounded diff, then [`src/jev.ts`](https://github.com/guilhem/jev-ci-selector/blob/c76225d74ed0bbab0d07e93881742c0ba28ebd68/src/jev.ts) calls `https://api.typesafe.ai` through `@typesafe-ai/sdk`. Code maps probabilities into per-task boolean outputs and a tested SHA. Default `enforce` applies selection; `mode: shadow` records proposals while keeping every task. Selection does not run your tests—it only decides whether a job should run.

## Get started

```sh
git clone https://github.com/guilhem/jev-ci-selector.git
cd jev-ci-selector
git checkout c76225d74ed0bbab0d07e93881742c0ba28ebd68
npm ci --ignore-scripts
npm test
# Wire the Action into a workflow with secrets.JEV_API_KEY; see README quick start.
```

## Examples and demos

- README two-job Go unit-test example and `examples/` workflows (shadow, matrix, static jobs).
- Docs for path filters and reference inputs/outputs.

## Limits and data handling

Diff text and task metadata are sent to TypeSafe when selection runs. Vague task descriptions produce weak decisions. A skipped job is not proof the suite passed—keep a required selection or final gate as documented upstream. Pin released Action SHAs for immutability.

## Review and maintenance

Reviewed on **2026-09-21** at [commit c76225d](https://github.com/guilhem/jev-ci-selector/tree/c76225d74ed0bbab0d07e93881742c0ba28ebd68): **0.1.0**, MIT. AI-assisted source review of README, `action.yml`, and `src/jev.ts`. **`npm test`**: **106 passed**. No live TypeSafe or GitHub Actions runs.

Related: [Moongate](moongate.md), [Metis](metis.md), [Jev Review Action](jev-review-action.md).
