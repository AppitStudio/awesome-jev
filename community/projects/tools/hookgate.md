# hookgate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Calibrated Claude Code / Codex hooks: TypeSafe Jev gates risky shell commands and unverified “done” claims in about 100 ms, with audit mode and fail-open defaults.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Allan-Nava/hookgate) |
| Maintainer | [Allan-Nava](https://github.com/Allan-Nava). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js ≥ 18 CLI/plugin (`hookgate` 0.0.2): PreToolUse/Stop/PostToolUse handlers, `doctor`/`report`, offline tests. |
| Requirements | Node **≥ 18**. Offline `npm test` needs no key. Live gating needs `TYPESAFE_API_KEY` (optional `HOOKGATE_ENDPOINT`, `HOOKGATE_MODE=audit`). |
| License | [MIT](https://github.com/Allan-Nava/hookgate/blob/e05c983148990d4d1dd66829b021c0263b98eea4/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `node --test` **44 passed**. Live TypeSafe / Claude Code / Codex sessions not run. Benchmark numbers in upstream README are still pending. |

## When to use

Use it when you want **harness-level** allow/ask/deny and completion checks answered by Jev instead of a full LLM prompt hook. Prefer [agy-jevgate](agy-jevgate.md) / [The Jev-enator](the-jev-enator.md) for narrower danger gates; prefer [clear-head](clear-head.md) when the Stop check is claim-vs-evidence only. Start in **audit** mode until you trust thresholds.

## How it works

[`bin/lib/jev.mjs`](https://github.com/Allan-Nava/hookgate/blob/e05c983148990d4d1dd66829b021c0263b98eea4/bin/lib/jev.mjs) POSTs to `https://api.typesafe.ai/v1/systemone` (overridable). Command gate: Choice `{allow,ask,deny}` plus destructive Noul; below-threshold answers become `ask` (Codex maps ask via config). Stop gate: Noul on unverified completion vs `git status`. Optional injection screen is off by default. Failures without a key/network fall open. Live mode sends command/message snippets to TypeSafe.

## Get started

```sh
git clone https://github.com/Allan-Nava/hookgate.git
cd hookgate
git checkout e05c983148990d4d1dd66829b021c0263b98eea4
npm test
# Install per upstream README (Claude Code plugin / Codex hooks); prefer mode audit first
# Live: export TYPESAFE_API_KEY; optional hookgate doctor
```

Docs: [allan-nava.github.io/hookgate](https://allan-nava.github.io/hookgate/).

## Examples and demos

- Offline `npm test`: **44 passed** (handlers, e2e against local fake endpoint, redaction, doctor).
- Upstream documents audit/`report` latency and cache hit summaries after real sessions.

## Limits and data handling

Does not widen harness permissions by default (`allowMode: "passthrough"`). Injection gate is experimental. Live calls incur TypeSafe usage and send tool/command text. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit e05c983](https://github.com/Allan-Nava/hookgate/tree/e05c983148990d4d1dd66829b021c0263b98eea4): **0.0.2**, MIT. AI-assisted review of README, LICENSE, `bin/lib/jev.mjs`, handlers, tests. **`npm test`: 44 passed**. No live TypeSafe.

Related: [agy-jevgate](agy-jevgate.md), [clear-head](clear-head.md), [The Jev-enator](the-jev-enator.md), [toolgate](toolgate.md).
