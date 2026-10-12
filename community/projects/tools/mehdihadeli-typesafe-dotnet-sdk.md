# TypeSafe .NET SDK (mehdihadeli)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community-maintained C# SDK for the TypeSafe System One API: send text or JSON state with named Noul, Choice and Score questions and read typed answers, probabilities and model metadata in .NET.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mehdihadeli/typesafe-dotnet-sdk) |
| Maintainer | [mehdihadeli](https://github.com/mehdihadeli). Independently curated. |
| Format | .NET library (netstandard2.0 / net10.0); project reference |
| Requirements | .NET 10 SDK to build; a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/mehdihadeli/typesafe-dotnet-sdk/blob/e4bacc10b6ada3198ce9c1d0f8bbe5babb86c651/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Call Jev from ASP.NET or worker services with typed request/response models.
- Supply your own `HttpClient` for resilience and DI integration.
- Mismatch: Not published under its own NuGet ID yet (the configured `Typesafe.Sdk` ID belongs to a different package), so reference the checkout. Several other .NET clients are listed; pick by API surface.

## How it works

`TypeSafeClient.SystemOneAsync` posts state and questions to `v1/systemone` (default base URL `https://api.typesafe.ai/`) and deserializes answers into C# models; thresholds and actions stay in your code. Jev integration: [`src/TypeSafeClient.cs`](https://github.com/mehdihadeli/typesafe-dotnet-sdk/blob/e4bacc10b6ada3198ce9c1d0f8bbe5babb86c651/src/TypeSafeClient.cs). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/mehdihadeli/typesafe-dotnet-sdk.git
# add a ProjectReference to src/Typesafe.Sdk.csproj, then:
export TYPESAFE_API_KEY="..."
```

## Limits and data handling

Sends state to the configured endpoint; does not run models locally. Distinct from other .NET clients (Jev.DotNet, jev-dotnet, CMaintz jev-dotnet, typesafe-sdk-csharp). Not built on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit e4bacc10b6ad](https://github.com/mehdihadeli/typesafe-dotnet-sdk/tree/e4bacc10b6ada3198ce9c1d0f8bbe5babb86c651). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
