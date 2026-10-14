# jev-cli (portlandhodl)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent-facing Rust CLI over the unofficial jev-sdk crate: predict, choose and score subcommands return JSON probabilities an agent can gate on.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/portlandhodl/jev-cli) |
| Maintainer | [portlandhodl](https://github.com/portlandhodl). Independently curated. |
| Format | Rust CLI |
| Requirements | Rust toolchain (cargo), TypeSafe API key. |
| License | [Apache-2.0 OR MIT](https://github.com/portlandhodl/jev-cli/blob/1bfc62daf6170338feb5374d374efe15afd9b373/LICENSE-APACHE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/run.rs`](https://github.com/portlandhodl/jev-cli/blob/1bfc62daf6170338feb5374d374efe15afd9b373/src/run.rs) at the pinned commit. |

## When to use

- Let a shell-driven agent ask a typed question before acting and branch on a threshold.
- Mismatch: unofficial SDK; not affiliated with TypeSafe.

## How it works

Each subcommand sends one typed question (noul, choice or score) with your state text and prints the typed answer as JSON; the calling agent or script decides what to do. Integration evidence: [`src/run.rs`](https://github.com/portlandhodl/jev-cli/blob/1bfc62daf6170338feb5374d374efe15afd9b373/src/run.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo install --git https://github.com/portlandhodl/jev-cli
jev-cli predict --state "$CONTEXT" --question "Will this deploy complete without errors?"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Examples for predict / choose / score in the upstream README.
- Live test file: `tests/live.rs` (opt-in).

## Limits and data handling

State text goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 1bfc62daf617](https://github.com/portlandhodl/jev-cli/tree/1bfc62daf6170338feb5374d374efe15afd9b373). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
