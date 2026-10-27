# TypeSafe.AI.Sdk for .NET by hardkoded (community port of the TypeSafe JavaScript SDK)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community .NET client for TypeSafe's System One API, ported from `@typesafe-ai/sdk` and maintained by Darío Kondratiuk (hardkoded), with behaviour aligned to the JavaScript SDK: typed questions and answers, NuGet package `TypeSafe.AI.Sdk`, targets net10.0 and netstandard2.0, with a documentation site written for agents. Not an official TypeSafe product.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hardkoded/typesafe-sdk-dotnet) |
| Maintainer | [hardkoded](https://github.com/hardkoded). Independently curated. |
| Format | .NET library (NuGet) |
| Requirements | .NET 10 SDK to build (netstandard2.0 supported); a TypeSafe API key. |
| License | [MIT](https://github.com/hardkoded/typesafe-sdk-dotnet/blob/be97f59b70d71e7815a62f64c791e2a3f1811230/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/hardkoded/status/2115067319009341536)). |
| Jev evidence | [`src/TypeSafe.AI.Sdk/TypeSafeClient.cs`](https://github.com/hardkoded/typesafe-sdk-dotnet/blob/be97f59b70d71e7815a62f64c791e2a3f1811230/src/TypeSafe.AI.Sdk/TypeSafeClient.cs) at the pinned commit. |

## When to use

- Call Jev from C# or other .NET apps with typed questions.
- Mismatch: one of several community .NET clients; unofficial.

## How it works

`src/TypeSafe.AI.Sdk/TypeSafeClient.cs` posts to `https://api.typesafe.ai/v1/systemone` with your `TYPESAFE_API_KEY`. Integration evidence: [`src/TypeSafe.AI.Sdk/TypeSafeClient.cs`](https://github.com/hardkoded/typesafe-sdk-dotnet/blob/be97f59b70d71e7815a62f64c791e2a3f1811230/src/TypeSafe.AI.Sdk/TypeSafeClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package TypeSafe.AI.Sdk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [hardkoded.github.io/typesafe-sdk-dotnet/](https://hardkoded.github.io/typesafe-sdk-dotnet/)
- NuGet: [www.nuget.org/packages/TypeSafe.AI.Sdk](https://www.nuget.org/packages/TypeSafe.AI.Sdk)

## Limits and data handling

Questions and state go to TypeSafe. Discovered on X from the author's post.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit be97f59b70d7](https://github.com/hardkoded/typesafe-sdk-dotnet/tree/be97f59b70d71e7815a62f64c791e2a3f1811230). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
