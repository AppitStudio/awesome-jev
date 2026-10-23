# SystemOne for .NET (typed client for System One decision models)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Typed .NET client for System One decision models with noul, choice, score and box questions, one API across self-hosted servers and hosted services including TypeSafe Jev, fallback chains, reusable request templates and a mock for tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/orlys/systemone) |
| Maintainer | [orlys](https://github.com/orlys). Independently curated. |
| Format | .NET library (NuGet: SystemOne.*) |
| Requirements | .NET 10; a TypeSafe API key for hosted Jev. |
| License | [MIT](https://github.com/orlys/systemone/blob/6565813b732d0a0530d254800a3f982373e72913/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/SystemOne.Providers.TypeSafe/TypeSafeProviders.cs`](https://github.com/orlys/systemone/blob/6565813b732d0a0530d254800a3f982373e72913/src/SystemOne.Providers.TypeSafe/TypeSafeProviders.cs) at the pinned commit. |

## When to use

- Call Jev from C# with typed requests and answers.
- Fall back from a self-hosted model to hosted Jev.
- Mismatch: early release (0.1.0 on NuGet as of 2026-10-24).

## How it works

`SystemOne.Providers.TypeSafe` adds `UseTypeSafeAi(apiKey)` (default `jev-latest`); other providers cover OpenRouter (`typesafe/jev-1.14`), Cloudflare, Vercel AI Gateway and local servers. Integration evidence: [`src/SystemOne.Providers.TypeSafe/TypeSafeProviders.cs`](https://github.com/orlys/systemone/blob/6565813b732d0a0530d254800a3f982373e72913/src/SystemOne.Providers.TypeSafe/TypeSafeProviders.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package SystemOne.Providers.TypeSafe
# var systemOne = SystemOne.Providers.UseTypeSafeAi(apiKey);
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quick start and provider table in the README: [github.com/orlys/systemone#readme](https://github.com/orlys/systemone#readme)

## Limits and data handling

Requests go to whichever provider you configure. Independent project, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 6565813b732d](https://github.com/orlys/systemone/tree/6565813b732d0a0530d254800a3f982373e72913). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
