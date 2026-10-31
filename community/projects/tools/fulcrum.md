# Fulcrum (.NET library that turns typed questions and ordered rules into one committed outcome for System One models)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

.NET library: you declare typed questions and ordered rules, Fulcrum asks a System One model, and one committed outcome (reply, page someone, send to a human) is dispatched to a handler that never sees a probability. Backends cover Jev on OpenRouter or any OpenAI-compatible endpoint, the native Jev API (experimental), and a fake model for tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Armanzahedi/fulcrum) |
| Maintainer | [Armanzahedi](https://github.com/Armanzahedi). Independently curated. |
| Format | NuGet packages (`Fulcrum`, `Fulcrum.OpenAI`, `Fulcrum.Jev`) |
| Requirements | .NET 10; an OpenRouter or TypeSafe key. |
| License | [MIT](https://github.com/Armanzahedi/fulcrum/blob/f730f710bdc06b9790b98b4b5feb9b95ae7ad415/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Fulcrum.Jev/JevClient.cs`](https://github.com/Armanzahedi/fulcrum/blob/f730f710bdc06b9790b98b4b5feb9b95ae7ad415/src/Fulcrum.Jev/JevClient.cs) at the pinned commit. |

## When to use

- Turn Jev probabilities into deterministic business actions in a .NET service.
- Mismatch: native Jev backend is marked experimental.

## How it works

`src/Fulcrum.Jev/JevClient.cs` calls Jev's native `POST /v1/systemone` (key from `JevOptions.ApiKey` or `JEV_API_KEY`); `Fulcrum.OpenAI` reaches `typesafe/jev-router` on OpenRouter. Rules are evaluated in order over the returned distributions to commit one outcome. Integration evidence: [`src/Fulcrum.Jev/JevClient.cs`](https://github.com/Armanzahedi/fulcrum/blob/f730f710bdc06b9790b98b4b5feb9b95ae7ad415/src/Fulcrum.Jev/JevClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package Fulcrum
dotnet add package Fulcrum.Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Guide: [github.com/Armanzahedi/fulcrum/blob/main/docs/guide.md](https://github.com/Armanzahedi/fulcrum/blob/main/docs/guide.md)

## Limits and data handling

Question state is sent to TypeSafe or OpenRouter. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit f730f710bdc0](https://github.com/Armanzahedi/fulcrum/tree/f730f710bdc06b9790b98b4b5feb9b95ae7ad415). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
