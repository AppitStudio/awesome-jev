# fuzzy-jev (Rust/Python client for Jev's typed answers with fuzzy rules over the probabilities)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust crate, CLI and Python package that ask Jev typed Choice, Score and Noul questions about text and images through OpenRouter's decisions endpoint, then apply a rules file that reads each probability as a fuzzy truth value (AND = min, OR = max) and can draw the rule graph. Includes an Agent Skill that teaches coding agents when to ask Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dsaad68/fuzzy-jev) |
| Maintainer | [dsaad68](https://github.com/dsaad68). Independently curated. |
| Format | Rust crate + CLI (`cargo install fuzzy-jev`) and Python package (`pip install fuzzy-jev`) |
| Requirements | An OpenRouter key (or `--url` for another System One host). |
| License | [MIT](https://github.com/dsaad68/fuzzy-jev/blob/6e55c5b8ed527e934efb0b51d322805ae7be2aa2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib.rs`](https://github.com/dsaad68/fuzzy-jev/blob/6e55c5b8ed527e934efb0b51d322805ae7be2aa2/src/lib.rs) at the pinned commit. |

## When to use

- Combine several Jev judgments into an explainable policy decision.
- Mismatch: defaults to OpenRouter rather than TypeSafe's direct API.

## How it works

`src/lib.rs` posts to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13`; the rules engine in `src/rules/` evaluates fuzzy policies over the returned probabilities. Integration evidence: [`src/lib.rs`](https://github.com/dsaad68/fuzzy-jev/blob/6e55c5b8ed527e934efb0b51d322805ae7be2aa2/src/lib.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo install fuzzy-jev --locked
# or: pip install fuzzy-jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- crates.io: [crates.io/crates/fuzzy-jev](https://crates.io/crates/fuzzy-jev)

## Limits and data handling

Text and images are sent to OpenRouter and TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 6e55c5b8ed52](https://github.com/dsaad68/fuzzy-jev/tree/6e55c5b8ed527e934efb0b51d322805ae7be2aa2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
