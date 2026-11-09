# Astria (codebase knowledge-graph builder with a TypeSafe Jev judge layer)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Builds a local SQLite knowledge graph of a codebase for CLI and MCP queries; `--judge jev` layers TypeSafe Jev over the semantic backend to gate trivial files and verify extracted relations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nodesify/astria) |
| Maintainer | [Nodesify](https://github.com/Nodesify). Independently curated. |
| Format | Rust core + npm CLI/MCP (MIT) |
| Requirements | `npm install -g @nodesify/astria`, an LLM backend for semantic extraction, and a TypeSafe key for `--judge jev`. |
| License | [MIT](https://github.com/Nodesify/astria/blob/3673ee87b2d94d80e0771a406387def5443e664c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/astria-semantic/src/jev.rs`](https://github.com/Nodesify/astria/blob/3673ee87b2d94d80e0771a406387def5443e664c/crates/astria-semantic/src/jev.rs) at the pinned commit. |

## When to use

- Cut semantic-extraction cost by gating trivial files.
- Get calibrated relation checks in a code graph.
- Mismatch: deterministic extraction works without Jev.

## How it works

`astria-semantic/src/jev.rs` wraps the completion engine: Jev answers keep/drop gates (`ASTRIA_LLM_JEV_GATE`) and verifies relation choices (`ASTRIA_LLM_JEV_VERIFY`); `backend_jev.rs` handles the API. Integration evidence: [`crates/astria-semantic/src/jev.rs`](https://github.com/Nodesify/astria/blob/3673ee87b2d94d80e0771a406387def5443e664c/crates/astria-semantic/src/jev.rs).

## Get started

Install the npm package and run a build with a semantic backend plus `--judge jev`.

```sh
npm install -g @nodesify/astria
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Nodesify/astria/blob/3673ee87b2d94d80e0771a406387def5443e664c/README.md](https://github.com/Nodesify/astria/blob/3673ee87b2d94d80e0771a406387def5443e664c/README.md)

## Limits and data handling

File snippets and candidate relations are sent to TypeSafe when the judge is on.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 3673ee87b2d9](https://github.com/Nodesify/astria/tree/3673ee87b2d94d80e0771a406387def5443e664c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
