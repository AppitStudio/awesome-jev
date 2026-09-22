# JevClient.jl

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Julia client for TypeSafe System One: build Noul/Choice/Score question sets, pin models, and POST to `api.typesafe.ai` with local validation and endpoint policy checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AtelierArith/JevClient.jl) |
| Maintainer | [AtelierArith](https://github.com/AtelierArith) / Satoshi Terasaki. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Julia package **0.1.0** (JuliaHub/docs site). |
| Requirements | Julia with the package environment. Live calls need `TYPESAFE_API_KEY` (or another credential helper documented upstream). |
| License | [MIT](https://github.com/AtelierArith/JevClient.jl/blob/0a8f493158880e734ff6bf4c41d3372b12619e33/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Julia was not installed on the review host; upstream CI for this SHA concluded **success**. No live TypeSafe calls. Distinct from Go/Java/.NET/Swift clients already listed. |

## When to use

Use it when a Julia program needs typed System One judgments without shelling out to another language’s SDK. Prefer the official Python/JS SDKs for first-party support, or language-matched clients such as [jevgo](jevgo.md) / [TypeSafe Go](typesafe-go.md) for Go.

## How it works

[`src/client.jl`](https://github.com/AtelierArith/JevClient.jl/blob/0a8f493158880e734ff6bf4c41d3372b12619e33/src/client.jl) evaluates a `QuestionSet` via POST `/v1/systemone`. [`src/transport.jl`](https://github.com/AtelierArith/JevClient.jl/blob/0a8f493158880e734ff6bf4c41d3372b12619e33/src/transport.jl) allows only `https://api.typesafe.ai` paths `/v1/systemone` and `/v1/models`. Credentials and bodies are kept out of logs per upstream docs. Application code owns thresholds and downstream actions.

## Get started

```sh
git clone https://github.com/AtelierArith/JevClient.jl.git
cd JevClient.jl
git checkout 0a8f493158880e734ff6bf4c41d3372b12619e33
julia --project=. -e 'using Pkg; Pkg.test()'
```

Docs: [atelierarith.github.io/JevClient.jl](https://atelierarith.github.io/JevClient.jl/). Live `with_client` examples send state/questions to TypeSafe.

## Examples and demos

- Upstream README shows Noul/Choice/Score construction and `PinnedModel("jev-1.13.0")`.
- Upstream Actions **CI** for [0a8f493](https://github.com/AtelierArith/JevClient.jl/tree/0a8f493158880e734ff6bf4c41d3372b12619e33): **success** (not re-run locally; no Julia on the review host).

## Limits and data handling

Endpoint policy rejects non-TypeSafe hosts. Live calls incur TypeSafe usage. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 0a8f493](https://github.com/AtelierArith/JevClient.jl/tree/0a8f493158880e734ff6bf4c41d3372b12619e33): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `client.jl`, `transport.jl`, and test expectations for `/v1/systemone`. No local Julia test run. No live TypeSafe.

Related: [jevgo](jevgo.md), [TypeSafe Go](typesafe-go.md), [jev-java](jev-java.md), [TypeSafe (Swift)](typesafe-swift.md).
