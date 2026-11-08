# Heartflow (AstrBot group-chat proactive reply plugin with TypeSafe Jev scoring)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

AstrBot plugin for group chats: a small model (TypeSafe Jev by default) scores each message on content, willingness, social fit, timing and coherence to decide whether the bot should join in; the main model then writes the reply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/advent259141/Astrbot_plugin_Heartflow) |
| Maintainer | [advent259141](https://github.com/advent259141). Independently curated. |
| Format | AstrBot plugin (Python, AGPL-3.0) |
| Requirements | AstrBot and a TypeSafe (or OpenRouter/compatible) API key. |
| License | [AGPL-3.0](https://github.com/advent259141/Astrbot_plugin_Heartflow/blob/d986b5e4b8e5480e30b2ef241e68e2782a0dd6fa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/advent259141/Astrbot_plugin_Heartflow/blob/d986b5e4b8e5480e30b2ef241e68e2782a0dd6fa/jev_client.py) at the pinned commit. |

## When to use

- Let a chat bot reply proactively only when it fits.
- Keep the expensive model out of every message.
- Mismatch: README in Chinese; AstrBot only.

## How it works

`jev_client.py` uses `https://api.typesafe.ai/v1` and `jev-latest` by default, reading `TYPESAFE_API_KEY` or plugin config. Integration evidence: [`jev_client.py`](https://github.com/advent259141/Astrbot_plugin_Heartflow/blob/d986b5e4b8e5480e30b2ef241e68e2782a0dd6fa/jev_client.py).

## Get started

Install the plugin in AstrBot, set the Jev key in plugin settings, and enable it for a group.

```sh
git clone https://github.com/advent259141/Astrbot_plugin_Heartflow.git && cd Astrbot_plugin_Heartflow
export TYPESAFE_API_KEY=...
pip install -r requirements.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/advent259141/Astrbot_plugin_Heartflow/blob/d986b5e4b8e5480e30b2ef241e68e2782a0dd6fa/README.md](https://github.com/advent259141/Astrbot_plugin_Heartflow/blob/d986b5e4b8e5480e30b2ef241e68e2782a0dd6fa/README.md)

## Limits and data handling

Group-chat messages are sent to TypeSafe on your key for scoring.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit d986b5e4b8e5](https://github.com/advent259141/Astrbot_plugin_Heartflow/tree/d986b5e4b8e5480e30b2ef241e68e2782a0dd6fa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
