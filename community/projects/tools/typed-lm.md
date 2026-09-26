# typed-lm

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rust (Candle) framework that turns dense decoder models into a typed semantic-routing API—Choice, Noul, Score in a single forward pass—with LoRA/QLoRA training and a System One–shaped HTTP server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/neurono-ml/typed-lm) |
| Maintainer | [neurono-ml](https://github.com/neurono-ml). Independently curated. Not hosted TypeSafe Jev. |
| Format | Rust crates (typed-lm-serve on crates.io) + docs site. |
| Requirements | Rust toolchain; GPU recommended; model weights from Hugging Face. |
| License | [Apache-2.0](https://github.com/neurono-ml/typed-lm/blob/8b90ae8f5524b247e97eebb64dc4eede951b0222/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Independent Jev-style alternative. |

## When to use

Use to **train or serve** your own typed decision head on Llama/Qwen/Mistral/Gemma-class models. Prefer hosted TypeSafe Jev for the managed calibrated API.

## How it works

HTTP handlers under [`typed-lm-serve/src/api/handlers/`](https://github.com/neurono-ml/typed-lm/tree/8b90ae8f5524b247e97eebb64dc4eede951b0222/typed-lm-serve/src/api/handlers) including [`systemone.rs`](https://github.com/neurono-ml/typed-lm/blob/8b90ae8f5524b247e97eebb64dc4eede951b0222/typed-lm-serve/src/api/handlers/systemone.rs).

## Get started

```sh
git clone https://github.com/neurono-ml/typed-lm.git
cd typed-lm
git checkout 8b90ae8f5524b247e97eebb64dc4eede951b0222
# follow https://neurono-ml.github.io/typed-lm/quickstart.html
```

## Examples and demos

- Docs: [https://neurono-ml.github.io/typed-lm/](https://neurono-ml.github.io/typed-lm/)
- Example Noul request JSON under examples/.

## Limits and data handling

Local inference keeps state on your machine. Not a drop-in calibrated substitute for hosted Jev without your own eval. Latency tables are upstream-reported.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 8b90ae8](https://github.com/neurono-ml/typed-lm/tree/8b90ae8f5524b247e97eebb64dc4eede951b0222). AI-assisted README and LICENSE inspection of serve handlers; install/live paths not executed.
