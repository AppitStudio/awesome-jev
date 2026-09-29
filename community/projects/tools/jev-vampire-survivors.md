# Jev Vampire Survivors

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

TypeSafe Jev picks character, stage, level-ups, and walk direction in real Steam Vampire Survivors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/oldmoldycake/jev_vampire_survivors) |
| Maintainer | [oldmoldycake](https://github.com/oldmoldycake). Independently curated. |
| Format | BepInEx plugin + Python brain: TypeSafe Jev plays real Steam Vampire Survivors with a live ops dashboard. |
| Requirements | Steam Vampire Survivors (Linux noted upstream); Python 3.12+; TypeSafe key; BepInEx. |
| License | [MIT](https://github.com/oldmoldycake/jev_vampire_survivors/blob/794e9a5fcfe5910a9001f3ac14da0fb8a07c36c9/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use as a game demo of fast typed decisions under live game state. Prefer simpler sims when you lack Steam/BepInEx.

## How it works

BepInEx exposes game state; Python brain asks Jev; dashboard streams decisions. Distinct from Mario/Pokémon Jev demos.

## Get started

```sh
git clone https://github.com/oldmoldycake/jev_vampire_survivors.git
cd jev_vampire_survivors
git checkout 794e9a5fcfe5910a9001f3ac14da0fb8a07c36c9
# follow upstream for BepInEx + brain setup
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 794e9a5](https://github.com/oldmoldycake/jev_vampire_survivors/tree/794e9a5fcfe5910a9001f3ac14da0fb8a07c36c9). AI-assisted README and license inspection; install/live paths not executed.
