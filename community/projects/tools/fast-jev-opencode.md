# fast-jev-opencode

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode **V2** plugin that scores tool calls/results with TypeSafe Jev and rewrites only the **outgoing model request** (drop/truncate), fail-open and cache-backed. Port of [fast-jev-compaction](fast-jev-compaction.md) ideas to OpenCode’s `context` hook—does **not** rewrite stored history or `/compact`. Distinct from [jev-compact](jev-compact.md) (Codex) and [omp-jev-compaction](omp-jev-compaction.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nrdz-labs/fast-jev-opencode) |
| Maintainer | [nrdz-labs](https://github.com/nrdz-labs). Independently curated; this entry is not an upstream submission or endorsement. Not affiliated with TypeSafe or OpenCode. |
| Format | TypeScript OpenCode plugin **`fast-jev-opencode` 0.1.0** — clone into `~/.config/opencode/plugins/fast-jev` (or project `.opencode/plugins/`). Runtime uses Node builtins only. |
| Requirements | OpenCode with V2 `context` hook (README validates against OpenCode **v2.0.7** / `@opencode/plugin` 2.0.7–2.0.8). `TYPESAFE_API_KEY` in the environment or `~/.config/opencode/.env`. Without a key the plugin stands down (fail-open). |
| License | [MIT](https://github.com/nrdz-labs/fast-jev-opencode/blob/4c4de4dcffa0201502fcb682c80b807cfd248140/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected. Local selftest/typecheck not run on the review host. Live OpenCode/TypeSafe pruning not run. |

## When to use

Use it when OpenCode sessions drown in stale tool calls and bulky results and you want Jev to prune the **next request** while leaving session history and built-in compaction alone. Prefer [fast-jev-compaction](fast-jev-compaction.md) for Claude Code session compaction; prefer [jev-compact](jev-compact.md) for Codex PreCompact repair; prefer [jev-gateway](jev-gateway.md) when Jev should choose tools rather than prune context.

## How it works

[`jev.ts`](https://github.com/nrdz-labs/fast-jev-opencode/blob/4c4de4dcffa0201502fcb682c80b807cfd248140/jev.ts) resolves `TYPESAFE_API_KEY` and asks TypeSafe System One (vendored fast-jev-compaction request helpers). Decisions are cached across requests; defaults ship **observe-only** (`dryRun: true`) until you set `"dryRun": false` in `config.json`. Failures (missing key, timeout, HTTP/malformed answers) leave the request unmodified. `/jev-prune` reports cached decisions and last-run stats; it does not trigger a rewrite of an already-dispatched request.

## Get started

```sh
git clone https://github.com/nrdz-labs/fast-jev-opencode.git \
  ~/.config/opencode/plugins/fast-jev
cd ~/.config/opencode/plugins/fast-jev
git checkout 4c4de4dcffa0201502fcb682c80b807cfd248140
cp config.example.json config.json   # observe-only by default
# Put TYPESAFE_API_KEY in ~/.config/opencode/.env or the environment
# Set "dryRun": false to apply drops/truncations
opencode service restart
```

Live pruning sends tool-call/result excerpts to TypeSafe and may incur charges. This listing did not run a live OpenCode session.

## Examples and demos

- `config.example.json` and [`docs/CONFIGURATION.md`](https://github.com/nrdz-labs/fast-jev-opencode/blob/4c4de4dcffa0201502fcb682c80b807cfd248140/docs/CONFIGURATION.md).
- [`docs/DESIGN.md`](https://github.com/nrdz-labs/fast-jev-opencode/blob/4c4de4dcffa0201502fcb682c80b807cfd248140/docs/DESIGN.md) — questions, thresholds, divergence from upstream compaction.
- Upstream CI badge; fixture-backed selftests documented in CONTRIBUTING.

## Limits and data handling

Tool-call arguments/results (and question text) leave the host when a key is set and dry-run is off. Stored OpenCode history is not rewritten by this plugin. Cost/quality claims were not measured here. No live TypeSafe calls on the review host.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 4c4de4d](https://github.com/nrdz-labs/fast-jev-opencode/tree/4c4de4dcffa0201502fcb682c80b807cfd248140): **0.1.0**, MIT. AI-assisted source review of README, `jev.ts`, `index.ts`, config example, LICENSE. No local Node/Bun test run. No live TypeSafe or OpenCode session.

Related: [fast-jev-compaction](fast-jev-compaction.md), [jev-compact](jev-compact.md), [omp-jev-compaction](omp-jev-compaction.md), [jev-pruner](jev-pruner.md), [jev-gateway](jev-gateway.md).
