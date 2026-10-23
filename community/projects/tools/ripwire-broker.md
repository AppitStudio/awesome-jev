# ripwire-broker (budgeted MCP code context with optional Jev relevance)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local MCP server that turns Ripwire's 33 verbs into three task-moment tools with a token budget, deduplication and provenance, plus hooks for Claude Code and Codex; an optional online mode lets Jev rate the files Ripwire ranked for a task.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aquental/ripwire-broker) |
| Maintainer | [aquental](https://github.com/aquental). Independently curated. |
| Format | Rust MCP server and CLI, Claude Code plugin |
| Requirements | Rust 1.98.1 or a release binary; ripwire 0.6.4+; for online mode, a build with `--features online` and a TypeSafe API key (or Cloudflare Workers AI). |
| License | [MIT](https://github.com/aquental/ripwire-broker/blob/d9aa86ebde43e5680224861bf5c769f4d8f759b9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/online/jev.rs`](https://github.com/aquental/ripwire-broker/blob/d9aa86ebde43e5680224861bf5c769f4d8f759b9/src/online/jev.rs) at the pinned commit. |

## When to use

- Give coding agents compact, budgeted repository context.
- Add a semantic relevance pass on top of Ripwire's ranking.
- Mismatch: offline and read-only by default; Jev is only used with `--online`.

## How it works

`src/online/jev.rs` sends the ranked files and their siblings to TypeSafe (`jev-1.13.0` on `api.typesafe.ai`) as relevance questions in `context_for_task`, and the broker merges the probabilities with Ripwire's facts. Integration evidence: [`src/online/jev.rs`](https://github.com/aquental/ripwire-broker/blob/d9aa86ebde43e5680224861bf5c769f4d8f759b9/src/online/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo build --release --features online
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Specification: [github.com/aquental/ripwire-broker/blob/main/spec/ripwire-broker-mcp.md](https://github.com/aquental/ripwire-broker/blob/main/spec/ripwire-broker-mcp.md)
- Claude Code plugin: [github.com/aquental/ripwire-broker/blob/main/integrations/claude-code/README.md](https://github.com/aquental/ripwire-broker/blob/main/integrations/claude-code/README.md)

## Limits and data handling

In online mode, file excerpts are sent to TypeSafe or Cloudflare; `--redact-workspace` is available.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit d9aa86ebde43](https://github.com/aquental/ripwire-broker/tree/d9aa86ebde43e5680224861bf5c769f4d8f759b9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
