# Huncho

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rust server that implements the Jev `/v1/systemone` API for self-hosted System One models (ONNX, Laya, Kev, Clef runtimes, plus a mock), so the TypeSafe SDK can point at your own server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/grafuls/huncho) |
| Maintainer | [grafuls](https://github.com/grafuls). Independently curated. |
| Format | Rust server/CLI (Cargo; Fedora/EPEL COPR packages) |
| Requirements | Rust toolchain, C/C++ compiler, OpenSSL headers (or the COPR RPM); model downloads from the Hub; CUDA optional. |
| License | [Apache-2.0](https://github.com/grafuls/huncho/blob/f0e509791638c75f5fb9376e1a6e7a9c2886c0c5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/huncho-api/src/routes.rs`](https://github.com/grafuls/huncho/blob/f0e509791638c75f5fb9376e1a6e7a9c2886c0c5/crates/huncho-api/src/routes.rs) at the pinned commit. |

## When to use

- Run Jev-shaped decisions on your own hardware with open models.
- Test a Jev integration locally against the deterministic mock model.
- Mismatch: does not run TypeSafe's Jev; answers come from the open model you load.

## How it works

Huncho exposes `/v1/systemone` and `/v1/models` following the documented Jev API, scoring answer options in a forward pass with the selected backend; the mock backend returns deterministic test values. Integration evidence: [`crates/huncho-api/src/routes.rs`](https://github.com/grafuls/huncho/blob/f0e509791638c75f5fb9376e1a6e7a9c2886c0c5/crates/huncho-api/src/routes.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/grafuls/huncho.git && cd huncho
cargo install --locked --path crates/huncho-cli --features onnx,clef
huncho serve --mock --bind 127.0.0.1:8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Backend and build guides: `docs/backends.md`, `docs/operations.md`.

## Limits and data handling

Runs locally; inputs stay on your server.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit f0e509791638](https://github.com/grafuls/huncho/tree/f0e509791638c75f5fb9376e1a6e7a9c2886c0c5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
