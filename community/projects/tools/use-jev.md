# use-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code/Codex skill: hand bounded choice/score/noul decisions to TypeSafe Jev via OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kmasterrr/use-jev) |
| Maintainer | [Kmasterrr](https://github.com/Kmasterrr). Independently curated. |
| Format | Claude Code / Codex skill handing bounded decisions to typesafe/jev-1.13 via OpenRouter. |
| Requirements | Claude Code or Codex; OpenRouter access to typesafe/jev-1.13 per upstream. |
| License | [MIT](https://github.com/Kmasterrr/use-jev/blob/317a53da4fe9273a72a53c2f7defc7885e4c2c13/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when an agent should route/detect/score with Jev and write prose itself. Prefer direct SDKs for non-agent apps.

## How it works

Skill documents patterns (route, gate, score, repeat) calling Jev through OpenRouter; agent remains workflow owner.

## Get started

```sh
git clone https://github.com/Kmasterrr/use-jev.git
cd use-jev
git checkout 317a53da4fe9273a72a53c2f7defc7885e4c2c13
# install skill per upstream README
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 317a53d](https://github.com/Kmasterrr/use-jev/tree/317a53da4fe9273a72a53c2f7defc7885e4c2c13). AI-assisted README and license inspection; install/live paths not executed.
