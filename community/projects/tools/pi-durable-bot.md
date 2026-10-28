# pi-durable-bot (self-hosted AI coworker for team chat, with Jev deciding when a message needs it)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source AI coworker you run on your own machine: it logs every message, edit and event in the channels you invite it to into local SQLite, keeps one long memory, writes and runs its own code, sets its own reminders and resumes after a crash without double-sending. Before waking the main model on an unprompted message, Jev answers two questions: is this about me, and do I need to respond.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Crokily/pi-durable-bot) |
| Maintainer | [Crokily](https://github.com/Crokily). Independently curated. |
| Format | TypeScript service (Pi agent runtime) |
| Requirements | Node.js, a Slack (or other supported) workspace, a model provider for the agent, and a TypeSafe API key for the wake-up check. |
| License | [MIT](https://github.com/Crokily/pi-durable-bot/blob/a8878517b93453ec2b703c320cc6ca1072c27d3a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/gateway/jev.ts`](https://github.com/Crokily/pi-durable-bot/blob/a8878517b93453ec2b703c320cc6ca1072c27d3a/src/gateway/jev.ts) at the pinned commit. |

## When to use

- Run an always-on team assistant that speaks up on its own, without paying a large model to read every message.
- Mismatch: it acts on its own computer; review what you give it access to.

## How it works

`src/gateway/jev.ts` uses the official `@typesafe-ai/sdk` to ask two Noul questions about each incoming item, given what the bot is responsible for; only items that pass wake the agent. Integration evidence: [`src/gateway/jev.ts`](https://github.com/Crokily/pi-durable-bot/blob/a8878517b93453ec2b703c320cc6ca1072c27d3a/src/gateway/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Crokily/pi-durable-bot && cd pi-durable-bot
# then follow the README Quick start (it can be set up by a coding agent)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Crokily/pi-durable-bot#readme](https://github.com/Crokily/pi-durable-bot#readme)

## Limits and data handling

Messages from invited channels go to TypeSafe for the wake-up check and, when woken, to your agent model. The full log stays in local SQLite.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit a8878517b934](https://github.com/Crokily/pi-durable-bot/tree/a8878517b93453ec2b703c320cc6ca1072c27d3a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
