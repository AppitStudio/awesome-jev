# typesafe-client (haileyok)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Go and Rust clients for TypeSafe's System One API (Jev).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/haileyok/typesafe-client) |
| Maintainer | [haileyok](https://github.com/haileyok). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go module + Rust crate with shared System One client patterns. |
| Requirements | Go 1.22+ or Rust 1.88+; `TYPESAFE_API_KEY` (optional base URL/model env vars). |
| License | [MIT](https://github.com/haileyok/typesafe-client/blob/4be2f97a92d8b1186c677273d44b4d85e89a2ec7/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when integrating Jev from Go or Rust without writing the wire protocol yourself. Prefer official Python/JS SDKs for those languages.

## How it works

Clients post typed questions and parse structured answers; retries cover 408/429/5xx including 529 with Retry-After and budgeted backoff. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
go get github.com/haileyok/typesafe-client/go@latest
# or: cargo add typesafe-system-one
export TYPESAFE_API_KEY=…
```

Pin revision `4be2f97a92d8b1186c677273d44b4d85e89a2ec7` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Unofficial; not a TypeSafe product. Live API calls not run on the review host. Distinct from jmelahman/typesafe-sdk-go.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 4be2f97](https://github.com/haileyok/typesafe-client/tree/4be2f97a92d8b1186c677273d44b4d85e89a2ec7). AI-assisted README and LICENSE inspection; install/live paths not executed.
