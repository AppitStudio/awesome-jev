# fast-jev-compaction-opencode

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

opencode plugin for verbatim session compaction via probabilistic keep/drop judgments (based on `tamaratran/fast-jev-compaction`); default judge is a local OpenAI-compatible endpoint (LM Studio), not hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dex-community/fast-jev-compaction-opencode) |
| Maintainer | [dex-community](https://github.com/dex-community). Independently curated. |
| Format | opencode plugin (`plugin/jev-compact.ts`) wrapping published fast-jev-compaction library. |
| Requirements | opencode; local OpenAI-compatible judge (LM Studio default) or other configured endpoint. |
| License | [MIT](https://github.com/dex-community/fast-jev-compaction-opencode/blob/86c675f8f2c38cef11a2d6a028d27298869d3239/LICENSE). Upstream Claude Code path uses TypeSafe Jev; this fork defaults to local judge. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Default path is local LM Studio—not hosted TypeSafe Jev—disclose when recommending. Live opencode/compaction not run on the review host. |

## When to use

Use when opencode sessions need Jev-style keep/drop compaction without rewriting text messages. Prefer the upstream Claude Code plugin when you want hosted TypeSafe Jev as judge.

## How it works

Builds conversation state, asks probability questions per non-pinned tool call/result, deletes judged-unneeded tool turns, preserves text verbatim; opencode write-back via `session.revert` + tail re-injection. Invoked via `/jev-compact` or `jev_compact` tool.

## Get started

```sh
git clone https://github.com/dex-community/fast-jev-compaction-opencode.git
cd fast-jev-compaction-opencode
git checkout 86c675f8f2c38cef11a2d6a028d27298869d3239
# follow upstream for opencode plugin install + LM Studio endpoint
```

## Examples and demos

- Upstream comparison table vs Claude Code / TypeSafe path.
- Library used as published from `tamaratran/fast-jev-compaction`.

## Limits and data handling

Local judge keeps history on your machine; pointing at hosted Jev would send history to TypeSafe. Catalog checks did not run compaction.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 86c675f](https://github.com/dex-community/fast-jev-compaction-opencode/tree/86c675f8f2c38cef11a2d6a028d27298869d3239). AI-assisted README and license inspection; install/live paths not executed.
