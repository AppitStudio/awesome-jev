# web-scout-ai

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Agentic Python web-research pipeline that opens and extracts the sources it finds and returns a cited answer with an audit trail; semantic classification and follow-up link selection default to TypeSafe Jev, with generative models doing extraction and synthesis.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RSO9192/web-scout-ai) |
| Product homepage | [pypi.org](https://pypi.org/project/web-scout-ai/) |
| Maintainer | [RSO9192](https://github.com/RSO9192). Independently curated. |
| Format | Python library + setup CLI (PyPI `web-scout-ai`, 1.8.1 at review) |
| Requirements | Python 3.13 (pyproject `>=3.13,<3.14`); Patchright Chromium (`web-scout-setup`); Amazon Bedrock credentials (default research models), Serper key for open-web search, Gemini key for vision fallback, `TYPESAFE_API_KEY` for the default Jev classification and link selection. |
| License | [MIT](https://github.com/RSO9192/web-scout-ai/blob/70016230c5e4befc8e527cdca0958747826f07a8/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run research questions that must cite pages the pipeline actually read, with a list of what was blocked or failed.
- Restrict research to chosen domains or extract a known URL while Jev picks follow-up links within budget.
- Mismatch: several paid providers are required by default; scraping must respect site terms.

## How it works

Generative models write queries, extract facts and synthesize. [`jev_link_selector.py`](https://github.com/RSO9192/web-scout-ai/blob/70016230c5e4befc8e527cdca0958747826f07a8/src/web_scout/jev_link_selector.py) asks Jev which discovered follow-up links are worth opening, and semantic classification also defaults to Jev (`WEB_SCOUT_CLASSIFICATION_BACKEND=gpt` switches back). The result object lists scraped, failed and bot-detected URLs.

## Get started

Install, set up the browser, configure keys, then run a question:

```sh
pip install web-scout-ai
web-scout-setup
export TYPESAFE_API_KEY=...   # plus Bedrock, SERPER_API_KEY, GEMINI_API_KEY
python -c 'import asyncio; from web_scout import run_web_research; r=asyncio.run(run_web_research("your question")); print(r.synthesis)'
```

Live runs call Bedrock, Serper, Gemini and TypeSafe; each bills separately.

## Examples and demos

- README quick start and the three modes (open-web, domain-restricted, direct URL extraction); [tests/test_jev_link_selector.py](https://github.com/RSO9192/web-scout-ai/blob/70016230c5e4befc8e527cdca0958747826f07a8/tests/test_jev_link_selector.py) shows the Jev selector contract offline.
- [Performance report](https://github.com/RSO9192/web-scout-ai/blob/70016230c5e4befc8e527cdca0958747826f07a8/docs/performance.md) with the maintainer's measurements.

## Limits and data handling

Page text and link candidates go to TypeSafe and the other configured providers. The browser fallback may not pass all bot protections (reported, not hidden). Performance figures are upstream. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 70016230c5e4](https://github.com/RSO9192/web-scout-ai/tree/70016230c5e4befc8e527cdca0958747826f07a8). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
