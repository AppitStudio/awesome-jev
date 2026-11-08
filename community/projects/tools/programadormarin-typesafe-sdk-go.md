# TypeSafe Go SDK by programadormarin (community Go client for the System One API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Go client for the TypeSafe System One API with typed questions and answers, context support, retries with backoff and Retry-After, zstd, and a typed error hierarchy. Distinct from the jmelahman Go SDK already listed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/programadormarin/typesafe-sdk-go) |
| Maintainer | [programadormarin](https://github.com/programadormarin). Independently curated. |
| Format | Go module (MIT) |
| Requirements | Go and a TypeSafe API key. |
| License | [MIT](https://github.com/programadormarin/typesafe-sdk-go/blob/c44a984432c0610e24f7aa8d69fe00573b6a03f0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`constants.go`](https://github.com/programadormarin/typesafe-sdk-go/blob/c44a984432c0610e24f7aa8d69fe00573b6a03f0/constants.go) at the pinned commit. |

## When to use

- Call Jev from Go services with typed answers.
- Rely on built-in retries and typed errors.
- Mismatch: unofficial; not maintained by TypeSafe.

## How it works

`constants.go` sets `https://api.typesafe.ai` and `jev-latest`; `typesafe.go` and `response.go` implement the typed request/response contract. Integration evidence: [`constants.go`](https://github.com/programadormarin/typesafe-sdk-go/blob/c44a984432c0610e24f7aa8d69fe00573b6a03f0/constants.go).

## Get started

Add the module with `go get`, set TYPESAFE_API_KEY, and follow the README examples.

```sh
git clone https://github.com/programadormarin/typesafe-sdk-go.git && cd typesafe-sdk-go
export TYPESAFE_API_KEY=...
go test ./...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/programadormarin/typesafe-sdk-go/blob/c44a984432c0610e24f7aa8d69fe00573b6a03f0/README.md](https://github.com/programadormarin/typesafe-sdk-go/blob/c44a984432c0610e24f7aa8d69fe00573b6a03f0/README.md)

## Limits and data handling

State and questions are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit c44a984432c0](https://github.com/programadormarin/typesafe-sdk-go/tree/c44a984432c0610e24f7aa8d69fe00573b6a03f0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
