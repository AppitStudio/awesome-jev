# semantic-test-matcher

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript CLI (`rbt`) that ranks which test files to re-run for a changed source file: it profiles paths, code structure and diffs, then TypeSafe Jev judges each candidate test in batched requests, with a local answer cache, score blending, an OpenAI Decisions ranker option and a heuristics fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JustasMonkev/semantic-test-matcher) |
| Product homepage | [www.npmjs.com](https://www.npmjs.com/package/semantic-test-matcher) |
| Maintainer | [JustasMonkev](https://github.com/JustasMonkev). Independently curated. |
| Format | npm package `semantic-test-matcher` (0.2.0 at review) exposing `rbt match`, `benchmark`, `status`, `completion` |
| Requirements | Node.js 22.12+; a `TYPESAFE_API_KEY` (without one, `rbt` ranks with local heuristics only). |
| License | [MIT](https://github.com/JustasMonkev/semantic-test-matcher/blob/f945ceb1c37d6594b5602b5d6119dd877bb31c25/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run the right subset of tests on a change in a large suite or agent loop.
- Benchmark the matcher against your own expected rankings with `rbt benchmark`.
- Mismatch: rankings are probabilistic; keep a full run in CI.

## How it works

Profiling builds a document per source and test file; [`src/services/jev.ts`](https://github.com/JustasMonkev/semantic-test-matcher/blob/f945ceb1c37d6594b5602b5d6119dd877bb31c25/src/services/jev.ts) asks Jev whether each candidate should re-run, batching larger suites; answers are cached and blended with structural signals. `--ranker decisions` uses OpenAI `/v1/decisions` instead.

## Get started

Install and match (README):

```sh
npm install --global semantic-test-matcher
export TYPESAFE_API_KEY=...
rbt match src/price-engine.ts --candidates tests --json
```

Uncached candidate judgments are billed to your TypeSafe key.

## Examples and demos

- Sample workspace `prompts-idea/` (README *Sample Dataset*).

## Limits and data handling

File paths, code profiles and diffs go to TypeSafe (or OpenAI with the Decisions ranker). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit f945ceb1c37d](https://github.com/JustasMonkev/semantic-test-matcher/tree/f945ceb1c37d6594b5602b5d6119dd877bb31c25). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
