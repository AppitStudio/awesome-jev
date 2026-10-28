# jev-playground by exponen-agi (16 interactive simulations and runnable cookbooks for designing with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Engineer's playground for Jev: sixteen browser simulations (no install, no key, nothing called) showing how a fast, calibrated, typed decision model changes an architecture, plus runnable Python cookbooks for triage cascades, RAG gatekeeping, agent guardrails, output verification, lead scoring and model routing, and a plain-English guide with a where-it-breaks section.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/exponen-agi/jev-playground) |
| Maintainer | [exponen-agi](https://github.com/exponen-agi). Independently curated. |
| Format | Static HTML simulations and Python cookbooks |
| Requirements | A browser for the simulations; Python and a TypeSafe API key for the cookbooks. |
| License | [MIT](https://github.com/exponen-agi/jev-playground/blob/ebec9e601bccb85a822f1dc7fb91b16ebedb34de/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cookbooks/01_triage_cascade.py`](https://github.com/exponen-agi/jev-playground/blob/ebec9e601bccb85a822f1dc7fb91b16ebedb34de/cookbooks/01_triage_cascade.py) at the pinned commit. |

## When to use

- Explain Jev-style decision layers to colleagues before writing code.
- Mismatch: learning material; cost figures quote TypeSafe's published numbers.

## How it works

The cookbooks use the official Python SDK (`from typesafe_sdk import Choice, Noul, Score`) with a confidence floor that sends uncertain cases on to a larger model. Integration evidence: [`cookbooks/01_triage_cascade.py`](https://github.com/exponen-agi/jev-playground/blob/ebec9e601bccb85a822f1dc7fb91b16ebedb34de/cookbooks/01_triage_cascade.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/exponen-agi/jev-playground.git
xdg-open jev-playground/simulations/index.html
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demos: [exponen-agi.github.io/jev-playground/](https://exponen-agi.github.io/jev-playground/)
- Cookbooks: [github.com/exponen-agi/jev-playground/tree/main/cookbooks](https://github.com/exponen-agi/jev-playground/tree/main/cookbooks)

## Limits and data handling

The simulations send nothing. Cookbook runs send their example text to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit ebec9e601bcc](https://github.com/exponen-agi/jev-playground/tree/ebec9e601bccb85a822f1dc7fb91b16ebedb34de). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
