# taurus-jev-sdk-go

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial stdlib-only Go client for TypeSafe System One / Jev: validated responses, masked credentials, redirect-safe bearer tokens, bounded retries. Distinct from jmelahman/typesafe-sdk-go.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KKloudTarus/taurus-jev-sdk-go) |
| Maintainer | [KKloudTarus](https://github.com/KKloudTarus). Independently curated. |
| Format | Go module (`package jev`); Go 1.22+; zero third-party deps. |
| Requirements | Go 1.22+; `TYPESAFE_API_KEY` (or documented env) for live calls. |
| License | [MIT](https://github.com/KKloudTarus/taurus-jev-sdk-go/blob/78d0cfc134548bbd32a9364469a1bdd3ba6d83ea/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use when you want a **hard-failing, credential-safe Go client** for Noul/Choice/Score rather than coercing truncated JSON.

## How it works

`client.SystemOne` rejects degraded bodies; masks keys in errors/logs; does not re-send bearer tokens on redirects; clamps retry-after.

## Get started

```sh
go get github.com/KKloudTarus/taurus-jev-sdk-go@78d0cfc134548bbd32a9364469a1bdd3ba6d83ea
# or clone tip 78d0cfc134548bbd32a9364469a1bdd3ba6d83ea
```

## Examples and demos

- README snippet: `response.NoulOf("billing")`.
- Forward-compatible `RawQuestion` / `Answer.Raw`.

## Limits and data handling

Unofficial—not maintained by TypeSafe. Distinct from [typesafe-sdk-go (jmelahman)](typesafe-sdk-go-jmelahman.md).

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 78d0cfc](https://github.com/KKloudTarus/taurus-jev-sdk-go/tree/78d0cfc134548bbd32a9364469a1bdd3ba6d83ea). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [typesafe-sdk-go (jmelahman)](typesafe-sdk-go-jmelahman.md), [Mechanical Jev](mechanical-jev.md).
