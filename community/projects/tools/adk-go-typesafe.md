# adk-go-typesafe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeSafe System One client and Google ADK-Go function tool: Choice/Score/Noul evaluations with OpenAPI-generated types (temporary bridge until an official Go SDK).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/craigh33/adk-go-typesafe) |
| Maintainer | [craigh33](https://github.com/craigh33). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go module (`github.com/craigh33/adk-go-typesafe`) with `typesafe` client + `tools/systemone` ADK tool. |
| Requirements | Go matching `go.mod` (**1.26.6** on reviewed tip). Live calls need `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/craigh33/adk-go-typesafe/blob/e299992701c1dee059514613efbf06feae748668/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `go test ./...`: packages `typesafe` and `tools/systemone` **ok** (**13** PASS lines). Live TypeSafe / ADK agent runs not executed. Distinct from [jevgo](jevgo.md) and [TypeSafe Go](typesafe-go.md) (ADK tool + generated OpenAPI types). |

## When to use

Use it when a Google ADK-Go agent should call System One as a typed function tool, or when you want a Go client generated from TypeSafe’s OpenAPI schema. Prefer [jevgo](jevgo.md) / [TypeSafe Go](typesafe-go.md) for smaller standalone clients without ADK.

## How it works

[`typesafe/client.go`](https://github.com/craigh33/adk-go-typesafe/blob/e299992701c1dee059514613efbf06feae748668/typesafe/client.go) POSTs to `{base}/v1/systemone` (default `https://api.typesafe.ai`), default model `jev-latest`. [`tools/systemone`](https://github.com/craigh33/adk-go-typesafe/blob/e299992701c1dee059514613efbf06feae748668/tools/systemone/tool.go) wraps that client as an ADK tool. Wire types under `internal/typesafe` are codegen from TypeSafe OpenAPI. Application code owns retries and thresholds.

## Get started

```sh
git clone https://github.com/craigh33/adk-go-typesafe.git
cd adk-go-typesafe
git checkout e299992701c1dee059514613efbf06feae748668
go test ./...
# Live: export TYPESAFE_API_KEY; see examples/ under the repo
```

## Examples and demos

- Offline **`go test ./...`**: `typesafe` and `tools/systemone` packages passed; example packages have no tests.
- Upstream examples `examples/typesafe-evaluate` and `examples/systemone-tool` demonstrate client and ADK wiring (not executed live here).

## Limits and data handling

Described as a temporary bridge pending an official Go SDK. Live calls send state/questions to TypeSafe. Default timeout is ten seconds; no automatic retries. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit e299992](https://github.com/craigh33/adk-go-typesafe/tree/e299992701c1dee059514613efbf06feae748668): Apache-2.0. AI-assisted review of README, LICENSE, `typesafe/client.go`, `tools/systemone`, and offline tests. **`go test ./...` ok**. No live TypeSafe.

Related: [jevgo](jevgo.md), [TypeSafe Go](typesafe-go.md), [semgate](semgate.md).
