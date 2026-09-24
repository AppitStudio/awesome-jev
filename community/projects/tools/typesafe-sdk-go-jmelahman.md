# typesafe-sdk-go (jmelahman)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Go client for the TypeSafe API with **no dependencies outside the standard library**—builders for Noul/Choice/Score and a `SystemOne` helper reading `TYPESAFE_API_KEY`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jmelahman/typesafe-sdk-go) |
| Maintainer | [jmelahman](https://github.com/jmelahman). Independently curated. |
| Format | Go module (`github.com/jmelahman/typesafe-sdk-go`). |
| Requirements | Go 1.27+ (per README); `TYPESAFE_API_KEY` for live calls. |
| License | [MIT](https://github.com/jmelahman/typesafe-sdk-go/blob/98425e689688b2da15637b04e74f76d6cdd7157e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live `go test`/Jev not run. Distinct from [TypeSafe Go](typesafe-go.md) (Stacklok) and [jevgo](jevgo.md). |

## When to use

Use it for a **minimal stdlib Go client**. Prefer [TypeSafe Go](typesafe-go.md) when you want explicit auth options without implicit env reads, or [jevgo](jevgo.md) for another lightweight client.

## How it works

[`client.go`](https://github.com/jmelahman/typesafe-sdk-go/blob/98425e689688b2da15637b04e74f76d6cdd7157e/client.go) posts System One requests; `answer.go` helpers extract typed answers. Example triage under `examples/triage`.

## Get started

```sh
go get github.com/jmelahman/typesafe-sdk-go@98425e689688b2da15637b04e74f76d6cdd7157e
# or
git clone https://github.com/jmelahman/typesafe-sdk-go.git
cd typesafe-sdk-go
git checkout 98425e689688b2da15637b04e74f76d6cdd7157e
TYPESAFE_API_KEY=... go run ./examples/triage
```

## Examples and demos

- README quick start.
- `examples/triage` and package tests (not executed here).

## Limits and data handling

State/question payloads leave your process for TypeSafe. Track Go version requirement (README cites 1.27+).

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 98425e6](https://github.com/jmelahman/typesafe-sdk-go/tree/98425e689688b2da15637b04e74f76d6cdd7157e). AI-assisted README + module layout inspection. No live TypeSafe spend.

Related: [TypeSafe Go](typesafe-go.md), [jevgo](jevgo.md), [adk-go-typesafe](adk-go-typesafe.md).
