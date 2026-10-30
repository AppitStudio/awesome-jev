# Jev evidence triage (screens PubMed abstracts for a systematic review with Jev, rules and confidence gates)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Demo pipeline that screens life-science abstracts for one systematic-review question (can faecal microbiota transplantation or a live bacterial product improve immune checkpoint inhibitor outcomes in cancer?). Plain code rules run first, Jev answers six questions per abstract in one call, and code confidence gates route each record to include, exclude or human review; an optional LLM pre-read only helps the human queue. Includes 24 fictional sample abstracts with planted traps, gold labels, evaluation with threshold sweeps and an offline mock.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anondo1969/jev-evidence-triage) |
| Maintainer | [anondo1969](https://github.com/anondo1969). Independently curated. |
| Format | Python CLI |
| Requirements | Python 3.10+; a TypeSafe key for live runs (offline `--mock` mode needs none); NCBI E-utilities for PubMed fetches. |
| License | [MIT](https://github.com/anondo1969/jev-evidence-triage/blob/06512c539460622f5ffa1428e74fa4bc10a4c01e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_triage/jev.py`](https://github.com/anondo1969/jev-evidence-triage/blob/06512c539460622f5ffa1428e74fa4bc10a4c01e/jev_triage/jev.py) at the pinned commit. |

## When to use

- Pre-screen abstracts for a review question while keeping every include/exclude decision in auditable code.
- Mismatch: built around one review question; editing `protocol.py` is needed for a new review.

## How it works

`jev.py` calls the TypeSafe SDK once per record with the six questions from `protocol.py`, with concurrency, metering and fail-safe errors; `route.py` applies the gates. Integration evidence: [`jev_triage/jev.py`](https://github.com/anondo1969/jev-evidence-triage/blob/06512c539460622f5ffa1428e74fa4bc10a4c01e/jev_triage/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -r requirements.txt
python -m jev_triage triage --mock --out out/mock
python -m jev_triage check --model jev-1.13.0
python -m jev_triage triage --model jev-1.13.0 --out out/sample
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Runbook: [github.com/anondo1969/jev-evidence-triage/blob/06512c539460622f5ffa1428e74fa4bc10a4c01e/RUNBOOK.md](https://github.com/anondo1969/jev-evidence-triage/blob/06512c539460622f5ffa1428e74fa4bc10a4c01e/RUNBOOK.md)

## Limits and data handling

Abstract text is sent to TypeSafe in live mode. Sample data is fictional; mock answers say nothing about Jev. A demo, not a validated screening tool. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 06512c539460](https://github.com/anondo1969/jev-evidence-triage/tree/06512c539460622f5ffa1428e74fa4bc10a4c01e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
