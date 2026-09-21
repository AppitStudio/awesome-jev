# TypeSafe Go

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Security-focused, idiomatic Go client for TypeSafe’s System One API (`POST /v1/systemone`, `GET /v1/models`). Community-maintained by Stacklok; not an official TypeSafe SDK. Distinct from [jevgo](jevgo.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stacklok/typesafe-go) |
| Maintainer | [Stacklok](https://github.com/stacklok) / [stacklok/typesafe-go](https://github.com/stacklok/typesafe-go). Independently curated; this page is not an upstream submission or endorsement. Unofficial—not maintained by TypeSafe. |
| Format | Go module `github.com/stacklok/typesafe-go` (stdlib HTTP; pre-v1 API may change). |
| Requirements | Go 1.26+; caller-supplied API key via `WithAPIKey` or an authenticated HTTP client (the SDK does **not** read environment variables). |
| License | [Apache-2.0](https://github.com/stacklok/typesafe-go/blob/10b73028990ba4c335f5be0646ae7f27af2f433d/LICENSE). TypeSafe inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `go test ./...`: **300 passed** (including example packages with httptest). Live TypeSafe calls were not run. |

## When to use

Use it when a Go service wants an explicit, option-driven System One client that avoids implicit env reads, logging, telemetry, or caching at construction time. Prefer [jevgo](jevgo.md) for a smaller unofficial client that reads `TYPESAFE_API_KEY` by default, or the official Python/JS SDKs for first-party support. Prefer [semgate](semgate.md) when you need Go HTTP middleware rather than a client library.

## How it works

`typesafe.NewClient` accepts mutually exclusive auth options (`WithAPIKey`, optional `WithHTTPClient`, or `WithAuthenticatedHTTPClient` alone). Callers post typed Noul/Choice/Score questions via `SystemOne`; answers decode to typed structs. The client performs no network I/O during construction. State and question text leave the host on live calls.

## Get started

```sh
go get github.com/stacklok/typesafe-go@10b73028990ba4c335f5be0646ae7f27af2f433d
# or
git clone https://github.com/stacklok/typesafe-go.git
cd typesafe-go
git checkout 10b73028990ba4c335f5be0646ae7f27af2f433d
go test ./...
```

Supply the key explicitly in application code (do not paste secrets into chat):

```go
client, err := typesafe.NewClient(
    typesafe.WithAPIKey(os.Getenv("TYPESAFE_API_KEY")),
    typesafe.WithDefaultModel("jev-1.13.0"),
)
```

Live `SystemOne` calls are billed by TypeSafe.

## Examples and demos

- README quick-start (Choice ticket triage).
- Example packages under [`examples/`](https://github.com/stacklok/typesafe-go/tree/10b73028990ba4c335f5be0646ae7f27af2f433d/examples) (support triage, security routing, RAG ranking, skill selection, and more)—offline-tested with httptest on the review host.
- Pre-v1 migration note: `NewClient(key)` → `NewClient(WithAPIKey(key))`.

## Limits and data handling

Request state and questions leave the host on live calls. Pre-v1 public API may change. The SDK does not invent policy—callers interpret probabilities and own downstream actions. This listing does not compare latency or feature completeness against jevgo.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 10b7302](https://github.com/stacklok/typesafe-go/tree/10b73028990ba4c335f5be0646ae7f27af2f433d), Apache-2.0. AI-assisted source review of README, license, and client packages. Offline `go test ./...` → **300 passed**. Live TypeSafe inference was not run.

Related: [jevgo](jevgo.md), [semgate](semgate.md), [jev-java](jev-java.md).
