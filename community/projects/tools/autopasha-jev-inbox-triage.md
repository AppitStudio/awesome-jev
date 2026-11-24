# Jev inbox triage experiment by AutoPasha (Russian 40-message inbox classification test with Jev through Polza.ai, with data and runs)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Published experiment from the AutoPasha team: 40 Russian customer messages sorted by Jev into sales, support, other and clarify over three runs, with a 0.85 confidence threshold that routes 35 of 40 automatically and sends the rest to a person. Dataset, criteria, raw runs and a verify script are included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AutoPasha/jev-inbox-triage) |
| Maintainer | [AutoPasha](https://github.com/AutoPasha). Independently curated. |
| Format | Python benchmark scripts and JSON data |
| Requirements | Python 3; a Polza.ai API key (the script calls Jev through Polza.ai's `/api/v1/systemone`). |
| License | [MIT](https://github.com/AutoPasha/jev-inbox-triage/blob/07e3ac6f4561b98a164884005399e115a7de0237/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bench.py`](https://github.com/AutoPasha/jev-inbox-triage/blob/07e3ac6f4561b98a164884005399e115a7de0237/bench.py) at the pinned commit. |

## When to use

- Copy a small, reproducible inbox-triage setup with a confidence threshold and human fallback.
- Mismatch: production email routing or non-Russian data; it is a 40-message experiment.

## How it works

`bench.py` sends each message with the class descriptions from `criteria.json` to `https://polza.ai/api/v1/systemone` as a Choice and writes `run-*.json`; `verify.py` recomputes the summary. Integration evidence: [`bench.py`](https://github.com/AutoPasha/jev-inbox-triage/blob/07e3ac6f4561b98a164884005399e115a7de0237/bench.py).

## Get started

Clone and re-run the benchmark or just verify the published runs.

```sh
git clone https://github.com/AutoPasha/jev-inbox-triage.git && cd jev-inbox-triage
python3 verify.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Russian): [github.com/AutoPasha/jev-inbox-triage/blob/07e3ac6f4561b98a164884005399e115a7de0237/README.md](https://github.com/AutoPasha/jev-inbox-triage/blob/07e3ac6f4561b98a164884005399e115a7de0237/README.md)
- Summary: [github.com/AutoPasha/jev-inbox-triage/blob/07e3ac6f4561b98a164884005399e115a7de0237/summary.json](https://github.com/AutoPasha/jev-inbox-triage/blob/07e3ac6f4561b98a164884005399e115a7de0237/summary.json)

## Limits and data handling

Reaches Jev through Polza.ai, a third-party aggregator, not TypeSafe directly. 40 messages written for the test; results are not a general accuracy claim. README is in Russian.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 07e3ac6f4561](https://github.com/AutoPasha/jev-inbox-triage/tree/07e3ac6f4561b98a164884005399e115a7de0237). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
