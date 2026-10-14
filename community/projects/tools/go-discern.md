# go-discern

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small typed Go decision layer for the TypeSafe Jev and Cloudflare Clef System One APIs, with validated observations and zero third-party runtime dependencies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mrz1836/go-discern) |
| Maintainer | [mrz1836](https://github.com/mrz1836). Independently curated. |
| Format | Go library |
| Requirements | Go toolchain; TypeSafe API key (or Cloudflare credentials for Clef). |
| License | [MIT](https://github.com/mrz1836/go-discern/blob/4ca48e64278ee3d77f4a7a5c7bbf63e31bca78d5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/jev.go`](https://github.com/mrz1836/go-discern/blob/4ca48e64278ee3d77f4a7a5c7bbf63e31bca78d5/jev/jev.go) at the pinned commit. |

## When to use

- Call Jev from Go services with typed Choice / Score / Noul questions and validated answers.
- Swap between Jev and Cloudflare Clef behind one interface.
- Mismatch: a client library; it does not host a model.

## How it works

A provider-neutral core defines questions and outcomes; the `jev` adapter builds the System One request, sends it to TypeSafe and validates the returned model, request ID and answers before your code reads them. Integration evidence: [`jev/jev.go`](https://github.com/mrz1836/go-discern/blob/4ca48e64278ee3d77f4a7a5c7bbf63e31bca78d5/jev/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
go get github.com/mrz1836/go-discern
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Runnable examples: `examples/` in the repository.

## Limits and data handling

Request state goes to TypeSafe (or Cloudflare) and is billed to your account; the library itself stores nothing.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 4ca48e64278e](https://github.com/mrz1836/go-discern/tree/4ca48e64278ee3d77f4a7a5c7bbf63e31bca78d5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
