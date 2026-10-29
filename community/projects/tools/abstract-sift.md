# Abstract Sift (screen research abstracts against your interests with Jev, OpenAI Decisions or both)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local CLI for screening conference or paper abstracts against a research-interest text with Jev, OpenAI Decisions or both side by side, with agreement and disagreement reports. Concurrent, resumable scoring, cost estimates and a `--max-cost-usd` cap, CSV/JSONL exports and an offline HTML report; an ESMO 2026 run guide is included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ValiusSciences/abstract-sift) |
| Maintainer | [ValiusSciences](https://github.com/ValiusSciences). Independently curated. |
| Format | Python CLI (uv) |
| Requirements | Python with uv and a TypeSafe key (`JEV_API_KEY` or `TYPESAFE_API_KEY`); an OpenAI key for the comparison mode. |
| License | [MIT](https://github.com/ValiusSciences/abstract-sift/blob/9be8ebfdda652b19a4e6af8bbecc0aee42563c6a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/abstract_sift/core.py`](https://github.com/ValiusSciences/abstract-sift/blob/9be8ebfdda652b19a4e6af8bbecc0aee42563c6a/src/abstract_sift/core.py) at the pinned commit. |

## When to use

- Triage thousands of abstracts before a conference or literature review.
- Mismatch: scores need a well-written interest text.

## How it works

`src/abstract_sift/core.py` posts each abstract with the interest text to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.14.0` and records per-request cost. Integration evidence: [`src/abstract_sift/core.py`](https://github.com/ValiusSciences/abstract-sift/blob/9be8ebfdda652b19a4e6af8bbecc0aee42563c6a/src/abstract_sift/core.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ValiusSciences/abstract-sift && cd abstract-sift
uv sync
uv run abstract-sift import examples/abstracts.jsonl --corpus demo
uv run abstract-sift score --corpus demo --query-file examples/interest.txt --provider jev --max-cost-usd 0.05
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- CLI reference: [github.com/ValiusSciences/abstract-sift/blob/main/docs/CLI.md](https://github.com/ValiusSciences/abstract-sift/blob/main/docs/CLI.md)
- ESMO run guide: [github.com/ValiusSciences/abstract-sift/blob/main/docs/ESMO_RUN.md](https://github.com/ValiusSciences/abstract-sift/blob/main/docs/ESMO_RUN.md)

## Limits and data handling

Abstracts and your interest text go to the selected providers.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 9be8ebfdda65](https://github.com/ValiusSciences/abstract-sift/tree/9be8ebfdda652b19a4e6af8bbecc0aee42563c6a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
