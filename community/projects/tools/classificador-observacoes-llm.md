# Classificador de observações (browser tool that sorts free-text production notes into categories, with Jev as one provider)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Browser prototype that classifies free-text production notes from a spreadsheet into configurable categories, with validated output, parallel batches, fallback when a batch fails and a live cost cap. Groq and OpenRouter LLMs classify in batches; with Jev each row becomes one yes/no question per category and a priority order picks the main category. README in Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/b3rtuzz1/classificador-observacoes-llm) |
| Maintainer | [b3rtuzz1](https://github.com/b3rtuzz1). Independently curated. |
| Format | Browser app (JavaScript) |
| Requirements | A modern browser and a Groq or OpenRouter key (Jev runs through OpenRouter). |
| License | [MIT](https://github.com/b3rtuzz1/classificador-observacoes-llm/blob/02abdd2c7eb642f06f14f70347b99c27e59b4ab7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers.js`](https://github.com/b3rtuzz1/classificador-observacoes-llm/blob/02abdd2c7eb642f06f14f70347b99c27e59b4ab7/src/providers.js) at the pinned commit. |

## When to use

- Sort a spreadsheet of short free-text notes into categories with a hard spending limit.
- Mismatch: prototype; Jev is one of several providers.

## How it works

`src/providers.js` defines the Jev provider (`typesafe/jev-1.13` through OpenRouter) and builds one probability question per category for each row. Integration evidence: [`src/providers.js`](https://github.com/b3rtuzz1/classificador-observacoes-llm/blob/02abdd2c7eb642f06f14f70347b99c27e59b4ab7/src/providers.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/b3rtuzz1/classificador-observacoes-llm && cd classificador-observacoes-llm
# open index.html in a browser (see README)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Portuguese): [github.com/b3rtuzz1/classificador-observacoes-llm#readme](https://github.com/b3rtuzz1/classificador-observacoes-llm#readme)

## Limits and data handling

Rows from your spreadsheet are sent to the chosen provider from the browser.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 02abdd2c7eb6](https://github.com/b3rtuzz1/classificador-observacoes-llm/tree/02abdd2c7eb642f06f14f70347b99c27e59b4ab7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
