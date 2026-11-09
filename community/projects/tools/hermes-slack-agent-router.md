# Hermes Slack Agent Router (Hermes plugin where Jev decides which Slack bots should respond)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes plugin for multi-bot Slack workspaces: each receiving bot asks Jev whether the current message addresses it, then gets only its exact source text; one message can address several bots.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/u1-liquid/hermes-slack-agent-router) |
| Maintainer | [u1-liquid](https://github.com/u1-liquid). Independently curated. |
| Format | Hermes plugin (Python, MIT) |
| Requirements | Python 3.11+, Hermes v0.22.5 at the pinned commit with Slack integration, and `TYPESAFE_API_KEY` in the serving runtime. |
| License | [MIT](https://github.com/u1-liquid/hermes-slack-agent-router/blob/c256fd73b80f0d80642955bbab67450105179476/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hermes_slack_agent_router/jev.py`](https://github.com/u1-liquid/hermes-slack-agent-router/blob/c256fd73b80f0d80642955bbab67450105179476/hermes_slack_agent_router/jev.py) at the pinned commit. |

## When to use

- Let several Hermes bots share Slack threads without all replying.
- Route mixed instructions to the right bot.
- Mismatch: pinned to one Hermes revision; uses private host seams.

## How it works

`jev.py` posts message text, bounded history and candidate identities to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; missing credentials or invalid answers produce no work. Integration evidence: [`hermes_slack_agent_router/jev.py`](https://github.com/u1-liquid/hermes-slack-agent-router/blob/c256fd73b80f0d80642955bbab67450105179476/hermes_slack_agent_router/jev.py).

## Get started

Install with `hermes plugins install https://github.com/u1-liquid/hermes-slack-agent-router.git --ref <reviewed sha>` and enable `slack-agent-router`.

```sh
hermes plugins install https://github.com/u1-liquid/hermes-slack-agent-router.git --ref REVIEWED_COMMIT_SHA --yes-deps --no-enable
hermes plugins enable slack-agent-router --no-allow-tool-override
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/u1-liquid/hermes-slack-agent-router/blob/c256fd73b80f0d80642955bbab67450105179476/README.md](https://github.com/u1-liquid/hermes-slack-agent-router/blob/c256fd73b80f0d80642955bbab67450105179476/README.md)

## Limits and data handling

Slack text, author metadata and bot identities are sent to TypeSafe; only enable where that is authorized.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit c256fd73b80f](https://github.com/u1-liquid/hermes-slack-agent-router/tree/c256fd73b80f0d80642955bbab67450105179476). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
