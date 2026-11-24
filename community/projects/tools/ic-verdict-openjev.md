# IC-Verdict by humandebri (Rust inference canister on the Internet Computer running an open openJev 151M model for Choice, Noul and Score decisions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Japanese-documented Rust workspace that runs an open Jev-style model on-chain: the openJev-verdict GLiClass model (ModernBERT-151M, Apache-2.0, `heman10x/rlcd-modernbert-151m`) inside an ICP canister, with INT8 kernels, a free `decide_query`, cycles-billed `decide` updates (implemented, not yet live), and a public demo. It does not call TypeSafe's Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/humandebri/IC-OpenJev) |
| Maintainer | [humandebri](https://github.com/humandebri). Independently curated. |
| Format | Rust workspace (ICP canisters, Candle inference) with web demos |
| Requirements | Rust toolchain and the ICP SDK to build; none to try the public demo or anonymous `decide_query`. |
| License | [MIT](https://github.com/humandebri/IC-OpenJev/blob/71cf6cc280800115879e5fc03eca3f0141490648/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`canisters/verdict-engine/src/lib.rs`](https://github.com/humandebri/IC-OpenJev/blob/71cf6cc280800115879e5fc03eca3f0141490648/canisters/verdict-engine/src/lib.rs) at the pinned commit. |

## When to use

- Run Jev-style typed decisions inside ICP canisters without an off-chain API.
- Mismatch: if you need Jev quality or English docs; this is a small open model, documented in Japanese, described by its author as a safety-first, limited-capacity proof of concept.

## How it works

`canisters/verdict-engine/src/lib.rs` loads the INT8 weight pack and serves `decide`, `decide_batch` and `decide_query` over text plus named options; `crates/verdict-candle` implements the GLiClass forward pass, checked against the reference checkpoint. Integration evidence: [`canisters/verdict-engine/src/lib.rs`](https://github.com/humandebri/IC-OpenJev/blob/71cf6cc280800115879e5fc03eca3f0141490648/canisters/verdict-engine/src/lib.rs).

## Get started

Try the public demo, or build the canister per the README.

```sh
git clone https://github.com/humandebri/IC-OpenJev.git && cd IC-OpenJev
cargo test --workspace
bash tools/build_one.sh verdict-engine
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Public demo: [openjev.kinic.xyz](https://openjev.kinic.xyz)
- Verdict engine notes (Japanese): [github.com/humandebri/IC-OpenJev/blob/71cf6cc280800115879e5fc03eca3f0141490648/docs/VERDICT_ENGINE.md](https://github.com/humandebri/IC-OpenJev/blob/71cf6cc280800115879e5fc03eca3f0141490648/docs/VERDICT_ENGINE.md)

## Limits and data handling

Uses an open third-party model, not TypeSafe Jev. Cycles billing is implemented but not deployed (as of the README); the author warns query answers are not certified and must not justify moving funds. Mock-ledger transfers only.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 71cf6cc28080](https://github.com/humandebri/IC-OpenJev/tree/71cf6cc280800115879e5fc03eca3f0141490648). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
