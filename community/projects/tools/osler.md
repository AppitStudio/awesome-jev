# Osler by Abhinand (open medical System One decision models, 4B and 9B, with the MedDecide training and evaluation code)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

MedDecide is the code behind Osler-4B and Osler-9B: medical decision models that take a clinical state (discharge note, trial record, drug label or question) and typed Noul, Choice or Score questions and return a calibrated distribution in one prefill pass. Weights are on Hugging Face under Apache-2.0; the repository also holds the evaluation harness, calibration and audit scripts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abhinand5/MedDecide) |
| Maintainer | [Abhinand](https://github.com/abhinand5). Independently curated. |
| Format | Python research code and Hugging Face weights |
| Requirements | Python with PyTorch and Transformers; a GPU (the author reports about 17 GB peak VRAM for Osler-9B). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/meddecide/model/d1.py`](https://github.com/abhinand5/MedDecide/blob/d82934a039ceed7cf8f189465fa38ba592c07cc5/src/meddecide/model/d1.py) at the pinned commit. |

## When to use

- Research calibrated typed decisions on clinical text.
- Mismatch: for any unsupervised clinical decision; the model card says outputs must be reviewed by qualified clinicians.

## How it works

`src/meddecide/model/d1.py` implements the `system_one` interface on open backbones; the models are the author's own, not TypeSafe's Jev, and no TypeSafe calls were found. Integration evidence: [`src/meddecide/model/d1.py`](https://github.com/abhinand5/MedDecide/blob/d82934a039ceed7cf8f189465fa38ba592c07cc5/src/meddecide/model/d1.py).

## Get started

Load the released weights with Transformers (remote code).

```sh
from transformers import AutoModel
model = AutoModel.from_pretrained("abhinand/Osler-9B", trust_remote_code=True)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Osler-9B: [huggingface.co/abhinand/Osler-9B](https://huggingface.co/abhinand/Osler-9B)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. (the Hugging Face weights are Apache-2.0). Research models, not medical devices or advice. Benchmark and audit figures are the author's own; `trust_remote_code` runs code from the model repository.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit d82934a039ce](https://github.com/abhinand5/MedDecide/tree/d82934a039ceed7cf8f189465fa38ba592c07cc5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
