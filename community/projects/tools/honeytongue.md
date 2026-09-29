# Honeytongue

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

NPC persuasion engine: TypeSafe Jev judges whether player dialogue convinced a character given persona and goals

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tbrought/honeytongue) |
| Maintainer | [tbrought](https://github.com/tbrought). Independently curated. |
| Format | JavaScript · library for text games (MIT). |
| Requirements | Node.js per upstream; TypeSafe API key for live judgments. |
| License | [MIT](https://github.com/tbrought/honeytongue/blob/2d5509c98bd5aceb13c1dd82d812b7653a641084/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Jev not run on the review host. |

## When to use

Use when a text game needs a typed “were they convinced?” judgment from a character’s values instead of free-form LLM roleplay alone.

## How it works

Supply persona + goal + player text; Jev returns a persuasion judgment the game code can branch on.

## Get started

```sh
git clone https://github.com/tbrought/honeytongue.git
cd honeytongue
git checkout 2d5509c98bd5aceb13c1dd82d812b7653a641084
# follow upstream README for API usage
```

## Examples and demos

Upstream README pitch and API sketch. No live judgment on the review host.

## Limits and data handling

Player dialogue is sent to TypeSafe when live. Treat persuasion quality as author-reported unless reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 2d5509c](https://github.com/tbrought/honeytongue/tree/2d5509c98bd5aceb13c1dd82d812b7653a641084). AI-assisted README + LICENSE inspection; live paths not executed.
