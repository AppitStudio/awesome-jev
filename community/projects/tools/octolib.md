# Octolib

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

One Rust API for 30+ AI providers (chat, tools, structured output, embeddings, reranking, media) whose `evaluation` feature asks TypeSafe Jev typed noul/choice/score questions — directly (`typesafe:jev-latest`) or billed through Cloudflare AI Gateway (`cloudflare:typesafe/jev`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Muvon/octolib) |
| Product homepage | [octomind.run](https://octomind.run/product/octolib) |
| Maintainer | [Muvon](https://github.com/Muvon). Independently curated. |
| Format | Rust library with feature flags (`evaluation`, `embeddings`, `media`, …) |
| Requirements | Rust toolchain; `TYPESAFE_API_KEY` for direct Jev, or Cloudflare AI Gateway credentials for the gateway route. |
| License | [Apache-2.0](https://github.com/Muvon/octolib/blob/46126f5050dabc17f5a249637af749201d90ada8/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add typed decisions (urgency, routing, frustration level) to a Rust service that already uses Octolib for chat or embeddings.
- Choose between paying TypeSafe directly and using Cloudflare AI Gateway credits without changing call sites.
- Mismatch: if you only need Jev, a dedicated TypeSafe client is smaller; Octolib's value is the multi-provider surface.

## How it works

`octolib::evaluate("typesafe:jev-latest", request)` sends one state with several independent questions and returns `Answer::Noul`, choice and score answers with probabilities plus usage/cost; the response's `model` field reports the versioned model that answered. Provider implementations live in [`src/evaluation/providers/`](https://github.com/Muvon/octolib/tree/46126f5050dabc17f5a249637af749201d90ada8/src/evaluation/providers) (TypeSafe, Cloudflare, OctoHub).

## Get started

Add the crate (latest 0.41.x at review) and call `evaluate` (live TypeSafe calls):

```sh
# Cargo.toml
# octolib = { version = "0.41", features = ["evaluation"] }
export TYPESAFE_API_KEY=...
# let response = octolib::evaluate("typesafe:jev-latest", request).await?;
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Evaluation* example: support-ticket urgency (noul), department (choice) and frustration (score) in one call.
- Provider support matrix covering evaluation via TypeSafe, Cloudflare Workers AI and OctoHub.

## Limits and data handling

Pricing figures in the README are upstream statements; check current TypeSafe pricing. State text is sent to TypeSafe or Cloudflare. Whether every feature in the pinned commit is already on crates.io was not verified. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 46126f5050da](https://github.com/Muvon/octolib/tree/46126f5050dabc17f5a249637af749201d90ada8). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
