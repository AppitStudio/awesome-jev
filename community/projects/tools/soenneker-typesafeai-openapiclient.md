# Soenneker.TypesafeAi.OpenApiClient (generated .NET client for the TypeSafe API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

.NET client generated from TypeSafe's OpenAPI document, published on NuGet, covering model listing and `POST /v1/systemone`. Part of the maintainer's large family of generated API clients.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/soenneker/soenneker.typesafeai.openapiclient) |
| Maintainer | [soenneker](https://github.com/soenneker). Independently curated. |
| Format | NuGet package (`Soenneker.TypesafeAi.OpenApiClient`) |
| Requirements | .NET; a TypeSafe key. |
| License | [MIT](https://github.com/soenneker/soenneker.typesafeai.openapiclient/blob/a79e8d1574358f0ad351743afb115722d064a697/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Soenneker.TypesafeAi.OpenApiClient/TypesafeAiOpenApiClient.cs`](https://github.com/soenneker/soenneker.typesafeai.openapiclient/blob/a79e8d1574358f0ad351743afb115722d064a697/src/Soenneker.TypesafeAi.OpenApiClient/TypesafeAiOpenApiClient.cs) at the pinned commit. |

## When to use

- Call TypeSafe from C# with generated request/response types.
- Mismatch: generated code with little documentation; no typed-question helpers.

## How it works

`TypesafeAiOpenApiClient.cs` and the `V1` request builders are generated (Kiota-style) from `openapi.fixed.json`, whose server is `https://api.typesafe.ai`. Integration evidence: [`src/Soenneker.TypesafeAi.OpenApiClient/TypesafeAiOpenApiClient.cs`](https://github.com/soenneker/soenneker.typesafeai.openapiclient/blob/a79e8d1574358f0ad351743afb115722d064a697/src/Soenneker.TypesafeAi.OpenApiClient/TypesafeAiOpenApiClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package Soenneker.TypesafeAi.OpenApiClient
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- NuGet: [www.nuget.org/packages/soenneker.typesafeai.openapiclient/](https://www.nuget.org/packages/soenneker.typesafeai.openapiclient/)

## Limits and data handling

Requests go to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit a79e8d157435](https://github.com/soenneker/soenneker.typesafeai.openapiclient/tree/a79e8d1574358f0ad351743afb115722d064a697). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
