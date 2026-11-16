# aiface (multi-provider Rust AI client whose decision API speaks System One natively to Jev and wraps LLMs in the same typed contract)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust crate that gives one `Connector` for about 30 providers (Claude, OpenAI, Gemini, Copilot and OpenAI-compatible endpoints) with streaming, mid-stream retry, tool calling, embeddings, OAuth and cost tracking. Its decision module implements the System One contract: Noul, Choice and Score questions answered natively by TypeSafe Jev, Microsoft-Decision-1 or OpenRouter's System One route, or by a generative LLM wrapped in the same schema, with every answer validated against the declared questions before it reaches your code. It is the standalone connector crate of the cosh SDK.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aidreamy/aiface) |
| Maintainer | [aidreamy](https://github.com/aidreamy). Independently curated. |
| Format | Rust crate (crates.io `aiface` 0.2.3, Apache-2.0) |
| Requirements | Rust toolchain and `TYPESAFE_API_KEY` for native Jev decisions (other providers optional). |
| License | [Apache-2.0](https://github.com/aidreamy/aiface/blob/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/connector/decision/systemone.rs`](https://github.com/aidreamy/aiface/blob/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c/src/connector/decision/systemone.rs) at the pinned commit. |

## When to use

- Use Jev decisions from Rust behind the same client as your chat models.
- Mismatch: if you only need Jev, a smaller single-provider client may be simpler.

## How it works

`src/connector/decision/systemone.rs` posts decision requests to `https://api.typesafe.ai/v1/systemone` (`jev-latest` in the tests) for `Connector::new("typesafe")`; `docs/decision.md` documents the contract and `examples/decision.rs` runs native and LLM-wrapped decisions side by side. Integration evidence: [`src/connector/decision/systemone.rs`](https://github.com/aidreamy/aiface/blob/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c/src/connector/decision/systemone.rs).

## Get started

Add the crate and run the decision example with your key.

```sh
cargo add aiface
export TYPESAFE_API_KEY=...
git clone https://github.com/aidreamy/aiface && cd aiface
cargo run --example decision
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/aidreamy/aiface/blob/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c/README.md](https://github.com/aidreamy/aiface/blob/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c/README.md)
- Decision guide: [github.com/aidreamy/aiface/blob/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c/docs/decision.md](https://github.com/aidreamy/aiface/blob/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c/docs/decision.md)

## Limits and data handling

Decision states go to TypeSafe (or the provider you pick) on your key. Jev is one backend among many in a general client.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 24bc62bf5eb5](https://github.com/aidreamy/aiface/tree/24bc62bf5eb5e0b4e91588439cee1e3feac3c09c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
