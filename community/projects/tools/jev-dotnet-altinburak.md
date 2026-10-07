# Jev.DotNet (altinburak)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial .NET 8+ client for TypeSafe Jev published on NuGet as `Jev.DotNet`: typed Choice/Score/Noul questions and answers, enum-backed choices, retries with backoff, timeouts, logging and `IHttpClientFactory` / ASP.NET Core dependency-injection support.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/altinburak/Jev.DotNet) |
| Product homepage | [www.nuget.org](https://www.nuget.org/packages/Jev.DotNet) |
| Maintainer | [altinburak](https://github.com/altinburak). Independently curated. |
| Format | NuGet package `Jev.DotNet` (0.2.0 at review); community package, not published by TypeSafe |
| Requirements | .NET 8 or later and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/altinburak/Jev.DotNet/blob/321b52de173b89a02334073ae90f1880dc5ac902/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add Jev decisions to an ASP.NET Core app through dependency injection.
- Map Choice answers straight to C# enums.
- Mismatch: a different, independently listed .NET client also exists ([jev-dotnet](jev-dotnet.md)); compare APIs.

## How it works

[`JevClient.cs`](https://github.com/altinburak/Jev.DotNet/blob/321b52de173b89a02334073ae90f1880dc5ac902/src/Jev.DotNet/JevClient.cs) posts a [`SystemOneRequest`](https://github.com/altinburak/Jev.DotNet/blob/321b52de173b89a02334073ae90f1880dc5ac902/src/Jev.DotNet/SystemOneRequest.cs) built from [`Questions.cs`](https://github.com/altinburak/Jev.DotNet/blob/321b52de173b89a02334073ae90f1880dc5ac902/src/Jev.DotNet/Questions.cs) and parses [`Answers.cs`](https://github.com/altinburak/Jev.DotNet/blob/321b52de173b89a02334073ae90f1880dc5ac902/src/Jev.DotNet/Answers.cs); [`Backoff.cs`](https://github.com/altinburak/Jev.DotNet/blob/321b52de173b89a02334073ae90f1880dc5ac902/src/Jev.DotNet/Backoff.cs) handles retries and [`ServiceCollectionExtensions.cs`](https://github.com/altinburak/Jev.DotNet/blob/321b52de173b89a02334073ae90f1880dc5ac902/src/Jev.DotNet/ServiceCollectionExtensions.cs) registers it for DI.

## Get started

Add the package (README *Install*):

```sh
dotnet add package Jev.DotNet
export TYPESAFE_API_KEY=...
# using Jev.DotNet;  using var client = new JevClient();
```

Requests are billed to your TypeSafe key.

## Examples and demos

- README *Quickstart*, *Typed choices with enums* and *ASP.NET Core / dependency injection*.

## Limits and data handling

Community package; not supported by TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 321b52de173b](https://github.com/altinburak/Jev.DotNet/tree/321b52de173b89a02334073ae90f1880dc5ac902). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
