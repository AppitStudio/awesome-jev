# XKS Jev-like Model Base by Lasimeri (jevbase: typed answers read from a local LLM's next-token odds, on the CPU)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

One Rust binary (`jevbase`) with llama.cpp linked statically that answers Noul, Choice and Score questions by reading a local GGUF model's next-token distribution, and serves the System One request format at `POST /v1/systemone` on localhost. A simpler re-implementation of the author's Intel-Phi-Jev, checked byte-for-byte against it on 113 decisions. It does not call TypeSafe's Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lasimeri/XKS_Jev-like_Model_Base) |
| Maintainer | [Lasimeri](https://github.com/Lasimeri). Independently curated. |
| Format | Rust CLI/server + TUI |
| Requirements | A CPU with AVX2/FMA, Rust and make; a GGUF model (default a 2B Qwen distill). |
| License | [MIT OR Apache-2.0](https://github.com/Lasimeri/XKS_Jev-like_Model_Base/blob/e6b62c2a1baf34df6b8a8a70227fde42718a8827/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/protocol.rs`](https://github.com/Lasimeri/XKS_Jev-like_Model_Base/blob/e6b62c2a1baf34df6b8a8a70227fde42718a8827/src/protocol.rs) at the pinned commit. |

## When to use

- Run a small local, offline stand-in that speaks the System One request format for testing or private data.
- Mismatch: Jev-level accuracy; it is an independent local model, not a validated substitute.

## How it works

`src/protocol.rs` and `src/validate.rs` implement and validate the documented `/v1/systemone` request shape; answers come from option-token probabilities of the local model, never generated text. Integration evidence: [`src/protocol.rs`](https://github.com/Lasimeri/XKS_Jev-like_Model_Base/blob/e6b62c2a1baf34df6b8a8a70227fde42718a8827/src/protocol.rs).

## Get started

Build with make, then ask a request file or serve the local endpoint.

```sh
git clone https://github.com/Lasimeri/XKS_Jev-like_Model_Base && cd XKS_Jev-like_Model_Base
make
jevbase ask examples/query.json
jevbase serve   # POST http://127.0.0.1:8097/v1/systemone
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Lasimeri/XKS_Jev-like_Model_Base/blob/e6b62c2a1baf34df6b8a8a70227fde42718a8827/README.md](https://github.com/Lasimeri/XKS_Jev-like_Model_Base/blob/e6b62c2a1baf34df6b8a8a70227fde42718a8827/README.md)
- Changelog: [github.com/Lasimeri/XKS_Jev-like_Model_Base/blob/e6b62c2a1baf34df6b8a8a70227fde42718a8827/CHANGELOG.md](https://github.com/Lasimeri/XKS_Jev-like_Model_Base/blob/e6b62c2a1baf34df6b8a8a70227fde42718a8827/CHANGELOG.md)

## Limits and data handling

Release candidate 0.1.0-rc.1; known gaps are listed in the changelog. Model weights carry their own licenses.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit e6b62c2a1baf](https://github.com/Lasimeri/XKS_Jev-like_Model_Base/tree/e6b62c2a1baf34df6b8a8a70227fde42718a8827). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
