# Jev-Omni

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Jev-Omni is an open multimodal System One–style decision classifier: give it a state, a question, and typed options over text, image, audio, or video, and it returns a probability for each option—not generated chat.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://huggingface.co/akhilaaa3/Jev-Omni) |
| Tags | `Open source` · `Free source build` |
| Maintainer | [akhilaaa3](https://huggingface.co/akhilaaa3) ([@Akhila_988](https://x.com/Akhila_988)). |
| Format | Hugging Face model repo: merged Gemma 4 12B IT backbone, decision head, reference Python loader (`jev_omni.py`), `example.py`, and `requirements.txt`. |
| Relationship to Jev | Independent open-weight classifier in the typed-option / System One shape. It does not call TypeSafe, ship official Jev weights, or claim API compatibility. |
| Requirements | CUDA GPU (reference loader refuses non-CUDA). FP32 weights are about **50 GB** before runtime overhead; inference uses BF16 autocast. Python deps in [`requirements.txt`](https://huggingface.co/akhilaaa3/Jev-Omni/resolve/main/requirements.txt) (`torch>=2.10`, `transformers==5.17.0`, …). `ffmpeg` for audio. Hosting/GPU electricity and Hugging Face downloads are separate costs. |
| License | [Apache-2.0](https://huggingface.co/akhilaaa3/Jev-Omni) on the model card (following Gemma 4). Dataset rights remain separate. |
| Disclosure | AI-assisted catalog review from public HF artifacts and the author’s X post. No affiliation. Listing is not an endorsement or a claim of parity with official Jev. |

## When to use

Use it to try a local multimodal decision head: one prompt with numbered options, probabilities back, across text and common media. It fits research and self-host experiments that need open weights rather than a hosted TypeSafe call.

It is not a chat model, not an official Jev drop-in, and not practical without a large CUDA GPU.

## How it works

[`jev_omni.py`](https://huggingface.co/akhilaaa3/Jev-Omni/blob/c127654e586e05b2e9b75b3aaef075ddcf57a286/jev_omni.py) downloads the card’s merged text backbone plus Google’s `google/gemma-4-12B-it` multimodal components, swaps in the fine-tuned decoder, and attaches a classification head over **2–256** options (quality above ~20 options is not established upstream).

`predict(...)` builds a numbered-option prompt, optionally attaches image / 16 video frames / ≤30 s mono audio, runs one forward pass under BF16 autocast, and softmaxes the head over the supplied options. The return value is `{prediction, prediction_index, confidence, probabilities}`—no free-form generation.

## Get started

CUDA GPU required. The first run downloads large weight files from Hugging Face (this model plus Gemma 4 multimodal pieces).

```sh
pip install -r https://huggingface.co/akhilaaa3/Jev-Omni/resolve/main/requirements.txt
# ffmpeg is also required for audio input
```

```python
from huggingface_hub import snapshot_download
import sys

path = snapshot_download("akhilaaa3/Jev-Omni")
sys.path.insert(0, path)
from jev_omni import load_jev_omni

classifier = load_jev_omni()
result = classifier.predict(
    state="The meeting starts at 10 AM. It is now 9 AM.",
    question="Has the meeting started?",
    options=["Yes", "No"],
)
print(result)
```

For media, pass `media="/path/to/file"` and `modality="image"`, `"audio"`, or `"video"`. Commands above were inspected against the model card and loader; they were **not** executed in this review (no GPU install).

## Examples and demos

- [`example.py`](https://huggingface.co/akhilaaa3/Jev-Omni/blob/c127654e586e05b2e9b75b3aaef075ddcf57a286/example.py) — short text `predict` snippet; same API for other modalities.
- Model card quick start and reported warm H200 latency notes (upstream; not reproduced here).
- No separate interactive Space was linked on the card at review time.

## Limits and data handling

- Upstream reports DecisionBench / JevBench / MMAU / MVBench figures on the card; those were **not** independently reproduced.
- Best supported at ≤20 options; head width is 256.
- Reference path is local CUDA inference. Downloads contact Hugging Face (and pull `google/gemma-4-12B-it` components). No TypeSafe API key is involved.
- Audio conversion shells out to `ffmpeg`; treat media paths as trusted local files.
- Self-host GPU memory, disk, and power costs are on the operator. `Free source build` does **not** mean free to run.

## Review and maintenance

Reviewed **2026-09-22** (~21:55 Europe/Sofia) at Hugging Face revision [`c127654e586e05b2e9b75b3aaef075ddcf57a286`](https://huggingface.co/akhilaaa3/Jev-Omni/tree/c127654e586e05b2e9b75b3aaef075ddcf57a286) (model `lastModified` **2026-09-22 20:52 Europe/Sofia**).

Inspected model card README, `license: apache-2.0` card metadata, `requirements.txt`, `example.py`, `decision_config.json`, and `jev_omni.py` loader/classifier. X attribution: [https://x.com/Akhila_988/status/2102171891410825520](https://x.com/Akhila_988/status/2102171891410825520).

Source/card review only: no weight download, no CUDA inference, no benchmark rerun, no live TypeSafe calls.
