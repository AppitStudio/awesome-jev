# FastBrain proactive replies for AstrBot (FastBrain-9B decides whether the bot should chime in to a group chat)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

AstrBot plugin: a FastBrain-9B System One model reads recent group messages and decides whether the bot should join the conversation unprompted; the session's own chat model writes the reply. Ships in observe mode with an empty group whitelist, so it never speaks until you configure it; rate limits, cooldowns and quiet failure on errors are built in. README in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/camera-2018/astrbot_plugin_fastbrain_proactive) |
| Maintainer | [camera-2018](https://github.com/camera-2018). Independently curated. |
| Format | Python plugin for AstrBot 4.29 |
| Requirements | AstrBot 4.29, and a FastBrain-9B `/v1/systemone` server (llama.cpp or a gateway) with its key. |
| License | [MIT](https://github.com/camera-2018/astrbot_plugin_fastbrain_proactive/blob/bd6b347cfca1cda4529e58865def8a0201edb136/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`engine.py`](https://github.com/camera-2018/astrbot_plugin_fastbrain_proactive/blob/bd6b347cfca1cda4529e58865def8a0201edb136/engine.py) at the pinned commit. |

## When to use

- Let a QQ or other AstrBot group bot speak up only when a fast judge thinks it should.
- Mismatch: built for FastBrain-9B, not TypeSafe's Jev; the default 0.5 threshold rarely fires in the author's tests.

## How it works

`engine.py` sends the trimmed group context and one yes/no question to the configured `/v1/systemone` endpoint and compares P(True) with the threshold. Integration evidence: [`engine.py`](https://github.com/camera-2018/astrbot_plugin_fastbrain_proactive/blob/bd6b347cfca1cda4529e58865def8a0201edb136/engine.py).

## Get started

From the upstream README (not run on the review host):

```sh
# copy the plugin into data/plugins/astrbot_plugin_fastbrain_proactive/ and reload
# set the endpoint, e.g. http://127.0.0.1:8080/v1/systemone, and model FastBrain-9B
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/camera-2018/astrbot_plugin_fastbrain_proactive#readme](https://github.com/camera-2018/astrbot_plugin_fastbrain_proactive#readme)
- FastBrain-9B listing: [jevlist.ai/projects/fastbrain-9b](https://jevlist.ai/projects/fastbrain-9b)

## Limits and data handling

Group messages go to whichever FastBrain server you configure; keep it self-hosted if chats are private.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit bd6b347cfca1](https://github.com/camera-2018/astrbot_plugin_fastbrain_proactive/tree/bd6b347cfca1cda4529e58865def8a0201edb136). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
