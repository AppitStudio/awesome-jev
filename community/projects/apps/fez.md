# Fez by Kenneth Ashley (Mac chat room for a team of AI agents where Jev decides who takes each message and whether a reply is needed)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Desktop app where several AI agents, each with its own identity, model and skills, work in shared channels with you. Instead of you picking the agent and checking the result, a judgment model routes each message to an agent (or nobody), decides whether the work is done and whether you need to read it. Messages are signed and stored on a nostr relay you run locally or on a server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KennethAshley/fez) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://fez.chat) |
| Pricing and access | Free MIT source and desktop download. You pay your own chat-model provider; Jev runs on the author's hosted router by default or on your own TypeSafe key. Checked 2026-11-27. |
| Jev evidence | [`packages/fez-orchestrator/src/judge.ts`](https://github.com/KennethAshley/fez/blob/a6896bd16dba4084fd7b6164204dc86f9e61e1b7/packages/fez-orchestrator/src/judge.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Kenneth Ashley](https://github.com/KennethAshley) (KennethAshley). Independently curated. |
| Format | Tauri desktop app (TypeScript/Rust) + CLI on nostr |
| Platform and availability | macOS desktop app (Apple Silicon, signed DMG); CLI and services from source on macOS or Linux. |
| Jev's role | Router and judge. The room asks Jev (`jev-1.13.0` by default) which agent should take a message, and a thread governor asks yes/no questions before a fellow agent's mention costs a full agent turn. `judge.ts` calls `https://api.typesafe.ai/v1/systemone` directly when the judge URL is TypeSafe's own API with your key. |
| Requirements | Apple Silicon Mac for the desktop app (or Node.js 20+ for the source path), a chat-model provider or CLI harness (Claude Code or pi); a TypeSafe key if you run the judge yourself. |
| License | [MIT](https://github.com/KennethAshley/fez/blob/a6896bd16dba4084fd7b6164204dc86f9e61e1b7/LICENSE) |

## When to use

- People running several coding or research agents who want the routing and 'is this done?' checks handled by the room.
- Mismatch: a single-assistant chat app; Fez is built around a team of agents and a relay.

## How it works

`packages/fez-orchestrator/src/judge.ts` sends routing and governor questions (up to 32 per call) as `choice` and `noul` questions and parses Jev's answers strictly. The author's hosted router (`deploy/router/`) also forwards to Jev with a local Qwen fallback; its README reports 96/97 messages routed correctly at a 184 ms median in one three-agent test. Integration evidence: [`packages/fez-orchestrator/src/judge.ts`](https://github.com/KennethAshley/fez/blob/a6896bd16dba4084fd7b6164204dc86f9e61e1b7/packages/fez-orchestrator/src/judge.ts).

## Get started

Download the desktop app from the author's releases, or build the CLI from source.

```sh
# desktop: https://github.com/KennethAshley/fez-releases/releases
git clone https://github.com/KennethAshley/fez && cd fez
npm install
npm run build   # gives ./dist/cli.js (fez)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Video tour: [youtu.be/eyirodwkW1Y](https://youtu.be/eyirodwkW1Y)
- Routing comparison: [github.com/KennethAshley/fez/blob/main/docs/superpowers/research/2026-09-18-typesafe-routing-results.md](https://github.com/KennethAshley/fez/blob/main/docs/superpowers/research/2026-09-18-typesafe-routing-results.md)

## Limits and data handling

By default routing requests go to the author's hosted router on DigitalOcean, which forwards message text to TypeSafe; pointing the judge at `api.typesafe.ai` with your own key avoids that hop. The routing figures are the author's single test. Chat-model usage is billed by your provider.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit a6896bd16dba](https://github.com/KennethAshley/fez/tree/a6896bd16dba4084fd7b6164204dc86f9e61e1b7). Inspected the README, LICENSE, `packages/fez-orchestrator/src/judge.ts`, `deploy/router/README.md` and the getting-started docs at the pinned commit; the desktop app was not downloaded or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
