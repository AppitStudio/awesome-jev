# jev-search (AnthonyDavidAdams)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python library/CLI for agentic search where fetch and parse stay deterministic and only candidate decisions go to TypeSafe Jev (OpenRouter) or local Laya.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AnthonyDavidAdams/jev-search) |
| Maintainer | [AnthonyDavidAdams](https://github.com/AnthonyDavidAdams). Independently curated. Part of EarthPilot. |
| Format | Python stdlib library + CLI + agent skill. |
| Requirements | Python 3.9+; OpenRouter key for hosted Jev, or Apple Silicon + Laya for local. |
| License | [MIT](https://github.com/AnthonyDavidAdams/jev-search/blob/407eba58fd21178c47f8787dd47f69c0d0ceeff8/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Distinct from the Jev Search web app. |

## When to use

Use when browsing agents waste tokens **reading whole pages** to pick a link. Prefer the hosted [Jev Search](../apps/jev-search.md) app for a UI over Search1API.

## How it works

[`jev_search/client.py`](https://github.com/AnthonyDavidAdams/jev-search/blob/407eba58fd21178c47f8787dd47f69c0d0ceeff8/jev_search/client.py) and rank/score modules send option lists to the Decisions API; crawl/extract stay local.

## Get started

```sh
git clone https://github.com/AnthonyDavidAdams/jev-search.git
cd jev-search
git checkout 407eba58fd21178c47f8787dd47f69c0d0ceeff8
# install per upstream README; set OPENROUTER_API_KEY for hosted Jev
```

## Examples and demos

- `examples/` pilots and `docs/race.gif`.
- Agent skill under `skills/jev-search/`.

## Limits and data handling

Candidate strings go to OpenRouter→Jev (or local Laya). Upstream 100–1000× cheaper claims are author-measured on specific pilots.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 407eba5](https://github.com/AnthonyDavidAdams/jev-search/tree/407eba58fd21178c47f8787dd47f69c0d0ceeff8). AI-assisted README and LICENSE inspection of client/rank modules; install/live paths not executed.
