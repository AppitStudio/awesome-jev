# winuse

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server and CLI that lets an AI observe and operate Windows desktop apps through UI Automation, WebView2, input, windows, processes and files, with Jev used for grounding and verification checks, and saved scenarios you can replay as end-to-end tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/straygizmo/winuse) |
| Maintainer | [straygizmo](https://github.com/straygizmo). Independently curated. |
| Format | MCP server + CLI (.NET 10, Windows) |
| Requirements | Windows and the .NET 10 SDK; `JEV_API_KEY` in the user environment. |
| License | [MIT](https://github.com/straygizmo/winuse/blob/4f472844d6cb5d41ba933bfbd6dedccc9d5ad16b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/WinUse.Core/Jev/JevClient.cs`](https://github.com/straygizmo/winuse/blob/4f472844d6cb5d41ba933bfbd6dedccc9d5ad16b/src/WinUse.Core/Jev/JevClient.cs) at the pinned commit. |

## When to use

- Let Claude Code operate Windows desktop apps over MCP.
- Replay saved desktop scenarios as E2E tests without AI.
- Mismatch: Windows only; build from source.

## How it works

`winuse --mcp` exposes observe and act tools. Grounding and verification checks call Jev through `src/WinUse.Core/Jev/JevClient.cs`, with `JEV_BASE_URL` defaulting to `https://api.typesafe.ai` in `WinUseConfig.cs`; allowed file roots and killable processes are configurable allowlists. Integration evidence: [`src/WinUse.Core/Jev/JevClient.cs`](https://github.com/straygizmo/winuse/blob/4f472844d6cb5d41ba933bfbd6dedccc9d5ad16b/src/WinUse.Core/Jev/JevClient.cs).

## Get started

From the upstream README: build and publish with dotnet, set `JEV_API_KEY`, then register with Claude Code.

```sh
dotnet publish src/WinUse -c Release -o out
claude mcp add winuse -- <repo>\out\winuse.exe --mcp
winuse run <scenario.json> --report <dir>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README CLI section (scenario replay)

## Limits and data handling

Screen and UI content used for checks goes to TypeSafe. The agent acts on your real desktop; keep the allowlists tight.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 4f472844d6cb](https://github.com/straygizmo/winuse/tree/4f472844d6cb5d41ba933bfbd6dedccc9d5ad16b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
