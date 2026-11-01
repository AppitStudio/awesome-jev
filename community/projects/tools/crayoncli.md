# CrayonCli (.NET CLI that asks Jev which of 8 crayon colors an image is closest to)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small .NET 10 prototype that sends an image to Jev and prints which of eight classic crayon colors it is closest to, with a probability for each, plus a script that checks Jev against labeled test images.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lonelyrobot/jev-prototyping) |
| Maintainer | [lonelyrobot](https://github.com/lonelyrobot). Independently curated. |
| Format | .NET 10 console app |
| Requirements | The .NET 10 SDK and a TypeSafe key. |
| License | [MIT](https://github.com/lonelyrobot/jev-prototyping/blob/ff6fe6df769e6053237d06dde2c3de2785731066/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`CrayonCli/Program.cs`](https://github.com/lonelyrobot/jev-prototyping/blob/ff6fe6df769e6053237d06dde2c3de2785731066/CrayonCli/Program.cs) at the pinned commit. |

## When to use

- See a minimal C# example of an image choice question with the tryAGI TypeSafeAI SDK.
- Mismatch: a prototype.

## How it works

`CrayonCli/Program.cs` uses the `tryAGI.TypeSafeAI` NuGet package to send the image with one eight-way choice question and prints the returned probabilities. Integration evidence: [`CrayonCli/Program.cs`](https://github.com/lonelyrobot/jev-prototyping/blob/ff6fe6df769e6053237d06dde2c3de2785731066/CrayonCli/Program.cs).

## Get started

From the upstream README (not run on the review host):

```sh
cd CrayonCli
echo 'TYPESAFE_API_KEY=...' > .env
dotnet run -- test-files/red.jpg
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/lonelyrobot/jev-prototyping#readme](https://github.com/lonelyrobot/jev-prototyping#readme)

## Limits and data handling

Images are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit ff6fe6df769e](https://github.com/lonelyrobot/jev-prototyping/tree/ff6fe6df769e6053237d06dde2c3de2785731066). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
