# jev-pruner

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Trim noisy Bash stdout with Jev after a command runs and before Claude Code or an opt-in Codex wrapper returns that result to the main model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tamaratran/jev-pruner) |
| Maintainer | [tamaratran](https://github.com/tamaratran). Independently curated; same author as [fast-jev-compaction](fast-jev-compaction.md). This entry is not an upstream submission or endorsement. |
| Format | TypeScript library with a Claude Code function-hook plugin and an opt-in Codex CLI wrapper/skill. |
| Requirements | Node.js 18+, npm. Claude path needs early-access function hooks and a TypeSafe key (`TYPESAFE_API_KEY` or plugin `apiKey`). Codex path needs Codex CLI (validated upstream with 0.152.1), a trusted PreToolUse hook, and the same TypeSafe key for Jev. Offline tests need no account. |
| License | [MIT](https://github.com/tamaratran/jev-pruner/blob/47d017c34eab7690b95f075ce6f4839247c5dc0a/LICENSE). |

## When to use

Use it when coding-agent Bash output is large and mostly progress or boilerplate, but you still need diagnostics, final results, and task-dependent facts verbatim. It scores output **chunks**, not a generated summary.

Prefer a simpler size or head/tail policy when you do not need semantic retention. The Claude plugin marketplace identifier is still `fast-jev-output` even though the repository is named `jev-pruner`. Codex does not rewrite native shell output automatically; pruning only applies when the agent uses the installed skill/wrapper.

## How it works

```text
Bash runs → eligible stdout above ~10k estimated tokens → archive full output
         → partition history + chunk output → Jev noul per chunk
         → keep diagnostics/uncertain/task-needed chunks → omit the rest with markers
```

The [Jev client](https://github.com/tamaratran/jev-pruner/blob/47d017c34eab7690b95f075ce6f4839247c5dc0a/src/jev.ts) posts to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest`. Each chunk gets one noul question: whether any line must remain. Default `keepThreshold` is `0.5`; scores above `0.1` are also retained as an uncertainty safeguard. Errors, recognized documents/source/diff/binary output, and whole-document commands bypass scoring. Failures and incomplete scoring leave the original host result untouched.

Claude archives under `.claude/fast-jev-output/`; Codex under `.jev-pruner/`. A credential-like heuristic can skip local archiving; it does **not** redact conversation content sent to Jev.

## Get started

**Setup downloads source and npm packages; it makes no inference requests.**

```sh
git clone https://github.com/tamaratran/jev-pruner.git
cd jev-pruner
git checkout 47d017c34eab7690b95f075ce6f4839247c5dc0a
npm ci --ignore-scripts --no-audit --no-fund
npm run build
npm test
```

Expected: offline Vitest suite passes (276 tests at this revision). For Claude Code installation, follow the upstream [Claude Code install](https://github.com/tamaratran/jev-pruner#claude-code-install) section (`fast-jev-output@fast-jev-output` marketplace identifiers). For Codex, follow the upstream [Codex](https://github.com/tamaratran/jev-pruner#codex) section and build before installing so `dist/codex/run.js` exists. Live pruning requires a TypeSafe key and incurs usage charges.

## Examples and demos

- [Offline tests](https://github.com/tamaratran/jev-pruner/tree/47d017c34eab7690b95f075ce6f4839247c5dc0a/tests): retention, token gate, history partitioning, hook helpers, and Codex wrapper behavior without provider calls.
- [Live library checks](https://github.com/tamaratran/jev-pruner#tests): `npm run test:live` with `TYPESAFE_API_KEY` (billable; not run for this listing).
- [Animated macOS demo](https://github.com/tamaratran/jev-pruner/tree/47d017c34eab7690b95f075ce6f4839247c5dc0a/demo/JevPrunerDemo): recorded playback, not live Jev; not built during this review.

## Limits and data handling

Jev receives partitioned conversation history (including tool inputs/results as supplied by the host) and command output chunks. Archives persist locally until removed. Missing keys, HTTP failures, budgets that cannot fit, and incomplete scoring preserve original stdout. Thresholds are operational retention policy, not measured accuracy. Secret detection is heuristic and incomplete. Host preview budgets can still truncate after pruning.

## Review and maintenance

Reviewed on **2026-09-19** at [commit 47d017c](https://github.com/tamaratran/jev-pruner/tree/47d017c34eab7690b95f075ce6f4839247c5dc0a): package version 0.1.0. AI-assisted source review covered the library, Claude hook, Codex wrapper paths, license, and README. On Node.js 22.19.0, **276 offline tests**, `npm run typecheck`, and `npm run build` passed. No live inference, Claude/Codex plugin installation, or model-quality evaluation was performed.

Related: [fast-jev-compaction](fast-jev-compaction.md) selects which old tool call/result pairs remain in a transcript; this project prunes a single Bash result before the model sees it.
