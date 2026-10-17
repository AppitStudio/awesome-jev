# Onion or Not?

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local web app that asks whether a headline is Onion satire or real news and shows three answers side by side: Jev, AnyJev L0 over a local Qwen3-8B, and raw Qwen3-8B, with an option to swap the answer order.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andrisgauracs/onion-or-not) |
| Maintainer | [andrisgauracs](https://github.com/andrisgauracs). Independently curated. |
| Format | Python web app (uv, llama.cpp) |
| Requirements | Python 3.10+, uv, a TypeSafe API key for the Jev card; about 5 GB for the optional local model. |
| License | [MIT](https://github.com/andrisgauracs/onion-or-not/blob/9634445160e6daf456164895d82859637c87b4d4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`onion_or_not/config.py`](https://github.com/andrisgauracs/onion-or-not/blob/9634445160e6daf456164895d82859637c87b4d4/onion_or_not/config.py) at the pinned commit. |

## When to use

- Compare hosted Jev with an open model and the AnyJev correction on the same small classification task.
- Show option-order sensitivity in plain LLMs by asking with the options swapped.
- Mismatch: a toy satire detector, not a fact-checking or misinformation tool.

## How it works

The Jev card sends the headline to TypeSafe with your key (`TYPESAFE_API_KEY`, model `jev-1.13.0` by default); the other two cards run Qwen3-8B locally through llama.cpp, with and without AnyJev L0. Each card shows its confidence and the cost of the answer. Integration evidence: [`onion_or_not/config.py`](https://github.com/andrisgauracs/onion-or-not/blob/9634445160e6daf456164895d82859637c87b4d4/onion_or_not/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/andrisgauracs/onion-or-not.git && cd onion-or-not
uv sync
cp .env.example .env          # add your TypeSafe key
uv run onion-or-not download  # optional, ~5 GB
uv run onion-or-not           # http://127.0.0.1:8000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshot: `docs/screenshot.png`.

## Limits and data handling

Headlines go to TypeSafe on your key for the Jev card only; the local models run on your machine.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 9634445160e6](https://github.com/andrisgauracs/onion-or-not/tree/9634445160e6daf456164895d82859637c87b4d4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
