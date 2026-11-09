# Outpatient EMR (Chinese clinic-record generator splitting closed fields to Jev and open fields to Qwen)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Generates an outpatient medical record from a consultation recording or transcript: ASR for audio, Jev for speaker roles, symptom screening and closed fields, Qwen for open text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/id5463/outpatient-emr) |
| Maintainer | [id5463](https://github.com/id5463). Independently curated. |
| Format | Python app (MIT; Chinese) |
| Requirements | Python, an ASR provider, a Qwen endpoint and a TypeSafe/Jev key. |
| License | [MIT](https://github.com/id5463/outpatient-emr/blob/2a5dc46dc4e562865d00179f35b3c00fb653c526/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/decision/jev.py`](https://github.com/id5463/outpatient-emr/blob/2a5dc46dc4e562865d00179f35b3c00fb653c526/app/decision/jev.py) at the pinned commit. |

## When to use

- Split typed vs free-text fields between Jev and an LLM.
- Keep confidence on closed clinical fields.
- Mismatch: demo only, not a certified medical device.

## How it works

`app/decision/jev.py` (`JevJudger`) posts state and questions to `/systemone` with `typesafe/jev-1.14.0`; closed fields keep Jev's probabilities so low-confidence values can be flagged. Integration evidence: [`app/decision/jev.py`](https://github.com/id5463/outpatient-emr/blob/2a5dc46dc4e562865d00179f35b3c00fb653c526/app/decision/jev.py).

## Get started

Clone, `pip install -r requirements.txt`, configure the model endpoints in `app/core/config.py` / environment per the README, and run `run.py`.

```sh
git clone https://github.com/id5463/outpatient-emr.git && cd outpatient-emr
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/id5463/outpatient-emr/blob/2a5dc46dc4e562865d00179f35b3c00fb653c526/README.md](https://github.com/id5463/outpatient-emr/blob/2a5dc46dc4e562865d00179f35b3c00fb653c526/README.md)

## Limits and data handling

Consultation text is sent to the configured Jev, Qwen and ASR providers; do not use with real patient data without proper agreements.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 2a5dc46dc4e5](https://github.com/id5463/outpatient-emr/tree/2a5dc46dc4e562865d00179f35b3c00fb653c526). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
