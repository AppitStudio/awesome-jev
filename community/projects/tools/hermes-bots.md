# Hermes Bots plugin

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Hermes agent plugin behind the Hermes Bots mobile app: native cards and forms, phone alerts, voice, model routing, and a card guard where Jev decides in about 0.2 s whether a prose reply should become a card.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/clearspace-to/hermes-bots) |
| Maintainer | [clearspace-to](https://github.com/clearspace-to). Independently curated. |
| Format | Hermes plugin (Python) |
| Requirements | Hermes 0.21.5+, the Hermes Bots connector for phone alerts; an OpenRouter key for the Jev card guard and routing reviews. |
| License | [Apache-2.0](https://github.com/clearspace-to/hermes-bots/blob/bfa3f7e31ec27f21469219d35192552ad27efb3a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cards/guard.py`](https://github.com/clearspace-to/hermes-bots/blob/bfa3f7e31ec27f21469219d35192552ad27efb3a/cards/guard.py) at the pinned commit. |

## When to use

- Run Hermes bots you answer from a phone with cards and alerts.
- Want replies that should be forms turned into cards automatically.
- Mismatch: needs the Hermes Bots connector and app for the mobile parts.

## How it works

The `cards` module adds card and form tools, approval and question hooks, and a task board. `cards/guard.py` sends replies that carry no card to `typesafe/jev-1.13` through OpenRouter's decisions API; only when Jev says card does the auxiliary model build one. The guard is fail-open and off by default. The `routing` module adds per-turn model and effort routing with Jev reviews. Integration evidence: [`cards/guard.py`](https://github.com/clearspace-to/hermes-bots/blob/bfa3f7e31ec27f21469219d35192552ad27efb3a/cards/guard.py).

## Get started

From the upstream README: `hermes plugins install <repo>` and `hermes plugins enable hermes-bots`, then restart `hermes serve`.

```sh
hermes plugins install https://github.com/clearspace-to/hermes-bots
hermes plugins enable hermes-bots
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README module table (cards, mobile, voice, routing)

## Limits and data handling

Reply text goes to OpenRouter when the card guard is on. Decisions are logged without content.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit bfa3f7e31ec2](https://github.com/clearspace-to/hermes-bots/tree/bfa3f7e31ec27f21469219d35192552ad27efb3a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
