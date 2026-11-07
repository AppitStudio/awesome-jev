# Job Fit Screener / Radar de Vagas (job-posting triage scored by TypeSafe Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python pipeline that collects ~3,500 job postings from 18 sources, asks TypeSafe Jev for a fit score against your CV and preferences, and outputs a ranked Excel sheet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/michelxxx2323/Radar-de-Vagas) |
| Maintainer | [michelxxx2323](https://github.com/michelxxx2323). Independently curated. |
| Format | Python pipeline (no SPDX license file on the reviewed commit) |
| Requirements | Python 3 and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/michelxxx2323/Radar-de-Vagas/blob/0b9f9ed784746078dcabaa89027965288c83ff9b/jev_client.py) at the pinned commit. |

## When to use

- Rank large job-posting batches against a personal profile.
- Calibrate Jev fit scores with the bundled scripts.
- Mismatch: Brazil-focused sources; no OSI license on the reviewed commit.

## How it works

`jev_client.py` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; scores feed the ranking and calibration scripts. Integration evidence: [`jev_client.py`](https://github.com/michelxxx2323/Radar-de-Vagas/blob/0b9f9ed784746078dcabaa89027965288c83ff9b/jev_client.py).

## Get started

Clone, edit `config.yaml` with your profile, set the key, and run the pipeline.

```sh
git clone https://github.com/michelxxx2323/Radar-de-Vagas.git && cd Radar-de-Vagas
export TYPESAFE_API_KEY=...
pip install -r requirements.txt && python compare_jobs.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/michelxxx2323/Radar-de-Vagas/blob/0b9f9ed784746078dcabaa89027965288c83ff9b/README.md](https://github.com/michelxxx2323/Radar-de-Vagas/blob/0b9f9ed784746078dcabaa89027965288c83ff9b/README.md)

## Limits and data handling

Job text and profile preferences are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 0b9f9ed78474](https://github.com/michelxxx2323/Radar-de-Vagas/tree/0b9f9ed784746078dcabaa89027965288c83ff9b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
