# jgrep (npm: jevgrep)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Node CLI that greps code, git diff hunks, or CSV rows by a plain-English description with one TypeSafe Jev Noul per chunk; `--diff` gates a change in CI with grep exit codes and `--tests` lists the test files a diff can affect. Distinct from the Python [jgrep](jgrep.md) by keltokhy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kyu1204/jgrep) |
| Maintainer | [kyu1204](https://github.com/kyu1204). Self-submission: the contributor maintains jgrep. Listing is not an endorsement. |
| Format | npm package **jevgrep 0.4.0** (bin `jgrep`); TypeScript built with Bun into a single-file Node CLI with no runtime dependencies. |
| Requirements | Node **≥ 18**; `TYPESAFE_API_KEY` (set by `jgrep init`, the environment, a project `.env`, or `~/.config/jgrep/env`); `git` for `--diff` and `--tests`. TypeSafe endpoint only (OpenRouter is [issue #7](https://github.com/kyu1204/jgrep/issues/7), open). |
| License | [MIT](https://github.com/kyu1204/jgrep/blob/131ae043e2140b2d955181f1ce48360f5f8f36c0/LICENSE). TypeSafe usage billed separately. |

## When to use

- **Gate a pull request on a rule written in English.** `jgrep --diff origin/main "adds an HTTP endpoint that has no auth check"` exits `0` on a match, `1` when clean, and `2` when it could not run (bad key, API down, malformed response), so a CI step can fail on a hit without turning an outage into a passing check.
- **Run only the tests a change can affect.** `jgrep --tests origin/main | xargs bun test` (or vitest, pytest, go test). Test files named after a changed file or importing a changed module are selected in code; the remaining files are asked of Jev.
- **Find code by what it does** when the identifier is unknown: `jgrep "reads user input without validating it" app/` prints `file:line` ranges with a probability.
- **Score a table** (CSV/JSONL) with one or more Jev questions per row: `jgrep --rows creators.csv --questions q.json --out scored.csv`.

Prefer [jegrep](jegrep.md) if you need OpenRouter, [jev-semgrep](jev-semgrep.md) for line-level AND/OR/NOT propositions, and the Python [jgrep](jgrep.md) for a library API. This tool has no index and no embeddings; every run re-reads the tree, with answers cached locally.

## How it works

1. Files come from `git ls-files` (untracked included, ignored excluded) or a directory walk; binaries and files over 1 MB are skipped.
2. Each file is split at column-0 line starts into 5 to 60 line chunks. With `--diff`, each hunk is a chunk and keeps its `+`/`-` markers; with `--rows`, each row is a chunk.
3. Sixteen chunks and sixteen Noul questions ("look only at chunk c3, does it match: ...") go into one System One request to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` ([`src/jgrep.ts`](https://github.com/kyu1204/jgrep/blob/131ae043e2140b2d955181f1ce48360f5f8f36c0/src/jgrep.ts); HTTP, retries with backoff, and typed errors in [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/131ae043e2140b2d955181f1ce48360f5f8f36c0/src/providers.ts)).
4. Probabilities at or above `-t` (default 0.7; 0.5 for `--tests`) are printed in file order. `--questions` also accepts Choice and Score questions and writes one column per question.
5. Answers are cached by `(model, question, chunk)` in `~/.cache/jgrep/`; `--no-cache` skips it. A failed batch marks only its own chunks as errored; the rest of the run still prints, and the summary on stderr reports errored chunks with exit `2`.

Jev decides only "does this chunk match this description?". Chunking, batching, name/import-graph test matching, thresholds, caching, and exit codes are application code.

## Get started

```sh
npm i -g jevgrep
jgrep init                      # verifies the key against the API and stores it (chmod 600); optional Claude Code / Codex skill install
cd my-repo
jgrep "builds an SQL string by concatenation" src/          # live: sends the chunks of src/ to TypeSafe
jgrep --diff --staged "leaves debug output such as console.log"
jgrep --tests origin/main
```

Every command above except `init` is a live call that sends the searched text to TypeSafe and is billed by input tokens ($0.042 per million input tokens, output free, at the time of review). There is no offline or mock mode. A CI recipe with the three exit codes kept apart is in the [README](https://github.com/kyu1204/jgrep/blob/131ae043e2140b2d955181f1ce48360f5f8f36c0/README.md#lint-a-change-with-rules-written-in-english).

Inspected revision:

```sh
git clone https://github.com/kyu1204/jgrep.git
cd jgrep
git checkout 131ae043e2140b2d955181f1ce48360f5f8f36c0
bun test src/            # 91 tests, offline (fetch is injected)
```

## Examples and demos

- [README usage section](https://github.com/kyu1204/jgrep/blob/131ae043e2140b2d955181f1ce48360f5f8f36c0/README.md#use): code search, `--diff` rules, the GitHub Actions gate, `--tests`, and a CSV scoring run with a questions file. All need a live key.
- [`src/*.test.ts`](https://github.com/kyu1204/jgrep/tree/131ae043e2140b2d955181f1ce48360f5f8f36c0/src): chunking, batching, cache, per-batch failure isolation, retry/backoff, and test selection, run offline against an injected `fetch`.
- No separate hosted demo exists.

## Limits and data handling

- The text of every chunk searched (source code, diff hunks including removed lines, or CSV/JSONL rows) is sent to TypeSafe's API. Do not point it at trees or files containing secrets or personal data you cannot send there.
- Cached answers are stored unencrypted under `~/.cache/jgrep/` keyed by model, question, and chunk.
- Hits are probabilities against a free-text description, not a verified rule engine; `--diff` gates catch what the description makes Jev likely to flag and should complement, not replace, deterministic linters. `--tests` is a fast first signal; upstream recommends running the full suite afterwards.
- TypeSafe endpoint only; no OpenRouter or local model path. Files over 1 MB and binaries are skipped.
- Author-reported figures (see below) are for the maintainer's repositories; no independent precision/recall measurement is claimed.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 131ae04](https://github.com/kyu1204/jgrep/tree/131ae043e2140b2d955181f1ce48360f5f8f36c0) (tag `v0.4.0`, npm `jevgrep@0.4.0`), MIT (`package.json` + LICENSE). The submitter is the maintainer; everything below is maintainer-run, not an independent review.

- Read: README, `src/jgrep.ts` (chunking, batching, cache, `ENDPOINT`/`MODEL` constants), `src/providers.ts` (request, rate limiting, retries, typed errors), `src/cli.ts` (flags and exit codes), and the seven `src/*.test.ts` files.
- Ran: `bun test src/` at this commit, 91 tests passed offline. Live runs with a TypeSafe key on 2026-09-23: `jgrep` over jgrep's own `src/` = 238 chunks, 1.0 s, 71,509 input tokens, $0.003; `jgrep --tests` on a small diff = 1 request, 3,430 tokens, 0.9 s. The README figure of 896 chunks, 1.8 s, 240k tokens, $0.010 on another TypeScript tree is author-reported (2026-09-19) and was not rerun here.
- External report: [issue #3](https://github.com/kyu1204/jgrep/issues/3) (closed) reported that empty answers read as "nothing found" and that the CI recipe turned an error into a pass; both were fixed in 0.4.0 (exit `2` on errored chunks, recipe keeps the three exit codes apart).
- Not checked: installation on Windows, behaviour on repositories larger than a few thousand chunks, and search quality on codebases other than the maintainer's.

Related: [jegrep](jegrep.md), [jev-semgrep](jev-semgrep.md), [jgrep](jgrep.md) (Python), [sgrep](sgrep.md).
