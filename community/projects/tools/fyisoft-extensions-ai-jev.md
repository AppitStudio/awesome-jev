# FYIsoft.Extensions.AI.Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

.NET `Microsoft.Extensions.AI` provider SDKs from FYIsoft, including a typed `JevClient` port of `@typesafe-ai/sdk` v0.6.0 and an `IChatClient` adapter for structured judgments, with a support-desk sample where Jev triages tickets and reviews Claude drafts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FYIsoft/FYIsoft.Extensions.AI.Providers) |
| Maintainer | [FYIsoft](https://github.com/FYIsoft). Independently curated. |
| Format | .NET libraries (NuGet) + sample |
| Requirements | Recent .NET SDK; TypeSafe API key. |
| License | [MIT](https://github.com/FYIsoft/FYIsoft.Extensions.AI.Providers/blob/7912356dda9c409005491d33f52a803a4dae37f1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/FYIsoft.Extensions.AI.Jev/JevClient.cs`](https://github.com/FYIsoft/FYIsoft.Extensions.AI.Providers/blob/7912356dda9c409005491d33f52a803a4dae37f1/src/FYIsoft.Extensions.AI.Jev/JevClient.cs) at the pinned commit. |

## When to use

- Call Jev from C# with typed results.
- Use Jev through the `Microsoft.Extensions.AI` abstractions.
- Mismatch: unofficial port; check parity with the official SDK.

## How it works

`JevClient.cs` implements the System One request and typed answers; `JevChatClient.cs` adapts it to `IChatClient`. The SupportDeskSample chains Jev triage, a Claude reply draft, and a Jev review. Integration evidence: [`src/FYIsoft.Extensions.AI.Jev/JevClient.cs`](https://github.com/FYIsoft/FYIsoft.Extensions.AI.Providers/blob/7912356dda9c409005491d33f52a803a4dae37f1/src/FYIsoft.Extensions.AI.Jev/JevClient.cs).

## Get started

From the upstream README: add the package or project reference, set your TypeSafe key (user secrets or environment), then create a `JevClient`.

```sh
dotnet user-secrets set "TypeSafe:ApiKey" "<your key>"
dotnet run --project samples/SupportDeskSample
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- samples/SupportDeskSample

## Limits and data handling

State and questions go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 7912356dda9c](https://github.com/FYIsoft/FYIsoft.Extensions.AI.Providers/tree/7912356dda9c409005491d33f52a803a4dae37f1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
