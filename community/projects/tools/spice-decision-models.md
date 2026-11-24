# Spice decision models by Spice AI (Jev as a model provider in the open-source Spice SQL engine, with decision functions in SQL and search reranking)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Since v2.4 the Apache-2.0 Spice runtime (a portable SQL query, acceleration and search engine) can register Jev as a model with `from: typesafe:jev` and ask it typed questions from SQL with `ai_if`, `ai_probability`, `ai_classify`, `ai_score` and `ai_decide`, over an OpenAI-compatible `POST /v1/decisions` API, or to rerank full-text search results. Jev is one of several decision-model providers Spice supports.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/spiceai/spiceai) |
| Maintainer | [Spice AI](https://github.com/spiceai) ([spice.ai](https://spice.ai)). Independently curated. |
| Format | Rust runtime (single binary or Docker) configured with a Spicepod YAML |
| Requirements | A Spice v2.4 or newer runtime and a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [Apache-2.0](https://github.com/spiceai/spiceai/blob/40af136fc6989bf19a685cb58d6a08e5509e903b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/spice_ai/status/2125288601336336681)). |
| Jev evidence | [`crates/llms/src/typesafe/mod.rs`](https://github.com/spiceai/spiceai/blob/40af136fc6989bf19a685cb58d6a08e5509e903b/crates/llms/src/typesafe/mod.rs) at the pinned release. |

## When to use

- Filter, route, score or rerank rows with Jev inside SQL queries over federated data.
- Mismatch: if you do not run Spice; this is a feature of the Spice runtime, not a standalone client.

## How it works

`crates/llms/src/typesafe/mod.rs` implements the TypeSafe provider (default base URL `https://api.typesafe.ai`, aliases for `jev-latest`, `jev-preview` and pinned `jev-1.13.0`); `docs/features/models/decisions.md` documents the SQL functions. Chat completions against a TypeSafe model return 400 by design. Integration evidence: [`crates/llms/src/typesafe/mod.rs`](https://github.com/spiceai/spiceai/blob/40af136fc6989bf19a685cb58d6a08e5509e903b/crates/llms/src/typesafe/mod.rs).

## Get started

Add a Jev model to your Spicepod, export your key, then ask decisions in SQL.

```sh
# spicepod.yaml
models:
  - from: typesafe:jev
    name: jev
    params:
      typesafe_api_key: ${secrets:TYPESAFE_API_KEY}
# then, in Spice SQL:
# SELECT id FROM tickets WHERE ai_if(body, 'Does this convey urgency?', model => 'jev');
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Blog: How to Use Decision Models in SQL and Search: [spice.ai/blog/decision-models](https://spice.ai/blog/decision-models)
- TypeSafe models doc: [github.com/spiceai/spiceai/blob/v2.4.3/docs/features/models/typesafe.md](https://github.com/spiceai/spiceai/blob/v2.4.3/docs/features/models/typesafe.md)
- Decisions doc: [github.com/spiceai/spiceai/blob/v2.4.3/docs/features/models/decisions.md](https://github.com/spiceai/spiceai/blob/v2.4.3/docs/features/models/decisions.md)

## Limits and data handling

Row data passed to decision functions is sent to TypeSafe per call, so a query over many rows makes many paid requests; use filters first and the runtime's rate controls. The blog's speed and price figures are TypeSafe's own. Spice is a commercial company that also offers a hosted cloud; this listing covers the open-source runtime only.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [release v2.4.3](https://github.com/spiceai/spiceai/tree/v2.4.3). Inspected the v2.4.3 TypeSafe provider source and the Decisions and TypeSafe model docs at that tag, plus Spice's blog post; the runtime was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
