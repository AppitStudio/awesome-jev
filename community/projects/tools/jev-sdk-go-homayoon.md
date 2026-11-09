# jev-sdk-go (zero-dependency Go client for the TypeSafe System One API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Standard-library-only Go client for TypeSafe: name your Noul, Choice and Score questions and get answers back under those names with probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HomayoonAlimohammadi/jev-sdk-go) |
| Maintainer | [HomayoonAlimohammadi](https://github.com/HomayoonAlimohammadi). Independently curated. |
| Format | Go module (MIT) |
| Requirements | Go 1.24+ and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/HomayoonAlimohammadi/jev-sdk-go/blob/4ec00b248f2f4776dec943b0ee0c242415396c01/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client.go`](https://github.com/HomayoonAlimohammadi/jev-sdk-go/blob/4ec00b248f2f4776dec943b0ee0c242415396c01/client.go) at the pinned commit. |

## When to use

- Call Jev from Go without extra dependencies.
- Get named, typed answers in Go services.
- Mismatch: community SDK, not official.

## How it works

`client.go` reads `TYPESAFE_API_KEY`, `TYPESAFE_BASE_URL` and `TYPESAFE_DEFAULT_MODEL` and calls System One; tests and `bench_test.go` cover the client. Integration evidence: [`client.go`](https://github.com/HomayoonAlimohammadi/jev-sdk-go/blob/4ec00b248f2f4776dec943b0ee0c242415396c01/client.go).

## Get started

`go get github.com/HomayoonAlimohammadi/jev-sdk-go`, set `TYPESAFE_API_KEY`, and call `client.SystemOne`.

```sh
go get github.com/HomayoonAlimohammadi/jev-sdk-go
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/HomayoonAlimohammadi/jev-sdk-go/blob/4ec00b248f2f4776dec943b0ee0c242415396c01/README.md](https://github.com/HomayoonAlimohammadi/jev-sdk-go/blob/4ec00b248f2f4776dec943b0ee0c242415396c01/README.md)

## Limits and data handling

Content you send is processed by TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 4ec00b248f2f](https://github.com/HomayoonAlimohammadi/jev-sdk-go/tree/4ec00b248f2f4776dec943b0ee0c242415396c01). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
