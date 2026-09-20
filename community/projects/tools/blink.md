# blink

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Search a codebase with TypeSafe Jev by walking directories with an ensemble of walkers that pick the most relevant next file or folder.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ellipsis-dev/blink) |
| Maintainer | [ellipsis-dev](https://github.com/ellipsis-dev). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Bun TypeScript CLI (`./blink`), package private; uses official `@typesafe-ai/sdk`. |
| Requirements | Bun 1.3.14+; `TYPESAFE_API_KEY`. Live search incurs TypeSafe usage. |
| License | Unspecified at the reviewed commit: no project license file or package `license` field was found. Public source access does not establish an open-source license or reuse permission. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live Jev search was not run. |

## When to use

Use it when you want a natural-language path finder over a local tree without building an embedding index. Prefer [jegrep](jegrep.md) for line-oriented semantic grep with ranked matches, or [jev-semgrep](jev-semgrep.md) when you filter individual lines against a proposition.

## How it works

[`src/search.ts`](https://github.com/ellipsis-dev/blink/blob/a621ede75649303a933828c18c27ad800bb43ef0/src/search.ts) lists immediate directory entries (honoring `settings.json` ignores), then posts a Choice question via `TypeSafeClient.systemOne` with model `jev-latest`: which candidate is most likely to be the relevant file or contain it. Walkers in [`src/walkers.ts`](https://github.com/ellipsis-dev/blink/blob/a621ede75649303a933828c18c27ad800bb43ef0/src/walkers.ts) explore recursively with optional parallelism (`--n_walkers`). Application code owns filesystem reads and ranking tables; Jev only answers the typed Choice.

## Get started

```sh
git clone https://github.com/ellipsis-dev/blink.git
cd blink
git checkout a621ede75649303a933828c18c27ad800bb43ef0
bun install
export TYPESAFE_API_KEY="your-key"
./blink "where is authentication handled?" test/example_codebase --n_walkers 100 --recursive
```

Review licensing before reuse. Live calls send directory/file names and the query to TypeSafe and can incur charges. This listing did not run Bun tests or live search.

## Examples and demos

- Bundled `test/example_codebase/` tree and README walkthrough tables.
- Offline-oriented tests under `test/` (`search.test.ts`, `walkers.test.ts`, `traces.test.ts`) — not executed on the review host.

## Limits and data handling

Query text and relative entry names leave the host for TypeSafe. Ignored node names come from `settings.json`. Upstream accuracy/speed anecdotes were not independently measured. Missing license file means reuse terms are unclear.

## Review and maintenance

Reviewed on **2026-09-20** at [commit a621ede](https://github.com/ellipsis-dev/blink/tree/a621ede75649303a933828c18c27ad800bb43ef0). AI-assisted source review of README, `package.json`, `src/search.ts`, `src/walkers.ts`, and license absence. No live TypeSafe calls.

Related: [jegrep](jegrep.md), [jev-semgrep](jev-semgrep.md).
