# decision-rs (typed Rust decisions across TypeSafe System One, OpenRouter Jev, OpenAI Decisions and Clef)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust crate where you declare decision questions once as derived types (`Predicate`, `Choice`, `Outcome`) and choose the backend when constructing the client: TypeSafe System One, OpenRouter's Jev route, OpenAI Decisions or Cloudflare Workers AI Clef, with the same acceptance methods and error categories on each; self-hosted System One endpoints are supported.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tyrchen/decision-rs) |
| Maintainer | [tyrchen](https://github.com/tyrchen). Independently curated. |
| Format | Rust library (crates.io `decision-rs`) |
| Requirements | Rust 1.99+ (edition 2024) and tokio; a key for the backend you choose. |
| License | [MIT](https://github.com/tyrchen/decision-rs/blob/3a60c650dd57978568bfdf020d0b9cf179d6b440/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/decision-rs/src/client.rs`](https://github.com/tyrchen/decision-rs/blob/3a60c650dd57978568bfdf020d0b9cf179d6b440/crates/decision-rs/src/client.rs) at the pinned commit. |

## When to use

- Write typed decision code in Rust that can switch between Jev and other decision APIs.
- Gate on calibrated probabilities with typed acceptance helpers.
- Mismatch: multi-provider; Jev is one backend among several.

## How it works

`crates/decision-rs/src/client.rs` provides `Client::typesafe(key)` for TypeSafe System One and `Client::openrouter(key)` for `typesafe/jev-1.14` via OpenRouter, sharing one schema derived from your Rust types. Integration evidence: [`crates/decision-rs/src/client.rs`](https://github.com/tyrchen/decision-rs/blob/3a60c650dd57978568bfdf020d0b9cf179d6b440/crates/decision-rs/src/client.rs).

## Get started

From the upstream README (not run on the review host):

```sh
# Cargo.toml
decision-rs = "0.5.1"
tokio = { version = "1", features = ["rt-multi-thread", "macros"] }
# let client = decision_rs::Client::typesafe(key)?;
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tyrchen/decision-rs#readme](https://github.com/tyrchen/decision-rs#readme)

## Limits and data handling

Decision state goes to the backend you choose. Unofficial; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 3a60c650dd57](https://github.com/tyrchen/decision-rs/tree/3a60c650dd57978568bfdf020d0b9cf179d6b440). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
