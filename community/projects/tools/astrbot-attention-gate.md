# astrbot_plugin_attention_gate by AcceleratorYue (AstrBot plugin where a Jev-style System One model decides whether a group-chat bot should chime in)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AstrBot plugin that replaces random proactive replies in group chats: after hard filters and a message buffer, a System One model judges intent, interest match, timing, risk and reply value, and the plugin returns act or pass. It never writes reply text; AstrBot's normal pipeline does that. Chinese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AcceleratorYue/astrbot_plugin_attention_gate) |
| Maintainer | [AcceleratorYue](https://github.com/AcceleratorYue). Independently curated. |
| Format | Python · AstrBot plugin |
| Requirements | AstrBot; a System One endpoint: TokenRhythm's hosted NeoHorse-Jev-4B (the default, needs a TokenRhythm `sk_` key), official TypeSafe Jev (`https://api.typesafe.ai/v1/systemone`, `jev-latest`, TypeSafe key) or a self-hosted NeoHorse-Jev-4B server. |
| License | [MIT](https://github.com/AcceleratorYue/astrbot_plugin_attention_gate/blob/31882d271480d69e645e1b8b87f7b31475dcc6d5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`main.py`](https://github.com/AcceleratorYue/astrbot_plugin_attention_gate/blob/31882d271480d69e645e1b8b87f7b31475dcc6d5/main.py) at the pinned commit. |

## When to use

- Make an AstrBot group-chat bot speak up only when a message is worth answering, with cooldowns and per-group caps.
- Mismatch: bots that should reply to every message, or setups that need official TypeSafe Jev by default (the default endpoint is a third-party model).

## How it works

`main.py` builds the state and typed questions and posts them to the configured `/v1/systemone` (or `/v1/decision`) URL; if the decision service is unavailable the plugin passes instead of falling back to another model. Cooldown, hourly caps and a dry-run mode are in `_conf_schema.json`. Integration evidence: [`main.py`](https://github.com/AcceleratorYue/astrbot_plugin_attention_gate/blob/31882d271480d69e645e1b8b87f7b31475dcc6d5/main.py).

## Get started

Copy the plugin into AstrBot's plugins folder, reload, then set `jev_provider_url`, `model` and `api_key` and keep `dry_run` on while you tune it.

```sh
cd AstrBot/data/plugins
git clone https://github.com/AcceleratorYue/astrbot_plugin_attention_gate.git
# reload plugins in AstrBot, then edit the plugin config
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/AcceleratorYue/astrbot_plugin_attention_gate/blob/31882d271480d69e645e1b8b87f7b31475dcc6d5/README.md](https://github.com/AcceleratorYue/astrbot_plugin_attention_gate/blob/31882d271480d69e645e1b8b87f7b31475dcc6d5/README.md)
- Config schema: [github.com/AcceleratorYue/astrbot_plugin_attention_gate/blob/31882d271480d69e645e1b8b87f7b31475dcc6d5/_conf_schema.json](https://github.com/AcceleratorYue/astrbot_plugin_attention_gate/blob/31882d271480d69e645e1b8b87f7b31475dcc6d5/_conf_schema.json)

## Limits and data handling

The default configuration points at TokenRhythm's NeoHorse-Jev-4B, a third-party Jev-style model, not TypeSafe's Jev; official TypeSafe Jev is option B in the README. Group-chat messages are sent to whichever decision endpoint you configure.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 31882d271480](https://github.com/AcceleratorYue/astrbot_plugin_attention_gate/tree/31882d271480d69e645e1b8b87f7b31475dcc6d5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
