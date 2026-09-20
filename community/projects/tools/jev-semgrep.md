# jev-semgrep

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Meaning-grep CLI: score each line against a plain-English (or other-language) proposition with TypeSafe Jev, combine meanings with AND/OR/NOT, and print matches—distinct from regex Semgrep Inc tooling.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uehaj/jev-semgrep) |
| Maintainer | [uehaj](https://github.com/uehaj) (Junji UEHARA). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **@uehaj/semgrep 0.2.2** (CLI binary name `semgrep`; single-file `semgrep.mjs`). |
| Requirements | Node.js ≥ 20.12; live search needs `TYPESAFE_API_KEY` (env, `./.env`, or `~/.config/semgrep/.env`). |
| License | [MIT](https://github.com/uehaj/jev-semgrep/blob/ba6ef50f85d0c5d6caa4db102ee4db4a08c85dd2/LICENSE). |

## When to use

Use it to filter ticket dumps, mixed-language logs, or corpora by whether a proposition holds for each line (“customer asks for a refund”), including cross-language queries. Prefer [jegrep](jegrep.md) to search a *code tree* by intent; prefer [jsort](jsort.md) to *rank* lines along a dimension rather than filter them. Do not confuse this package with [Semgrep](https://semgrep.dev/) static analysis—the CLI name overlaps, but the projects are unrelated.

## How it works

[`semgrep.mjs`](https://github.com/uehaj/jev-semgrep/blob/ba6ef50f85d0c5d6caa4db102ee4db4a08c85dd2/semgrep.mjs) batches lines (default 30) into TypeSafe `https://api.typesafe.ai/v1/systemone` requests (model `jev-latest`) with concurrent workers, applies a probability threshold, and supports AND/OR/NOT meaning composition. Matching is conceptual: a Japanese meaning can select English (and other) lines without a translation step.

## Get started

```sh
# Prefer an unambiguous install path if `semgrep` already refers to Semgrep Inc:
npm install -g @uehaj/semgrep
# or:
git clone https://github.com/uehaj/jev-semgrep.git
cd jev-semgrep
git checkout ba6ef50f85d0c5d6caa4db102ee4db4a08c85dd2
export TYPESAFE_API_KEY=…
./semgrep -n -e "customer is angry or frustrated" tests/corpus.txt
npm test   # offline fixture checks in tests/check.sh
```

Live runs send line text to TypeSafe and incur provider charges. This listing did not call the API.

## Examples and demos

- Multilingual corpus demos in the README (`tests/multi.txt`, Japanese↔English examples).
- Offline checks under [`tests/`](https://github.com/uehaj/jev-semgrep/tree/ba6ef50f85d0c5d6caa4db102ee4db4a08c85dd2/tests) (`check.sh`, `cases.json`).

## Limits and data handling

Scanned line text leaves the machine for TypeSafe. Thresholds and batching affect cost/latency but do not remove provider charges. Upstream notes English meanings are safest near the threshold. The published CLI name `semgrep` can collide with Semgrep Inc on `PATH`.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ba6ef50](https://github.com/uehaj/jev-semgrep/tree/ba6ef50f85d0c5d6caa4db102ee4db4a08c85dd2): **0.2.2**, MIT. AI-assisted source review of README, `semgrep.mjs`, `package.json`, and license. Offline `npm test` / live TypeSafe calls were not run on the review host.

Related: [jegrep](jegrep.md), [jsort](jsort.md).
