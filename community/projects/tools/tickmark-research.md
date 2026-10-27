# Tickmark Research (cited financial research with a measured Jev source router)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Research assistant for financial analysts that splits a question into parts, routes each to SEC filings, internal research or the web, enforces role-based access before retrieval, and checks every figure and citation against its source; the router is swappable between an LLM, Jev and a Jev-first cascade, each evaluated in the repo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/J-A-Y-0/tickmark-financial-research) |
| Maintainer | [J-A-Y-0](https://github.com/J-A-Y-0). Independently curated. |
| Format | Python web app with evaluation suite |
| Requirements | Python 3.12; an LLM provider key; a TypeSafe API key for the Jev and cascade routers. |
| License | [MIT](https://github.com/J-A-Y-0/tickmark-financial-research/blob/0c9f57347a05a5b08c537ba062e141d0cf2391c7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tickmark/routing.py`](https://github.com/J-A-Y-0/tickmark-financial-research/blob/0c9f57347a05a5b08c537ba062e141d0cf2391c7/tickmark/routing.py) at the pinned commit. |

## When to use

- Study a source router with access control enforced in code, not by the model.
- Compare LLM, Jev and cascade routing on the same questions.
- Mismatch: demo data; router accuracy figures are the author's.

## How it works

`tickmark/routing.py` defines a `jev` router that asks one Choice over the source catalog with `jev-latest` and falls back to another router on error; an optional Jev step also helps check figures. Integration evidence: [`tickmark/routing.py`](https://github.com/J-A-Y-0/tickmark-financial-research/blob/0c9f57347a05a5b08c537ba062e141d0cf2391c7/tickmark/routing.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/J-A-Y-0/tickmark-financial-research && cd tickmark-financial-research
make install && make demo   # see the README quick start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with evaluation: [github.com/J-A-Y-0/tickmark-financial-research#readme](https://github.com/J-A-Y-0/tickmark-financial-research#readme)

## Limits and data handling

Sub-questions go to TypeSafe when a Jev router is selected; documents go to your LLM provider. Not investment advice.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 0c9f57347a05](https://github.com/J-A-Y-0/tickmark-financial-research/tree/0c9f57347a05a5b08c537ba062e141d0cf2391c7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
