# Alpha (personal signal feed that judges X, GitHub, Hugging Face and Substack finds with Jev and Claude, then turns them into agent skills)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Self-hosted feed that pulls from your X bookmarks and timelines, GitHub stars and trending, Hugging Face likes, Substacks and papers, keeps only items it judges useful, and turns them into skills your agents read through an MCP server. A shared judge scores candidates against your focus briefs with Jev and a second pass with Claude; an item becomes a find only when both agree.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juandi-net/alpha-oss) |
| Maintainer | [juandi-net](https://github.com/juandi-net). Independently curated. |
| Format | Python app (uv), SQLite warehouse, local dashboard and MCP server |
| Requirements | Python with uv, an Anthropic API key (`ALPHA_CLAUDE_API_KEY`) and a `TYPESAFE_API_KEY`; sources are off until enabled in `config.toml`. |
| License | [MIT](https://github.com/juandi-net/alpha-oss/blob/5f7d0f205910f8cf0bf5c685ca47c8f18c1d96a3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`alpha/jev.py`](https://github.com/juandi-net/alpha-oss/blob/5f7d0f205910f8cf0bf5c685ca47c8f18c1d96a3/alpha/jev.py) at the pinned commit. |

## When to use

- Filter a noisy research feed with a cheap typed judge before an LLM sees it.
- See a two-judge (Jev plus Claude) agreement pattern.
- Mismatch: needs several accounts and keys; the README notes Jev is strict about usable-now items.

## How it works

`alpha/jev.py` holds the Jev question definitions and the idea rule; `judge.py` runs stage 1 (Jev scores title and preview against focus briefs) and stage 2 (full text to Jev and Claude). Integration evidence: [`alpha/jev.py`](https://github.com/juandi-net/alpha-oss/blob/5f7d0f205910f8cf0bf5c685ca47c8f18c1d96a3/alpha/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv run alpha run
uv run alpha install   # launchd: a run every 6 hours plus the dashboard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the judge pipeline: [github.com/juandi-net/alpha-oss/blob/5f7d0f205910f8cf0bf5c685ca47c8f18c1d96a3/README.md](https://github.com/juandi-net/alpha-oss/blob/5f7d0f205910f8cf0bf5c685ca47c8f18c1d96a3/README.md)

## Limits and data handling

Item text from your sources goes to TypeSafe and Anthropic on your keys; behaviour of the two judges depends on your taste profile and briefs. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 5f7d0f205910](https://github.com/juandi-net/alpha-oss/tree/5f7d0f205910f8cf0bf5c685ca47c8f18c1d96a3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
