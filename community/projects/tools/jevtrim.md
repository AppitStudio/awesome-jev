# jevtrim

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Benchmark: TypeSafe Jev as a context-relevance judge vs retrieval/summarization on LoCoMo, with matched token budgets and reproducible reports.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pdrpinto/jevtrim) |
| Maintainer | [pdrpinto](https://github.com/pdrpinto). Independently curated. |
| Format | Python/Jupyter research harness + reports. |
| Requirements | Python; LoCoMo dataset; OpenRouter access to `typesafe/jev-1.13` (or documented path); notebook/runtime deps per README. |
| License | [MIT](https://github.com/pdrpinto/jevtrim/blob/2d0bab66d75c45d64f6eb0149053a2418909d3b1/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **measure whether Jev-scored chunk selection** beats cosine top-k under the same segmenters and budgets before adopting a compaction strategy.

## How it works

Segments long conversations (native events, LangChain splitters), scores chunks with Jev or retrieval, then applies the same greedy budget selector so accuracy differences come from ranking.

## Get started

```sh
git clone https://github.com/pdrpinto/jevtrim.git
cd jevtrim
git checkout 2d0bab66d75c45d64f6eb0149053a2418909d3b1
# Follow README for LoCoMo setup, OpenRouter key, and report notebooks
```

## Examples and demos

- README accuracy-vs-budget figures and headline LoCoMo matrix (upstream-reported spend/accuracy).

## Limits and data handling

Benchmark numbers and dollar spend on the README are upstream-reported, not re-measured here. Conversation text goes to OpenRouter/TypeSafe when scoring live.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 2d0bab6](https://github.com/pdrpinto/jevtrim/tree/2d0bab66d75c45d64f6eb0149053a2418909d3b1). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [Waxmell jev-compaction](waxmell114514-jev-compaction.md).
