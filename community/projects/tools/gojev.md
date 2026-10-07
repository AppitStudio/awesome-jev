# gojev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go harness for System One decision models — TypeSafe's hosted Jev, Jev via Vercel AI Gateway, Cloudflare Clef and in-process open-weight Kev — with typed Choice/Noul/Score question builders, calibrated answers, gating helpers and a CLI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/taigrr/gojev) |
| Product homepage | [pkg.go.dev](https://pkg.go.dev/github.com/taigrr/gojev) |
| Maintainer | [taigrr](https://github.com/taigrr). Independently curated. |
| Format | Go module `github.com/taigrr/gojev` with `cmd/gojev` CLI |
| Requirements | Go; a TypeSafe or Vercel AI Gateway key for hosted Jev, a Cloudflare account for Clef, or local Kev weights for in-process use. |
| License | [0BSD](https://github.com/taigrr/gojev/blob/d856c5f228279ba9b197928976c2c0c74c5a48f7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route tickets or gate agent actions from a Go service with typed questions.
- Switch between hosted Jev and in-process Kev without changing call sites.
- Mismatch: builds on the maintainer's `fantasy` provider library; read the trust model before gating.

## How it works

[`gojev.go`](https://github.com/taigrr/gojev/blob/d856c5f228279ba9b197928976c2c0c74c5a48f7/gojev.go) defines `Evaluate` and question builders (`Choice`, `Noul`, `Score`) over an evaluation model from the `fantasy` provider layer (TypeSafe, Vercel AI Gateway, Cloudflare, local Kev); [`cmd/gojev`](https://github.com/taigrr/gojev/tree/d856c5f228279ba9b197928976c2c0c74c5a48f7/cmd/gojev) wraps it as a CLI.

## Get started

Add the module:

```sh
go get github.com/taigrr/gojev
```

Hosted Jev calls are billed by TypeSafe or Vercel AI Gateway; local Kev runs on your hardware.

## Examples and demos

- README *Usage* (department routing Choice) and *Typed decisions for gating*.
- README *Local Kev, in-process* and latency notes (maintainer, M4 Max).

## Limits and data handling

State text goes to the hosted provider you choose; local Kev keeps data on your machine. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit d856c5f22827](https://github.com/taigrr/gojev/tree/d856c5f228279ba9b197928976c2c0c74c5a48f7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
