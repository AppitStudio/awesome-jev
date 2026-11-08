# BAML (agent programming language with a built-in TypeSafe Jev client in its standard library)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

BoundaryML's programming language for agents ships a `typesafeai` standard-library client that maps BAML types to TypeSafe Jev System One questions, defaulting to `jev-latest`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BoundaryML/baml) |
| Maintainer | [BoundaryML](https://github.com/BoundaryML). Independently curated. |
| Format | Rust compiler + BAML std library (Apache-2.0) |
| Requirements | BAML toolchain and a TypeSafe API key for Jev calls. |
| License | [Apache-2.0](https://github.com/BoundaryML/baml/blob/36adf40540998cc8c2e5ee72fcb673c23f460b4a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`baml_language/crates/baml_builtins2/baml_std/typesafeai/client.baml`](https://github.com/BoundaryML/baml/blob/36adf40540998cc8c2e5ee72fcb673c23f460b4a/baml_language/crates/baml_builtins2/baml_std/typesafeai/client.baml) at the pinned commit. |

## When to use

- Use Jev for typed classification inside BAML programs.
- Keep schemas in BAML and let the std library build Jev questions.
- Mismatch: Jev does not stream; use an LLM client for generation.

## How it works

The std client posts to `{base_url}/systemone` (default `https://api.typesafe.ai/v1`, `jev-latest`, `TYPESAFE_API_KEY`); `ns_internal/jev.baml` converts enums, literals and classes into Jev questions and rejects types Jev cannot represent. Jev does not stream. Integration evidence: [`baml_language/crates/baml_builtins2/baml_std/typesafeai/client.baml`](https://github.com/BoundaryML/baml/blob/36adf40540998cc8c2e5ee72fcb673c23f460b4a/baml_language/crates/baml_builtins2/baml_std/typesafeai/client.baml).

## Get started

Follow the BAML docs to install the toolchain, then call the `typesafeai` client from a BAML function with your key in the environment.

```sh
git clone https://github.com/BoundaryML/baml.git && cd baml
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/BoundaryML/baml/blob/36adf40540998cc8c2e5ee72fcb673c23f460b4a/README.md](https://github.com/BoundaryML/baml/blob/36adf40540998cc8c2e5ee72fcb673c23f460b4a/README.md)

## Limits and data handling

Values you pass to the client are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 36adf4054099](https://github.com/BoundaryML/baml/tree/36adf40540998cc8c2e5ee72fcb673c23f460b4a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
