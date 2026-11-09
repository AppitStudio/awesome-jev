# Jev Active Reply for AstrBot (Chinese group-chat plugin where Jev decides when the bot joins in)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AstrBot plugin that lets the bot join group chats naturally: Jev quickly decides whether a message is worth replying to and AstrBot's main model writes the reply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply) |
| Maintainer | [muyouzhi6](https://github.com/muyouzhi6). Independently curated. |
| Format | AstrBot plugin (Python, no license file) |
| Requirements | AstrBot 4.26.8+ (<5.0) with aiocqhttp, and a Jev key (official TypeSafe, a listed relay, or a custom Jev-format relay). |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client.py`](https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply/blob/ad75082bf4e62b9c5605961d940dac9ffd76acbb/client.py) at the pinned commit. |

## When to use

- Make a group bot speak only when it fits.
- Keep persona and memory in AstrBot's normal pipeline.
- Mismatch: no license file; ask the author before reuse. Third-party relays are an extra data party.

## How it works

`client.py` targets `https://api.typesafe.ai/v1/systemone` (`jev-latest`), a third-party Nanbei relay, or a custom relay; `policy.py` applies the reply decision. Integration evidence: [`client.py`](https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply/blob/ad75082bf4e62b9c5605961d940dac9ffd76acbb/client.py).

## Get started

Install from the AstrBot plugin market or repo URL, set the group scope, choose the Jev service and paste the key.

```sh
git clone https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/muyouzhi6/astrbot_plugin_jev_active_reply/blob/ad75082bf4e62b9c5605961d940dac9ffd76acbb/README.md](https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply/blob/ad75082bf4e62b9c5605961d940dac9ffd76acbb/README.md)

## Limits and data handling

Chat messages go to the selected Jev service (official or relay).

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit ad75082bf4e6](https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply/tree/ad75082bf4e62b9c5605961d940dac9ffd76acbb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
