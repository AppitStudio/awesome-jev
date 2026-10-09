# jev-plays-runescape

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Archived hobby project in which Jev picks every action (chop, walk, bank, deposit, wait) for a character on a private, local 2004Scape/LostCity server via rs-sdk, with live probability overlays and local safety vetoes for death and low HP.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vhsgreed/jev-plays-runescape) |
| Maintainer | [vhsgreed](https://github.com/vhsgreed). Independently curated. |
| Format | Game-agent demo (archived) |
| Requirements | Local LostCity/2004Scape emulator and rs-sdk; Jev access (README links the OpenRouter Jev model page). |
| License | [MIT](https://github.com/vhsgreed/jev-plays-runescape/blob/02a0cb942c48b21ca5754c2138212c2ec1e9ccb5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- See a decision model drive a simple game loop with calibrated per-action probabilities.
- Mismatch: archived; local emulator only, and it must not be used against Old School RuneScape.

## How it works

Game state becomes state text; Jev makes a choice over five actions plus a threat score; ordinary code performs pathfinding and overrides the model when dead, low on HP, or looping. (Summarized from the upstream [README](https://github.com/vhsgreed/jev-plays-runescape/blob/02a0cb942c48b21ca5754c2138212c2ec1e9ccb5/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): See the upstream README for setup against a local 2004Scape server.

## Limits and data handling

Runs against a local private server only. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 02a0cb942c48](https://github.com/vhsgreed/jev-plays-runescape/tree/02a0cb942c48b21ca5754c2138212c2ec1e9ccb5). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
