# BetterChat (AstrBot plugin that waits for you to finish typing and uses Jev to decide when to speak in group chats)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AstrBot plugin with two features: in private chats it merges messages sent in a burst and cancels stale replies, and in group chats it asks Jev whether the bot should join in, including filtering @-mentions that need no reply. Chinese documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AS214933/astrbot-betterchat) |
| Maintainer | [AS214933](https://github.com/AS214933). Independently curated. |
| Format | AstrBot plugin (Python) |
| Requirements | An AstrBot install; a TypeSafe key (or an OpenCode endpoint) for group-chat judgments. |
| License | [MIT](https://github.com/AS214933/astrbot-betterchat/blob/4d3d69ee67ad2d08ffccaed50c18bc61cdce7f81/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`betterchat_jev.py`](https://github.com/AS214933/astrbot-betterchat/blob/4d3d69ee67ad2d08ffccaed50c18bc61cdce7f81/betterchat_jev.py) at the pinned commit. |

## When to use

- Make a chat bot speak up in groups only when it is useful.
- Mismatch: private-chat merging works without Jev.

## How it works

`betterchat_jev.py` calls `https://api.typesafe.ai/v1/systemone` (or an OpenCode-hosted System One endpoint) with recent group context and asks for a probability; the threshold policy lives in the plugin code. Integration evidence: [`betterchat_jev.py`](https://github.com/AS214933/astrbot-betterchat/blob/4d3d69ee67ad2d08ffccaed50c18bc61cdce7f81/betterchat_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
cd AstrBot/data/plugins
git clone https://github.com/AS214933/astrbot-betterchat.git
# reload plugins in the WebUI, then set the Jev key in the plugin config
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README (Chinese): [github.com/AS214933/astrbot-betterchat#readme](https://github.com/AS214933/astrbot-betterchat#readme)

## Limits and data handling

Group chat context is sent to TypeSafe for each judgment. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 4d3d69ee67ad](https://github.com/AS214933/astrbot-betterchat/tree/4d3d69ee67ad2d08ffccaed50c18bc61cdce7f81). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
