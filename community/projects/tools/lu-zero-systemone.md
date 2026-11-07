# systemone (Rust client for the TypeSafe Jev System One API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community Rust crate for TypeSafe's `systemone` API: ask named, typed questions about text or structured state and get probabilistic answers from Jev, with a typed-facet companion crate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lu-zero/systemone) |
| Maintainer | [lu-zero](https://github.com/lu-zero). Independently curated. |
| Format | Rust crate (MIT) |
| Requirements | Rust toolchain and a TypeSafe API key. |
| License | [MIT](https://github.com/lu-zero/systemone/blob/26fd38e15ad078e676bea3c14539c6ee622e4b2d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`systemone/src/config.rs`](https://github.com/lu-zero/systemone/blob/26fd38e15ad078e676bea3c14539c6ee622e4b2d/systemone/src/config.rs) at the pinned commit. |

## When to use

- Call Jev from Rust services without hand-writing HTTP.
- Use typed facets to map answers into Rust types.
- Mismatch: unofficial community client, not a TypeSafe SDK.

## How it works

`systemone/src/config.rs` reads `TYPESAFE_API_KEY`, defaults the API root to `https://api.typesafe.ai` and the model to `jev-latest`; `systemone/src/lib.rs` builds the typed request. Integration evidence: [`systemone/src/config.rs`](https://github.com/lu-zero/systemone/blob/26fd38e15ad078e676bea3c14539c6ee622e4b2d/systemone/src/config.rs).

## Get started

Add the crate (`cargo add systemone`), set TYPESAFE_API_KEY, and run the bundled example.

```sh
git clone https://github.com/lu-zero/systemone.git && cd systemone
export TYPESAFE_API_KEY=...
cargo run --example demo -p systemone
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lu-zero/systemone/blob/26fd38e15ad078e676bea3c14539c6ee622e4b2d/README.md](https://github.com/lu-zero/systemone/blob/26fd38e15ad078e676bea3c14539c6ee622e4b2d/README.md)

## Limits and data handling

Questions and state are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 26fd38e15ad0](https://github.com/lu-zero/systemone/tree/26fd38e15ad078e676bea3c14539c6ee622e4b2d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
