# Fastpunkt

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Evidence-first research agent for Norwegian companies (built for the Builderr Signalpost challenge): given organisation numbers it returns one profile per company where every published fact links to its source with retrieval time; official registers anchor identity, and Jev (`jev-1.13.0`) is used only to select among candidates the code found (links, sentences, job titles) or to give a calibrated same-entity probability — no model-written facts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ritesist/fastpunkt) |
| Maintainer | [Ritesist](https://github.com/Ritesist). Independently curated. |
| Format | CLI (`./run.sh organisations.jsonl out`) producing JSONL envelopes, a report and an HTML viewer |
| Requirements | Python 3.12+; `TYPESAFE_API_KEY` (optional — `--no-typesafe` uses keyword rules only). |
| License | [MIT](https://github.com/Ritesist/fastpunkt/blob/79a496b86997f8f93f504ec4a933e28e18b44f73/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Build auditable company profiles with explicit missing-data states.
- Pattern for using Jev as a selector over extracted candidates.
- Mismatch: Norway-specific registers.

## How it works

[`fastpunkt/judge.py`](https://github.com/Ritesist/fastpunkt/blob/79a496b86997f8f93f504ec4a933e28e18b44f73/fastpunkt/judge.py) asks Jev selection and identity questions; [`fastpunkt/website.py`](https://github.com/Ritesist/fastpunkt/blob/79a496b86997f8f93f504ec4a933e28e18b44f73/fastpunkt/website.py) requires P(same entity) ≥ 0.9 plus other evidence before publishing a site; hard caps limit requests and paid calls.

## Get started

Run a batch (README *Run it*):

```sh
git clone https://github.com/Ritesist/fastpunkt.git && cd fastpunkt
export TYPESAFE_API_KEY=...
./run.sh organisations.jsonl out
```

Jev calls bill your key, capped by `--max-typesafe-calls`.

## Examples and demos

- Smoke test report: [`docs/SMOKE_TEST_REPORT.md`](https://github.com/Ritesist/fastpunkt/blob/79a496b86997f8f93f504ec4a933e28e18b44f73/docs/SMOKE_TEST_REPORT.md).

## Limits and data handling

Page snippets go to TypeSafe; obeys robots.txt. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 79a496b86997](https://github.com/Ritesist/fastpunkt/tree/79a496b86997f8f93f504ec4a933e28e18b44f73). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
