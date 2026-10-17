# Jev Workshop (notebooks and deck)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Teaching kit for Jev: five notebooks executed live against the API, a 42-slide deck with speaker notes, and a cited reference covering the primitives, confidence and common patterns.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fnusatvik07/jev-workshop) |
| Maintainer | [fnusatvik07](https://github.com/fnusatvik07). Independently curated. |
| Format | Python notebooks, PowerPoint deck and Markdown reference |
| Requirements | Python 3.11+ and uv; a TypeSafe API key to re-run the notebooks. |
| License | [MIT](https://github.com/fnusatvik07/jev-workshop/blob/7d6d34196b3ed1322958fb73fa23484eab81ea18/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`notebooks/01_hello_jev.ipynb`](https://github.com/fnusatvik07/jev-workshop/blob/7d6d34196b3ed1322958fb73fa23484eab81ea18/notebooks/01_hello_jev.ipynb) at the pinned commit. |

## When to use

- Learn Jev from hello world to real-world patterns, or run a workshop for a team.
- Reuse the measured numbers and charts in the deck.
- Mismatch: teaching material, not a library; numbers were recorded on specific Jev versions and may change.

## How it works

The notebooks walk from a first call through Choice, Score and Noul, confidence handling, patterns and real-world examples, each executed against `api.typesafe.ai`; the deck is generated from Python scripts in `deck/build/`. Integration evidence: [`notebooks/01_hello_jev.ipynb`](https://github.com/fnusatvik07/jev-workshop/blob/7d6d34196b3ed1322958fb73fa23484eab81ea18/notebooks/01_hello_jev.ipynb).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/fnusatvik07/jev-workshop.git
cd jev-workshop
uv sync
export TYPESAFE_API_KEY="your-key"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Deck: `deck/Jev-Workshop.pptx`; reference: `reference/JEV-REFERENCE.md`.

## Limits and data handling

Notebook inputs go to TypeSafe on your key when you re-run cells.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 7d6d34196b3e](https://github.com/fnusatvik07/jev-workshop/tree/7d6d34196b3ed1322958fb73fa23484eab81ea18). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
