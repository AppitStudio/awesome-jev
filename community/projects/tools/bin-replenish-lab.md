# Bin Replenish Lab (pre-registered test of estimating warehouse bin fill levels from photos, with a Jev comparison)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Companion study to Parcel Lens on real warehouse pick-bin photos (Amazon Bin Image Dataset). A fine-tuned model is compared with Jev (`jev-1.14.0`, experimental image input) picking empty, low, medium or high on 150 test photos: 99% vs 93% on empty-or-not, and 78% vs 58% accuracy on the four levels, with Jev calling 26 of 45 medium bins low. The repository holds no dataset photos.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RajaRuling/bin-replenish-lab) |
| Maintainer | [RajaRuling](https://github.com/RajaRuling). Independently curated. |
| Format | Study + Python scripts + static site |
| Requirements | Python 3 and PyTorch for the offline tests; the dataset (non-commercial licence) and a key in `JEV_API_KEY` to re-run the Jev part. |
| License | [MIT (code); dataset CC BY-NC-SA 3.0](https://github.com/RajaRuling/bin-replenish-lab/blob/e636cc2f4d31f5d1ad4ce9e42b10c03a8cbb0c84/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/common.py`](https://github.com/RajaRuling/bin-replenish-lab/blob/e636cc2f4d31f5d1ad4ce9e42b10c03a8cbb0c84/jev/common.py) at the pinned commit. |

## When to use

- Compare a general image decision model with a fine-tuned one on a real inventory task before choosing one.
- Mismatch: one Jev run, one prompt; labels come from inventory records, so the accuracy ceiling is unknown.

## How it works

The scripts in `jev/` send each test photo with one Choice question over four fill levels and save every answer; `analyse.py` computes accuracy and macro F1 against the inventory labels. Integration evidence: [`jev/common.py`](https://github.com/RajaRuling/bin-replenish-lab/blob/e636cc2f4d31f5d1ad4ce9e42b10c03a8cbb0c84/jev/common.py).

## Get started

From the upstream README (not run on the review host):

```sh
.venv/bin/pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu128
.venv/bin/python -m pytest -q tests
(cd jev && ../.venv/bin/python -m pytest tests)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev report: [github.com/RajaRuling/bin-replenish-lab/blob/e636cc2f4d31f5d1ad4ce9e42b10c03a8cbb0c84/jev/REPORT.md](https://github.com/RajaRuling/bin-replenish-lab/blob/e636cc2f4d31f5d1ad4ce9e42b10c03a8cbb0c84/jev/REPORT.md)

## Limits and data handling

Code is MIT; the Amazon Bin Image Dataset it uses is CC BY-NC-SA 3.0 (non-commercial). The author's own study, not a TypeSafe benchmark.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit e636cc2f4d31](https://github.com/RajaRuling/bin-replenish-lab/tree/e636cc2f4d31f5d1ad4ce9e42b10c03a8cbb0c84). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
