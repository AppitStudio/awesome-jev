# astrbot_plugin_jev_gate (AstrBot plugin: Jev decides when a group-chat bot should speak up)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AstrBot plugin that has Jev score each group-chat message and triggers one proactive reply only when it is worth joining in, with persona, questions, thresholds, cooldowns, daily caps and a dry-run audit mode; the reply itself is still written by AstrBot's main LLM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sodapopper-pixel/astrbot_plugin_jev_gate) |
| Maintainer | [Sodapopper-pixel](https://github.com/Sodapopper-pixel). Independently curated. |
| Format | AstrBot plugin (Python) |
| Requirements | An AstrBot instance; a TypeSafe API key. |
| License | [MIT](https://github.com/Sodapopper-pixel/astrbot_plugin_jev_gate/blob/c4636b83616f20e71545544fca2e24255f1e4f37/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`main.py`](https://github.com/Sodapopper-pixel/astrbot_plugin_jev_gate/blob/c4636b83616f20e71545544fca2e24255f1e4f37/main.py) at the pinned commit. |

## When to use

- Let a group bot join conversations sparingly instead of replying to everything.
- Audit scores in dry-run mode before turning on real triggers.
- Mismatch: README is in Chinese; the plugin only decides when to speak, not what to say.

## How it works

`main.py` posts each message with recent context to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default, or a compatible endpoint you set) and triggers AstrBot's reply pipeline above the threshold. Integration evidence: [`main.py`](https://github.com/Sodapopper-pixel/astrbot_plugin_jev_gate/blob/c4636b83616f20e71545544fca2e24255f1e4f37/main.py).

## Get started

From the upstream README (not run on the review host):

```sh
# AstrBot WebUI → Plugins → Install → https://github.com/Sodapopper-pixel/astrbot_plugin_jev_gate
# then set your TypeSafe API key in the plugin config
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/Sodapopper-pixel/astrbot_plugin_jev_gate#readme](https://github.com/Sodapopper-pixel/astrbot_plugin_jev_gate#readme)

## Limits and data handling

Group messages are sent to TypeSafe. Distinct from the listed astrbot_plugin_jev_router.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit c4636b83616f](https://github.com/Sodapopper-pixel/astrbot_plugin_jev_gate/tree/c4636b83616f20e71545544fca2e24255f1e4f37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
