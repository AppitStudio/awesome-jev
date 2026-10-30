# wiki-agent-kit (Claude Code plugin for Wikimedia editors, with optional Jev citation checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Read-only Claude Code plugin for Wikipedia and other Wikimedia editors: translate articles, find and verify sources, and port content between wikis, with a human doing every publish. With a TypeSafe key, citation checks turn each claim and source passage into one Jev question (supports, contradicts or says nothing); confident verdicts are accepted and only unclear ones go to the chat model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muzaffar-murodovich/wiki-agent-kit) |
| Maintainer | [muzaffar-murodovich](https://github.com/muzaffar-murodovich). Independently curated. |
| Format | Claude Code plugin with a Python MCP server |
| Requirements | Claude Code, uv, and optionally a TypeSafe API key. |
| License | [MIT](https://github.com/muzaffar-murodovich/wiki-agent-kit/blob/5c7dbf57b932117f1fa380d564393bd1fb424b26/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`wikikit/jev.py`](https://github.com/muzaffar-murodovich/wiki-agent-kit/blob/5c7dbf57b932117f1fa380d564393bd1fb424b26/wikikit/jev.py) at the pinned commit. |

## When to use

- Check whether cited sources actually back each sentence before you edit a wiki article.
- Mismatch: Jev is optional; without a key the chat model does the checks.

## How it works

`wikikit/jev.py` posts claim-passage pairs to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; `wikikit/cite.py` uses the answer to accept or escalate each citation. Integration evidence: [`wikikit/jev.py`](https://github.com/muzaffar-murodovich/wiki-agent-kit/blob/5c7dbf57b932117f1fa380d564393bd1fb424b26/wikikit/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add muzaffar-murodovich/wiki-agent-kit
/plugin install wikikit@wiki-agent-kit
# set your contact and, optionally, the TypeSafe key in the plugin settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/muzaffar-murodovich/wiki-agent-kit#readme](https://github.com/muzaffar-murodovich/wiki-agent-kit#readme)

## Limits and data handling

Claims and source excerpts are sent to TypeSafe when Jev is enabled. The kit never publishes edits.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 5c7dbf57b932](https://github.com/muzaffar-murodovich/wiki-agent-kit/tree/5c7dbf57b932117f1fa380d564393bd1fb424b26). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
