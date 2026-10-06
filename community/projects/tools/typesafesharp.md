# TypeSafeSharp (.NET)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial .NET client for TypeSafe's System One API and Jev on `net10.0` and `netstandard2.0`: typed answers, retries and error types modeled on the official SDKs, `EvaluateManyAsync` batching, dependency injection and OpenTelemetry spans; not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sanamhub/typesafe-dotnet) |
| Product homepage | [www.nuget.org](https://www.nuget.org/packages/TypeSafeSharp) |
| Maintainer | [sanamhub](https://github.com/sanamhub). Independently curated. |
| Format | .NET library (NuGet `TypeSafeSharp` 0.1.0 + `TypeSafeSharp.Extensions.DependencyInjection`) |
| Requirements | .NET 10+ or .NET Framework 4.7.2+ (via `netstandard2.0`); `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/sanamhub/typesafe-dotnet/blob/0b014ae3f416f823735a00523d08a1eabfd5f85e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add typed Jev decisions (choice/score/noul) to ASP.NET Core or worker services with DI.
- Run many evaluations concurrently with `EvaluateManyAsync` and trace them with OpenTelemetry.
- Mismatch: async only; no streaming or chat interface (Jev is not a chat model).

## How it works

`TypeSafeClient.SystemOneAsync` posts state and questions to `/v1/systemone` and returns typed answers ([`src/TypeSafeSharp`](https://github.com/sanamhub/typesafe-dotnet/tree/0b014ae3f416f823735a00523d08a1eabfd5f85e/src/TypeSafeSharp)); the DI package registers the client from configuration. Design decisions are recorded as ADRs.

## Get started

Add the package and read the key from the environment:

```sh
dotnet add package TypeSafeSharp
export TYPESAFE_API_KEY=...
# using var client = new TypeSafeClient(new TypeSafeClientOptions());
# var response = await client.SystemOneAsync(state, questions);
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [Samples solution](https://github.com/sanamhub/typesafe-dotnet/tree/0b014ae3f416f823735a00523d08a1eabfd5f85e/sample) and README quick start.
- README *Limits* section (streaming, sync, metrics, retried timeouts).

## Limits and data handling

Unofficial. Retried timeouts can bill twice (upstream note). State is sent to TypeSafe or the configured endpoint. Not compiled on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 0b014ae3f416](https://github.com/sanamhub/typesafe-dotnet/tree/0b014ae3f416f823735a00523d08a1eabfd5f85e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
