# Gut

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Elixir DSL for typed decisions in ordinary control flow (`Gut.feel/3` returns an Elixir value) with a `Gut.ReqLLM.Jev` adapter for TypeSafe Jev, plus other LLM, Ollama, and custom adapters.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vinibrsl/gut) |
| Product homepage | [hexdocs.pm](https://hexdocs.pm/gut) |
| Maintainer | [vinibrsl](https://github.com/vinibrsl). Independently curated. |
| Format | Elixir library with telemetry and async test helpers |
| Requirements | Elixir/Mix with `{:gut, "~> 0.1.0"}` and `{:req_llm, "~> 1.24"}`; `TYPESAFE_API_KEY` for the Jev adapter (model `typesafe:jev-latest`). |
| License | [Apache-2.0](https://github.com/vinibrsl/gut/blob/3885c8daa28e93fda7f24502142ad0a2c50dabb5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Replace brittle if/else heuristics with a typed decision in Phoenix or background jobs.
- Swap between Jev, another LLM, or a local model behind one API.
- Mismatch: deterministic rules you can express in code do not need a model call.

## How it works

`Gut.feel(subject, question, options)` builds a typed choice from the option keywords and descriptions; the configured adapter (`Gut.ReqLLM.Jev`) asks Jev and maps the answer back to the Elixir value ([README](https://github.com/vinibrsl/gut/blob/3885c8daa28e93fda7f24502142ad0a2c50dabb5/README.md)).

## Get started

Add the deps and configure the Jev adapter (live calls):

```sh
# mix.exs: {:gut, "~> 0.1.0"}, {:req_llm, "~> 1.24"}
# config :gut, adapter: {Gut.ReqLLM.Jev, model: "typesafe:jev-latest", api_key: System.fetch_env!("TYPESAFE_API_KEY")}
mix deps.get
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README ticket-routing example and [HexDocs](https://hexdocs.pm/gut).

## Limits and data handling

Each decision sends the subject to TypeSafe and incurs charges. `jev-latest` is an alias; pin a version for stable behavior.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 3885c8daa28e](https://github.com/vinibrsl/gut/tree/3885c8daa28e93fda7f24502142ad0a2c50dabb5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
