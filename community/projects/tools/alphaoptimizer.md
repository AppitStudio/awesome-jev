# AlphaOptimizer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex-oriented tool that keeps large command/tool outputs usable: store the full text locally with limits, and optionally ask TypeSafe Jev which chunks matter before returning a compact view.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alpha-tales/alphaoptimizer) |
| Maintainer | [alpha-tales](https://github.com/alpha-tales). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js TypeScript package **0.1.0** (Codex plugin / MCP-oriented tooling, Vitest). |
| Requirements | Node tooling for install/tests. Offline `npm test` needs no key. Live ranking needs a TypeSafe API key (`enabled` Jev path). |
| License | [MIT](https://github.com/alpha-tales/alphaoptimizer/blob/87389d482c86d964c58ae32696028c78ed662c77/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline vitest: **66 passed / 1 failed** (`spawn E2BIG` on a multi-process quota test on this host). Live TypeSafe / Codex sessions not run. Upstream payload-reduction percentages were not independently reproduced. |

## When to use

Use it when Codex (or a similar agent) routinely blows the context window with large logs/search dumps and you want local storage plus optional Jev relevance ranking of chunks. Prefer [jev-codex-token-saver](jev-codex-token-saver.md) / [jev-in-codex](jev-in-codex.md) when the workflow is MCP excerpt selection rather than this AlphaTales optimizer. Do not treat upstream reduction percentages as guaranteed savings.

## How it works

Application code decides whether an output should be processed, splits it into chunks, and may call [`src/providers/jev.ts`](https://github.com/alpha-tales/alphaoptimizer/blob/87389d482c86d964c58ae32696028c78ed662c77/src/providers/jev.ts) which POSTs noul questions to `https://api.typesafe.ai/v1/systemone` (endpoint hard-locked). Secret-looking / non-normal privacy classes skip Jev. Ranked compact text goes back to the agent; the full artifact can be requested by ID until expiry/quota cleanup. Without a key or with Jev disabled, ranking is skipped.

## Get started

```sh
git clone https://github.com/alpha-tales/alphaoptimizer.git
cd alphaoptimizer
git checkout 87389d482c86d964c58ae32696028c78ed662c77
npm ci --ignore-scripts
npm test
```

Live Codex use follows the upstream README (plugin/MCP config and TypeSafe key). Live calls send chunk text to TypeSafe and can incur charges.

## Examples and demos

- Offline **`npm test` (vitest)**: **66 passed**, **1 failed** on this host (`tests/quota.test.ts` multi-process spawn hit `E2BIG`). Nine of ten files passed cleanly.
- Upstream documents observed payload reduction ranges; those figures were not re-measured here.

## Limits and data handling

Jev is optional and skipped for sensitive/secret privacy classes and when disabled. Live calls send candidate chunk text to TypeSafe. Local full-output storage has expiry and quota limits. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 87389d4](https://github.com/alpha-tales/alphaoptimizer/tree/87389d482c86d964c58ae32696028c78ed662c77): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `src/providers/jev.ts`, and offline tests. **No live TypeSafe**.

Related: [jev-codex-token-saver](jev-codex-token-saver.md), [jev-in-codex](jev-in-codex.md), [fast-jev-compaction](fast-jev-compaction.md).
