# s1-mcp by gerchowl (MCP server that gives coding agents Jev and other System One models, and logs where they helped)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A small Rust MCP server for Claude Code, Codex and opencode: agents ask typed `noul`, `choice` and `score` questions of any `/v1/systemone` endpoint (TypeSafe's hosted Jev, Clef, Kev or your own fine-tune) and get interpreted answers (`answer`, `p`, `margin`, `band`). Every call is logged locally with a use case, agents rate calls once they know the truth, and `s1_report` shows accuracy, usefulness and latency per use case and model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gerchowl/s1-mcp) |
| Maintainer | [gerchowl](https://github.com/gerchowl). Independently curated. |
| Format | Rust MCP server (stdio) + CLI |
| Requirements | Rust 1.95 (pinned Nix toolchain, or cargo); a model registry file listing your endpoints; `TYPESAFE_API_KEY` for the hosted Jev entry. |
| License | [Apache-2.0](https://github.com/gerchowl/s1-mcp/blob/264c31afbec39d6c90d30cb73af9ba019dbc9ba9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/s1.rs`](https://github.com/gerchowl/s1-mcp/blob/264c31afbec39d6c90d30cb73af9ba019dbc9ba9/src/s1.rs) at the pinned commit. |

## When to use

- Give a coding agent cheap typed judgements (did the run really fail, which bucket does this error go in) and measure per use case whether they help.
- Mismatch: a one-line SDK call; you must maintain a model registry, and the README examples point at the author's own fleet endpoints.

## How it works

`src/s1.rs` normalises and validates the questions, posts one System One request to the model chosen from the registry (`src/registry.rs`; the Jev entry uses `https://api.typesafe.ai/v1/systemone` with `jev-latest`) and checks every answer against the questions asked. `s1_compare` sends the same request to several models in parallel. Integration evidence: [`src/s1.rs`](https://github.com/gerchowl/s1-mcp/blob/264c31afbec39d6c90d30cb73af9ba019dbc9ba9/src/s1.rs).

## Get started

Build the binary, add a Jev entry to `~/.config/s1-mcp/models.json`, then register the server with your agent.

```sh
git clone https://github.com/gerchowl/s1-mcp && cd s1-mcp
cargo build --release   # or: nix build .#default
export TYPESAFE_API_KEY=...
claude mcp add s1 -- $PWD/target/release/s1-mcp
./target/release/s1-mcp models --probe
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Agent guide: [github.com/gerchowl/s1-mcp/blob/264c31afbec39d6c90d30cb73af9ba019dbc9ba9/docs/agent-guide.md](https://github.com/gerchowl/s1-mcp/blob/264c31afbec39d6c90d30cb73af9ba019dbc9ba9/docs/agent-guide.md)
- README registry example: [github.com/gerchowl/s1-mcp/blob/264c31afbec39d6c90d30cb73af9ba019dbc9ba9/README.md](https://github.com/gerchowl/s1-mcp/blob/264c31afbec39d6c90d30cb73af9ba019dbc9ba9/README.md)

## Limits and data handling

The call log (`~/.local/state/s1-mcp/calls.jsonl`) stores the state, questions and answers locally with light redaction of credential-shaped strings; whatever state an agent sends goes to the configured endpoint. Early project (created 2026-10-09).

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 264c31afbec3](https://github.com/gerchowl/s1-mcp/tree/264c31afbec39d6c90d30cb73af9ba019dbc9ba9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
