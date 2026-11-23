# Sapho by Agent IX (Rust library and CLI for compound decisions: many small Jev questions combined by rules you write in a decision graph)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Split a decision into simple questions, ask a System One model each one, and combine the answers with rules (and, or, min, max, thresholds) written as a YAML or JSON decision graph. Reports keep every answer and intermediate result, so you can replay recorded runs offline, measure a rule against labelled examples and tighten it without changing the questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agent-ix/sapho) |
| Maintainer | [agent-ix](https://github.com/agent-ix). Independently curated. |
| Format | Rust workspace (library crates + `sapho` CLI) with Claude Code skills |
| Requirements | Rust 1.98+; a TypeSafe API key and a CLI built with the `jev` feature for live runs (replaying the included recordings needs no key). |
| License | [AGPL-3.0-or-later](https://github.com/agent-ix/sapho/blob/3f386c821eca6708c23e726fe3bbdd6a467d2411/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/sapho-jev/src/lib.rs`](https://github.com/agent-ix/sapho/blob/3f386c821eca6708c23e726fe3bbdd6a467d2411/crates/sapho-jev/src/lib.rs) at the pinned commit. |

## When to use

- Build a decision you can audit from several typed Jev answers plus your own thresholds, and test rule changes against recorded answers.
- Mismatch: a single yes/no call; Sapho adds a graph format and a Rust toolchain.

## How it works

The `sapho-jev` crate wraps the official TypeSafe Rust SDK crates (`typesafe_sdk_client`, `typesafe_sdk_config`) and reads `TYPESAFE_API_KEY` from the environment; other crates add Ollama, Claude and other decision backends, recording and replay. Integration evidence: [`crates/sapho-jev/src/lib.rs`](https://github.com/agent-ix/sapho/blob/3f386c821eca6708c23e726fe3bbdd6a467d2411/crates/sapho-jev/src/lib.rs).

## Get started

Install the CLI from the checkout and replay the recorded code-review example offline.

```sh
git clone https://github.com/agent-ix/sapho.git && cd sapho
cargo install --path crates/sapho-cli --locked
sapho replay examples/graphs/code-review.yaml \
  --input examples/data/code-review-input.json \
  --recording examples/recordings/code-review.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example graphs: [github.com/agent-ix/sapho/tree/3f386c821eca6708c23e726fe3bbdd6a467d2411/examples/graphs](https://github.com/agent-ix/sapho/tree/3f386c821eca6708c23e726fe3bbdd6a467d2411/examples/graphs)
- Documentation index: [github.com/agent-ix/sapho/blob/3f386c821eca6708c23e726fe3bbdd6a467d2411/docs/index.md](https://github.com/agent-ix/sapho/blob/3f386c821eca6708c23e726fe3bbdd6a467d2411/docs/index.md)

## Limits and data handling

Live runs send graph inputs to TypeSafe (or another configured backend). The repository is early (version 0.1.0). AGPL-3.0-or-later, which matters if you embed the library in a network service.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 3f386c821eca](https://github.com/agent-ix/sapho/tree/3f386c821eca6708c23e726fe3bbdd6a467d2411). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
