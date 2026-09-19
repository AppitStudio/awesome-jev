# TypeSafeAI.Net

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Use Jev from a .NET application with typed questions and answers, dependency injection, and optional Microsoft.Extensions.AI adapters.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Hawxy/TypeSafeAI.Net) |
| Maintainer | [Hawxy](https://github.com/Hawxy). Independent community SDK, not an official TypeSafe client. |
| Format | C# client library and optional integration package. |
| Requirements | The library targets .NET 8 and .NET 10; repository samples target .NET 10. Live calls need a TypeSafe key. |
| License | [Apache-2.0](https://github.com/Hawxy/TypeSafeAI.Net/blob/main/LICENSE). |

## When to use

- Your application already uses .NET and needs Choice, Score, or Noul judgments.
- You want typed question handles and normal .NET dependency injection.
- You want to integrate judgments into a Microsoft.Extensions.AI routing or evaluation pipeline.

The client provides integration primitives. Your application still defines the questions, policy, and downstream actions.

## How it works

Build a `QuestionSet`, retain each question's handle, call `SystemOneAsync`, and retrieve typed results using those handles. The optional `TypeSafeAI.Extensions.AI` package adds adapters for chat routing, screening, tools, and evaluation. It does not turn Jev into a text-generating chat model. The [upstream usage guide](https://github.com/Hawxy/TypeSafeAI.Net#readme) covers both typed and dictionary-based access.

## Get started

From your existing .NET project:

```sh
dotnet add package TypeSafeAI
```

Pass your key through your application's private configuration to the client or its DI options. Do not assume the library automatically reads `TYPESAFE_API_KEY`; the sample programs explicitly do so. See the upstream [configuration](https://github.com/Hawxy/TypeSafeAI.Net#configuration) and [dependency injection](https://github.com/Hawxy/TypeSafeAI.Net#dependency-injection) examples.

For a complete learning example, clone the repository and run TicketTriage with the .NET 10 SDK:

```sh
git clone https://github.com/Hawxy/TypeSafeAI.Net.git
cd TypeSafeAI.Net
dotnet run --project samples/TicketTriage
```

With no `TYPESAFE_API_KEY` set, that sample prints the number of constructed questions and exits without inference. If a key is present, the same command sends its sample ticket to TypeSafe and can incur charges. It prints decisions; it does not actually assign tickets. This behavior is visible in the [sample source](https://github.com/Hawxy/TypeSafeAI.Net/blob/7f014c92ec4d0cf89896989eb7cd20a0e033e621/samples/TicketTriage/Program.cs).

## Examples and demos

- [TicketTriage](https://github.com/Hawxy/TypeSafeAI.Net/tree/main/samples/TicketTriage) — typed questions and confidence-based routing.
- [GuardedChat](https://github.com/Hawxy/TypeSafeAI.Net/tree/main/samples/GuardedChat) — adapters around a stand-in chat client.
- [EvaluationReport](https://github.com/Hawxy/TypeSafeAI.Net/tree/main/samples/EvaluationReport) — integration with a reporting pipeline.
- [Microsoft.Extensions.AI integration](https://github.com/Hawxy/TypeSafeAI.Net#microsoftextensionsai) — choose only the adapters your app needs.

## Limits and data handling

State and questions are sent to the configured API endpoint. Configure model versions, timeouts, and retries deliberately. Trace-level diagnostics can include request/response bodies; review logging before sending sensitive state. Model screening and routing do not replace application permissions or security controls. Some integration APIs inherit experimental status from Microsoft.Extensions.AI.

## Review and maintenance

Documentation was rechecked on 2026-09-19 at [7f014c9](https://github.com/Hawxy/TypeSafeAI.Net/tree/7f014c92ec4d0cf89896989eb7cd20a0e033e621). The catalog's 2026-09-18 review passed 89 mocked tests on .NET 10; .NET 8, live inference, and model quality were not evaluated. See [validation scope](../../../docs/validation.md#community-project-checks).

Related: [decision patterns](../../../docs/decision-patterns.md) and the repository's [support-routing example](../../../examples/support-routing/README.md) explain the same policy separation in a smaller Python workflow.
