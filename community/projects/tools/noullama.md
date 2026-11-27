# Noullama (local desktop workbench and API for Jev-style decision models on llama.cpp)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Desktop app for running native decision models locally: download a GGUF from the Hub tab or load your own, start llama.cpp from the Runtime tab, try noul, choice and score questions in a Playground with saved presets, and connect apps to a local API whose `/v1/systemone` route follows Jev's request format. Does not call TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Noullama/noullama) |
| Maintainer | [Noullama](https://github.com/Noullama) (formerly parasite6/noullama); site [noullama.dev](https://noullama.dev). Independently curated. |
| Format | Tauri desktop app (Rust and TypeScript) |
| Requirements | Linux x86-64 (early beta; `.deb`/`.rpm` packages), a llama.cpp build downloaded from the Runtime tab and a decision-model GGUF. Building from source needs Node.js and Rust for Tauri. |
| License | [AGPL-3.0](https://github.com/Noullama/noullama/blob/17149270bed78739be398bae6f67a70e2b8dd038/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src-tauri/src/api.rs`](https://github.com/Noullama/noullama/blob/17149270bed78739be398bae6f67a70e2b8dd038/src-tauri/src/api.rs) at the pinned commit. |

## When to use

- Test open decision models locally behind a Jev-shaped API.
- Mismatch: not TypeSafe's Jev; model quality depends on the GGUF.

## How it works

`src-tauri/src/api.rs` serves `POST /v1/systemone` on `127.0.0.1:11435` and forwards to the local llama.cpp runtime. Integration evidence: [`src-tauri/src/api.rs`](https://github.com/Noullama/noullama/blob/17149270bed78739be398bae6f67a70e2b8dd038/src-tauri/src/api.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://noullama.dev/install.sh | sh   # picks .deb or .rpm, checks the SHA-256
# or from source:
git clone https://github.com/Noullama/noullama.git && cd noullama
npm install
npm run desktop
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Noullama/noullama#readme](https://github.com/Noullama/noullama#readme)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe. Linux x86-64 only and in early beta per the README. Licence changed from GPL-3.0 to AGPL-3.0 when the repository moved to the Noullama organisation (re-checked 2026-11-27). A Python client is included for the local API.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 17149270bed7](https://github.com/Noullama/noullama/tree/17149270bed78739be398bae6f67a70e2b8dd038). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
