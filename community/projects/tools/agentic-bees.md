# agentic-bees (agent-directed Btrfs deduplication CLI with an advisory Jev next-step check)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust CLI and MCP interface that lets an AI agent inspect Btrfs storage, run bounded scans, review matches and apply kernel deduplication inside an authorized scope. An optional `decide` command asks Jev for an advisory next step using only allowlisted counters.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LIghtJUNction/agentic-bees) |
| Maintainer | [LIghtJUNction](https://github.com/LIghtJUNction). Independently curated. |
| Format | Rust CLI + MCP server + agent skill |
| Requirements | Linux x86_64 with Btrfs (5.6+), Rust 1.88+; optional Jev key. |
| License | [GPL-3.0-or-later](https://github.com/LIghtJUNction/agentic-bees/blob/87d0e9ec5f4824ff575dc5bedd342a30b59496ec/COPYING) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/LIghtJUNction/agentic-bees/blob/87d0e9ec5f4824ff575dc5bedd342a30b59496ec/src/jev.rs) at the pinned commit. |

## When to use

- Let an agent drive careful, reviewable deduplication of a Btrfs directory.
- Mismatch: Jev is advisory only and cannot authorize execution.

## How it works

`agentic-bees decide PLAN.json` (`src/jev.rs`) sends allowlisted counters and a completion flag to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); paths, hashes and file contents are excluded and the result is always `advisory_only`. Integration evidence: [`src/jev.rs`](https://github.com/LIghtJUNction/agentic-bees/blob/87d0e9ec5f4824ff575dc5bedd342a30b59496ec/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo build --locked --release
./target/release/agentic-bees --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/LIghtJUNction/agentic-bees#readme](https://github.com/LIghtJUNction/agentic-bees#readme)

## Limits and data handling

Not yet at parity with upstream bees. Deduplication modifies files on disk; read the README warnings. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 87d0e9ec5f48](https://github.com/LIghtJUNction/agentic-bees/tree/87d0e9ec5f4824ff575dc5bedd342a30b59496ec). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
