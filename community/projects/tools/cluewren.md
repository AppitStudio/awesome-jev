# Cluewren (MCP server that lets Claude Code or Codex playtest a game open in the Unity, Godot or Unreal editor, with Jev making the in-play choices)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

MCP server, skill and frame-describer subagent that plays the game open in your Unity, Godot or Unreal editor for your coding agent. The agent researches the game's code, writes a C# harness, and Jev makes the choices during play inside that harness; the agent then reports what play showed, with evidence. Cluewren holds no language-model key itself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/crane-valley/cluewren) |
| Maintainer | [crane-valley](https://github.com/crane-valley). Independently curated. |
| Format | MCP server (.NET 10) with Unity, Godot and Unreal editor plugins |
| Requirements | .NET 10 SDK; Claude Code or Codex CLI; Unity 6000.0+, Godot 4 or Unreal Engine 5 (Win64, beta); a TypeSafe API key for the decision model. |
| License | [Apache-2.0](https://github.com/crane-valley/cluewren/blob/82d3a3915f4e4b231099a63d365296f60ff89893/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Cluewren/Jev/JevClient.cs`](https://github.com/crane-valley/cluewren/blob/82d3a3915f4e4b231099a63d365296f60ff89893/src/Cluewren/Jev/JevClient.cs) at the pinned commit. |

## When to use

- Let your coding agent explore a game for bugs, verify a claim about how it works, or reach a goal in play.
- Mismatch: needs a supported engine editor and a coding agent; the Unreal plugin is Win64-only and beta.

## How it works

`src/Cluewren/Jev/JevClient.cs` sends the goal, situation, options and recent actions to `https://api.typesafe.ai` (pinned `jev-1.13.0`) with a 1 s attempt and 1.5 s total timeout, a kept-warm connection and a retry, so the harness can decide in real time. Integration evidence: [`src/Cluewren/Jev/JevClient.cs`](https://github.com/crane-valley/cluewren/blob/82d3a3915f4e4b231099a63d365296f60ff89893/src/Cluewren/Jev/JevClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/crane-valley/cluewren.git
cd cluewren
dotnet build -c Release
./src/Cluewren/bin/Release/net10.0/cluewren connect claude
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs and engine install guides: [docs.cluewren.dev/](https://docs.cluewren.dev/)

## Limits and data handling

Decision requests carry text about the game state to TypeSafe on your key (no pictures); your coding agent talks to its own provider as usual, and frames reach its model through the frame-describer. The README states there is no upload, telemetry or accounts. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 82d3a3915f4e](https://github.com/crane-valley/cluewren/tree/82d3a3915f4e4b231099a63d365296f60ff89893). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
