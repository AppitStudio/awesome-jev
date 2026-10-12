# bouncer (Faycall1l)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Programmable live-chat moderator that applies per-server rules in one System One pass (~30ms). Built primarily on Laya with Jev-compatible typed decisions; Discord/Twitch adapters included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Faycall1l/bouncer) |
| Maintainer | [Faycall1l](https://github.com/Faycall1l). Independently curated. |
| Format | Python · Discord/Twitch/webhook adapters |
| Requirements | Python 3.10+; Laya or Jev-compatible System One endpoint. |
| License | [Apache-2.0](https://github.com/Faycall1l/bouncer/blob/0c32b11e0099d473d7e8c7131f0f85fe505000d1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Moderate live chat with typed allow/timeout decisions without per-community retraining.
- Mismatch: Default path is Laya; confirm Jev endpoint if you need TypeSafe hosted.

## How it works

Gatekeeper package loads rules, calls the System One adapter, and enforces actions. Code under [`src/gatekeeper/`](https://github.com/Faycall1l/bouncer/tree/0c32b11e0099d473d7e8c7131f0f85fe505000d1/src/gatekeeper).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Faycall1l/bouncer.git
cd bouncer
# install + configure per README
```

## Limits and data handling

Chat text goes to the configured System One provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 0c32b11e0099](https://github.com/Faycall1l/bouncer/tree/0c32b11e0099d473d7e8c7131f0f85fe505000d1). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
