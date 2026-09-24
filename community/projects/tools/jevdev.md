# jevdev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust coding-agent harness centered on TypeSafe Jev System One decisions (HTTP or local transport) for gated agent steps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ibrahimcesar/jevdev) |
| Maintainer | [ibrahimcesar](https://github.com/ibrahimcesar). Independently curated. |
| Format | Rust crate/CLI (`jevdev` on crates.io per README badge). |
| Requirements | Rust toolchain; `TYPESAFE_API_KEY` for HTTP transport (default TypeSafe base). |
| License | [Apache-2.0](https://github.com/ibrahimcesar/jevdev/blob/33cadde05bfbfa7a0447f1485eae96d333da1d92/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Offline/unit tests and live agent loops not run here. |

## When to use

Use it when you want a **Rust harness** that asks Jev before agent actions. Prefer TypeScript/Python harnesses already in this catalog when that is your stack.

## How it works

[`src/jev/http.rs`](https://github.com/ibrahimcesar/jevdev/blob/33cadde05bfbfa7a0447f1485eae96d333da1d92/src/jev/http.rs) POSTs to `{endpoint}/v1/systemone` with bearer `TYPESAFE_API_KEY`, retries on 429/5xx, and decodes typed answers. A local transport path exists alongside HTTP.

## Get started

```sh
git clone https://github.com/ibrahimcesar/jevdev.git
cd jevdev
git checkout 33cadde05bfbfa7a0447f1485eae96d333da1d92
cargo build --release
# TYPESAFE_API_KEY=... follow README for harness commands
```

## Examples and demos

- README overview and `TODO.md` roadmap.
- Modules under `src/jev/`.

## Limits and data handling

Task/state payloads leave the host on HTTP Jev calls. Treat as an early harness—review safety gates before unattended use.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 33cadde](https://github.com/ibrahimcesar/jevdev/tree/33cadde05bfbfa7a0447f1485eae96d333da1d92). AI-assisted README/LICENSE/`src/jev/http.rs` inspection. No live TypeSafe spend.

Related: [System One Harness](systemone-harness.md), [jev-harness](jev-harness.md).
