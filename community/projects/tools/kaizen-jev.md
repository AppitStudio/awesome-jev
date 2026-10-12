# Kaizen.Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

.NET 11 client for the TypeSafe Jev API: typed noul, choice and score questions about a piece of state (NuGet `KaizenIO.Jev`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kaizen-hq/Kaizen.Jev) |
| Maintainer | [kaizen-hq](https://github.com/kaizen-hq). Independently curated. |
| Format | NuGet package |
| Requirements | .NET 11; TypeSafe key. |
| License | [MIT](https://github.com/kaizen-hq/Kaizen.Jev/blob/6da87a229f2f7359f4be18a88da32fe95595de8d/LICENSE) |
| Jev evidence | [`src/Kaizen.Jev/JevClient.cs`](https://github.com/kaizen-hq/Kaizen.Jev/blob/6da87a229f2f7359f4be18a88da32fe95595de8d/src/Kaizen.Jev/JevClient.cs) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Call Jev from C# with typed answers.
- Mismatch: community client; check API changes against docs.typesafe.ai.

## How it works

`JevClient` builds System One requests and maps responses to typed answer objects. (Summarized from the upstream [README](https://github.com/kaizen-hq/Kaizen.Jev/blob/6da87a229f2f7359f4be18a88da32fe95595de8d/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `dotnet add package KaizenIO.Jev`.

## Limits and data handling

State you send goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 6da87a229f2f](https://github.com/kaizen-hq/Kaizen.Jev/tree/6da87a229f2f7359f4be18a88da32fe95595de8d). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
