# DecisionKit

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Keep a .NET application's decision model independent of the decision provider: the domain package knows nothing about Jev, and the Jev protocol lives in a separate package behind one interface.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iamjonatha/decisionkit-dotnet) |
| Maintainer | [Jonatha Panni](https://github.com/iamjonatha). Independent community project, not an official TypeSafe client. Submitted by its author; no commercial relationship with TypeSafe. |
| Format | Four C# NuGet packages: domain, Jev provider, DI/configuration, test doubles. |
| Requirements | `net8.0` or `net10.0`; samples target `net10.0`. Live calls need a TypeSafe key supplied as `Jev:ApiKey` (environment form `Jev__ApiKey`). |
| License | [MIT](https://github.com/iamjonatha/decisionkit-dotnet/blob/main/LICENSE). |

## When to use

- You want the application's questions and answers expressed in domain terms, with the provider swappable without touching that model.
- You need Choice, Score, and Noul answers in .NET and want distinguishable failures — validation, authentication, transport, timeout, cancellation, rate limiting — rather than one exception type.
- You test application logic that depends on a decision and want no HTTP in those tests.

It is not a good fit when you want the shortest possible path to a single API call: a one-file client is smaller than four packages. The split pays off when the decision model outlives the provider choice.

## How it works

The application builds typed questions (`ChoiceQuestion<T>`, `ScoreQuestion`, `ProbabilityQuestion`) and asks them through `IDecisionProvider`. The question instance is the key that reads its own answer back, so the answer keeps its type without a cast. `DecisionKit.Jev` maps those questions to the Jev names `choice`, `score` and `noul`, posts them to `v1/systemone`, and maps the reply back. Question types the domain does not model are carried through as `UnknownQuestion` with the provider's own type name rather than dropped, and Jev's confidence, legend and probability data is preserved as answer metadata.

Policy stays in application code: the [ticket-triage sample](https://github.com/iamjonatha/decisionkit-dotnet/blob/v0.1.0/samples/DependencyInjection/TicketTriage.cs) reads the Score, normalizes it, and decides at a threshold of 0.8 that a human should look at the ticket. The model does not make that call.

Retrying is off by default: Jev has no idempotency mechanism, so a repeated call is a second billed evaluation that may answer differently. Enabling it is a deliberate configuration step. The [wire-protocol reference](https://github.com/iamjonatha/decisionkit-dotnet/blob/v0.1.0/docs/providers/jev-protocol.md) records the payload, header precedence, and retry rules the transport follows.

## Get started

From an existing .NET project:

```sh
dotnet add package DecisionKit.Extensions
```

Register the provider and bind its configuration:

```csharp
builder.Services
    .AddDecisionKit()
    .AddJevProvider(builder.Configuration.GetSection("Jev"));
```

The key is never read from an implicit variable — it comes from the bound configuration section, so supply it through your own secret store or `Jev__ApiKey`. Configuration is validated while the host starts rather than on the first request.

To see the model without any credential or network access, clone the repository and run the offline sample with the .NET 10 SDK:

```sh
git clone https://github.com/iamjonatha/decisionkit-dotnet.git
cd decisionkit-dotnet
dotnet run --project samples/Basic
```

That sample answers from `DeterministicDecisionProvider`, which derives answers from a hash of the request, so it prints typed choice, score, multi-question, unknown-question, error-handling and cancellation walkthroughs and contacts nothing.

The `DependencyInjection` sample is the live path and needs a key; running it sends its ticket text to the TypeSafe API and can incur charges:

```sh
export Jev__ApiKey="<your-api-key>"
dotnet run --project samples/DependencyInjection
curl -s localhost:5000/tickets/triage -H 'content-type: application/json' \
  -d '{"text":"I have been charged twice for the same month."}'
```

## Examples and demos

- [Basic](https://github.com/iamjonatha/decisionkit-dotnet/tree/v0.1.0/samples/Basic) — typed questions, error categories and cancellation, offline.
- [DependencyInjection](https://github.com/iamjonatha/decisionkit-dotnet/tree/v0.1.0/samples/DependencyInjection) — ASP.NET Core minimal API, `AddJevProvider`, failures mapped to `ProblemDetails`. Needs a key.
- [Testing](https://github.com/iamjonatha/decisionkit-dotnet/tree/v0.1.0/samples/Testing) — `FakeDecisionProvider` and `DecisionAssert` against application logic, offline.
- [Resilience](https://github.com/iamjonatha/decisionkit-dotnet/tree/v0.1.0/samples/Resilience) — how the retry policy computes backoff, honours `Retry-After` and classifies failures, offline.
- [CustomProvider](https://github.com/iamjonatha/decisionkit-dotnet/tree/v0.1.0/samples/CustomProvider) — implementing `IDecisionProvider` without referencing the Jev package, offline.
- [Aot](https://github.com/iamjonatha/decisionkit-dotnet/tree/v0.1.0/samples/Aot) — Native AOT publish; needs a native toolchain, no key.

There is no hosted demo.

## Limits and data handling

The state and questions you pass are sent to the configured Jev endpoint when you use the Jev provider; nothing is sent by the domain, testing or custom-provider paths. API keys are not logged, not serialized into diagnostics and not included in exception messages; request and response bodies are not logged by default, and raw protocol capture is opt-in. The 0.8 escalation threshold in the sample is illustrative — thresholds need evaluation on your own data before they mean anything.

The project is pre-release: the public API is unstable until 1.0.0, and the [roadmap](https://github.com/iamjonatha/decisionkit-dotnet/blob/v0.1.0/docs/roadmap.md) records what is implemented. Jev answers are model output and must not stand in for authorization or permission checks. No accuracy, latency or cost claim is made: the project measures nothing about the quality of Jev's answers.

## Review and maintenance

Reviewed by the project's own author on 2026-09-29 at [357aa84](https://github.com/iamjonatha/decisionkit-dotnet/tree/357aa849a3f714fda2eada964b6cf5ba6cd45e84), released as [v0.1.0](https://github.com/iamjonatha/decisionkit-dotnet/releases/tag/v0.1.0) on NuGet. `dotnet test --solution DecisionKit.slnx -c Release` ran 1,096 tests across `net8.0` and `net10.0` with no failures; the suite uses stubbed HTTP handlers and a controlled `TimeProvider`, so it establishes code behavior only. Live inference against the TypeSafe API, the Native AOT publish on a non-Windows runtime, and answer quality were not exercised in this check. Public CI runs the same build and test on every push with warnings treated as errors.

The project was substantially written with AI assistance; its author reviewed and is responsible for the result.

Related: [TypeSafeAI.Net](typesafeai-net.md) and [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md) cover the same runtime with a single-client design, where DecisionKit keeps the provider behind a separate package.
