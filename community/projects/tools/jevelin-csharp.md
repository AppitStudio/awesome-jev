# Jevelin by Nick Proud (simple unofficial C# client for Jev on NuGet)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small unofficial .NET client for Jev: build a request with a state and named questions (`JevQuestion.Noul`, `Choice` with up to 255 options, `Score` with up to 10 levels), call `AskAsync`, and read typed answers with probabilities; `AskYesNoAsync` is a one-line shortcut for a single yes/no. Not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nickproud/Jevelin) |
| Maintainer | [nickproud](https://github.com/nickproud). Independently curated. |
| Format | .NET library (NuGet `Jevelin`) |
| Requirements | .NET 10 SDK and a TypeSafe API key. |
| License | [MIT](https://github.com/nickproud/Jevelin/blob/c0e161121a2cd653bda56d2b4078e9970db3e5df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Jevelin/JevClient.cs`](https://github.com/nickproud/Jevelin/blob/c0e161121a2cd653bda56d2b4078e9970db3e5df/src/Jevelin/JevClient.cs) at the pinned commit. |

## When to use

- Call Jev from C# without hand-writing HTTP and JSON.
- Mismatch: unofficial; compare with the other .NET clients in this catalog.

## How it works

`src/Jevelin/JevClient.cs` posts to `https://api.typesafe.ai/` with `jev-latest` as the default model and maps each answer to typed fields. Integration evidence: [`src/Jevelin/JevClient.cs`](https://github.com/nickproud/Jevelin/blob/c0e161121a2cd653bda56d2b4078e9970db3e5df/src/Jevelin/JevClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet add package Jevelin
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- NuGet: [www.nuget.org/packages/Jevelin](https://www.nuget.org/packages/Jevelin)
- README: [github.com/nickproud/Jevelin#readme](https://github.com/nickproud/Jevelin#readme)

## Limits and data handling

Each state you send goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit c0e161121a2c](https://github.com/nickproud/Jevelin/tree/c0e161121a2cd653bda56d2b4078e9970db3e5df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
