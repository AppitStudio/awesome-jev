# TypeSafe.AI (.NET SDK)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial .NET client (`TypeSafe.AI`) for TypeSafe System One: typed Noul/Choice/Score questions, DI registration, HTTP resilience, and OpenTelemetry activity tags—distinct from the separately listed TypeSafeAI.Net package.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/typesafe-sdk-csharp/typesafe-sdk) |
| Maintainer | [typesafe-sdk-csharp](https://github.com/typesafe-sdk-csharp). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | .NET library NuGet **TypeSafe.AI** (reviewed tag **v1.0.0**); sample `TypeSafe.Sample.HelloJav`. |
| Requirements | .NET 10 per upstream badges/global.json; live calls need `TYPESAFE_API_KEY` (or configured options). Default model `jev-latest`; base URL `https://api.typesafe.ai/`. |
| License | [MIT](https://github.com/typesafe-sdk-csharp/typesafe-sdk/blob/143f5c043fd32cec5f79433c382d7bdeb143de42/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and upstream CI inspected; .NET SDK was not installed on the Linux review host. Live TypeSafe calls were not run. Distinct from [TypeSafeAI.Net](typesafeai-net.md) (`Hawxy/TypeSafeAI.Net`). |

## When to use

Use it when you want a NativeAOT-oriented, DI-friendly .NET client that posts to `/v1/systemone` with structured questions and typed answer decoding. Prefer [TypeSafeAI.Net](typesafeai-net.md) if you specifically need that package’s Microsoft.Extensions.AI adapters and samples; compare APIs before mixing both.

## How it works

[`TypeSafeClient`](https://github.com/typesafe-sdk-csharp/typesafe-sdk/blob/143f5c043fd32cec5f79433c382d7bdeb143de42/src/TypeSafe.AI/TypeSafeClient.cs) posts `SystemOneRequest` JSON to `v1/systemone` (default base `https://api.typesafe.ai/`). [`QuestionBuilder`](https://github.com/typesafe-sdk-csharp/typesafe-sdk/blob/143f5c043fd32cec5f79433c382d7bdeb143de42/src/TypeSafe.AI/QuestionBuilder.cs) / [`SystemOne`](https://github.com/typesafe-sdk-csharp/typesafe-sdk/blob/143f5c043fd32cec5f79433c382d7bdeb143de42/src/TypeSafe.AI/SystemOne.cs) model Noul, Choice, and Score questions. Resilience uses `Microsoft.Extensions.Http.Resilience`; telemetry uses `ActivitySource` tags for model/tokens/request id without attaching provider bodies or credentials.

## Get started

```sh
dotnet add package TypeSafe.AI
# or pin the reviewed source:
git clone https://github.com/typesafe-sdk-csharp/typesafe-sdk.git
cd typesafe-sdk
git checkout 143f5c043fd32cec5f79433c382d7bdeb143de42
# on a machine with the .NET 10 SDK:
dotnet test
```

Configure the API key through DI (`AddTypeSafeClient`) or `TypeSafeClientOptions`; do not commit secrets. Live `SystemOneAsync` calls incur TypeSafe usage.

## Examples and demos

- Sample: [`samples/TypeSafe.Sample.HelloJav`](https://github.com/typesafe-sdk-csharp/typesafe-sdk/tree/143f5c043fd32cec5f79433c382d7bdeb143de42/samples/TypeSafe.Sample.HelloJav).
- Unit/contract tests under [`tests/TypeSafe.AI.Tests`](https://github.com/typesafe-sdk-csharp/typesafe-sdk/tree/143f5c043fd32cec5f79433c382d7bdeb143de42/tests/TypeSafe.AI.Tests) (HTTP fakes; no live key required).

## Limits and data handling

Request state and questions leave the host on live calls. Default model alias `jev-latest` can move. This listing does not compare performance or feature completeness against TypeSafeAI.Net. Preview packages may also publish to GitHub Packages—prefer NuGet.org stable releases unless you intentionally consume previews.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 143f5c0](https://github.com/typesafe-sdk-csharp/typesafe-sdk/tree/143f5c043fd32cec5f79433c382d7bdeb143de42) / tag **v1.0.0**: MIT. AI-assisted source review of `TypeSafeClient`, `SystemOne`, options, README, and LICENSE. Review host lacked `dotnet`; upstream **CI & Beta Preview** and **Release GA** workflows succeeded on this SHA. No live TypeSafe calls.

Related: [TypeSafeAI.Net](typesafeai-net.md), [TypeSafe (Swift)](typesafe-swift.md), [typesafe-api (Rust)](typesafe-api-rs.md).
