# sieve

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local MCP server for coding agents: code enumerates repository/file/search candidates; TypeSafe Jev scores them via `jev_grep`, `jev_rank`, and `jev_search`—returning locations and probabilities, never generated prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/derwells/sieve) |
| Maintainer | [derwells](https://github.com/derwells). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python MCP server (`sieve` 0.1.0) with `bin/sieve-mcp` launcher. |
| Requirements | Python **≥ 3.12**, [uv](https://docs.astral.sh/uv/); `TYPESAFE_API_KEY` (launcher may source `~/.config/sieve/env`). Optional `BRAVE_API_KEY` for `jev_search`. |
| License | [MIT](https://github.com/derwells/sieve/blob/d3ff9c3cf4fa19a93126d67c45a61b2d37678447/LICENSE) (+ [NOTICE](https://github.com/derwells/sieve/blob/d3ff9c3cf4fa19a93126d67c45a61b2d37678447/NOTICE)). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `uv run pytest` **184 passed, 8 skipped** on the review host. Live MCP/TypeSafe sessions not run. Distinct from [winnow](winnow.md)’s Claude Code context sieve. |

## When to use

Use it when an agent should **filter or rank local candidates with Jev** before opening files itself. Prefer [sgrep](sgrep.md) / [jegrep](jegrep.md) / [jgrep](jgrep.md) for standalone CLIs, or [winnow](winnow.md) for hiding tool-result blocks already in context. Optional Brave search sends queries/results through your configured backend.

## How it works

[`sieve/client.py`](https://github.com/derwells/sieve/blob/d3ff9c3cf4fa19a93126d67c45a61b2d37678447/sieve/client.py) builds an `AsyncTypeSafeClient` (`jev-latest`) from `TYPESAFE_API_KEY`. [`sieve/jev.py`](https://github.com/derwells/sieve/blob/d3ff9c3cf4fa19a93126d67c45a61b2d37678447/sieve/jev.py) batches Noul/Choice scoring with cache and token budgets. The MCP tools expose grep/rank/search; the agent still reads survivors. File previews and candidate text go to TypeSafe when live.

## Get started

```sh
git clone https://github.com/derwells/sieve.git
cd sieve
git checkout d3ff9c3cf4fa19a93126d67c45a61b2d37678447
uv sync
uv run pytest
# Live MCP (charges): set TYPESAFE_API_KEY, register bin/sieve-mcp with your harness
```

Live tools send candidate text to TypeSafe. This listing did not register an MCP client or call live APIs.

## Examples and demos

- Offline `tests/` — **184 passed, 8 skipped** (live-marked tests skipped without a key).
- Eval notes under `evals/` (upstream illustrations; not re-run here).

## Limits and data handling

Requires a TypeSafe key for live scoring. Candidate previews leave the machine. Brave is optional and separate. Experimental early release; treat recall/cost notes in the upstream README as author-reported unless you re-measure.

## Review and maintenance

Reviewed on **2026-09-22** at [commit d3ff9c3](https://github.com/derwells/sieve/tree/d3ff9c3cf4fa19a93126d67c45a61b2d37678447): MIT **0.1.0**. AI-assisted source review of README, LICENSE, `sieve/client.py`, `sieve/jev.py`, and tests. Offline pytest as above. No live TypeSafe spend.

Related: [sgrep](sgrep.md), [jegrep](jegrep.md), [jgrep](jgrep.md), [winnow](winnow.md), [jev-reranker](jev-reranker.md).
