# Deeds

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and Claude Code plugin that reads every commit diff and counts what actually got built (new, deepened, regressed, removed capabilities); TypeSafe Jev answers typed questions per commit and a fixed policy turns them into counts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danielmiessler/Deeds) |
| Product homepage | [workdeeds.ai](https://workdeeds.ai) |
| Maintainer | [danielmiessler](https://github.com/danielmiessler). Independently curated. |
| Format | CLI (release tarball installer with sha256 check) and Claude Code plugin |
| Requirements | Bun and `TYPESAFE_API_KEY` (the only key needed in default `jev` mode); `--mode full` uses Anthropic or OpenAI instead. |
| License | [MIT](https://github.com/danielmiessler/Deeds/blob/072e9b1af26f5025abadb010f166c720dde228ef/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Measure real shipped capability rather than commit or line counts across a repo's history.
- Ask Claude Code "show me deeds progress" via the plugin.
- Mismatch: if diffs must not leave your machine, do not run it (diffs go to Jev).

## How it works

Code extracts exact facts from each diff (files, routes/commands added or removed, size); Jev answers a short set of typed questions; a fixed policy combines facts and answers. Results are cached per commit; docs-only, lockfile, and merge commits are settled by code without a call ([README](https://github.com/danielmiessler/Deeds/blob/072e9b1af26f5025abadb010f166c720dde228ef/README.md)).

## Get started

Install and analyze a repo (live Jev calls, one per commit that needs judging):

```sh
export TYPESAFE_API_KEY=...
curl -fsSL https://raw.githubusercontent.com/danielmiessler/deeds/main/install.sh | sh
deeds version
deeds analyze . --since 30d
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README example run over danielmiessler/LifeOS (717 commits) with `examples/lifeos.html`.

## Limits and data handling

Each commit's diff and changed paths go to TypeSafe on your key (secret-shaped strings are redacted first). First runs cost one call per judged commit; later runs use the cache.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 072e9b1af26f](https://github.com/danielmiessler/Deeds/tree/072e9b1af26f5025abadb010f166c720dde228ef). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
