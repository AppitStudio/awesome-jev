# Minos.NET

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial .NET client for Jev `/v1/systemone` (direct or OpenRouter) with source-generated, Native AOT-friendly typed questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MarcelRoozekrans/Minos.NET) |
| Maintainer | [MarcelRoozekrans](https://github.com/MarcelRoozekrans). Independently curated. |
| Format | .NET library + source generator |
| Requirements | .NET 10 SDK; TypeSafe or OpenRouter API key. |
| License | [MIT](https://github.com/MarcelRoozekrans/Minos.NET/blob/bac356ec98055ea66e97dd9b8aa3e8673b9c8350/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Use Jev from C#/.NET services.
- Mismatch: not yet on NuGet per upstream status.

## How it works

Questions are declared as a C# type; a Roslyn source generator writes request building and answer parsing so no reflection is needed. (Summarized from the upstream [README](https://github.com/MarcelRoozekrans/Minos.NET/blob/bac356ec98055ea66e97dd9b8aa3e8673b9c8350/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Per the upstream README: `dotnet add package Minos.NET` (status: early development, NuGet publication pending).

## Limits and data handling

Unofficial; early development. State is sent to the configured provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit bac356ec9805](https://github.com/MarcelRoozekrans/Minos.NET/tree/bac356ec98055ea66e97dd9b8aa3e8673b9c8350). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
