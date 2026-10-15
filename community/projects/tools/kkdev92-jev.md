# Kkdev92.Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial .NET 10 SDK for Jev that validates a typed decision plan once, reuses the encoded bytes on every call, and returns answers through typed handles only after contract checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kkdev92/jev-dotnet) |
| Maintainer | [kkdev92](https://github.com/kkdev92). Independently curated. |
| Format | .NET 10 NuGet package (prerelease) + DI package |
| Requirements | .NET 10; TypeSafe API key. |
| License | [MIT](https://github.com/kkdev92/jev-dotnet/blob/19d0ac419a460c53f1b5da2d6fec82667d3e568b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Kkdev92.Jev/JevClient.cs`](https://github.com/kkdev92/jev-dotnet/blob/19d0ac419a460c53f1b5da2d6fec82667d3e568b/src/Kkdev92.Jev/JevClient.cs) at the pinned commit. |

## When to use

- Make a decision on every call in a .NET service and fail loudly on malformed answers.
- Wire Jev into ASP.NET Core via `Kkdev92.Jev.DependencyInjection`.
- Mismatch: alpha (`0.1.x`); distinct from the listed ukashanoor/jev-dotnet.

## How it works

A decision plan is declared once and validated/encoded up front; each call sends the cached request to the System One API and checks the response against the contract before typed handles expose answers. Offline fakes follow TypeSafe's OpenAPI document. Integration evidence: [`src/Kkdev92.Jev/JevClient.cs`](https://github.com/kkdev92/jev-dotnet/blob/19d0ac419a460c53f1b5da2d6fec82667d3e568b/src/Kkdev92.Jev/JevClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package Kkdev92.Jev --prerelease
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Integration tests: `src/tests/Kkdev92.Jev.IntegrationTests` (author ran live on 2026-09-25).

## Limits and data handling

Requests go to TypeSafe and are billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 19d0ac419a46](https://github.com/kkdev92/jev-dotnet/tree/19d0ac419a460c53f1b5da2d6fec82667d3e568b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
