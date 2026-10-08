# astrbot_plugin_smart_wake

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Chinese AstrBot plugin that lets a group-chat bot join conversations without being @-mentioned: topic keywords trigger a weighted dice roll, then TypeSafe Jev judges reply value × naturalness × heat × energy before waking the bot; Jev also debounces when a conversation ends and confirms 'please be quiet' requests to enter a muted state, with the last 200 decisions in the dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mikachiyo/astrbot_plugin_smart_wake) |
| Maintainer | [Mikachiyo](https://github.com/Mikachiyo). Independently curated. |
| Format | AstrBot plugin (dashboard-configurable) |
| Requirements | AstrBot; a TypeSafe API key (`https://api.typesafe.ai`) or an OpenRouter key (`typesafe/jev-1.13`). |
| License | [MIT](https://github.com/Mikachiyo/astrbot_plugin_smart_wake/blob/d9fc120f1b41ba3ecf9997b65f2ee45fc102eb6d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Make a QQ/AstrBot group bot chime in naturally on chosen topics.
- Let members silence the bot with Jev-confirmed requests.
- Mismatch: Chinese-only docs; behaviour tuned for lively group chats.

## How it works

[`core/jev_client.py`](https://github.com/Mikachiyo/astrbot_plugin_smart_wake/blob/d9fc120f1b41ba3ecf9997b65f2ee45fc102eb6d/core/jev_client.py) sends recent context to Jev; plugin state (energy, cooldown, muted, conversation) persists in AstrBot's `plugin_data` directory.

## Get started

Install as an AstrBot plugin from the repository and set the Jev channel in the dashboard (README §1):

```sh
# AstrBot dashboard → plugins → install from https://github.com/Mikachiyo/astrbot_plugin_smart_wake
# then set channel (typesafe | openrouter), base_url and API key
```

Jev calls billed to your TypeSafe or OpenRouter key; dice rolls filter most messages first.

## Examples and demos

- README 功能 and decision-funnel diagram.

## Limits and data handling

Unmentioned group messages that pass the keyword stage go to Jev. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit d9fc120f1b41](https://github.com/Mikachiyo/astrbot_plugin_smart_wake/tree/d9fc120f1b41ba3ecf9997b65f2ee45fc102eb6d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
