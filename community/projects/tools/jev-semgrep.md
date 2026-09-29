# sys1grep (formerly jev-semgrep)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Meaning-grep CLI: score each line against a plain-English (or other-language) proposition with TypeSafe Jev, combine meanings with AND/OR/NOT, and print matches—distinct from regex Semgrep Inc tooling. Repository and npm package renamed from `jev-semgrep` / `@uehaj/semgrep` to **sys1grep** / `@uehaj/sys1grep`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uehaj/sys1grep) |
| Maintainer | [uehaj](https://github.com/uehaj) (Junji UEHARA). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **@uehaj/sys1grep** (CLI binaries `sys1grep`, `git-sys1grep`). Older `@uehaj/semgrep` still resolves historically; prefer the new name. |
| Requirements | Node.js ≥ 20.16; live search needs `TYPESAFE_API_KEY` (env or documented config paths). |
| License | [MIT](https://github.com/uehaj/sys1grep/blob/e27aef4fc39ae3a53a6a45ecaa868640290951a2/LICENSE). Provider usage may incur charges when live. |

## When to use

Use it to filter ticket dumps, mixed-language logs, or corpora by whether a proposition holds for each line (“customer asks for a refund”), including cross-language queries. Prefer [jegrep](jegrep.md) to search a *code tree* by intent; prefer [jsort](jsort.md) to *rank* lines along a dimension rather than filter them. Do not confuse this package with [Semgrep](https://semgrep.dev/) static analysis—the projects are unrelated (and the CLI no longer shadows the `semgrep` binary name).

## How it works

[`sys1grep.mjs`](https://github.com/uehaj/sys1grep/blob/e27aef4fc39ae3a53a6a45ecaa868640290951a2/sys1grep.mjs) batches lines into TypeSafe `https://api.typesafe.ai/v1/systemone` requests (model `jev-latest`) with concurrent workers, applies a probability threshold, and supports AND/OR/NOT meaning composition. Matching is conceptual: a Japanese meaning can select English (and other) lines without a translation step.

## Get started

```sh
npm install -g @uehaj/sys1grep
# or:
git clone https://github.com/uehaj/sys1grep.git
cd sys1grep
git checkout e27aef4fc39ae3a53a6a45ecaa868640290951a2
export TYPESAFE_API_KEY=…
./sys1grep -n -e "customer is angry or frustrated" tests/corpus.txt
npm test   # offline fixture checks
```

Live runs send line text to TypeSafe and incur provider charges. This listing did not call the API.

## Examples and demos

See upstream README demos and docs SVGs. Offline tests: `npm test`. Live search was not run on the review host.

## Limits and data handling

Each matching run sends line batches to TypeSafe. Threshold and batch size are CLI flags—tune for cost. Old GitHub URL `uehaj/jev-semgrep` redirects to `uehaj/sys1grep`.

## Review and maintenance

Rename refresh **2026-09-29** (Europe/Sofia) at [commit e27aef4](https://github.com/uehaj/sys1grep/tree/e27aef4fc39ae3a53a6a45ecaa868640290951a2). Catalog slug `jev-semgrep` kept for stable jevlist.ai URL; display name and links updated to sys1grep. AI-assisted README + LICENSE + package.json inspection; live API not called.
