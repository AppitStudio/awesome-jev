# claude-jev-funnel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin and zero-dependency Python CLI that batch TypeSafe Jev Noul/Choice/Score questions over many items, resolve confident ends in code, and send only the uncertain band to Claude or a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Shakibuzzaman3104/claude-jev-funnel) |
| Maintainer | [Shakibuzzaman3104](https://github.com/Shakibuzzaman3104). Independently curated. |
| Format | Claude Code plugin + `skills/jev/scripts/jev.py` CLI. |
| Requirements | Python 3.9+; TypeSafe API access; Claude Code for the plugin path. |
| License | [Apache-2.0](https://github.com/Shakibuzzaman3104/claude-jev-funnel/blob/05cc8fe9c2015b1dcd3e07da1404432ff307c8ed/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live funnel runs not executed. |

## When to use

Use to **cheaply triage** large item batches before spending frontier tokens. Prefer [ask-jev-skill](ask-jev-skill.md) for single Hermes tie-breaks.

## How it works

Code collects items → `jev.py` sends bulk typed questions → thresholds map to ACT/CONFIDENT vs UNCERTAIN/REVIEW → only the uncertain slice reaches Claude/human.

## Get started

```sh
git clone https://github.com/Shakibuzzaman3104/claude-jev-funnel.git
cd claude-jev-funnel
git checkout 05cc8fe9c2015b1dcd3e07da1404432ff307c8ed
# install Claude plugin per README; or run skills/jev/scripts/jev.py directly
```

## Examples and demos

- `benchmarks/` and `examples/`.
- CI workflow badge (not re-run here).

## Limits and data handling

Item text reaches TypeSafe. Threshold tuning is your responsibility.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 05cc8fe](https://github.com/Shakibuzzaman3104/claude-jev-funnel/tree/05cc8fe9c2015b1dcd3e07da1404432ff307c8ed). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [ask-jev-skill](ask-jev-skill.md), [askjev](askjev.md).
