# OpenMausBot (desktop chat app for a team of AI agent bots, with Jev picking which bot answers)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Electron desktop app for macOS, Windows and Ubuntu where each bot in a chat-style sidebar is a local Claude Code, Codex or Grok CLI agent with its own personality, model, computer and connected apps. With a decision model enabled, rooms set to Auto send each un-mentioned message to Jev, which picks the bot that should answer in a few hundred milliseconds; the room's lead bot answers whenever the decision model is off, slow or unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milind-soni/OpenMausBot) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://www.openmausbot.com/) |
| Pricing and access | Desktop app free (Apache-2.0); you bring your own agent CLI subscriptions and TypeSafe/OpenRouter key. An optional paid Cloud plan and an Enterprise license for `enterprise/` features exist. Checked 2026-10-30. |
| Jev evidence | [`server/decider/jev.ts`](https://github.com/milind-soni/OpenMausBot/blob/10af83e74dd7b5f7895fa498e0009c6ccc12a813/server/decider/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [milind-soni](https://github.com/milind-soni). Independently curated. |
| Format | Desktop app (Electron; signed macOS, Windows and Ubuntu installers) |
| Platform and availability | macOS (Apple silicon and Intel), Windows x64 and Ubuntu desktop installers from GitHub releases (v0.1.134, 2026-10-30). |
| Jev's role | Picks which bot in an Auto room should answer each message that does not mention one. |
| Requirements | The `claude`, `codex` or `grok` CLI signed in on your machine; a TypeSafe key (or an OpenRouter key) under Settings → Decision model for the Jev features. |
| License | [Apache-2.0 (except `enterprise/`)](https://github.com/milind-soni/OpenMausBot/blob/10af83e74dd7b5f7895fa498e0009c6ccc12a813/LICENSE) |

## When to use

- Run several role-specific agent bots in shared rooms and let a fast classifier route each message to the right one.
- Mismatch: Jev only routes; the bots' work runs on your own agent CLIs and subscriptions.

## How it works

`server/decider/jev.ts` sends the room state (members, recent lines, the new message) and bot descriptions to `api.typesafe.ai/v1/systemone` (`jev-latest`) as a choice; answers below the 0.6 threshold, errors and replies over 1.5 seconds fall back to the room lead. An OpenRouter route to `typesafe/jev-1.13` or other decisions models is also supported. Integration evidence: [`server/decider/jev.ts`](https://github.com/milind-soni/OpenMausBot/blob/10af83e74dd7b5f7895fa498e0009c6ccc12a813/server/decider/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# Download the installer for your OS from https://www.openmausbot.com/download
# then Settings -> Decision model -> TypeSafe Jev -> paste key -> Save -> Test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision model guide: [github.com/milind-soni/OpenMausBot/blob/10af83e74dd7b5f7895fa498e0009c6ccc12a813/docs/decision-model.md](https://github.com/milind-soni/OpenMausBot/blob/10af83e74dd7b5f7895fa498e0009c6ccc12a813/docs/decision-model.md)

## Limits and data handling

With the decision model on, each decision sends the room name, its members, recent room lines, the new message and the bots' descriptions to TypeSafe or OpenRouter. Code under `enterprise/` is source-available under a separate license, not Apache-2.0. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 10af83e74dd7](https://github.com/milind-soni/OpenMausBot/tree/10af83e74dd7b5f7895fa498e0009c6ccc12a813). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
