# go-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go SDK and `jev-cli` for TypeSafe Jev: typed yes/no (Noul), Choice, and Score decisions over HTTPS—distinct from [jevgo](jevgo.md) and [TypeSafe Go](typesafe-go.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mattn/go-jev) |
| Maintainer | [mattn](https://github.com/mattn). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go module **`github.com/mattn/go-jev`** + CLI `cmd/jev-cli` (go 1.27 toolchain in `go.mod`). |
| Requirements | Go toolchain matching module; API key passed explicitly via `jev.WithAPIKey` (package does **not** read env itself). |
| License | [MIT](https://github.com/mattn/go-jev/blob/85f5994cb5136ff5360dd904b65253469dc95d2e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `jev.go`, CLI). Live TypeSafe calls were **not** executed on the review host. |

## When to use

Use it for idiomatic Go callers or UNIX-pipeline `jev-cli` use against TypeSafe Jev. Prefer [jevgo](jevgo.md) for another unofficial stdlib client, or [TypeSafe Go](typesafe-go.md) (Stacklok) when you want that auth-options style.

## How it works

`Client.Ask` / `Evaluate` send System One-shaped questions and return typed answers with probabilities/confidence ([`jev.go`](https://github.com/mattn/go-jev/blob/85f5994cb5136ff5360dd904b65253469dc95d2e/jev.go)). The CLI wraps the same client for shell pipelines.

## Get started

```sh
go get github.com/mattn/go-jev@85f5994cb5136ff5360dd904b65253469dc95d2e
# or clone and: go test ./...
```

Pin for review: [commit 85f5994](https://github.com/mattn/go-jev/tree/85f5994cb5136ff5360dd904b65253469dc95d2e). Live calls need a key you supply and may incur TypeSafe charges.

## Examples and demos

- README Choice/Noul/Score snippets.
- `cmd/jev-cli` and package tests upstream (not re-run here).

## Limits and data handling

No implicit env auth—callers must pass the key. This listing did not hit the live API.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 85f5994](https://github.com/mattn/go-jev/tree/85f5994cb5136ff5360dd904b65253469dc95d2e) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [jevgo](jevgo.md), [TypeSafe Go](typesafe-go.md), [daf-jev](daf-jev.md).
