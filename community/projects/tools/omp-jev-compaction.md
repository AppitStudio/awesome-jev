# omp-jev-compaction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Verbatim, Jev-scored context reduction for [omp](https://github.com/jerryfane/oh-my-pi): tool calls and results are scored with TypeSafe Jev (or OpenRouter’s Decisions path); low-scoring payloads are truncated with recoverable spill notes while user/assistant text stays byte-identical.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jerryfane/omp-jev-compaction) |
| Maintainer | [jerryfane](https://github.com/jerryfane). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript omp plugin / npm package **`omp-jev-compaction` 0.1.0**. Vendors scoring core from [fast-jev-compaction](fast-jev-compaction.md) at commit `e3f262a`. |
| Requirements | Node.js ≥ 18; [omp](https://github.com/jerryfane/oh-my-pi); live scoring needs `TYPESAFE_API_KEY` and/or `OPENROUTER_API_KEY` (`TYPESAFE_API_KEY` wins when both are set). |
| License | [MIT](https://github.com/jerryfane/omp-jev-compaction/blob/3719495ceb109c0d6e40d29053675f0d6ecb2e9f/LICENSE). TypeSafe/OpenRouter usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from [fast-jev-compaction](fast-jev-compaction.md) (Claude Code) and [jev-compact](jev-compact.md) (Codex). |

## When to use

Use it when omp sessions should shrink large tool-heavy contexts with Jev keep/truncate decisions without rewriting prose. Prefer [fast-jev-compaction](fast-jev-compaction.md) for Claude Code hooks, or [jev-compact](jev-compact.md) for Codex PreCompact repair.

## How it works

The package maps omp messages into the vendored fast-jev scoring core, posts Noul-style keep questions to `https://api.typesafe.ai/v1/systemone` or OpenRouter Decisions, and applies a sticky rewrite policy so the provider prompt-cache prefix stays stable between rare rewrites. Continuous `context` reduction is the primary path; `session_before_compact` is registered but often declines when omp’s own shake already emptied tool bodies. Dropped payloads can spill under `~/.omp/jev-spill/` for one-read recovery.

## Get started

```sh
omp plugin install jerryfane/omp-jev-compaction
omp
```

```sh
git clone https://github.com/jerryfane/omp-jev-compaction.git
cd omp-jev-compaction
git checkout 3719495ceb109c0d6e40d29053675f0d6ecb2e9f
npm ci
npm test   # offline vitest; skips live.test.ts without JEV_LIVE=1
```

Live compaction sends conversation state (tool names, inputs, and message text; tool outputs are size-noted first) to the chosen decision endpoint and can incur charges.

## Examples and demos

- README sticky/cache-guard measurements and spill recoverability notes.
- Offline vitest suite under `tests/` (live suite gated by `JEV_LIVE=1`).

## Limits and data handling

Judged state leaves the host on live calls. Upstream recall measurements are vendor-reported; this listing did not re-run live sessions. omp plugin settings env wiring is documented; reading omp’s settings store was noted as not fully wired upstream.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 3719495](https://github.com/jerryfane/omp-jev-compaction/tree/3719495ceb109c0d6e40d29053675f0d6ecb2e9f): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, hook/asker, and vendored fast-jev core. Offline `npm test`: **61 passed**, 2 live tests skipped. No live TypeSafe/OpenRouter calls.

Related: [fast-jev-compaction](fast-jev-compaction.md), [jev-compact](jev-compact.md), [yoshi](yoshi.md).
