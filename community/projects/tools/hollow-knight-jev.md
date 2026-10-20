# Hollow Knight + Jev

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Source-only research prototype that patches Hollow Knight with a C# bridge exposing bounded numeric observations, lets Jev choose movement and nail strikes as separate questions against Gruz Mother in Godhome, and applies short input leases, with a spending ledger and a local dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mbrajk/hollow-knight-jev) |
| Maintainer | [mbrajk](https://github.com/mbrajk). Independently curated. |
| Format | C# bridge, Mono.Cecil patcher and .NET 10 controller CLI with PowerShell scripts |
| Requirements | Windows, PowerShell 7, .NET SDK 10, Steam Hollow Knight 1.5.12620 (hash-checked), an empty save slot 4, and a TypeSafe key for live trials. |
| License | [MIT](https://github.com/mbrajk/hollow-knight-jev/blob/fac76c93ee640d721d659761ee53f7c73a848f69/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`controller/Program.cs`](https://github.com/mbrajk/hollow-knight-jev/blob/fac76c93ee640d721d659761ee53f7c73a848f69/controller/Program.cs) at the pinned commit. |

## When to use

- See how a decision model handles real-time action control with tight input timing.
- Reuse the bounded-observation bridge and budget ledger pattern for another game.
- Mismatch: research prototype; avoidance dominates, so the controller can be too passive.

## How it works

The bridge reads game state and the controller (`controller/Program.cs`) posts grouped movement and strike questions to `https://api.typesafe.ai/v1/systemone` with `jev-1.13.0`. Local forecasts check danger, the bridge applies finite input leases, and every paid run has its own call and spend cap and stops itself. Integration evidence: [`controller/Program.cs`](https://github.com/mbrajk/hollow-knight-jev/blob/fac76c93ee640d721d659761ee53f7c73a848f69/controller/Program.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet build ./controller/JevController.csproj -c Release
dotnet ./controller/bin/Release/net10.0/JevController.dll self-test   # offline
# paid, after docs/INSTALLATION.md setup:
./scripts/Run-Trial.ps1 -GameDirectory $game -Seconds 10 -MaxCalls 24 -MaxSpendUSD 0.05
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/synthetic-gruz.json (offline request preview)
- docs/INSTALLATION.md

## Limits and data handling

Bring your own game copy; no game assets included. Live trials call TypeSafe within the caps you set.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit fac76c93ee64](https://github.com/mbrajk/hollow-knight-jev/tree/fac76c93ee640d721d659761ee53f7c73a848f69). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
