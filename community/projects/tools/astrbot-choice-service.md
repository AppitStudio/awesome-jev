# Choice Service (AstrBot plugin for typed choice and yes/no judgements over System One)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

AstrBot plugin that gives the bot and other plugins a shared judgement service: it calls Jev or another System One-compatible model with given options or yes/no propositions and returns structured results for proactive replies, intent routing and action choice, with built-in TypeSafe, OpenRouter and Vercel AI Gateway presets; Chinese documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lxfight/astrbot_plugin_choice_service) |
| Maintainer | [lxfight](https://github.com/lxfight). Independently curated. |
| Format | AstrBot plugin (Python) |
| Requirements | AstrBot 4.28 to below 5; a TypeSafe, OpenRouter or Vercel AI Gateway key, or a compatible endpoint. |
| License | [AGPL-3.0-or-later](https://github.com/lxfight/astrbot_plugin_choice_service/blob/2c9db72bc67712b032fc6b491cec7ee6bcdbcc87/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decision_service.py`](https://github.com/lxfight/astrbot_plugin_choice_service/blob/2c9db72bc67712b032fc6b491cec7ee6bcdbcc87/decision_service.py) at the pinned commit. |

## When to use

- Let an AstrBot chatbot decide whether to reply, wait or react with an emoji.
- Share one decision client across AstrBot plugins.
- Mismatch: AGPL-3.0 licensed; other providers can stand in for Jev.

## How it works

`decision_service.py` defaults to `https://api.typesafe.ai/v1/systemone` with `jev-latest` and offers OpenRouter and other presets; other plugins get the `DecisionService` directly, and `/choose` runs a choice from chat. Integration evidence: [`decision_service.py`](https://github.com/lxfight/astrbot_plugin_choice_service/blob/2c9db72bc67712b032fc6b491cec7ee6bcdbcc87/decision_service.py).

## Get started

From the upstream README (not run on the review host):

```sh
# AstrBot WebUI → Plugins → Install from link:
# https://github.com/lxfight/astrbot_plugin_choice_service
/choose Should the bot reply now? :: reply | wait | emoji only
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lxfight/astrbot_plugin_choice_service#readme](https://github.com/lxfight/astrbot_plugin_choice_service#readme)
- Releases: [github.com/lxfight/astrbot_plugin_choice_service/releases](https://github.com/lxfight/astrbot_plugin_choice_service/releases)

## Limits and data handling

Messages and options you judge go to the configured provider.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 2c9db72bc677](https://github.com/lxfight/astrbot_plugin_choice_service/tree/2c9db72bc67712b032fc6b491cec7ee6bcdbcc87). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
