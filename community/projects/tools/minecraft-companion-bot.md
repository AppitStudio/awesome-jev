# Minecraft companion bot by slime12122005-max (Java 1.21.1 companion where Antigravity plans and Jev makes fast combat and survival calls)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

A Mineflayer-based companion bot for Minecraft Java 1.21.1 with three layers: Antigravity plans and executes your requests through a 12-tool MCP server, Jev makes fast probabilistic choices when the bot is in danger, and local reflexes handle movement, combat, survival, mining, crafting, smelting, schematic building and swarms, with a humanised motor layer and a web dashboard. README is in Vietnamese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/slime12122005-max/minecraft-companion-bot) |
| Maintainer | [slime12122005-max](https://github.com/slime12122005-max). Independently curated. |
| Format | Node.js bot + stdio MCP server + dashboard |
| Requirements | Node.js 22.5+ (built-in `node:sqlite`), a Minecraft Java 1.21.1 world open to LAN or a server, Antigravity for the MCP planning layer; `TYPESAFE_API_KEY` is optional. |
| License | [MIT](https://github.com/slime12122005-max/minecraft-companion-bot/blob/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/llm.js`](https://github.com/slime12122005-max/minecraft-companion-bot/blob/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0/src/llm.js) at the pinned commit. |

## When to use

- A Minecraft companion that follows natural-language requests and reacts quickly in fights.
- Mismatch: English-only documentation; the README and in-game commands are Vietnamese.

## How it works

`src/llm.js` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` for `chooseCombat` and `chooseSurvivalAction`, with timeouts and abort signals; without a key the bot keeps working with the MCP planner and local combat reflexes. Integration evidence: [`src/llm.js`](https://github.com/slime12122005-max/minecraft-companion-bot/blob/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0/src/llm.js).

## Get started

Open your world to LAN, copy the example config with your host, port and owner, optionally add a TypeSafe key, then run the doctor check and start the bot (or use Docker Compose).

```sh
git clone https://github.com/slime12122005-max/minecraft-companion-bot && cd minecraft-companion-bot
cp config.example.json config.json   # host, port, username, owner
cp .env.example .env                 # optional TYPESAFE_API_KEY
node src/index.js --doctor && node src/index.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev client: [github.com/slime12122005-max/minecraft-companion-bot/blob/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0/src/llm.js](https://github.com/slime12122005-max/minecraft-companion-bot/blob/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0/src/llm.js)
- MCP server: [github.com/slime12122005-max/minecraft-companion-bot/blob/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0/src/mcp/server.js](https://github.com/slime12122005-max/minecraft-companion-bot/blob/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0/src/mcp/server.js)

## Limits and data handling

Game state for danger decisions is sent to TypeSafe when a key is set. New project (created 2026-11-22).

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 2a165b50afa8](https://github.com/slime12122005-max/minecraft-companion-bot/tree/2a165b50afa8c34e87f660a6a9afd8ddc657bbf0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
