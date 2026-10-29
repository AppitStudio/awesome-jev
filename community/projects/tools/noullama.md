# Noullama (local desktop workbench and API for Jev-style decision models on llama.cpp)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Desktop app for running native decision models locally: download a GGUF from the Hub tab or load your own, start llama.cpp from the Runtime tab, try noul, choice and score questions in a Playground with saved presets, and connect apps to a local API whose `/v1/systemone` route follows Jev's request format. Does not call TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/parasite6/noullama) |
| Maintainer | [parasite6](https://github.com/parasite6). Independently curated. |
| Format | Tauri desktop app (Rust and TypeScript) |
| Requirements | Node.js, Rust for Tauri, a llama.cpp build and a decision-model GGUF. |
| License | [GPL-3.0](https://github.com/parasite6/noullama/blob/61dc706bdb28e2102444909aff6bbc0ef5b8c1fd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src-tauri/src/api.rs`](https://github.com/parasite6/noullama/blob/61dc706bdb28e2102444909aff6bbc0ef5b8c1fd/src-tauri/src/api.rs) at the pinned commit. |

## When to use

- Test open decision models locally behind a Jev-shaped API.
- Mismatch: not TypeSafe's Jev; model quality depends on the GGUF.

## How it works

`src-tauri/src/api.rs` serves `POST /v1/systemone` on `127.0.0.1:11435` and forwards to the local llama.cpp runtime. Integration evidence: [`src-tauri/src/api.rs`](https://github.com/parasite6/noullama/blob/61dc706bdb28e2102444909aff6bbc0ef5b8c1fd/src-tauri/src/api.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/parasite6/noullama.git && cd noullama
npm install
npm run desktop
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/parasite6/noullama#readme](https://github.com/parasite6/noullama#readme)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 61dc706bdb28](https://github.com/parasite6/noullama/tree/61dc706bdb28e2102444909aff6bbc0ef5b8c1fd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
