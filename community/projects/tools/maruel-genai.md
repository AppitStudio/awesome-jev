# genai (maruel)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

High-performance multi-provider Go AI package whose `Provider.SystemOne()` asks typed decision questions across TypeSafe Jev, Cloudflare CLEF/CLEF-Flash, Ollama and local llama.cpp decision models with shared `genai.Questions` / `genai.Answers` maps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maruel/genai) |
| Maintainer | [maruel](https://github.com/maruel). Independently curated. |
| Format | Go module with provider packages and runnable examples |
| Requirements | Go toolchain; a TypeSafe key for the `typesafe` provider, or a local llama.cpp/Ollama server for local decisions. |
| License | [Apache-2.0](https://github.com/maruel/genai/blob/ecce1d4b87600eb127aee3585ea14dadcc596753/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add Jev decisions to a Go service that already talks to several LLM providers.
- Compare hosted Jev with local decision models through the same interface.
- Mismatch: document/image support differs per provider; check the scoreboard before relying on multimodal decisions.

## How it works

Decision-capable providers implement `SystemOne()`, taking typed questions about text or JSON state and returning typed answers with probabilities. The `typesafe` provider is SystemOne-only (no chat); Cloudflare, llama.cpp and Ollama providers also expose it. A provider scoreboard in the README lists which modalities each supports ([docs/typesafe.md](https://github.com/maruel/genai/blob/ecce1d4b87600eb127aee3585ea14dadcc596753/docs/typesafe.md), [`providers/typesafe/example_test.go`](https://github.com/maruel/genai/blob/ecce1d4b87600eb127aee3585ea14dadcc596753/providers/typesafe/example_test.go)).

## Get started

Add the module and run the text-to-decisions example (live TypeSafe call):

```sh
go get github.com/maruel/genai
# see examples/txt_to_decisions/main.go (hosted) and examples/txt_to_decisions_local/main.go (local)
TYPESAFE_API_KEY=... go run ./examples/txt_to_decisions
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `examples/txt_to_decisions`, `examples/txt_to_decisions_local` and `examples/img-txt_to_decisions_local`.
- Provider scoreboard (README) and recorded test data per provider.

## Limits and data handling

Hosted Jev calls send your state to TypeSafe and are billed. Local decision models are not Jev and may behave differently. Examples were not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit ecce1d4b8760](https://github.com/maruel/genai/tree/ecce1d4b87600eb127aee3585ea14dadcc596753). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
