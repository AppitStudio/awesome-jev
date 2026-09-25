# Claude x Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill and slash commands that use TypeSafe Jev (via OpenRouter) to classify, route, and gate so Claude deep-reads only the unsure items.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/charlesdove977/claude-x-jev) |
| Maintainer | [charlesdove977](https://github.com/charlesdove977). Independently curated. |
| Format | npm package `claude-x-jev` installer + Claude Code skill/commands; Python 3.8+ helper. |
| Requirements | `python3` ≥ 3.8; OpenRouter API key; Claude Code. |
| License | [MIT](https://github.com/charlesdove977/claude-x-jev/blob/c8662b0550b2a999d1dbcfb148683615cf92636a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Cost/latency comparison tables are author-reported; live OpenRouter/Claude Code paths not run on the review host. |

## When to use

Use when Claude Code should **pre-sort or gate** bulk items with cheap typed Jev calls. Prefer other Claude skills when you already have a TypeSafe-native connector and do not want OpenRouter.

## How it works

Install adds `/jev-setup`, `/jev-classify`, `/jev-route`, and `/jev-gate`. Jev answers Choice/Noul/Score; Claude handles reading and writing on the remainder.

## Get started

```sh
npx claude-x-jev install --with-commands
# Reviewed tree:
git clone https://github.com/charlesdove977/claude-x-jev.git
cd claude-x-jev
git checkout c8662b0550b2a999d1dbcfb148683615cf92636a
```

## Examples and demos

- README inbox labeling comparison (author-reported).
- Slash-command workflow in the skill docs.

## Limits and data handling

Item text goes to OpenRouter/TypeSafe Jev. Marketing links in the README are not part of this catalog entry. Comparison metrics are upstream-reported.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit c8662b0](https://github.com/charlesdove977/claude-x-jev/tree/c8662b0550b2a999d1dbcfb148683615cf92636a). AI-assisted README and LICENSE inspection; live install not executed.
