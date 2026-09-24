# systemone (justintout)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Go module for TypeSafe System One / Jev: compile-time typed Choice/Noul/Score questions with explicit client options.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/justintout/systemone) |
| Maintainer | [justintout](https://github.com/justintout). Independently curated; upstream states unofficial / not TypeSafe-supported. |
| Format | Go module `github.com/justintout/systemone`. |
| Requirements | Go toolchain; TypeSafe API key passed explicitly to the client (see README). |
| License | [MIT](https://github.com/justintout/systemone/blob/0279872ce04251b85129560f58e78617f23138cc/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Distinct from [TypeSafe Go](typesafe-go.md) (Stacklok) and [go-jev](go-jev.md). CI badge present; tests not re-run here. |

## When to use

Use it for **idiomatic Go generics** over System One answers. Prefer [TypeSafe Go](typesafe-go.md) when you specifically want Stacklok's explicit-auth / no-implicit-env client.

## How it works

[`client.go`](https://github.com/justintout/systemone/blob/0279872ce04251b85129560f58e78617f23138cc/client.go) and question constructors (`NewChoice`, `NewNoul`, …) bind answer types in Go. Patterns under `pattern/` compose hierarchies. Calls target the System One HTTP API.

## Get started

```sh
go get github.com/justintout/systemone@0279872ce04251b85129560f58e78617f23138cc
```

See upstream README for typed question examples and CI.

## Examples and demos

- README Usage block with `NewChoice[Team]` / `NewNoul`.
- `example_test.go` and `pattern/` packages.

## Limits and data handling

Request state leaves the host on live calls. Unofficial client—track TypeSafe API changes yourself.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 0279872](https://github.com/justintout/systemone/tree/0279872ce04251b85129560f58e78617f23138cc). AI-assisted README/LICENSE/client inspection. No live TypeSafe spend.

Related: [TypeSafe Go](typesafe-go.md), [go-jev](go-jev.md).
