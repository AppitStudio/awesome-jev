# Covan (local-first personal agent desktop app with Jev reply decisions)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Local-first personal agent desktop app with memory, tools, workspaces and scheduled tasks, where several bots can chat with you or in groups; an optional Jev strategy decides whether each bot should reply in a group or follow up, with low-confidence answers falling back to the LLM strategy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lichas/covan) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Lichas/covan#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (Apache-2.0); free source build. Model and Jev calls use your own keys or CLIs. Checked 2026-10-25. |
| Jev evidence | [`main/decisionStrategy.ts`](https://github.com/Lichas/covan/blob/faa8150e66a5b25511cac3b634b5d9b82baba9f9/main/decisionStrategy.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Lichas](https://github.com/Lichas). Independently curated. |
| Format | Desktop app (Electron, React, TypeScript, SQLite) |
| Platform and availability | macOS mainly; run from source with `./start.command`. |
| Jev's role | Optional: Jev answers the speak-or-stay-quiet and follow-up decisions; text is written by the bot's chosen model. |
| Requirements | macOS and Node.js 22.19+ to run from source; your choice of cloud API, local model or a signed-in Codex/Claude CLI; a TypeSafe key for the Jev strategy. |
| License | [Apache-2.0](https://github.com/Lichas/covan/blob/faa8150e66a5b25511cac3b634b5d9b82baba9f9/LICENSE) |

## When to use

- Run several persona bots in a group chat that only speak when it adds something.
- Keep conversations and results on your own machine.
- Mismatch: README is in Chinese; macOS-first.

## How it works

`main/decisionStrategy.ts` sends trimmed bot identity and recent conversation state to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, 0.6 confidence threshold, 12 s timeout); the TypeSafe key is stored with Electron safeStorage. Integration evidence: [`main/decisionStrategy.ts`](https://github.com/Lichas/covan/blob/faa8150e66a5b25511cac3b634b5d9b82baba9f9/main/decisionStrategy.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Lichas/covan.git && cd covan
./start.command   # or: npm install && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture (Chinese): [github.com/Lichas/covan/blob/main/docs/ARCHITECTURE.md](https://github.com/Lichas/covan/blob/main/docs/ARCHITECTURE.md)
- README (Chinese): [github.com/Lichas/covan#readme](https://github.com/Lichas/covan#readme)

## Limits and data handling

With the Jev strategy on, trimmed conversation state goes to TypeSafe. Bots can use workspace Bash and file tools; set CLI permissions to read-only if unsure.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit faa8150e66a5](https://github.com/Lichas/covan/tree/faa8150e66a5b25511cac3b634b5d9b82baba9f9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
