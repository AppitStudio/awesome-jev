# Beyond CLIP: decision models for industrial image QC

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Ongoing research study (R code, data and rendered analysis) comparing Jev and the open-weight Clef-Flash with few-shot CLIP for calibrated defect detection on five industrial image datasets, with a five-stage audit, refine, calibrate and freeze framework.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fmegahed/decision-models-for-industrial-image-qc) |
| Maintainer | [fmegahed](https://github.com/fmegahed). Independently curated. |
| Format | Research repository (R, Quarto analysis) |
| Requirements | R; a TypeSafe API key to rerun the Jev arms; local Clef-Flash for the open-weight arm. |
| License | [MIT](https://github.com/fmegahed/decision-models-for-industrial-image-qc/blob/33ffd591a2b42b3e72841b4e9d2531bdfa038c2a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`R/industrial_defect_classifier.R`](https://github.com/fmegahed/decision-models-for-industrial-image-qc/blob/33ffd591a2b42b3e72841b4e9d2531bdfa038c2a/R/industrial_defect_classifier.R) at the pinned commit. |

## When to use

- See how Jev compares with CLIP on defect detection with only a few reference images.
- Reuse the calibration and frozen-evaluation workflow for your own image QC task.
- Mismatch: work in progress; an R package is still in design.

## How it works

`R/industrial_defect_classifier.R` sends each image with defect criteria and reference images to Jev (`jev-1.13.0`) or a local Clef-Flash server; probabilities are calibrated on validation (Platt or isotonic) and scored once on held-out test images. Integration evidence: [`R/industrial_defect_classifier.R`](https://github.com/fmegahed/decision-models-for-industrial-image-qc/blob/33ffd591a2b42b3e72841b4e9d2531bdfa038c2a/R/industrial_defect_classifier.R).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/fmegahed/decision-models-for-industrial-image-qc
# see the README for the replication scripts (scripts/optimize_jev.R, scripts/evaluate_frozen.R)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Rendered analysis: [fmegahed.github.io/decision-models-for-industrial-image-qc/pages/beyond_clip_analysis.html](https://fmegahed.github.io/decision-models-for-industrial-image-qc/pages/beyond_clip_analysis.html)

## Limits and data handling

Results are the authors' own and not peer reviewed yet (abstract submitted to MSEC 2027). Rerunning the Jev arms sends images to TypeSafe.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 33ffd591a2b4](https://github.com/fmegahed/decision-models-for-industrial-image-qc/tree/33ffd591a2b42b3e72841b4e9d2531bdfa038c2a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
