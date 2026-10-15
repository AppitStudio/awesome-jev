# ElBruno.AI.Decisions

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

.NET 10 decision SDK with one API for Choose, Score and Assess across Microsoft-Decision-1 on Foundry, local Ollama models and a native Jev package, plus Microsoft.Extensions.AI routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/elbruno/ElBruno.AI.Decisions) |
| Maintainer | [elbruno](https://github.com/elbruno). Independently curated. |
| Format | .NET 10 NuGet packages (`ElBruno.AI.Decisions`, `ElBruno.AI.Decisions.Jev`) |
| Requirements | .NET 10 SDK; TypeSafe API key for the Jev provider. |
| License | [MIT](https://github.com/elbruno/ElBruno.AI.Decisions/blob/bd8332e3df799b21b54183ecdb24fa4ab240d92b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/ElBruno.AI.Decisions.Jev/JevClient.cs`](https://github.com/elbruno/ElBruno.AI.Decisions/blob/bd8332e3df799b21b54183ecdb24fa4ab240d92b/src/ElBruno.AI.Decisions.Jev/JevClient.cs) at the pinned commit. |

## When to use

- Write classification, routing and rubric scoring once and switch between Jev, Foundry and Ollama.
- Use Jev from .NET apps through dependency injection and Microsoft.Extensions.AI.
- Mismatch: multi-provider abstraction; Jev is one of three backends.

## How it works

A provider-neutral `IDecisionClient` returns probability distributions; the `.Jev` package implements it over the TypeSafe System One API with its own models, serialization and transport. Samples run offline against labeled synthetic fixtures. Integration evidence: [`src/ElBruno.AI.Decisions.Jev/JevClient.cs`](https://github.com/elbruno/ElBruno.AI.Decisions/blob/bd8332e3df799b21b54183ecdb24fa4ab240d92b/src/ElBruno.AI.Decisions.Jev/JevClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package ElBruno.AI.Decisions.Jev
dotnet run --project samples/01-HelloChoice -- --offline
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Introduction and quickstarts: `docs/blog/introducing-elbruno-ai-decisions.md`.

## Limits and data handling

Requests go to the provider you configure (TypeSafe for Jev) and are billed to that account; `--offline` samples make no network calls.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit bd8332e3df79](https://github.com/elbruno/ElBruno.AI.Decisions/tree/bd8332e3df799b21b54183ecdb24fa4ab240d92b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
