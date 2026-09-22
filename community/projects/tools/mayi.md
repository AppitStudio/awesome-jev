# mayi

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Permission gate for Claude Code, Cursor, and Codex: TypeSafe Jev scores each shell/file/MCP tool call before it runs; routine work passes silently and anything else prompts for approve/deny.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AidenHadisi/mayi) |
| Maintainer | [AidenHadisi](https://github.com/AidenHadisi). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust CLI (`mayi`) with host hooks for Claude Code, Cursor, and Codex; optional OpenAI/Anthropic classifiers. |
| Requirements | Rust **1.96+** (or a [prebuilt release](https://github.com/AidenHadisi/mayi/releases)); TypeSafe API key via `mayi config set api_key` (default provider `jev`, model `jev-latest`). |
| License | [MIT](https://github.com/AidenHadisi/mayi/blob/e51371c6f05376f579467fb597b700cbdb1b5279/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source and upstream CI inspected; local `cargo test` needs Rust ≥1.96 (review host had 1.85.1). No live TypeSafe or agent-hook session on the review host. |

## When to use

Use it when coding-agent tool calls should be **scored by Jev before execution**, with a local dialog on unsafe calls. Prefer [agy-jevgate](agy-jevgate.md) for fail-closed Antigravity shell gating, [claude-code-jev](claude-code-jev.md) for OpenRouter Decisions allow/block/ask, or [toolgate](toolgate.md) for static rules plus Jev. This is not a sandbox.

## How it works

[`src/classifier.rs`](https://github.com/AidenHadisi/mayi/blob/e51371c6f05376f579467fb597b700cbdb1b5279/src/classifier.rs) posts to `{api_url}/v1/systemone` (default `https://api.typesafe.ai`) with a noul gate question. Safe (default Jev threshold **0.85**) allows silently; not-safe opens a dialog; classifier/network/config errors **deny**. The process exits **0** so hosts that treat hook crashes as allow do not accidentally permit. OpenAI and Anthropic providers are optional alternatives with fixed JSON schemas.

## Get started

```sh
git clone https://github.com/AidenHadisi/mayi.git
cd mayi
git checkout e51371c6f05376f579467fb597b700cbdb1b5279
# Requires rustc 1.96+: cargo test
# Or: cargo install --git https://github.com/AidenHadisi/mayi --locked
mayi config set api_key tsk_...
mayi --agent claude install   # or cursor, codex
```

Live hooks send action lines to TypeSafe and can incur charges. This listing did not install hooks into a real agent or call live APIs.

## Examples and demos

- Offline suite under `tests/` (mocked Jev httpmock paths for `/v1/systemone`).
- Upstream CI: [CI run](https://github.com/AidenHadisi/mayi/actions/runs/35690858809) **success** at tip `e51371c`.
- Local review host: `cargo test` blocked by rustc **1.85.1** vs package MSRV **1.96**.

## Limits and data handling

Cloud/remote agent sessions are not configured by `install`. Codex requires approving the hook via `/hooks`. Dialog errors deny. Not a complete authorization system. Provider keys and decisions stay in local config/logs per upstream docs.

## Review and maintenance

Reviewed on **2026-09-22** at [commit e51371c](https://github.com/AidenHadisi/mayi/tree/e51371c6f05376f579467fb597b700cbdb1b5279): MIT **0.1.0**. AI-assisted source review of README, LICENSE, `src/classifier.rs`, `src/config.rs`, and `tests/hook.rs`. Upstream CI success cited; no live TypeSafe spend.

Related: [agy-jevgate](agy-jevgate.md), [claude-code-jev](claude-code-jev.md), [toolgate](toolgate.md), [stop-rules](stop-rules.md).
