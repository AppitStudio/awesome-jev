# skycmd (tiny System One decision models trained from scratch in Rust on a Mac)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent research repo that trains tiny System One-style decision models (s1 to s6, the smallest about 445k parameters and 251 KB ternary) from scratch in Rust with MLX on Apple silicon, answers `/v1/systemone`-shaped requests from GGUF files and plays four games live in the browser through WebAssembly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maxgfr/skycmd) |
| Maintainer | [maxgfr](https://github.com/maxgfr). Independently curated. |
| Format | Rust workspace, GGUF models and WebAssembly demos |
| Requirements | macOS on Apple silicon with Rust for training; any modern browser for the demos. |
| License | [Apache-2.0](https://github.com/maxgfr/skycmd/blob/49626ca8097ec005430250e68f680f9391f78f37/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/sky-py/src/lib.rs`](https://github.com/maxgfr/skycmd/blob/49626ca8097ec005430250e68f680f9391f78f37/crates/sky-py/src/lib.rs) at the pinned commit. |

## When to use

- Study how small a model can answer typed System One questions well enough to play a game.
- Run the request format locally with no hosted model.
- Mismatch: not affiliated with TypeSafe; makes no Jev calls and is not a drop-in Jev replacement.

## How it works

`crates/sky-py/src/lib.rs` answers a System One request (the `POST /v1/systemone` body) with a local GGUF model; the games pose canonical Choice questions in the same format. Integration evidence: [`crates/sky-py/src/lib.rs`](https://github.com/maxgfr/skycmd/blob/49626ca8097ec005430250e68f680f9391f78f37/crates/sky-py/src/lib.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo run --release -p sky-data -- fetch-decisions
cargo run --release -p sky-arena -- models/s1-pico-g2 --episodes 30
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Play in the browser: [maxgfr.github.io/skycmd/play/](https://maxgfr.github.io/skycmd/play/)
- Results: [maxgfr.github.io/skycmd/results/](https://maxgfr.github.io/skycmd/results/)
- Model card: [huggingface.co/maxgfr/s3-pico](https://huggingface.co/maxgfr/s3-pico)

## Limits and data handling

Everything runs locally; training data is fetched from Hugging Face. Independent models evaluated by the author, not by TypeSafe.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 49626ca8097e](https://github.com/maxgfr/skycmd/tree/49626ca8097ec005430250e68f680f9391f78f37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
