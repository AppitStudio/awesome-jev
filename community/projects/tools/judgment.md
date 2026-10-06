# judgment (Rust)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust crate that turns TypeSafe System One (Jev) answers into verified, testable Rust types — typed choice/noul/score questions, a `Fake` backend that checks scripted answers like a server would, and `.jud` rubric documents that keep thresholds beside the questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chussenot/judgment) |
| Product homepage | [crates.io](https://crates.io/crates/judgment) |
| Maintainer | [chussenot](https://github.com/chussenot). Independently curated. |
| Format | Rust library (crates.io `judgment`, 0.9.0 at review) |
| Requirements | Rust + Tokio; `TYPESAFE_API_KEY` for `Client::from_env()`; works with any server speaking the same wire. |
| License | [MIT](https://github.com/chussenot/judgment/blob/fa5711b1de3a6ff62e05ea933491f9b0b303fdd5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route or gate in a Rust service with typed Jev answers (`Choice<T>`, `Noul`) and explicit confidence thresholds.
- Test decision logic without network using the validating `Fake` backend.
- Mismatch: a client library — you still design questions and policy.

## How it works

`Questions` builds typed questions; the `SystemOne` trait is implemented by the live `Client` and the `Fake` backend ([`src/backend.rs`](https://github.com/chussenot/judgment/blob/fa5711b1de3a6ff62e05ea933491f9b0b303fdd5/src/backend.rs)), so the same code runs in tests and production. `.jud` rubrics hold questions and thresholds in one reviewable document; the policy is never sent to the model.

## Get started

Add the crate and run the offline quickstart:

```sh
cargo add judgment serde_json tokio --features tokio/macros,tokio/rt
# or clone and run the bundled example (no key, no network):
git clone https://github.com/chussenot/judgment.git && cd judgment
cargo run --example quickstart
```

The `Fake` example makes no requests; `Client` calls are billed by TypeSafe or the configured server.

## Examples and demos

- `examples/quickstart.rs` (offline) and README `.jud` rubric example.
- [Hosted TypeSafe verification notes](https://github.com/chussenot/judgment/blob/fa5711b1de3a6ff62e05ea933491f9b0b303fdd5/docs/verification/hosted-typesafe.md) recorded by the maintainer.

## Limits and data handling

Early (0.x) API. State you pass is sent to the configured server. Not compiled on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit fa5711b1de3a](https://github.com/chussenot/judgment/tree/fa5711b1de3a6ff62e05ea933491f9b0b303fdd5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
