# Clutch (automatic Haiku, Sonnet or Opus choice for each Claude Code message, with Jev deciding)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that picks the model and thinking effort for every message you send: a "thanks!" runs on Haiku, a hard bug on Opus with deep thinking, everything else on Sonnet. A short Haiku session brief gives the decider context, and per-project floors and ceilings keep production code above a tier or scratch repos below one. The decider is Jev, or a local llama.cpp `/v1/systemone` server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Louistuis/clutch) |
| Maintainer | [Louistuis](https://github.com/Louistuis). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code; an OpenRouter key for Jev, or a local llama.cpp decision server. |
| License | [MIT](https://github.com/Louistuis/clutch/blob/73a3930ea6b5e77f5a55cc5519cbfb96da08a8cd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/register.ts`](https://github.com/Louistuis/clutch/blob/73a3930ea6b5e77f5a55cc5519cbfb96da08a8cd/hooks/register.ts) at the pinned commit. |

## When to use

- Save Claude usage by sending easy messages to smaller models automatically.
- Mismatch: works only inside Claude Code.

## How it works

`hooks/register.ts` sends each message with the session brief to Jev (`typesafe/jev-1.14`), or to a local `/v1/systemone` endpoint when that is on, and sets the model and effort before Claude answers. Integration evidence: [`hooks/register.ts`](https://github.com/Louistuis/clutch/blob/73a3930ea6b5e77f5a55cc5519cbfb96da08a8cd/hooks/register.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add Louistuis/clutch
/plugin install clutch@clutch
/reload-plugins
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Louistuis/clutch#readme](https://github.com/Louistuis/clutch#readme)

## Limits and data handling

Each message and the session brief go to the decider (OpenRouter or your local server) before Claude sees them.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 73a3930ea6b5](https://github.com/Louistuis/clutch/tree/73a3930ea6b5e77f5a55cc5519cbfb96da08a8cd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
