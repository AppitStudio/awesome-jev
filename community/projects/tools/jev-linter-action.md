# jev-linter-action

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that runs your own yes/no review questions over selected repository files with TypeSafe Jev and fails CI when expected answers miss configured probability thresholds. Distinct from [jev-ci-selector](jev-ci-selector.md) (which CI *jobs* apply) and from [jev-lint](jev-lint.md) / [JevLint](jevlint.md) (local semantic lint CLIs).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sable-inc/jev-linter-action) |
| Maintainer | [sable-inc](https://github.com/sable-inc). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js 24 GitHub Action **1.0.0** (`action.yml` + `src/*.mjs`; no npm runtime deps). |
| Requirements | GitHub Actions (or local `node src/main.mjs`); `TYPESAFE_API_KEY` secret for live checks. Offline `npm test` needs no key. |
| License | [MIT](https://github.com/sable-inc/jev-linter-action/blob/1d085f1ccfc430e4bd9262cffe291d049ec7f5e2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `node --test` inspected. Live Action runs and live TypeSafe calls were not executed. |

## When to use

Use it when prompts, agent configs, or policy docs need semantic consistency checks in CI with explicit expect/threshold suites in `.jev-lint.json`. Prefer path filters for purely structural change detection; prefer [Moongate](moongate.md) for diff-vs-rule annotations; prefer [jev-ci-selector](jev-ci-selector.md) to choose which jobs run.

## How it works

[`src/lint.mjs`](https://github.com/sable-inc/jev-linter-action/blob/1d085f1ccfc430e4bd9262cffe291d049ec7f5e2/src/lint.mjs) posts Noul questions to `https://api.typesafe.ai/v1/systemone` with matched file contents (filenames preserved; optional `perFile`). Code maps yes probabilities to pass/fail against `expect` and `minProbability` (> 0.5). Paths outside the repo root (including symlink escapes) are refused. Failures fail closed; rate limits retry with backoff. Reports omit target contents.

## Get started

```sh
git clone https://github.com/sable-inc/jev-linter-action.git
cd jev-linter-action
git checkout 1d085f1ccfc430e4bd9262cffe291d049ec7f5e2
npm test
# Wire uses: sable-inc/jev-linter-action@v1 with secrets.TYPESAFE_API_KEY
# and a .jev-lint.json suite file — see upstream README.
```

## Examples and demos

- README shows a prompt-consistency suite and Action permissions snippet.
- Review host: **`npm test`** (`node --test`): **10 passed** (mocked HTTP; no key).

## Limits and data handling

Selected file contents and questions go to TypeSafe. Do not target credentials. Fork PRs typically lack secrets—skip or run offline checks there. PRs that edit the Action config can change the rubric; keep review on those diffs. Byte/file caps are not token counts—respect model context. Pin Action SHAs for immutability.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 1d085f1](https://github.com/sable-inc/jev-linter-action/tree/1d085f1ccfc430e4bd9262cffe291d049ec7f5e2): **1.0.0**, MIT. AI-assisted source review of README, `action.yml`, and `src/lint.mjs`. Offline tests: **10 passed**. No live TypeSafe or GitHub Actions runs.

Related: [jev-ci-selector](jev-ci-selector.md), [Moongate](moongate.md), [jev-lint](jev-lint.md), [Jev Review Action](jev-review-action.md).
