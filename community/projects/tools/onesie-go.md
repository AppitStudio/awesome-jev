# onesie-go (Go client library for the TypeSafe System One API and compatible providers, with typed Noul, Choice and Score questions)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go client package for System One: build typed Noul, Choice and Score questions, read answers with `result.Noul("id")`, and use TypeSafe by default or OpenRouter, Berget, Levanto, Cloudflare or a custom base URL. Includes typed errors, validation before sending, response-size caps and image support. The onesie CLI uses it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frodi-karlsson/onesie-go) |
| Maintainer | [frodi-karlsson](https://github.com/frodi-karlsson). Independently curated. |
| Format | Go module `github.com/frodi-karlsson/onesie-go` |
| Requirements | Go toolchain and a provider API key (for example `TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/frodi-karlsson/onesie-go/blob/82ea9e6240cec6ba3847cc56246e2deb9f94078e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client.go`](https://github.com/frodi-karlsson/onesie-go/blob/82ea9e6240cec6ba3847cc56246e2deb9f94078e/client.go) at the pinned commit. |

## When to use

- Call Jev from Go services with typed requests and errors.
- Switch between TypeSafe and other System One providers by changing the provider option.
- Mismatch: ports parts of the official JavaScript SDK (see NOTICE); not an official TypeSafe client.

## How it works

`client.go` defines `New` and `SystemOne`, posts to `/v1/systemone` and decodes answers into typed results; `NOTICE` credits the TypeSafe JavaScript SDK it was ported from. Integration evidence: [`client.go`](https://github.com/frodi-karlsson/onesie-go/blob/82ea9e6240cec6ba3847cc56246e2deb9f94078e/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
go get github.com/frodi-karlsson/onesie-go
# client, err := onesie.New(onesie.WithAPIKey(apiKey))
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with usage and provider options: [github.com/frodi-karlsson/onesie-go/blob/82ea9e6240cec6ba3847cc56246e2deb9f94078e/README.md](https://github.com/frodi-karlsson/onesie-go/blob/82ea9e6240cec6ba3847cc56246e2deb9f94078e/README.md)
- NOTICE crediting the TypeSafe JS SDK: [github.com/frodi-karlsson/onesie-go/blob/82ea9e6240cec6ba3847cc56246e2deb9f94078e/NOTICE](https://github.com/frodi-karlsson/onesie-go/blob/82ea9e6240cec6ba3847cc56246e2deb9f94078e/NOTICE)

## Limits and data handling

Requests go to the configured provider on your key and are billed there; the project is independent and not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 82ea9e6240ce](https://github.com/frodi-karlsson/onesie-go/tree/82ea9e6240cec6ba3847cc56246e2deb9f94078e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
