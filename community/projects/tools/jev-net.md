# Jev.Net

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community .NET client for the TypeSafe System One API with a single dependency, built-in retries, and Native AOT compatibility.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brightshore/jev-net) |
| Maintainer | [brightshore](https://github.com/brightshore). Independently curated. |
| Format | .NET library (NuGet `Jev.Net`) |
| Requirements | .NET 8 or 10, TypeSafe API key. |
| License | [MIT](https://github.com/brightshore/jev-net/blob/59275dd1ad47882b9d2135ed363c2ea3583a711a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Jev.Net/TypeSafeClient.cs`](https://github.com/brightshore/jev-net/blob/59275dd1ad47882b9d2135ed363c2ea3583a711a/src/Jev.Net/TypeSafeClient.cs) at the pinned commit. |

## When to use

- Call Jev from a C# service, CLI or desktop app.
- Mismatch: community package, not affiliated with TypeSafe.

## How it works

Typed questions/answers mirror the official Python SDK; retries, backoff, Retry-After and per-attempt timeouts are implemented in the library. Integration evidence: [`src/Jev.Net/TypeSafeClient.cs`](https://github.com/brightshore/jev-net/blob/59275dd1ad47882b9d2135ed363c2ea3583a711a/src/Jev.Net/TypeSafeClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package Jev.Net
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Samples: `samples/`.
- Tests: `tests/Jev.Net.Tests/`.

## Limits and data handling

Requests go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 59275dd1ad47](https://github.com/brightshore/jev-net/tree/59275dd1ad47882b9d2135ed363c2ea3583a711a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
