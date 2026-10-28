# astrbot_plugin_at_gate (AstrBot plugin that merges split messages and silences repeated @ pings, with Jev deciding)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

AstrBot chat-bot plugin for two common group-chat problems: users who send one sentence in several pieces (it waits and merges them, images included) and users who keep @-ing the bot while a long answer is generating (it stops the queued "I'm here" replies). Whether a fragment is finished or a ping needs a reply can be decided by Jev, another configured model, or offline rules. Chinese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Meru-tea/astrbot_plugin_at_gate) |
| Maintainer | [Meru-tea](https://github.com/Meru-tea). Independently curated. |
| Format | AstrBot plugin (Python) |
| Requirements | An AstrBot install; optionally a TypeSafe or OpenRouter key for Jev. |
| License | [MIT](https://github.com/Meru-tea/astrbot_plugin_at_gate/blob/a8729f77ebbef4ec9e2867a2681f1a32a1f865fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/Meru-tea/astrbot_plugin_at_gate/blob/a8729f77ebbef4ec9e2867a2681f1a32a1f865fc/jev_client.py) at the pinned commit. |

## When to use

- Stop a QQ, Feishu, WeCom or Telegram bot from answering every half-sentence.
- Mismatch: Chinese docs; Jev is one of four decision backends.

## How it works

`jev_client.py` posts to `https://api.typesafe.ai/v1/systemone` (or OpenRouter's System One endpoint) and uses the Noul probability; network failures fall back to a zero-token rule state machine. Integration evidence: [`jev_client.py`](https://github.com/Meru-tea/astrbot_plugin_at_gate/blob/a8729f77ebbef4ec9e2867a2681f1a32a1f865fc/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
cd AstrBot/data/plugins
git clone https://github.com/Meru-tea/astrbot_plugin_at_gate.git
# restart AstrBot and configure the plugin
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/Meru-tea/astrbot_plugin_at_gate#readme](https://github.com/Meru-tea/astrbot_plugin_at_gate#readme)

## Limits and data handling

Recent chat fragments go to the selected decision backend; with the rules backend nothing leaves the bot.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit a8729f77ebbe](https://github.com/Meru-tea/astrbot_plugin_at_gate/tree/a8729f77ebbef4ec9e2867a2681f1a32a1f865fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
