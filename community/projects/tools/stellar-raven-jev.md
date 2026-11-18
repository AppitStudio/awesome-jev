# Stellar Raven Jev by stellar-experimental (CLI for AI agents that searches 45 Stellar ecosystem sources and scores each document's relevance with Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Rust command-line tool and agent skill for answering questions about the Stellar ecosystem. It searches 45 sources (Stellar developer docs on Mintlify, Algolia indexes of stellar.org, LumenLoop and Stellar Scout), scores every document with Jev, and prints compact JSON with ranked URLs, 400-character excerpts, text file paths and a per-call cost. It does not write answers; the agent reads the text. Jev can run via Cloudflare Workers AI, TypeSafe or OpenRouter, with a required per-call spend limit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stellar-experimental/stellar-raven-jev) |
| Maintainer | [stellar-experimental](https://github.com/stellar-experimental). Independently curated. |
| Format | Rust CLI and agent skill (Apache-2.0) |
| Requirements | Rust toolchain, source keys (LumenLoop, Mintlify, Algolia), at least one Jev provider key, and a `JEV_BUDGET_USD` spending limit above 0 and at most 100. |
| License | [Apache-2.0](https://github.com/stellar-experimental/stellar-raven-jev/blob/6377a890cde9ab124bdcc1522b597d0c313142f3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/stellar-experimental/stellar-raven-jev/blob/6377a890cde9ab124bdcc1522b597d0c313142f3/src/jev.rs) at the pinned commit. |

## When to use

- Give a coding agent grounded, ranked Stellar documentation with source URLs and spend control.
- Mismatch: a general web search; it covers the configured Stellar sources only.

## How it works

`src/jev.rs` posts relevance questions to the `/v1/systemone` endpoint of TypeSafe (`jev-latest`), OpenRouter or Cloudflare, and records the cost of each call. Integration evidence: [`src/jev.rs`](https://github.com/stellar-experimental/stellar-raven-jev/blob/6377a890cde9ab124bdcc1522b597d0c313142f3/src/jev.rs).

## Get started

Install with cargo, copy `.env.example` to `.env`, run `doctor` (no network), then search.

```sh
cargo install --git https://github.com/stellar-experimental/stellar-raven-jev --locked
stellar-raven-jev doctor
stellar-raven-jev search "How does a wallet resolve a federation address to an account ID?"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/stellar-experimental/stellar-raven-jev/blob/6377a890cde9ab124bdcc1522b597d0c313142f3/README.md](https://github.com/stellar-experimental/stellar-raven-jev/blob/6377a890cde9ab124bdcc1522b597d0c313142f3/README.md)

## Limits and data handling

Queries and fetched document text go to the chosen Jev provider on your key; live calls cost money, bounded by the budget setting. Source access needs third-party keys. The ranking quality was not independently measured.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 6377a890cde9](https://github.com/stellar-experimental/stellar-raven-jev/tree/6377a890cde9ab124bdcc1522b597d0c313142f3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
