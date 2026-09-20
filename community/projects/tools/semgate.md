# semgate

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go `net/http` middlewares that ask TypeSafe Jev typed questions about each request, then let your handler allow, block, or route.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/m-mizutani/semgate) |
| Maintainer | [m-mizutani](https://github.com/m-mizutani). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go module `github.com/m-mizutani/semgate` (Go **1.26** toolchain in reviewed `go.mod`). |
| Requirements | Go toolchain matching the module; live middlewares need a TypeSafe API key passed to `typesafe.New` (library does not read env vars). |
| License | [Apache-2.0](https://github.com/m-mizutani/semgate/blob/530a8efaf2bbdc71495a68888d4dfd79845324a6/LICENSE). |

## When to use

Use it to filter or route HTTP traffic with calibrated noul/choice/score judgments (prompt-injection screens, intent routing) inside a Go server. Prefer language SDKs for non-HTTP apps, or agent toolgates such as [toolgate](toolgate.md) for coding-agent shells.

## How it works

[`providers/typesafe/client.go`](https://github.com/m-mizutani/semgate/blob/530a8efaf2bbdc71495a68888d4dfd79845324a6/providers/typesafe/client.go) calls `https://api.typesafe.ai` System One (default model `jev-latest`). `g.Noul` / `g.Choice` / `g.Score` wrap one question per middleware; `g.Ask` batches several in one request. Your callback receives typed answers and decides whether to call `next`, respond, or hand off to another handler. **By default every header and query parameter is sent**—use denylist/allowlist options before production.

## Get started

```sh
go get github.com/m-mizutani/semgate@530a8efaf2bbdc71495a68888d4dfd79845324a6
```

Inspected revision:

```sh
git clone https://github.com/m-mizutani/semgate.git
cd semgate
git checkout 530a8efaf2bbdc71495a68888d4dfd79845324a6
go test ./...
```

Live middlewares send request-derived state to TypeSafe. This listing did not call the API.

## Examples and demos

- README snippets for injection detection and intent routing.
- Provider client tests under [`providers/typesafe/`](https://github.com/m-mizutani/semgate/tree/530a8efaf2bbdc71495a68888d4dfd79845324a6/providers/typesafe).

## Limits and data handling

Header/query denylists are essential: Authorization and Cookie are included unless denied. Application code owns allow/block/route policy. Go 1.26 in `go.mod` may be ahead of older toolchains—match the module before building.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 530a8ef](https://github.com/m-mizutani/semgate/tree/530a8efaf2bbdc71495a68888d4dfd79845324a6): Apache-2.0. AI-assisted source review of the TypeSafe client, README privacy warnings, and license. On the review host (Go toolchain auto-downloaded **1.26**), **`go test ./...`**: **ok** (`semgate` + `providers/typesafe`). No live TypeSafe HTTP calls were performed.

Related: [Advocaat](advocaat.md), [TypeSafeAI.Net](typesafeai-net.md), [toolgate](toolgate.md).
