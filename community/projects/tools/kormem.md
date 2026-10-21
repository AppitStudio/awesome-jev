# kormem (local agent memory ranked by Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local long-term memory for coding agents with QMD-style commands: it files chats and documents into an Obsidian-compatible vault, and Jev judges the top 30 local matches for each question in parallel so the agent gets ranked, relevant sources in about 0.3 s.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kushalsinha/kormem) |
| Maintainer | [kushalsinha](https://github.com/kushalsinha). Independently curated. |
| Format | CLI, MCP server and agent skill (npm and PyPI `kormem`) |
| Requirements | Node.js or Python; `OPENAI_API_KEY` for filing; optional `TYPESAFE_API_KEY` for Jev ranking. |
| License | [MIT](https://github.com/kushalsinha/kormem/blob/e993cb0865ae4e03f62e50aea89472aac48f6925/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/sinkush/status/2112970927650611332)). |
| Jev evidence | [`packages/engine/kormem/retrieve/jev.py`](https://github.com/kushalsinha/kormem/blob/e993cb0865ae4e03f62e50aea89472aac48f6925/packages/engine/kormem/retrieve/jev.py) at the pinned commit. |

## When to use

- Give Claude Code, Codex or Cursor recall over past chats and files.
- Replace a slow recall agent with a fast Jev relevance pass on every question.
- Mismatch: without a TypeSafe key ranking stays local only.

## How it works

A free local pass (embeddings, keyword search, cross-encoder) finds candidate sources; `retrieve/jev.py` asks Jev whether each preview helps answer the question and the scores are merged with the local ranking (`jev-1.13.0` by default). Integration evidence: [`packages/engine/kormem/retrieve/jev.py`](https://github.com/kushalsinha/kormem/blob/e993cb0865ae4e03f62e50aea89472aac48f6925/packages/engine/kormem/retrieve/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g kormem   # or: pip install kormem
kormem init
# put OPENAI_API_KEY and TYPESAFE_API_KEY in ~/.kormem/.env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes on the Jev step: [github.com/kushalsinha/kormem/blob/main/docs/research/jev-decisions.md](https://github.com/kushalsinha/kormem/blob/main/docs/research/jev-decisions.md)
- README benchmarks: [github.com/kushalsinha/kormem#readme](https://github.com/kushalsinha/kormem#readme)

## Limits and data handling

Short previews of matching sources are sent to TypeSafe when the key is set; filing sends content to OpenAI. Benchmark figures are the author's.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit e993cb0865ae](https://github.com/kushalsinha/kormem/tree/e993cb0865ae4e03f62e50aea89472aac48f6925). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
