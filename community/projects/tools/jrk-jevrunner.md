# JRK.JevRunner (.NET client for Jev with source-generated typed questions)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

.NET client for Jev and the TypeSafe System One API: submit application state and named questions and get typed responses, with source generators that turn your query classes into requests, plus an image package.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jeppevammenkristensen/jev-runner) |
| Maintainer | [jeppevammenkristensen](https://github.com/jeppevammenkristensen). Independently curated. |
| Format | NuGet package (C#) |
| Requirements | .NET 11 or later; a TypeSafe API key. |
| License | [MIT](https://github.com/jeppevammenkristensen/jev-runner/blob/8b82a16ecfc6d52b5943f987645d6e83968f1143/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`JRK.JevRunner/JevRunner.cs`](https://github.com/jeppevammenkristensen/jev-runner/blob/8b82a16ecfc6d52b5943f987645d6e83968f1143/JRK.JevRunner/JevRunner.cs) at the pinned commit. |

## When to use

- Call Jev from C# services with typed answers instead of raw JSON.
- Generate request code from your own query types.
- Mismatch: needs .NET 11; early versions (0.5.0 on NuGet at review).

## How it works

`JevRunner.cs` posts requests to `https://api.typesafe.ai/v1/systemone`; the source generators create the questions and response accessors from attributed classes. Integration evidence: [`JRK.JevRunner/JevRunner.cs`](https://github.com/jeppevammenkristensen/jev-runner/blob/8b82a16ecfc6d52b5943f987645d6e83968f1143/JRK.JevRunner/JevRunner.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package JRK.JevRunner
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- NuGet: [www.nuget.org/packages/JRK.JevRunner](https://www.nuget.org/packages/JRK.JevRunner)
- README: [github.com/jeppevammenkristensen/jev-runner#readme](https://github.com/jeppevammenkristensen/jev-runner#readme)

## Limits and data handling

Application state you submit is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 8b82a16ecfc6](https://github.com/jeppevammenkristensen/jev-runner/tree/8b82a16ecfc6d52b5943f987645d6e83968f1143). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
