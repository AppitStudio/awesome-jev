# jev-image-checks (field test where Jev 1.14 answers 129 yes/no questions about 29 AI-generated product images, scored against a Claude vision audit)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and saved results of a field test by the team at LARGE FORMAT on whether a cheap typed model can check AI-generated product images. Jev 1.14 answered 129 yes/no questions on each of 29 images of an electric bike in three ways of asking (whole image, with close-ups, camera angle), scored against a full Claude vision audit; the images are not published, but the saved answers, labels and scoring are, so the figures can be recomputed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lrgfrmt/jev-image-checks) |
| Maintainer | [lrgfrmt](https://github.com/lrgfrmt). Independently curated. |
| Format | Python scripts (standard library) with saved JSONL results |
| Requirements | Python 3 and Pillow for `prepare.py`; a TypeSafe key only to re-run `run_jev.py` with your own images (recomputing from saved results needs none). |
| License | [MIT](https://github.com/lrgfrmt/jev-image-checks/blob/e7344a6802367a09edccf1604d468bd81876157e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run_jev.py`](https://github.com/lrgfrmt/jev-image-checks/blob/e7344a6802367a09edccf1604d468bd81876157e/run_jev.py) at the pinned commit. |

## When to use

- See a worked field test of Jev as an advisory image checker with a person approving every image.
- Mismatch: one product, one set of 29 images, and Jev's image reading is an experimental feature that TypeSafe says is not ready for production.

## How it works

`run_jev.py` calls the Jev API once per image for each of three ways of asking and logs the model, status, latency and attempts; `score.py` compares the saved answers with the audit labels and writes the metrics, which include per-gate catches, false passes and false alarms. Integration evidence: [`run_jev.py`](https://github.com/lrgfrmt/jev-image-checks/blob/e7344a6802367a09edccf1604d468bd81876157e/run_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 score.py   # recompute the saved results
pip install pillow
python3 prepare.py  # your own images, then run_jev.py with a key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up: [www.lrgfrmt.com/lab/jev-image-checks](https://www.lrgfrmt.com/lab/jev-image-checks)
- Saved metrics: [github.com/lrgfrmt/jev-image-checks/blob/main/data/runs/metrics.md](https://github.com/lrgfrmt/jev-image-checks/blob/main/data/runs/metrics.md)

## Limits and data handling

The reported figures are the authors' own on a small sample, for example at a 0.3 gate the full-question whole-image arm caught 94 of 98 problems with 656 false alarms; they are not independently verified and do not generalise. Re-running sends your images to TypeSafe on your key. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit e7344a680236](https://github.com/lrgfrmt/jev-image-checks/tree/e7344a6802367a09edccf1604d468bd81876157e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
