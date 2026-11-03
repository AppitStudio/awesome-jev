# opencode-fast-context (OpenCode plugin that finds the files and lines answering a code question and ranks the candidates with Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

OpenCode plugin that answers a code question with a bounded local search, then optionally ranks the candidate files and line ranges with a decision model (Jev or Clef) before returning compact citations. Without a provider it falls back to a lexical ranking. The author's small pinned benchmark shows median search time falling from 18.5 s to 4.5 s with Jev ranking, with lower retrieval quality than stock OpenCode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/enkay01/opencode-fast-context) |
| Maintainer | [enkay01](https://github.com/enkay01). Independently curated. |
| Format | OpenCode plugin (TypeScript, built locally) |
| Requirements | OpenCode 1.x or 2.x; Node to build; `TYPESAFE_API_KEY` with `FAST_CONTEXT_PROVIDER=jev` for Jev ranking. |
| License | [MIT](https://github.com/enkay01/opencode-fast-context/blob/78a18df2eae6f0830ccc4b1bc9d6a9137fc9b54d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers/systemone.ts`](https://github.com/enkay01/opencode-fast-context/blob/78a18df2eae6f0830ccc4b1bc9d6a9137fc9b54d/src/providers/systemone.ts) at the pinned commit. |

## When to use

- Speed up codebase research for a coding agent by ranking local search candidates with a fast decision model.
- Mismatch: not published to npm, and the README recommends explicit use while it is measured, not as a default replacement for search.

## How it works

`src/providers/systemone.ts` posts the query and each candidate to `{base}/v1/systemone` (`jev-latest` by default) with a per-call deadline, and returns the ranked citations to the agent; with no provider it returns the deterministic lexical ranking. Integration evidence: [`src/providers/systemone.ts`](https://github.com/enkay01/opencode-fast-context/blob/78a18df2eae6f0830ccc4b1bc9d6a9137fc9b54d/src/providers/systemone.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/enkay01/opencode-fast-context.git
cd opencode-fast-context
npm install && npm run build
export FAST_CONTEXT_PROVIDER=jev
export TYPESAFE_API_KEY=...   # then register the folder as a local plugin in opencode.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with install, providers and status: [github.com/enkay01/opencode-fast-context#readme](https://github.com/enkay01/opencode-fast-context#readme)
- Benchmark notes: [github.com/enkay01/opencode-fast-context/blob/main/BENCHMARK.md](https://github.com/enkay01/opencode-fast-context/blob/main/BENCHMARK.md)

## Limits and data handling

Candidate snippets and your query go to TypeSafe on your key when the provider is set; the benchmark is the author's own and small. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 78a18df2eae6](https://github.com/enkay01/opencode-fast-context/tree/78a18df2eae6f0830ccc4b1bc9d6a9137fc9b54d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
