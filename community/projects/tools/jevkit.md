# jevkit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fast Rust CLI for TypeSafe Jev: ask typed decision questions from the shell, and `jev lint` validates question sets offline before you spend on a call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ariel-frischer/jevkit) |
| Maintainer | [ariel-frischer](https://github.com/ariel-frischer). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Rust CLI crate **jevkit 0.3.0** (`rust-version = "1.88"`); install script and Cargo package. |
| Requirements | Rust **≥ 1.88** to build from source; TypeSafe or OpenRouter credentials for live `jev ask` (lint works offline). |
| License | [MIT](https://github.com/ariel-frischer/jevkit/blob/4bda844160cca340897a72d4fa2763dd7b826a82/LICENSE). TypeSafe/OpenRouter usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; **`cargo test` not run** on the review host (rustc 1.85 &lt; required 1.88). Live `jev ask` not run. Name collision note: unrelated to the `jevkit/` Python client folder inside [Hermes Jev Skills](hermes-jev-skills.md). |

## When to use

Use it when you want a native CLI for one-shot typed decisions and offline question linting before paying for inference. Prefer [typesafeai-cli](typesafeai-cli.md) for a Python CLI, or [askjev](askjev.md) for MCP agent integration.

## How it works

[`src/auth.rs`](https://github.com/ariel-frischer/jevkit/blob/4bda844160cca340897a72d4fa2763dd7b826a82/src/auth.rs) configures the TypeSafe endpoint `https://api.typesafe.ai/v1/systemone` (OpenRouter also supported). [`src/lint.rs`](https://github.com/ariel-frischer/jevkit/blob/4bda844160cca340897a72d4fa2763dd7b826a82/src/lint.rs) validates question YAML/config offline. Live asks send state and questions to the chosen provider.

## Get started

```sh
curl -fsSL https://raw.githubusercontent.com/ariel-frischer/jevkit/main/install.sh | sh
# or: cargo install --git https://github.com/ariel-frischer/jevkit (needs rustc ≥ 1.88)
jev lint -q severity.yaml
# jev ask -q severity.yaml "..."   # live; needs credentials
```

Pinned review checkout:

```sh
git clone https://github.com/ariel-frischer/jevkit.git
cd jevkit
git checkout 4bda844160cca340897a72d4fa2763dd7b826a82
# cargo test   # requires rustc ≥ 1.88
```

## Examples and demos

- Upstream README console example and CI badge.
- This listing did not execute `cargo test` or live asks (toolchain/key limits). Evidence is source + license + documented install path.

## Limits and data handling

Live asks send passage/state to TypeSafe or OpenRouter. Keyring/env storage is documented upstream—confirm before production use. Do not confuse this crate with Hermes’s internal `jevkit` Python package.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 4bda844](https://github.com/ariel-frischer/jevkit/tree/4bda844160cca340897a72d4fa2763dd7b826a82): **0.3.0**, MIT, rust-version **1.88**. AI-assisted source review of README, LICENSE, `src/auth.rs`, `src/lint.rs`, `src/config.rs`, and `Cargo.toml`. Host rustc 1.85 could not compile tests. No live TypeSafe/OpenRouter call.

Related: [askjev](askjev.md), [typesafeai-cli](typesafeai-cli.md), [Hermes Jev Skills](hermes-jev-skills.md).
