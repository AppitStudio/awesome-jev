# Keeping an NPC on quest

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Companion code for Old Nain episode 002: a local-LLM NPC kept on quest with staged facts, while TypeSafe Jev classifies player messages and checks every NPC line for leaks, inventions and broken character.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ghosthat-studio/keeping-an-npc-on-quest) |
| Maintainer | [ghosthat-studio](https://github.com/ghosthat-studio). Independently curated. |
| Format | Python tutorial project |
| Requirements | Python; local LLM per README; TypeSafe key. |
| License | [Apache-2.0](https://github.com/ghosthat-studio/keeping-an-npc-on-quest/blob/01afd4f26e3afabeb4411c272649e6db7cf66c92/LICENSE) |
| Jev evidence | [`src/npc_on_quest/judge.py`](https://github.com/ghosthat-studio/keeping-an-npc-on-quest/blob/01afd4f26e3afabeb4411c272649e6db7cf66c92/src/npc_on_quest/judge.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Learn a pattern for guarding generated dialogue with typed checks.
- Mismatch: author marks it for educational use only.

## How it works

Code stages which facts the local model may see; Jev answers one Choice (message type) and four Nouls per line, and code decides what the NPC does. (Summarized from the upstream [README](https://github.com/ghosthat-studio/keeping-an-npc-on-quest/blob/01afd4f26e3afabeb4411c272649e6db7cf66c92/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow the README to install and run the episode code.

## Limits and data handling

Player and NPC lines go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 01afd4f26e3a](https://github.com/ghosthat-studio/keeping-an-npc-on-quest/tree/01afd4f26e3afabeb4411c272649e6db7cf66c92). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
