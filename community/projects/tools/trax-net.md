# Trax .NET

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Headless .NET web framework that records every run in Postgres; its `Trax.Effect.Decisions.SystemOne` package adds System One decisions pinned to models such as `jev-1.13.0`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TraxSharp/Trax) |
| Maintainer | [TraxSharp](https://github.com/TraxSharp). Independently curated. |
| Format | .NET framework (NuGet packages) |
| Requirements | .NET; Postgres; TypeSafe API key for the System One decisions package. |
| License | [MIT](https://github.com/TraxSharp/Trax/blob/a963d707972e175771952a40282c4b2efa368424/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Trax.Effect/src/Trax.Effect.Decisions.SystemOne/SystemOneDecider.cs`](https://github.com/TraxSharp/Trax/blob/a963d707972e175771952a40282c4b2efa368424/Trax.Effect/src/Trax.Effect.Decisions.SystemOne/SystemOneDecider.cs) at the pinned commit. |

## When to use

- Add typed decisions to Trax trains (chains of junctions) with run recording.
- Point the decider at TypeSafe Jev or a self-hosted compatible server.
- Mismatch: decisions are one optional package of a broader framework.

## How it works

The SystemOne decider sends junction state with typed questions to the configured endpoint (TypeSafe for Jev) using a pinned model and a confidence threshold, and records the outcome with the run. Integration evidence: [`Trax.Effect/src/Trax.Effect.Decisions.SystemOne/SystemOneDecider.cs`](https://github.com/TraxSharp/Trax/blob/a963d707972e175771952a40282c4b2efa368424/Trax.Effect/src/Trax.Effect.Decisions.SystemOne/SystemOneDecider.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet new install Trax.Samples.Templates
dotnet new trax-hub -n MyApp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [traxsharp.net/docs](https://traxsharp.net/docs)

## Limits and data handling

Decision state goes to the configured System One endpoint and is billed to your key; run records stay in your Postgres.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit a963d707972e](https://github.com/TraxSharp/Trax/tree/a963d707972e175771952a40282c4b2efa368424). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
