# jevals

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local evaluation workbench for TypeSafe Jev: author Noul/Choice/Score (and combined) questions with expected answers, run them, and compare saved results in the browser.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dayhaysoos/jevals) |
| Maintainer | [dayhaysoos](https://github.com/dayhaysoos) / Nick DeJesus. Independently curated; this page is not an upstream submission or endorsement. |
| Format | Node.js local server + browser UI; npm package **jevals 0.1.1** (`npx jevals`). |
| Requirements | Node.js **≥ 22.13**; `TYPESAFE_API_KEY` in workspace `.env` to run evaluations (edit without a key). |
| License | [MIT](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline node:test suite passed; live TypeSafe runs and browser UI smoke were **not** run. Distinct from [jeval](jeval.md) (calibration CLI over recorded confidences), [Jevaluate](jevaluate.md) (confidence-gated walkthroughs), [JevScope](jevscope.md), and [Typed Evals](typed-evals.md). |

## When to use

Use it when you want a local UI to design Jev questions, attach expected answers, and diff run history before wiring those questions into production code. Prefer [jeval](jeval.md) for ECE/cost thresholds on already-labeled confidences, or [Typed Evals](typed-evals.md) for library judges in Python.

## How it works

[`src/run-executor.ts`](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/src/run-executor.ts) and [`src/workspace-config.ts`](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/src/workspace-config.ts) read `TYPESAFE_API_KEY` / optional `TYPESAFE_BASE_URL` and execute evaluation cases against TypeSafe. Field labels in the UI map to SDK request fields. Case text and questions leave the host when a run executes.

## Get started

```sh
npx jevals
# Optional: create .env with TYPESAFE_API_KEY=... then restart
# npx jevals --dir ./my-evals --port 4318 --no-open
```

Pinned offline tests:

```sh
git clone https://github.com/dayhaysoos/jevals.git
cd jevals
git checkout af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580
npm ci --ignore-scripts
npm test
```

Live evaluation runs call TypeSafe and can incur charges.

## Examples and demos

- Upstream seed/examples and workbench docs.
- Offline `npm test` on the review host: **69 passed**. No live TypeSafe run or headed browser walkthrough.

## Limits and data handling

Evaluation states and questions go to TypeSafe when you run. Keys stay in `.env`. Upstream UX/performance claims were not remeasured. Creating/editing cases without a key does not call the API.

## Review and maintenance

Reviewed on **2026-09-21** at [commit af6fecc](https://github.com/dayhaysoos/jevals/tree/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580): **0.1.1**, MIT. AI-assisted source review of README, LICENSE, `src/run-executor.ts`, `src/workspace-config.ts`, and tests. **`npm test`: 69 passed**. No live TypeSafe or browser UI session.

Related: [jeval](jeval.md), [Jevaluate](jevaluate.md), [JevScope](jevscope.md), [Typed Evals](typed-evals.md).
