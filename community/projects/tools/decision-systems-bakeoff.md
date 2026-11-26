# Decision systems bakeoff by Mark Rizzn Hopkins (Jev, Laya and a fly-connectome model on the same frozen public tests, with accuracy, Brier score and speed)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible bakeoff that asks hosted Jev, on-prem Laya and an in-repo "Flybrain" (a larva connectome with a trained ridge head) the same locked questions on frozen public test sets: movie-review sentiment, phone intents, 150 intents plus "none of these", and Eclipse bug severity. It reports accuracy, Brier score, median seconds and whether each system finished, plus a second "fair-turf" suite.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/actuallyrizzn/decision-systems-bakeoff) |
| Maintainer | [Mark Rizzn Hopkins](https://github.com/actuallyrizzn) (Decision Science Corp). Independently curated. |
| Format | Python benchmark harness and write-up |
| Requirements | Python 3 with pip; the frozen datasets (checksums in `lockfile.json`); a Venice API key for the Jev arm and the `laya` package for the Laya arm. |
| License | [AGPL-3.0-or-later (code) / CC-BY-SA-4.0 (docs)](https://github.com/actuallyrizzn/decision-systems-bakeoff/blob/13f09e94297eb53bfa18ed3251914aa859ddb666/LICENSING.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision_bakeoff/jev.py`](https://github.com/actuallyrizzn/decision-systems-bakeoff/blob/13f09e94297eb53bfa18ed3251914aa859ddb666/src/decision_bakeoff/jev.py) at the pinned commit. |

## When to use

- Comparing hosted Jev with an open on-prem decision model on public tasks before choosing one, or reusing the locked questions for your own arm.
- Mismatch: an independent benchmark of your workload; four tasks, run by the author.

## How it works

`src/decision_bakeoff/jev.py` calls Jev through Venice's Decisions endpoint (`api.venice.ai/api/v1/decisions`), not TypeSafe's own API; `scripts/verify_data.py` refuses to run if test checksums drift, and `scripts/run_arm.py` runs one system on one task. Integration evidence: [`src/decision_bakeoff/jev.py`](https://github.com/actuallyrizzn/decision-systems-bakeoff/blob/13f09e94297eb53bfa18ed3251914aa859ddb666/src/decision_bakeoff/jev.py).

## Get started

Install, point at the frozen data, verify checksums, then run an arm.

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
python scripts/verify_data.py --data "$BAKEOFF_DATA"
export VENICE_JEV_AB_API_KEY=...
python scripts/run_arm.py --data "$BAKEOFF_DATA" --out runs/jev --task sst2 --arm jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with headline numbers and full scorecard: [github.com/actuallyrizzn/decision-systems-bakeoff/blob/13f09e94297eb53bfa18ed3251914aa859ddb666/README.md](https://github.com/actuallyrizzn/decision-systems-bakeoff/blob/13f09e94297eb53bfa18ed3251914aa859ddb666/README.md)
- Fair-turf rematch: [github.com/actuallyrizzn/decision-systems-bakeoff/blob/13f09e94297eb53bfa18ed3251914aa859ddb666/docs/FAIR_BAKEOFF.md](https://github.com/actuallyrizzn/decision-systems-bakeoff/blob/13f09e94297eb53bfa18ed3251914aa859ddb666/docs/FAIR_BAKEOFF.md)

## Limits and data handling

The Jev arm goes through Venice, a third-party host, so test rows are sent there. Results are the author's own: Jev led on sentiment (94.6%) and phone intents (99.3%) but its 150-intent score covers only the 4,060 rows it completed before the hosted API stopped answering, and on bug severity Flybrain (78.4%) beat Jev (49.1%). Code is AGPL-3.0-or-later, docs and question files CC-BY-SA-4.0.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 13f09e94297e](https://github.com/actuallyrizzn/decision-systems-bakeoff/tree/13f09e94297eb53bfa18ed3251914aa859ddb666). Inspected the README, LICENSING.md and the Jev arm at the pinned commit; no arm was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
