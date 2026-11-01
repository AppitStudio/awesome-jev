# agent-sdk-2048 (two Agent SDK players race 2048 in an emulator: a normal model turn vs Jev decide())

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Side-by-side race in mGBA: one Agent SDK player takes a normal model turn per move, the other uses Jev `decide()` to make a typed choice among up, down, left and right, with traces of what Jev saw. Without a key the Jev player refuses to run unless you pass a labeled stand-in.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rperry2174/agent-sdk-2048) |
| Maintainer | [Rperry2174](https://github.com/Rperry2174). Independently curated. |
| Format | TypeScript (Agent SDK) players and emulator scripts |
| Requirements | macOS, mGBA, Node.js; a TypeSafe API key. |
| License | [MIT](https://github.com/Rperry2174/agent-sdk-2048/blob/bd221fb4af09744b8edf1110ff5b37c13f11baaf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/policy.ts`](https://github.com/Rperry2174/agent-sdk-2048/blob/bd221fb4af09744b8edf1110ff5b37c13f11baaf/lib/policy.ts) at the pinned commit. |

## When to use

- Compare per-move LLM turns with typed Jev decisions in the same game.
- Mismatch: macOS-only scripts; a demo.

## How it works

`lib/policy.ts` calls `decide()` from the Agent SDK Jev extension with the 4x4 board and the four moves; `agents/jev/bot/agent.ts` exposes it as `choose_move`, and moves are direct tool calls with no model turn. Integration evidence: [`lib/policy.ts`](https://github.com/Rperry2174/agent-sdk-2048/blob/bd221fb4af09744b8edf1110ff5b37c13f11baaf/lib/policy.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run race
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/Rperry2174/agent-sdk-2048#readme](https://github.com/Rperry2174/agent-sdk-2048#readme)

## Limits and data handling

Board state is sent to TypeSafe on every move. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit bd221fb4af09](https://github.com/Rperry2174/agent-sdk-2048/tree/bd221fb4af09744b8edf1110ff5b37c13f11baaf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
