# MineLog (Minecraft agent harness where a planner plans and Jev picks each action)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Minecraft bot harness in which a chat model writes plans asynchronously and Jev picks one bounded action per tick from a closed catalog, with a safety check and an urgency score.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/beamnxw/minelog) |
| Maintainer | [beamnxw](https://github.com/beamnxw). Independently curated. |
| Format | Node.js harness (JavaScript, MIT) |
| Requirements | Node.js, a Minecraft server for the bot, a planner-model key and `TYPESAFE_API_KEY` for Jev. |
| License | [MIT](https://github.com/beamnxw/minelog/blob/c733137d4c6ad87966dd509d48370a94063c386d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/controller/jev.mjs`](https://github.com/beamnxw/minelog/blob/c733137d4c6ad87966dd509d48370a94063c386d/src/controller/jev.mjs) at the pinned commit. |

## When to use

- Study a planner/decider split for a game agent.
- Let a typed model pick from a fixed action list instead of free text.
- Mismatch: backend for minelog.xyz; small project with no releases.

## How it works

`src/controller/jev.mjs` posts the bot snapshot to `/v1/systemone` with a choice over the action catalog plus noul and score questions; `src/controller/policy.mjs` applies the safety and urgency results before an action runs. Integration evidence: [`src/controller/jev.mjs`](https://github.com/beamnxw/minelog/blob/c733137d4c6ad87966dd509d48370a94063c386d/src/controller/jev.mjs).

## Get started

Copy `.env.example` to `.env`, set the Minecraft server, planner key and TypeSafe key, then start the harness.

```sh
git clone https://github.com/beamnxw/minelog.git && cd minelog
npm install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/beamnxw/minelog/blob/c733137d4c6ad87966dd509d48370a94063c386d/README.md](https://github.com/beamnxw/minelog/blob/c733137d4c6ad87966dd509d48370a94063c386d/README.md)

## Limits and data handling

Game-state snapshots go to TypeSafe and plan prompts to the planner provider on your keys.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit c733137d4c6a](https://github.com/beamnxw/minelog/tree/c733137d4c6ad87966dd509d48370a94063c386d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
