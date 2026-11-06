# AstrBot whale reply gate (group-chat reply gate that uses Jev to decide when to answer or chime in)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AstrBot plugin that merges same-group messages and asks TypeSafe Jev whether to reply or proactively chime in, while the actual reply still uses AstrBot’s configured chat model and context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate) |
| Maintainer | [panchen00001-blip](https://github.com/panchen00001-blip). Independently curated. |
| Format | AstrBot Python plugin (AGPL-3.0) |
| Requirements | AstrBot, Python, and a TypeSafe API key (default API base `https://api.typesafe.ai/v1`). |
| License | [AGPL-3.0](https://github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/blob/a6572dbb9fd0af241e53dcd6afb297ba014419f2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`judge.py`](https://github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/blob/a6572dbb9fd0af241e53dcd6afb297ba014419f2/judge.py) at the pinned commit. |

## When to use

- Cut noisy group-chat replies by gating with Jev.
- Allow optional proactive interjections when Jev says so.
- Mismatch: AstrBot-specific; AGPL-3.0 license.

## How it works

`judge.py` builds an `AsyncTypeSafeClient` against TypeSafe and asks Choice/Noul questions about whether to reply; `decision.py` applies the gate. Integration evidence: [`judge.py`](https://github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/blob/a6572dbb9fd0af241e53dcd6afb297ba014419f2/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
# install as an AstrBot plugin, set the TypeSafe key in plugin settings (see _conf_schema.json)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/blob/a6572dbb9fd0af241e53dcd6afb297ba014419f2/README.md](https://github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/blob/a6572dbb9fd0af241e53dcd6afb297ba014419f2/README.md)
- judge.py: [github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/blob/a6572dbb9fd0af241e53dcd6afb297ba014419f2/judge.py](https://github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/blob/a6572dbb9fd0af241e53dcd6afb297ba014419f2/judge.py)

## Limits and data handling

Group message text considered by the gate is sent to TypeSafe on your key. Replies still go through AstrBot’s chat model.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit a6572dbb9fd0](https://github.com/panchen00001-blip/astrbot_plugin_whale_reply_gate/tree/a6572dbb9fd0af241e53dcd6afb297ba014419f2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
