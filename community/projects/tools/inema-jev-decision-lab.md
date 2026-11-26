# Jev Decision Lab by INEMA TDS (Portuguese-language lab with 20 cases and 18 activity packages for designing, testing and comparing Jev decisions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Lab for defining, testing and comparing Jev decisions, with 20 worked cases (support, contracts, logs, agents, diff review and more), 18 reusable activity packages, batch experiments with macro-F1, Brier/ECE and cost, and a `jev-decidir` skill for Codex and Claude Code. The public site shows labelled simulations without an API key; the local server makes real calls. The interface and course material are in Portuguese, with English and Spanish READMEs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/inematds/jev) |
| Maintainer | [Nei Maldaner / INEMA TDS](https://github.com/inematds). Independently curated. |
| Format | Python standard-library local server, static web lab and packages |
| Requirements | Python 3.10+; a TypeSafe API key or an OpenRouter key for real inference (the public site and offline examples need none). |
| License | [MIT](https://github.com/inematds/jev/blob/f6f90292dc4db442c4176d361f5de57587528c66/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_lab/core.py`](https://github.com/inematds/jev/blob/f6f90292dc4db442c4176d361f5de57587528c66/jev_lab/core.py) at the pinned commit. |

## When to use

- Portuguese-speaking teams learning to write Choice, Noul and Score questions and to measure them on a labelled set before integrating.
- Mismatch: a production connector; the packages' fixtures are fictional and the site's answers are simulations.

## How it works

`jev_lab/core.py` validates requests and posts them to `https://api.typesafe.ai/v1/systemone` or OpenRouter's Decisions endpoint (`~typesafe/jev-latest`); thresholds and abstention are applied in code as an educational policy, and no external action is executed. Integration evidence: [`jev_lab/core.py`](https://github.com/inematds/jev/blob/f6f90292dc4db442c4176d361f5de57587528c66/jev_lab/core.py).

## Get started

Try the public lab, or run the local server for real calls.

```sh
git clone https://github.com/inematds/jev.git
cd jev
python3 -m jev_lab serve      # http://127.0.0.1:8765
python3 -m pacotes.executar atendimento   # offline example
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Public lab: [inematds.github.io/jev/app/](https://inematds.github.io/jev/app/)
- User guide: [inematds.github.io/jev/guia/](https://inematds.github.io/jev/guia/)
- Overstatements and open questions: [github.com/inematds/jev/blob/f6f90292dc4db442c4176d361f5de57587528c66/docs/07-exageros-e-duvidas.md](https://github.com/inematds/jev/blob/f6f90292dc4db442c4176d361f5de57587528c66/docs/07-exageros-e-duvidas.md)

## Limits and data handling

Responses on the public site are labelled simulations, not Jev output. The README's OpenRouter smoke test (ten fictional examples) is an integration test, not a benchmark. Live mode sends your text to TypeSafe or OpenRouter. The project's own "overstatements and open questions" document is worth reading first.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit f6f90292dc4d](https://github.com/inematds/jev/tree/f6f90292dc4db442c4176d361f5de57587528c66). Inspected the README (Portuguese and English), LICENSE and `jev_lab/core.py` at the pinned commit; the local server was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
