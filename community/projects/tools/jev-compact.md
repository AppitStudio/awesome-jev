# jev-compact

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex CLI plugin that scores tool calls with TypeSafe Jev before compaction, then re-injects verbatim any critical outputs the built-in summary dropped. Inspired by [fast-jev-compaction](fast-jev-compaction.md) (Claude Code) but written for Codex hooks. Not affiliated with TypeSafe or OpenAI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fatelei/jev-compact) |
| Maintainer | [fatelei](https://github.com/fatelei). Independently curated; this entry is not an upstream submission or endorsement. Independent/unofficial—not maintained by TypeSafe. |
| Format | Codex plugin marketplace package **jev-compact 0.1.0** under `plugins/jev-compact` (TypeScript; Node or Bun). |
| Requirements | Codex CLI ≥ 0.155 with hooks enabled; `node` or `bun` on PATH; `TYPESAFE_API_KEY` (or `apiKey` in `~/.codex/fast-jev-compaction.json`). Without a key the plugin is a no-op. |
| License | [MIT](https://github.com/fatelei/jev-compact/blob/213a37faef2bc87c4d8ea830f8b779f379a32da8/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline vitest inspected. Live Codex sessions and TypeSafe calls were not run. |

## When to use

Use it when Codex auto/manual compaction should keep Jev-selected tool outputs verbatim after the summary. Prefer [fast-jev-compaction](fast-jev-compaction.md) for Claude Code session compaction. Prefer [jev-codex-token-saver](jev-codex-token-saver.md) when you want MCP-selected workspace excerpts rather than compaction repair.

## How it works

1. **PreCompact** hook reads the rollout JSONL, pairs tool calls, and asks Jev noul questions (batched) for keep / drop_result / drop_call; decisions are archived with TTL.
2. Codex built-in compaction still runs (`continue: true`—the plugin never blocks it). Codex 0.155 hooks cannot fully replace the compacted message list the way Claude Code can.
3. **SessionStart** (`source=compact`) checks membership (call_id / sha256 / head substring), ranks missing keeps by score, and supplies `additionalContext` within a char budget.

Jev HTTP client: [`plugins/jev-compact/src/jev/client.ts`](https://github.com/fatelei/jev-compact/blob/213a37faef2bc87c4d8ea830f8b779f379a32da8/plugins/jev-compact/src/jev/client.ts).

## Get started

```sh
git clone https://github.com/fatelei/jev-compact.git
cd jev-compact
git checkout 213a37faef2bc87c4d8ea830f8b779f379a32da8
cd plugins/jev-compact
# Offline tests (review host used bun):
bun test
# Install into Codex (after trusting hooks in the TUI):
#   codex plugin marketplace add /path/to/jev-compact
#   codex plugin add jev-compact@fast-jev
```

## Examples and demos

- Upstream README architecture diagram and config defaults (`keepThreshold`, `maxBackfillChars`).
- Rollout fixtures under `plugins/jev-compact/test/fixtures/`.
- Review host: **`bun test`**: **107 passed** across 13 files (0 fail). No live Codex/TypeSafe.

## Limits and data handling

Tool-call arguments/results and question text can leave the host toward TypeSafe when a key is set. Untrusted hooks are skipped until you approve them in Codex. Compaction quality still depends on Codex's built-in summary; the plugin guides and repairs, it does not replace summarization.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 213a37f](https://github.com/fatelei/jev-compact/tree/213a37faef2bc87c4d8ea830f8b779f379a32da8): **0.1.0**, MIT. AI-assisted source review of README, PreCompact/SessionStart hooks, Jev client, and LICENSE. Offline vitest via bun: **107 passed**. No live TypeSafe or Codex compaction session.

Related: [fast-jev-compaction](fast-jev-compaction.md), [jev-codex-token-saver](jev-codex-token-saver.md), [jev-in-codex](jev-in-codex.md).
