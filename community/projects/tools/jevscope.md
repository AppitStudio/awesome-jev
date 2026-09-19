# JevScope

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first visual decision workbench and regression testbench for TypeSafe Jev: edit structured state and questions, inspect distributions, batch JSONL cases, and compare project definitions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jeiel85/jevscope) |
| Maintainer | [jeiel85](https://github.com/jeiel85). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | pnpm monorepo: React/Vite Studio, local API, core schemas, evaluator, and `@typesafe-ai/sdk` provider adapter. v0.1 workbench. |
| Requirements | Node.js 20+, pnpm. Live evaluation needs `TYPESAFE_API_KEY` in the API process `.env` (never `VITE_*`). Studio defaults to `http://localhost:5173` with API on loopback `:4317`. |
| License | [MIT](https://github.com/jeiel85/jevscope/blob/d39ab43e88af20be7142b4335c84fbf69c740e0e/LICENSE). |

## When to use

Use it to design and regression-test typed Jev questions against fixture state, inspect probability distributions, and compare two definitions on the same cases. Prefer a CLI or library when you do not need a visual workbench.

## How it works

The Studio edits `.jevscope.json` projects locally. The [TypeSafe provider](https://github.com/jeiel85/jevscope/blob/d39ab43e88af20be7142b4335c84fbf69c740e0e/packages/provider-typesafe/src/index.ts) calls `TypeSafeClient.systemOne` with your state and questions. Local policy thresholds derive auto/review buckets from Choice/Score confidence and Noul YES/NO cuts—those buckets are JevScope-derived, not raw Jev answers. Batch and compare flows run JSONL cases with optional expectation checks. Project editing, validation, and history browsing stay local; only live evaluation leaves the machine via the API process.

## Get started

```sh
git clone https://github.com/jeiel85/jevscope.git
cd jevscope
git checkout d39ab43e88af20be7142b4335c84fbf69c740e0e
cp .env.example .env   # set TYPESAFE_API_KEY for live runs
pnpm install
pnpm validate:example
pnpm test
# Live UI (billable when evaluating): pnpm dev
```

GitHub Pages hosts a project overview only—not a hosted evaluator. This listing did not start the Studio against a live key.

## Examples and demos

- [examples/game-ai](https://github.com/jeiel85/jevscope/tree/d39ab43e88af20be7142b4335c84fbf69c740e0e/examples/game-ai): sample project and JSONL cases.
- Upstream workbench screenshots in `docs/` illustrate the UI (upstream assets, not re-captured here).
- Package unit tests cover core, evaluator, and provider normalization.

## Limits and data handling

Live runs send state and questions to TypeSafe through the local API. Keys must remain in the API environment. Default bind is loopback with a 1 MiB body limit and Studio-origin allowlist. Expectation metrics are local checks, not model-quality claims. Studio/API packages currently ship few UI/API tests beyond packages.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d39ab43](https://github.com/jeiel85/jevscope/tree/d39ab43e88af20be7142b4335c84fbf69c740e0e): MIT. AI-assisted source review of provider adapter, README, example project, and license. On Node.js 22.19.0 with pnpm 12.4.2: **`pnpm validate:example` OK**; **`pnpm -r test`**: core 5, evaluator 5, provider-typesafe 1 passed (apps had no test files). No live TypeSafe evaluation or Studio session was performed.

Related: [Advocaat](advocaat.md).
