# 2048 with Jev

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

2048 experiment where a bot chooses moves via the TypeSafe SDK (`typesafe-sdk`, pinned) using a fixed Jev model id so runs do not silently follow `jev-latest` alias moves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abarslan04/2048-with-jev) |
| Maintainer | [abarslan04](https://github.com/abarslan04). Independently curated. |
| Format | Python 2048 bot + game UI pieces |
| Requirements | Python; typesafe-sdk; TypeSafe API key. |
| License | [MIT](https://github.com/abarslan04/2048-with-jev/blob/46b77e576754fa0ba11978241c87c24ec3cad2f4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bot/config.py`](https://github.com/abarslan04/2048-with-jev/blob/46b77e576754fa0ba11978241c87c24ec3cad2f4/bot/config.py) at the pinned commit. |

## When to use

- Toy environment for Jev move selection on 2048.
- Want pinned model ids for reproducible bot runs.
- Mismatch: experiment; crowded games category—listed as a small pinned-SDK demo.

## How it works

`bot/config.py` documents Jev via `typesafe-sdk` with a pinned model rather than `jev-latest`. The bot asks typed questions for each move. Integration evidence: [`bot/config.py`](https://github.com/abarslan04/2048-with-jev/blob/46b77e576754fa0ba11978241c87c24ec3cad2f4/bot/config.py).

## Get started

Clone, install deps including typesafe-sdk, set credentials, run the bot.

```sh
git clone https://github.com/abarslan04/2048-with-jev && cd 2048-with-jev
# pip install -r requirements (see README); set TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- bot/config.py pin notes
- README experiment description

## Limits and data handling

Toy scale. Live play bills TypeSafe. Not a competitive 2048 solver claim.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 46b77e576754](https://github.com/abarslan04/2048-with-jev/tree/46b77e576754fa0ba11978241c87c24ec3cad2f4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
