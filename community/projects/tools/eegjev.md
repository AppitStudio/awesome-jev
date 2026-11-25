# EEGJev by Dengzhe Hou (System One decision model and benchmark for answering typed questions about EEG recordings)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research model and benchmark that answer typed questions about brain-signal (EEG) recordings: a CBraMod EEG encoder and frozen MPNet question and option embeddings feed a shared decision head that scores the offered answers in one pass. EEGJev-Bench covers six question types over 19 public EEG sources, split by participant.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dengzhe-hou/EEGJev) |
| Maintainer | [Dengzhe Hou](https://github.com/dengzhe-hou). Independently curated. |
| Format | Python research code, Hugging Face model and dataset |
| Requirements | Python 3.13 and NumPy for the synthetic scoring example; local weights from Hugging Face to run the model. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`model/README.md`](https://github.com/dengzhe-hou/EEGJev/blob/79edd625c03e6117a1e5ab7a1a157e383a5cb805/model/README.md) at the pinned commit. |

## When to use

- Research question-guided decoding of EEG with a fixed answer set.
- Mismatch: not a clinical or diagnostic tool.

## How it works

Jev-style model, not TypeSafe's Jev: the decision head picks among offered answers and can refuse when none is valid. `model/README.md` covers CPU inference with the shared checkpoint; `bench/` reads the corpus and scores answers. Integration evidence: [`model/README.md`](https://github.com/dengzhe-hou/EEGJev/blob/79edd625c03e6117a1e5ab7a1a157e383a5cb805/model/README.md).

## Get started

Run the synthetic benchmark example (no EEG data or weights needed).

```sh
python3.13 -m venv .venv && . .venv/bin/activate
python -m pip install numpy==2.4.3
python -I -B bench/examples/score_linked_demo.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [dengzhe-hou.github.io/EEGJev/](https://dengzhe-hou.github.io/EEGJev/)
- Model: [huggingface.co/dengzhe-hou/EEGJev](https://huggingface.co/dengzhe-hou/EEGJev)
- Benchmark dataset: [huggingface.co/datasets/dengzhe-hou/EEGJev-Bench](https://huggingface.co/datasets/dengzhe-hou/EEGJev-Bench)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Model and dataset access terms are on Hugging Face, and source EEG datasets keep their own terms. Research results are the authors' own (arXiv preprint).

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 79edd625c03e](https://github.com/dengzhe-hou/EEGJev/tree/79edd625c03e6117a1e5ab7a1a157e383a5cb805). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
