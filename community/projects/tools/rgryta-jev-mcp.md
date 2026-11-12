# jev-mcp by rgryta (Rust MCP server with typed Jev ask and parallel rank tools)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust MCP server over streamable HTTP with two tools: `ask` sends several typed Jev questions (yes/no, choice, score) about one piece of content in a single request, and `rank` asks the same yes/no question of up to 200 candidates in parallel and returns them best first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rgryta/jev-mcp) |
| Maintainer | [rgryta](https://github.com/rgryta). Independently curated. |
| Format | MCP server (Rust, scratch Docker image on GHCR; no license file) |
| Requirements | Rust toolchain or Docker, plus `TYPESAFE_API_KEY`; an MCP client that speaks streamable HTTP. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. No license file on the reviewed commit, so reuse rights are not granted. |
| Jev evidence | [`src/jev.rs`](https://github.com/rgryta/jev-mcp/blob/7eef9b34a2f5d9016c436668828916613c5954d3/src/jev.rs) at the pinned commit. |

## When to use

- Let an agent triage many files, log chunks or diff hunks with Jev and read only the promising ones.
- Mismatch: stdio-only MCP clients; this server speaks streamable HTTP.

## How it works

`src/jev.rs` calls TypeSafe System One with defaults set in `src/config.rs` (`https://api.typesafe.ai`, `jev-latest`, overridable via `TYPESAFE_BASE_URL` and `JEV_MODEL`); `ask` returns Jev's response unchanged and `rank` issues one request per candidate, eight at a time. Integration evidence: [`src/jev.rs`](https://github.com/rgryta/jev-mcp/blob/7eef9b34a2f5d9016c436668828916613c5954d3/src/jev.rs).

## Get started

Build and run locally, or use the example compose file with your key in `.env`; then point your MCP client at `/mcp`.

```sh
cargo build --release --bins
export TYPESAFE_API_KEY="your-key"
./target/release/jev-mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/rgryta/jev-mcp/blob/7eef9b34a2f5d9016c436668828916613c5954d3/README.md](https://github.com/rgryta/jev-mcp/blob/7eef9b34a2f5d9016c436668828916613c5954d3/README.md)
- Compose example: [github.com/rgryta/jev-mcp/blob/7eef9b34a2f5d9016c436668828916613c5954d3/deploy/compose.yaml](https://github.com/rgryta/jev-mcp/blob/7eef9b34a2f5d9016c436668828916613c5954d3/deploy/compose.yaml)

## Limits and data handling

Content and candidates go to TypeSafe on your key; `rank` costs one request per candidate.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 7eef9b34a2f5](https://github.com/rgryta/jev-mcp/tree/7eef9b34a2f5d9016c436668828916613c5954d3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
