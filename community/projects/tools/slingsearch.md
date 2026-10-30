# SlingSearch (multi-provider web and scholarly search for agents, ranked by Jev by default)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Ask a question and get ranked, source-backed excerpts with URLs, identifiers and provider provenance, with no generated answer. Several search providers run in parallel, results are deduplicated and fused, then ranked once against the question with Jev Latest as the default ranker (D1, Decider, Voyage, ensembles or plain fusion are alternatives). A relevance cutoff drops sources that would not help, and JSON output reports costs and timings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sileod/slingsearch) |
| Maintainer | [sileod](https://github.com/sileod). Independently curated. |
| Format | Python library and CLI |
| Requirements | Python; an OpenRouter key for the Jev ranker and keys for the search providers you enable. |
| License | [MIT](https://github.com/sileod/slingsearch/blob/d12984033263c09c95663a100422a7eafc52ef92/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/slingsearch/config.py`](https://github.com/sileod/slingsearch/blob/d12984033263c09c95663a100422a7eafc52ef92/src/slingsearch/config.py) at the pinned commit. |

## When to use

- Give a research agent fewer, better sources with a relevance score it can filter on.
- Mismatch: provider keys and costs add up; results depend on which providers you enable.

## How it works

`src/slingsearch/config.py` maps the `jev` ranker to `~typesafe/jev-latest` on OpenRouter; each candidate excerpt gets a relevance score from 0 to 1 against the question. Integration evidence: [`src/slingsearch/config.py`](https://github.com/sileod/slingsearch/blob/d12984033263c09c95663a100422a7eafc52ef92/src/slingsearch/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install 'git+https://github.com/sileod/slingsearch.git'
slingsearch "What limits diffusion models for time-series forecasting?" --mode scholar
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision-budget benchmark: [github.com/sileod/slingsearch/blob/d12984033263c09c95663a100422a7eafc52ef92/benchmarks/decision_budget.py](https://github.com/sileod/slingsearch/blob/d12984033263c09c95663a100422a7eafc52ef92/benchmarks/decision_budget.py)

## Limits and data handling

Your question goes to the search providers; the question and excerpts go to OpenRouter for ranking.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit d12984033263](https://github.com/sileod/slingsearch/tree/d12984033263c09c95663a100422a7eafc52ef92). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
