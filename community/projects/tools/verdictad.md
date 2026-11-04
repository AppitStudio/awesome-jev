# VerdictAD

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper code for training-free few-shot industrial anomaly detection: an open decision model judges the query image and its local windows against a few normal references, and the probabilities refine an existing detector's image score and anomaly map.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sgstq0811/VerdictAD-Jev-AD) |
| Maintainer | [sgstq0811](https://github.com/sgstq0811). Author submission. |
| Format | Research repository (Python) with experiment logs and a public decision cache |
| Requirements | Python 3.12, PyTorch, a GPU for the decision model (`--batch 4` fits 24 GB); MVTec AD, VisA or MVTec LOCO AD; a patched [SubspaceAD](https://github.com/CLendering/SubspaceAD) checkout for the base detector. No API key. |
| License | [Apache-2.0](https://github.com/sgstq0811/VerdictAD-Jev-AD/blob/7a57de0a191d751fb04188dbd5ca1c9cedba5a02/LICENSE) |
| Disclosure | Submitted by the project author; the code and this page were written with AI assistance (Claude Code). Uses Cloudflare's open [Clef-Flash 9B](https://huggingface.co/Cloudflare/clef-flash) locally and does not call hosted TypeSafe Jev. Listing is not an endorsement. |
| Jev evidence | [`verdictad/decider.py`](https://github.com/sgstq0811/VerdictAD-Jev-AD/blob/7a57de0a191d751fb04188dbd5ca1c9cedba5a02/verdictad/decider.py) sends `noul` questions in the System One state/questions shape to Clef-Flash and reads one logit per question. |

## When to use

- Add a decision layer to a few-shot anomaly detector (PatchCore, DINOv2, AnomalyDINO or SubspaceAD) without training.
- Reproduce the paper's tables on MVTec AD, VisA and MVTec LOCO AD from the released logs or decision cache.
- Mismatch: it targets image anomaly detection benchmarks; it is not a general Jev client and does not use the hosted API.

## How it works

For each test image, [`decide.py`](https://github.com/sgstq0811/VerdictAD-Jev-AD/blob/7a57de0a191d751fb04188dbd5ca1c9cedba5a02/decide.py) asks Clef-Flash `noul` questions on whether the whole image, and each of 32 local windows (crops and red-box views), shows a defect, with and without the normal reference images. [`verdictad/fuse.py`](https://github.com/sgstq0811/VerdictAD-Jev-AD/blob/7a57de0a191d751fb04188dbd5ca1c9cedba5a02/verdictad/fuse.py) turns the logits into weights: the image score is multiplied by a power of the probability from the averaged image-level logits, and each anomaly-map pixel by the mean powered probability of the windows covering it. [`evaluate.py`](https://github.com/sgstq0811/VerdictAD-Jev-AD/blob/7a57de0a191d751fb04188dbd5ca1c9cedba5a02/evaluate.py) scores the detector with and without these weights using Image AUROC/AUPR, Pixel AUROC and AUPRO.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sgstq0811/VerdictAD-Jev-AD.git && cd VerdictAD-Jev-AD
pip install -r requirements.txt
git clone https://github.com/CLendering/SubspaceAD.git && (cd SubspaceAD && git apply ../patches/subspacead.patch)
# run the base detector, then decisions and evaluation, as in the README "Usage" section
python decide.py $RUN runs/jev_mvtec_k4_s42 --data_root data/mvtec_anomaly_detection
python evaluate.py $RUN runs/jev_mvtec_k4_s42 --subspacead SubspaceAD
```

Clef-Flash is downloaded from Hugging Face on first use and runs locally; no data leaves the machine apart from that download. The decision step can be skipped with the released [decision cache](https://huggingface.co/datasets/sunsean/VerdictAD).

## Examples and demos

- Paper: [arXiv:2611.02654](https://arxiv.org/abs/2611.02654).
- Per-seed, per-class results in [`logs/`](https://github.com/sgstq0811/VerdictAD-Jev-AD/tree/7a57de0a191d751fb04188dbd5ca1c9cedba5a02/logs); `python tools/summarize_logs.py` rebuilds the tables.
- No hosted demo.

## Limits and data handling

Reported numbers are the authors' own, on the official test splits of the three datasets. The decision model needs a GPU; Clef-Flash is an independent open model with its own license and behavior, distinct from TypeSafe's Jev.

## Review and maintenance

Reviewed **2026-11-05** at [commit 7a57de0a191d](https://github.com/sgstq0811/VerdictAD-Jev-AD/tree/7a57de0a191d751fb04188dbd5ca1c9cedba5a02). Inspected the README, license and the decision-model call site linked above; install, live inference and the catalog checks were not run for this submission.
