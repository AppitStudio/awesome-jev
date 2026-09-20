# J++

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental language and Rust runtime for composing semantic Jev questions with exact methods as first-class values, plus a retained Python reference and offline Towow discovery demos that replay recorded Jev responses.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Towow-ai/jpp) |
| Maintainer | [Towow-ai](https://github.com/Towow-ai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Standalone `.jpp` sources via Rust `jpp-cli`; Python 3.12 reference package; browser demos with published response recordings. |
| Requirements | Rust toolchain for native build; Python for the reference tree. Fixture/replay runs need no live key. Live Jev adapters use TypeSafe System One when configured. |
| License | [MIT](https://github.com/Towow-ai/jpp/blob/ec1720a4b93768502e176545dadda436ff1c5b32/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `cargo test` inspected. Live TypeSafe calls were not run. Discovery demos use recorded responses unless you enable live clients. |

## When to use

Use it to study judgment-as-composition: questions and solving methods as reusable values, with offline fixtures proving the kernel without API spend. Prefer ordinary SDKs/CLIs when you only need a one-shot System One call rather than a language/runtime experiment.

## How it works

The Rust kernel parses `.jpp`, checks language rules, and executes methods; fixtures supply observations so examples run without a model. The Python reference includes [`src/foundation/jv/client.py`](https://github.com/Towow-ai/jpp/blob/ec1720a4b93768502e176545dadda436ff1c5b32/src/foundation/jv/client.py) (`JevClient`) and Rust effects that can POST to `https://api.typesafe.ai/v1/systemone` when a key is present. Towow demos compare semantic-plus-lexical compositions against BM25 using published recordings.

## Get started

```sh
git clone https://github.com/Towow-ai/jpp.git
cd jpp/rust
git checkout ec1720a4b93768502e176545dadda436ff1c5b32
cargo test --locked --workspace
cargo run -p jpp-cli -- run examples/composition.jpp
cargo run -p jpp-cli -- run examples/adaptive.jpp --fixtures examples/fixtures/adaptive.json
```

These fixture runs do not call a model API.

## Examples and demos

- Native composition / adaptive / partial examples under `rust/examples/`.
- Hosted Towow lab pages (population, lab, real-relations) at the upstream GitHub Pages site; they execute published recordings in-browser.
- Language design docs under [`docs/`](https://github.com/Towow-ai/jpp/tree/ec1720a4b93768502e176545dadda436ff1c5b32/docs).

## Limits and data handling

Experimental language; APIs and grammar may change. Live paths send judgment payloads to TypeSafe when enabled. Demo metrics and retrieval comparisons are author-documented offline experiments, not catalog-remeasured quality claims.

## Review and maintenance

Reviewed on **2026-09-21** at [commit ec1720a](https://github.com/Towow-ai/jpp/tree/ec1720a4b93768502e176545dadda436ff1c5b32): MIT. AI-assisted source review of Rust CLI examples, `JevClient`, README, and LICENSE. **`cargo test --locked --workspace`** passed (all crates green; no failures). No live TypeSafe calls.

Related: [Advocaat](advocaat.md), [jevc](jevc.md), [Jev Lab](jev-lab.md).
