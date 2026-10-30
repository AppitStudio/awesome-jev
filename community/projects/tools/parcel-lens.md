# Parcel Lens (pre-registered test of spotting damaged parcels in synthetic images, with a Jev Box comparison)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible study with claims written before training: a small trained model versus Jev (`jev-1.14.0`, experimental image input) on 150 synthetic parcel images. The trained model scored AUC 96 against Jev's 76 on damage yes/no, and Jev caught about 1 in 6 damaged parcels with no false alarms; Jev's Box overlapped the true damage by at least half 59% of the time but drew a box on all 75 clean parcels. Static results site in `docs/`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RajaRuling/parcel-lens) |
| Maintainer | [RajaRuling](https://github.com/RajaRuling). Independently curated. |
| Format | Study + Python scripts + static site |
| Requirements | Python 3 for the offline tests and `make results`; a TypeSafe key only to re-run the Jev part (real calls). |
| License | [MIT](https://github.com/RajaRuling/parcel-lens/blob/00aab1ce960773696e2f31c18a433136df986029/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/run_jev_parcels.py`](https://github.com/RajaRuling/parcel-lens/blob/00aab1ce960773696e2f31c18a433136df986029/jev/run_jev_parcels.py) at the pinned commit. |

## When to use

- See how Jev's experimental image input and Box answer behave on a defect-locating task before trying it on your own pictures.
- Mismatch: synthetic images only, a single Jev run with one fixed prompt; says nothing about real parcels.

## How it works

`run_jev_parcels.py` sends each enlarged image with a yes/no and a Box question; `analyse.py` and `make_report.py` score the saved answers against the generator's ground truth. Integration evidence: [`jev/run_jev_parcels.py`](https://github.com/RajaRuling/parcel-lens/blob/00aab1ce960773696e2f31c18a433136df986029/jev/run_jev_parcels.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python -m pytest
(cd jev && ../.venv/bin/python -m pytest tests)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev report: [github.com/RajaRuling/parcel-lens/blob/00aab1ce960773696e2f31c18a433136df986029/jev/REPORT.md](https://github.com/RajaRuling/parcel-lens/blob/00aab1ce960773696e2f31c18a433136df986029/jev/REPORT.md)

## Limits and data handling

Images were enlarged 2x because the API refused the small originals; answer stability was not checked. The author's own study, not a TypeSafe benchmark.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 00aab1ce9607](https://github.com/RajaRuling/parcel-lens/tree/00aab1ce960773696e2f31c18a433136df986029). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
