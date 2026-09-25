# Jevlet

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

From-scratch research reconstruction of a Jev-like System One decision model (typed Noul/Choice/Score → probabilities, no text generation) plus a Windows command-palette daily driver.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NAME0x0/Jevlet) |
| Maintainer | [NAME0x0](https://github.com/NAME0x0). Independently curated. |
| Format | Python package + training/research notebooks; Hugging Face weights; optional Windows tray/command palette. |
| Requirements | Python 3.11+; PyTorch 2.3+; extras for desktop/colab per `pyproject.toml`. |
| License | [MIT](https://github.com/NAME0x0/Jevlet/blob/40d8c520cb4a4014fd8531a06d41a750328f9c82/LICENSE). |
| Disclosure | Research reconstruction—not TypeSafe's implementation (upstream README). AI-assisted catalog review; no affiliation. Listing is not an endorsement. Benchmark tables are author-reported; training/desktop paths not run on the review host. |

## When to use

Use for **local System One–style research** or a Windows Alt+Space assistant driven by calibrated decisions. Prefer hosted TypeSafe Jev for production cloud judgments.

## How it works

Packed sequences share state across question branches; `[DECIDE]` bilinear scoring yields listwise logits. Pretrained (BERT-family) and scratch byte-level backbones share topology and API.

## Get started

```sh
git clone https://github.com/NAME0x0/Jevlet.git
cd Jevlet
git checkout 40d8c520cb4a4014fd8531a06d41a750328f9c82
python -m pip install -e ".[dev,semantic,desktop,colab]"
# Weights/demo: https://huggingface.co/NAME0x0/Jevlet
```

## Examples and demos

- Colab notebook badge in README; `research/` design notes.
- Windows: `pythonw -m jevlet.app` (upstream).

## Limits and data handling

Local inference stays on-device unless you use remote Colab/HF. Route/gate accuracy numbers are upstream lab results on small hand-written benches—not independent verification.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 40d8c52](https://github.com/NAME0x0/Jevlet/tree/40d8c520cb4a4014fd8531a06d41a750328f9c82). AI-assisted README and LICENSE inspection; install/train/desktop not executed.
