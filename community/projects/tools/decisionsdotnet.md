# DecisionsDotNet (C# client for Jev through TypeSafe, OpenRouter's Decisions API or OpenAI's Decisions API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Type-safe .NET 10 client for TypeSafe's Jev models with typed `noul`, `choice` and `score` questions, batching, image inputs and dependency-injection registration; the same request types also run through OpenRouter's or OpenAI's Decisions API, and a companion package handles OpenRouter extraction models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HillPhelmuth/JevDotNet) |
| Maintainer | [HillPhelmuth](https://github.com/HillPhelmuth). Independently curated. |
| Format | NuGet prerelease package `DecisionsDotNet` (C#, .NET 10) |
| Requirements | .NET 10 SDK and `TYPESAFE_API_KEY` (or `OPENROUTER_API_KEY` / an OpenAI key for those clients). |
| License | [MIT (declared in the package metadata; no LICENSE file in the repository)](https://github.com/HillPhelmuth/JevDotNet/blob/d2953a9cb34bdacbea69d37fb631746f6ccd60ad/JevDotNet/JevDotNet.csproj) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`JevDotNet/JevClient.cs`](https://github.com/HillPhelmuth/JevDotNet/blob/d2953a9cb34bdacbea69d37fb631746f6ccd60ad/JevDotNet/JevClient.cs) at the pinned commit. |

## When to use

- Call Jev from C# services with typed questions and answers instead of hand-written JSON.
- Switch between TypeSafe direct, OpenRouter and OpenAI Decisions without changing request code.
- Mismatch: if you need a stable 1.0 API; this is a preview package.

## How it works

`JevDotNet/JevClient.cs` and `DecisionsHttp.cs` send requests to `https://api.typesafe.ai/v1/systemone` with bearer auth and validate responses against the typed question set (`JevResponseValidator.cs`); `OpenRouterDecisionsClient.cs` and `OpenAIDecisionsClient.cs` map the same request types to those providers. The base URL can point at a local server that implements the Jev contract. The package is a 0.x preview; the xUnit contract tests use fake HTTP handlers. Integration evidence: [`JevDotNet/JevClient.cs`](https://github.com/HillPhelmuth/JevDotNet/blob/d2953a9cb34bdacbea69d37fb631746f6ccd60ad/JevDotNet/JevClient.cs).

## Get started

Add the prerelease package, set your key, then build a `DecisionsRequest` and call `JevClient.FromEnvironment()`.

```sh
dotnet add package DecisionsDotNet --prerelease
export TYPESAFE_API_KEY="your-key"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README quick starts: [github.com/HillPhelmuth/JevDotNet/blob/d2953a9cb34bdacbea69d37fb631746f6ccd60ad/README.md](https://github.com/HillPhelmuth/JevDotNet/blob/d2953a9cb34bdacbea69d37fb631746f6ccd60ad/README.md)
- Demo project: [github.com/HillPhelmuth/JevDotNet/tree/d2953a9cb34bdacbea69d37fb631746f6ccd60ad/JevDotNet.Demo](https://github.com/HillPhelmuth/JevDotNet/tree/d2953a9cb34bdacbea69d37fb631746f6ccd60ad/JevDotNet.Demo)
- NuGet package: [www.nuget.org/packages/DecisionsDotNet](https://www.nuget.org/packages/DecisionsDotNet)

## Limits and data handling

States and questions go to the provider you choose on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit d2953a9cb34b](https://github.com/HillPhelmuth/JevDotNet/tree/d2953a9cb34bdacbea69d37fb631746f6ccd60ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
