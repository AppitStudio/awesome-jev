# maibot-jev-gate (MaiBot plugin: Jev pre-judges ambiguous group-chat messages)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MaiBot plugin that asks Jev about group-chat messages only when the host's local reply gate is undecided, blends Jev's reply probability with the local one weighted by Jev's confidence, and can mark background chatter as read without waking the planner; multiple provider profiles can be saved and switched in the WebUI; Chinese documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HaoxiangXia/maibot-jev-gate) |
| Maintainer | [HaoxiangXia](https://github.com/HaoxiangXia). Independently curated. |
| Format | MaiBot plugin (Python) |
| Requirements | MaiBot; a TypeSafe API key, or another System One-compatible endpoint configured as a profile. |
| License | [GPL-3.0](https://github.com/HaoxiangXia/maibot-jev-gate/blob/46680248071851cee7f9e9cb70bfe84afc1c9fbb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/HaoxiangXia/maibot-jev-gate/blob/46680248071851cee7f9e9cb70bfe84afc1c9fbb/jev_client.py) at the pinned commit. |

## When to use

- Cut planner calls in busy MaiBot group chats without changing the reply-frequency slider's behaviour.
- Let a cheap decision model settle only the borderline messages.
- Mismatch: MaiBot only; profiles may point at third-party relays, which are not TypeSafe.

## How it works

`jev_client.py` defaults to `https://api.typesafe.ai/v1` with `jev-latest` and posts the recent messages with reply questions to `/v1/systemone`; the plugin returns the fused probability, or a silent-consume decision at high confidence, to MaiBot's reply gate. Integration evidence: [`jev_client.py`](https://github.com/HaoxiangXia/maibot-jev-gate/blob/46680248071851cee7f9e9cb70bfe84afc1c9fbb/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
# copy the plugin folder into MaiBot's plugins directory, then in the WebUI
# add a profile with your TypeSafe api_key, base_url https://api.typesafe.ai/v1 and model jev-latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/HaoxiangXia/maibot-jev-gate#readme](https://github.com/HaoxiangXia/maibot-jev-gate#readme)

## Limits and data handling

Recent group-chat messages in the ambiguous band go to the configured provider. GPL-3.0 licensed.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 466802480718](https://github.com/HaoxiangXia/maibot-jev-gate/tree/46680248071851cee7f9e9cb70bfe84afc1c9fbb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
