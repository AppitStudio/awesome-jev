# jev-datafusion

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Rust crate that runs Jev decisions (noul, choice, score, ask) as Apache DataFusion SQL functions, so you can score tickets, route email or question meeting notes at warehouse scale.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/parable-work/jev-datafusion) |
| Maintainer | [parable-work](https://github.com/parable-work). Independently curated. |
| Format | Rust crate |
| Requirements | Rust + DataFusion from crates.io; TypeSafe or OpenRouter key. |
| License | [Apache-2.0](https://github.com/parable-work/jev-datafusion/blob/7d73f2cf971f395fcf16d32a83673b8c4e03f847/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/provider.rs`](https://github.com/parable-work/jev-datafusion/blob/7d73f2cf971f395fcf16d32a83673b8c4e03f847/src/provider.rs) at the pinned commit. |

## When to use

- Ask typed questions of every row in a DataFusion query and join the answers to other tables.
- Use TypeSafe directly or Jev via OpenRouter behind the same functions.
- Mismatch: the crate does not bundle DataFusion.

## How it works

You register the functions on a `SessionContext`; the provider batches row states into Jev requests to TypeSafe (or OpenRouter) and returns typed columns. Integration evidence: [`src/provider.rs`](https://github.com/parable-work/jev-datafusion/blob/7d73f2cf971f395fcf16d32a83673b8c4e03f847/src/provider.rs).

## Get started

Add the crates (illustrative; see upstream README, not run on the review host):

```sh
cargo add jev-datafusion datafusion
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example queries: `EXAMPLES.md`; `examples/live.rs`.

## Limits and data handling

Row data is sent to TypeSafe or OpenRouter and billed to your key; large queries can be costly.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 7d73f2cf971f](https://github.com/parable-work/jev-datafusion/tree/7d73f2cf971f395fcf16d32a83673b8c4e03f847). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
