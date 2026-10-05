# dailypaper-skills

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Agent-skills pipeline (Chinese-language docs) that finds new papers from HuggingFace Daily/Trending and arXiv, uses TypeSafe Jev to score topic relevance against your research interests, then has your agent write reviews and Obsidian notes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/huangkiki/dailypaper-skills) |
| Maintainer | [huangkiki](https://github.com/huangkiki). Independently curated. |
| Format | Agent skill pack with Python helpers (`install.py`) and optional web viewer |
| Requirements | An agent that can read/write files, run commands and access the network; Python 3.10+, Git, curl; Poppler for PDF extraction. Default Jev scoring needs `TYPESAFE_API_KEY` in the agent's environment; a keyword-filter mode works without it. |
| License | [Apache-2.0](https://github.com/huangkiki/dailypaper-skills/blob/10c9921357dee38c8a342c8dd89b4b773758c104/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Get a daily, interest-filtered reading list without spending the host model's tokens on relevance scoring.
- Keep a linked Obsidian knowledge base of paper and concept notes, with Zotero as an optional source.
- Mismatch: the README and prompts are in Chinese; non-Chinese readers should expect to adapt the skills.

## How it works

`daily-papers-fetch` collects candidates; `skills/_shared/jev_ranker.py` sends your research interests as state and each paper's title and abstract as a Score question to `api.typesafe.ai/v1/systemone` (default `jev-1.13.0`), validates the returned model, distributions and usage, and keeps the scores visible. The host agent then writes the critique and full-paper notes ([`jev_ranker.py`](https://github.com/huangkiki/dailypaper-skills/blob/10c9921357dee38c8a342c8dd89b4b773758c104/skills/_shared/jev_ranker.py)).

## Get started

Clone, install the skills into your agent, create a config, and ask for today's papers (live Jev calls when the key is set):

```sh
git clone https://github.com/huangkiki/dailypaper-skills.git
cd dailypaper-skills
python3 install.py --agent codex   # or claude, cursor, copilot, gemini, opencode, openclaw
python3 skills/_shared/user_config.py --init
export TYPESAFE_API_KEY=...
# then, in the agent: 今日论文推荐  ("today's paper recommendations")
```

Relevance scoring contacts TypeSafe and incurs usage charges; reviews and notes use your host agent's model.

## Examples and demos

- [docs/jev-benchmark.md](https://github.com/huangkiki/dailypaper-skills/blob/10c9921357dee38c8a342c8dd89b4b773758c104/docs/jev-benchmark.md): a single maintainer-run comparison on 2026-10-05 (30 candidates, list-price cost of the scoring step only, 9/10 overlap with the LLM picks). Upstream-reported, not reproduced here.
- Linked video demo and `docs/usage.md` in the upstream README.

## Limits and data handling

Paper titles/abstracts and your research-interest list go to TypeSafe. The benchmark is one run of the scoring step; overlap with LLM picks is not a human quality evaluation. Offline unit tests exist upstream (`tests/test_jev_ranker.py`) but were not run here.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 10c9921357de](https://github.com/huangkiki/dailypaper-skills/tree/10c9921357dee38c8a342c8dd89b4b773758c104). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
