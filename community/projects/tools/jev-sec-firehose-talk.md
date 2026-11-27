# Jev on the SEC firehose by Alexander Galea (AI Tinkerers Toronto live demo: Jev vs a GPT model on change-of-control clauses)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Notebook and slides from a six-minute live demo at AI Tinkerers Toronto (26 Nov 2026). It asks Jev and an OpenAI GPT model the same yes/no question (does the contract change if the company is sold?) about SEC EDGAR contracts, checks both against lawyers' labels from eight CUAD contracts, then runs a month of filings through both with a spend limit. Includes 750 November 2026 exhibit contracts and the EDGAR download script.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zazencodes/jev-sec-firehose-talk) |
| Maintainer | [Alexander Galea](https://github.com/zazencodes) (zazencodes). Independently curated. |
| Format | Jupyter notebook + slides + data |
| Requirements | uv, a TypeSafe key and an OpenAI key. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`demo.ipynb`](https://github.com/zazencodes/jev-sec-firehose-talk/blob/9c9c3e35ad698ac659217f41d1189f05d5d1e3b5/demo.ipynb) at the pinned commit. |

## When to use

- People who want a short, concrete example of using Jev for bulk document extraction and comparing its cost with an LLM.
- Mismatch: a contract-review product; this is a talk demo.

## How it works

`demo.ipynb` uses `typesafe_sdk`'s `AsyncTypeSafeClient` to send each contract as state with one `noul` question and compares the probability, accuracy and cost with a GPT model on the same contracts; the bulk run stops each model at `SPEND_LIMIT`. The slides' monthly cost figures are labelled estimates, not measurements. Integration evidence: [`demo.ipynb`](https://github.com/zazencodes/jev-sec-firehose-talk/blob/9c9c3e35ad698ac659217f41d1189f05d5d1e3b5/demo.ipynb).

## Get started

Clone the repo and open the notebook.

```sh
git clone https://github.com/zazencodes/jev-sec-firehose-talk.git && cd jev-sec-firehose-talk
export TYPESAFE_API_KEY=... OPENAI_API_KEY=...
uv run --with jupyterlab --with openai --with typesafe-sdk --with pydantic jupyter lab demo.ipynb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Slides: [github.com/zazencodes/jev-sec-firehose-talk/blob/main/slides.pdf](https://github.com/zazencodes/jev-sec-firehose-talk/blob/main/slides.pdf)
- Event: [toronto.aitinkerers.org/p/ai-tinkerers-toronto-november-2026-meetup-legal-tech-with-clio](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-november-2026-meetup-legal-tech-with-clio)

## Limits and data handling

Contracts come from SEC EDGAR and the labelled sample from CUAD v1 (CC BY 4.0). No licence file for the repo's own code and slides, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 9c9c3e35ad69](https://github.com/zazencodes/jev-sec-firehose-talk/tree/9c9c3e35ad698ac659217f41d1189f05d5d1e3b5). Inspected the README, `demo.ipynb` and `edgar.py` at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
