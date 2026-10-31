# jev-mobile-pilot (MCP server that lets coding agents drive iOS Simulators and Android devices, with Jev picking each step)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server and CLI for coding agents: code reads the iOS Simulator or Android accessibility tree, Jev picks the next element and decides whether the goal is done, and your agent only plans. Screenshots are never sent to Jev; tests run against a fake device and a fake Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/heyk1njo/jev-mobile-pilot) |
| Maintainer | [heyk1njo](https://github.com/heyk1njo). Independently curated. |
| Format | Node.js MCP server + CLI (TypeScript) |
| Requirements | Node.js; Xcode Simulator (with AXe) or an Android device/emulator with ADB; a TypeSafe key. |
| License | [MIT](https://github.com/heyk1njo/jev-mobile-pilot/blob/9b848326e25a4cf8ba76b460c45b7e8b42c77439/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/heyk1njo/jev-mobile-pilot/blob/9b848326e25a4cf8ba76b460c45b7e8b42c77439/src/jev/client.ts) at the pinned commit. |

## When to use

- Let Claude Code or another agent test mobile flows without sending screenshots to an LLM.
- Mismatch: needs a local simulator or device; not a cloud device farm.

## How it works

`src/jev/client.ts` calls TypeSafe (`https://api.typesafe.ai/v1`, `jev-latest` by default) with the element list and goal; `src/task/engine.ts` loops find, act and done-check under step limits. Integration evidence: [`src/jev/client.ts`](https://github.com/heyk1njo/jev-mobile-pilot/blob/9b848326e25a4cf8ba76b460c45b7e8b42c77439/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/heyk1njo/jev-mobile-pilot.git && cd jev-mobile-pilot
npm ci && npm run build
claude mcp add -s project jev-mobile-pilot -- node $PWD/dist/cli.js mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/heyk1njo/jev-mobile-pilot#readme](https://github.com/heyk1njo/jev-mobile-pilot#readme)

## Limits and data handling

Accessibility-tree text and hints are sent to TypeSafe; screenshots stay local. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 9b848326e25a](https://github.com/heyk1njo/jev-mobile-pilot/tree/9b848326e25a4cf8ba76b460c45b7e8b42c77439). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
