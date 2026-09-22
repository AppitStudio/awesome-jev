# jevseek

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek proposes next-token candidates; TypeSafe Jev (via OpenRouter System One) chooses which token to append—turning a decision model into a sampler.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blingdivinity/jevseek) |
| Maintainer | [blingdivinity](https://github.com/blingdivinity). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python ≥ 3.11 CLI (`jevseek` 0.1.0): REPL/presets, optional Pangram scoring, recorded traces. |
| Requirements | Python **≥ 3.11**. Offline `pytest` needs no keys. Live sampling needs DeepSeek + OpenRouter keys (`typesafe/jev-1.13` on System One). |
| License | [MIT](https://github.com/blingdivinity/jevseek/blob/24b8235590d4f7bb8c1793fb7d712212ce88284c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline **pytest 14 passed**. Live DeepSeek/OpenRouter sampling not run. |

## When to use

Use it to **experiment with Jev as a token chooser** over DeepSeek logprobs (chat/essay/gated/pure presets). Prefer ordinary chat models when you need fluent long-form generation without per-token Jev cost. Related idea: [jevgpt](https://github.com/bewinxed/jevgpt) (dictionary-driven; not listed here).

## How it works

[`src/jevseek/jev.py`](https://github.com/blingdivinity/jevseek/blob/24b8235590d4f7bb8c1793fb7d712212ce88284c/src/jevseek/jev.py) calls `https://openrouter.ai/api/v1/systemone` with model `typesafe/jev-1.13`. Each step: DeepSeek returns top-k tokens; Jev answers a Choice over those candidates (often multi-order averaged); optional stop/ramble Noul questions end the reply. Application code owns decoding loops, presets, and recording. Live mode sends conversation/candidate text to DeepSeek and OpenRouter/TypeSafe.

## Get started

```sh
git clone https://github.com/blingdivinity/jevseek.git
cd jevseek
git checkout 24b8235590d4f7bb8c1793fb7d712212ce88284c
python3 -m pip install -e '.[dev]'
python3 -m pytest -q
# Live: copy .env.example; set DeepSeek + OpenRouter keys; jevseek --say "..."
```

## Examples and demos

- Offline `pytest`: **14 passed**.
- README shows side-by-side DeepSeek-alone vs Jev-chosen samples and `--record` traces.

## Limits and data handling

Per-token Jev calls add latency and OpenRouter/TypeSafe cost. Output quality depends on candidate floors (`--min-p`) and instruction presets. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 24b8235](https://github.com/blingdivinity/jevseek/tree/24b8235590d4f7bb8c1793fb7d712212ce88284c): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `src/jevseek/jev.py`, pyproject. **`pytest`: 14 passed**. No live DeepSeek/OpenRouter.

Related: [jeval](jeval.md), [jevals](jevals.md), [System One Playground](system-one-playground.md).
