# MemexOS (memory OS that turns what you read and watch into a reviewed wiki your agents can search, with Jev as an optional judge)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Collects what you save (YouTube, Bilibili, X bookmarks, RSS, links), decides what is worth keeping, and compiles it into a reviewed, linked wiki that agents can search. Small yes/no judgments such as self-checks and reranking can go to a local model or, optionally, Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/liushengyu/memexos) |
| Maintainer | [liushengyu](https://github.com/liushengyu). Independently curated. |
| Format | Python CLI with a local web console |
| Requirements | macOS or Linux; worker model access; optional Jev key (`JEV_API_KEY`). |
| License | [MIT](https://github.com/liushengyu/memexos/blob/8c80e3d37da55d62e954951aa6b46cc32adc4c2d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/memexos/judge.py`](https://github.com/liushengyu/memexos/blob/8c80e3d37da55d62e954951aa6b46cc32adc4c2d/src/memexos/judge.py) at the pinned commit. |

## When to use

- Build a personal knowledge base that coding agents can query.
- Mismatch: Jev is one optional judge backend.

## How it works

`src/memexos/judge.py` answers fixed-format questions for the self-check, category screen, inbox ranking and reranking; with `[judge] backend = "jev"` it calls `https://api.typesafe.ai/v1/systemone` (`jev-latest`) as configured in `src/memexos/default_config.toml`. Integration evidence: [`src/memexos/judge.py`](https://github.com/liushengyu/memexos/blob/8c80e3d37da55d62e954951aa6b46cc32adc4c2d/src/memexos/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/liushengyu/memexos/main/install.sh | sh
memex setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Chinese README: [github.com/liushengyu/memexos/blob/main/README.zh-CN.md](https://github.com/liushengyu/memexos/blob/main/README.zh-CN.md)

## Limits and data handling

With the Jev judge on, the sentences being judged are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 8c80e3d37da5](https://github.com/liushengyu/memexos/tree/8c80e3d37da55d62e954951aa6b46cc32adc4c2d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
