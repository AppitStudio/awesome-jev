# jeff (Discord bot)

[All projects](../README.md) · [Discord bots](README.md#discord-bots)

Discord bot built with botbox where every feature is a typed Jev question: settle debates, rank lists, tag forum posts with the forum's own tags, answer FAQ repeats, and track unanswered help questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saembit/jeff-bot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/saembit/jeff-bot#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-19. |
| Jev evidence | [`src/utils/jev.py`](https://github.com/saembit/jeff-bot/blob/7adc0a2ad5c817dda5d60a2dfc497f3f8a3e36ad/src/utils/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [saembit](https://github.com/saembit). Independently curated. |
| Format | Discord bot (Python, botbox) |
| Platform and availability | Self-hosted Discord bot. |
| Jev's role | Every command is one Jev request with a few typed questions; code owns the thresholds. |
| Requirements | Discord bot token; TypeSafe API key. |
| License | [MIT](https://github.com/saembit/jeff-bot/blob/7adc0a2ad5c817dda5d60a2dfc497f3f8a3e36ad/LICENSE) |

## When to use

- Give a server quick, probability-backed judgments for debates and tagging.
- Mismatch: self-host only; not a spam moderation bot.

## How it works

`src/utils/jev.py` calls the System One API with `TYPESAFE_API_KEY`; commands like `/settle` post the pick with probabilities and confidence. Integration evidence: [`src/utils/jev.py`](https://github.com/saembit/jeff-bot/blob/7adc0a2ad5c817dda5d60a2dfc497f3f8a3e36ad/src/utils/jev.py).

## Get started

From the upstream README: create a Discord bot, set the token and TypeSafe key, then run the bot.

```sh
git clone https://github.com/saembit/jeff-bot
# set DISCORD token and TYPESAFE_API_KEY per README, then run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README Commands section

## Limits and data handling

Message text you pass to commands goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 7adc0a2ad5c8](https://github.com/saembit/jeff-bot/tree/7adc0a2ad5c817dda5d60a2dfc497f3f8a3e36ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
