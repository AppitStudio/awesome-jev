# similarity-ts-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI for TypeScript maintainers that runs `similarity-ts` and `fallow` duplicate detection, asks TypeSafe Jev which reported pairs a careful reviewer would have merged, and prints only those families—each with the change to make.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kongyo2/similarity-ts-jev) |
| Maintainer | [kongyo2](https://github.com/kongyo2). This update is a self-submission by the maintainer; the catalog first listed the project independently on 2026-09-22. The CLI is MIT-licensed and free; Jev usage is billed by the provider to the user's own key. |
| Format | TypeScript CLI and ESM library, npm package (`@kongyo2/similarity-ts-jev` 0.2.0). Detection uses the maintainer's [`@kongyo2/similarity-ts`](https://www.npmjs.com/package/@kongyo2/similarity-ts) (an edition of mizchi/similarity) and [`fallow`](https://www.npmjs.com/package/fallow). |
| Requirements | Node.js **≥ 22**. `TYPESAFE_API_KEY` for live judging; `TYPESAFE_BASE_URL` and `TYPESAFE_DEFAULT_MODEL` for a TypeSafe-compatible gateway. `--dry-run`, `--replay`, and fully cached runs need no key. |
| Jev's role | Four questions per pair: a 0–3 `refactor` score, `same_logic`, `same_concept`, and the `shape` of the change. Code batches the requests, applies the `--min-score` cutoff (default 1.9), adds flags, and groups families. |
| License | [MIT](https://github.com/kongyo2/similarity-ts-jev/blob/b1cf4a44e4caad9da12181b58fdc87ca7d125d65/LICENSE). |
| Disclosure | Maintainer self-submission prepared with AI assistance. Listing is not endorsement. Offline `npm test` **62 pass**; live runs are summarized under Review and maintenance. |

## When to use

- Clone detectors flood you with lookalikes and you want **Jev to keep only the pairs a reviewer would merge**, each labeled `copy` (delete one copy), `derive` (write one in terms of the other), or `extract` (pull out a shared helper).
- Gate CI on reported duplication with `--fail-on-duplicates`, or hand the report to a coding agent as a refactoring worklist.
- Fit the cutoff to one repository: record a run, label 20–40 pairs, and check precision and recall with `--calibrate --labels` before trusting the default.

Prefer [sgrep](sgrep.md) / [jegrep](jegrep.md) for intent search, or [Supercov](supercov.md) for per-file quality scores. A reported pair is a review suggestion, not proof that a merge is required.

## How it works

1. **Detect.** `similarity-ts` (functions, types, classes) and `fallow dupes --near` in four modes run on the same paths; their findings are merged into one list of pairs. Tests are included unless excluded with `--exclude`.
2. **Judge.** [`questions.ts`](https://github.com/kongyo2/similarity-ts-jev/blob/b1cf4a44e4caad9da12181b58fdc87ca7d125d65/src/questions.ts) asks four independent questions about both declarations (file path, leading comment, source text): `refactor` (0–3), `same_logic`, `same_concept`, and a `shape` choice among `remove_copy`, `derive`, and `extract_shared`. [`judge.ts`](https://github.com/kongyo2/similarity-ts-jev/blob/b1cf4a44e4caad9da12181b58fdc87ca7d125d65/src/judge.ts) packs up to 64 pairs or about 50,000 estimated tokens into one `@typesafe-ai/sdk` request, keeps 32 in flight, halves concurrency after a rate limit, retries transient failures, and splits a batch the gateway rejects.
3. **Decide in code.** [`decide.ts`](https://github.com/kongyo2/similarity-ts-jev/blob/b1cf4a44e4caad9da12181b58fdc87ca7d125d65/src/decide.ts) keeps pairs at or over `--min-score` and sets the flags; the reported pairs are then grouped into families. Flags change the wording, never the list: `?` when confidence is under `--unsure-below` (0.5), `~` within `--margin` (0.25) of the cutoff, and `!` when the passes of `--repeat` disagree.

`--conventions <text>` sends a note on what the repository keeps apart on purpose. `--record` and `--replay` re-decide a run under other thresholds without requests, and `--cache` asks again only for batches whose text changed.

## Get started

Offline checks from a clone (no key; tests replay a recorded fixture cache):

```sh
git clone https://github.com/kongyo2/similarity-ts-jev.git
cd similarity-ts-jev
git checkout b1cf4a44e4caad9da12181b58fdc87ca7d125d65
npm ci --ignore-scripts
npm test
```

Live use from the root of the repository you want to check:

```sh
npx @kongyo2/similarity-ts-jev . --dry-run    # pair, request, token and cost estimate; nothing is sent
export TYPESAFE_API_KEY=...                    # live judging sends code to the configured endpoint and incurs charges
npx @kongyo2/similarity-ts-jev . --stats --record run.json
npx @kongyo2/similarity-ts-jev --replay run.json --calibrate
```

Each family prints as its score, a flag, the shape, and the member locations. Empty output means nothing cleared the cutoff. Add `--labels labels.json` (pair keys mapped to `true` for merge or `false` for keep) to the replay for precision, recall, AUC, and a 5-fold hold-out.

## Examples and demos

- Offline suite under `test/`: **62 pass** at b1cf4a4, including end-to-end CLI runs from a fixture cache recorded against the live API.
- Upstream CI: [Actions run](https://github.com/kongyo2/similarity-ts-jev/actions/runs/35750604577) **success** at b1cf4a4; npm 0.2.0 was published from the same commit with provenance ([publish run](https://github.com/kongyo2/similarity-ts-jev/actions/runs/35750865423)).
- [`docs/measurements.md`](https://github.com/kongyo2/similarity-ts-jev/blob/b1cf4a44e4caad9da12181b58fdc87ca7d125d65/docs/measurements.md) is the maintainer's write-up behind every default: 61,371 requests over 8,253 pairs from date-fns, es-toolkit, remeda, and zod, and 132 hand labels, with raw summaries, labels, and CLI outputs under `docs/measurements/`. These are upstream measurements, not catalog results.

## Limits and data handling

Live judging needs an API key for TypeSafe or a TypeSafe-compatible gateway. It sends each pair's code, leading comments, relative file paths, and the working directory's name to the configured endpoint. A `--cache` file keeps those requests, code included, on disk; a `--record` file keeps locations and judgments. The `--dry-run` and `--stats` cost figures assume $0.042 per million input tokens.

Scores form a continuum rather than two clusters, so pairs near the cutoff can change sides between runs; `~` and `!` mark them, and `--repeat` decides on the mean. On the maintainer's hand labels the default cutoff favors recall over precision, and most false positives were repository conventions that `--conventions` can describe. A broad note can also suppress real duplicates, so check its effect with `--calibrate --labels`.

## Review and maintenance

Updated on **2026-09-23** at [commit b1cf4a4](https://github.com/kongyo2/similarity-ts-jev/tree/b1cf4a44e4caad9da12181b58fdc87ca7d125d65) (npm **0.2.0**, MIT): a maintainer update prepared with AI assistance, in which an AI agent ran the checks below. Offline: `npm ci --ignore-scripts` and `npm test` **62 pass** (13 suites) with `TYPESAFE_*` unset; `typecheck`, `build`, and the comment lint pass. The local build's `dist/` is byte-identical to the published package.

Live: the published package ran through a TypeSafe-compatible gateway with requested model `auto`; all 1,506 recorded responses reported `typesafe/jev-latest`. On zod's `packages/zod/src` (npm 4.6.5 sources, tests excluded), one pass judged 5,286 pairs in 230 requests (10.7M input tokens) and reported 335; the `--dry-run` token estimate was within 3.3%. Against the maintainer's 32 zod labels, the default cutoff gave precision 0.25 and recall 1.00 (maintainer: 0.23 and 1.00), and 1.00 and 1.00 with the maintainer's conventions note. Single passes over the TypeScript sources of nine other npm packages (effect, @effect/platform, mobx, @reduxjs/toolkit, rxjs, @trpc/server, @tanstack/query-core, @tanstack/router-core, and immer) left no pair unjudged; on effect (5,141 pairs) one rejected batch was split and asked again. These runs confirm the request path and reproduce the maintainer's figures on one corpus; they are not an independent quality evaluation.

An earlier catalog review on 2026-09-22 at [commit 90e41c2](https://github.com/kongyo2/similarity-ts-jev/tree/90e41c2a65dddddd86b807af7f5765c14a46e93e) (0.1.0) ran the offline suite (39 pass) without live spend; those results apply to that revision.

Related: [sgrep](sgrep.md), [jegrep](jegrep.md), [jgrep](jgrep.md), [Supercov](supercov.md).
