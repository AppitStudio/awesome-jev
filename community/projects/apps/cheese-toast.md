# Cheese Toast

[All projects](../README.md) · [Web apps](README.md#web-apps)

Jim Bumgardner's teapot-in-space arcade game ported to JavaScript and canvas; TypeSafe Jev moderates new high-score names and can play the game as a bot.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jbum/cheesetoast) |
| Tags | `Open source` · `Free` |
| Product homepage | [ct.krazydad.com](https://ct.krazydad.com) |
| Pricing and access | Free to play online; self-hosting the score server with Jev moderation needs your own TypeSafe key. |
| Jev evidence | [`bots/policies/jev.mjs`](https://github.com/jbum/cheesetoast/blob/05082694c797dae0ae34067016f3bcf46b8401c3/bots/policies/jev.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [jbum](https://github.com/jbum). Independently curated. |
| Format | Browser game (JavaScript) + Python score server |
| Platform and availability | Web (play at ct.krazydad.com; self-host with Python score server) |
| Jev's role | Jev checks new score-table names for PG-13 compliance (moderator override available) and, as an optional bot policy, reads a symbolic game view and picks controls. |
| Requirements | Browser; for self-hosted scores: Python 3 and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/jbum/cheesetoast/blob/05082694c797dae0ae34067016f3bcf46b8401c3/LICENSE) |

## When to use

- Play the game; study a small example of name moderation and a game-playing decision policy.
- Mismatch: Jev is a side feature, not the gameplay.

## How it works

The score server sends each new name to Jev before accepting it; the bot harness renders a symbolic state and asks Jev for control choices each tick. (Summarized from the upstream [README](https://github.com/jbum/cheesetoast/blob/05082694c797dae0ae34067016f3bcf46b8401c3/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): play at ct.krazydad.com, or run `python3 tools/serve.py` locally.

## Limits and data handling

Submitted names (and bot states) go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 05082694c797](https://github.com/jbum/cheesetoast/tree/05082694c797dae0ae34067016f3bcf46b8401c3). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
