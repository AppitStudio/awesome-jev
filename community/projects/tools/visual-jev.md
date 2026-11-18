# Visual Jev by Guanxu Yu (research code and open adapters that extend Jev-style typed decisions to images)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Official code and results for the paper *Visual Jev: Accurate and Efficient Decisions from Shared Visual Context* (arXiv:2609.25845). It extends the Jev-style decision interface to vision: one image and shared context, many independent questions each with its own choices, scored from the existing LM head of a LoRA-tuned Qwen3-VL (4B and 8B adapters on Hugging Face). The quickstart accepts Jev's named `questions` with a shared `state`. With 32 questions per image the authors report 5.7 ms amortized per question, and include a calibration script because raw probabilities are overconfident. Independent of TypeSafe; it does not call the Jev API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/guanxuyu-sv/Visual-Jev) |
| Maintainer | [guanxuyu-sv](https://github.com/guanxuyu-sv). Independently curated. |
| Format | Python research code with released LoRA adapters (Apache-2.0) |
| Requirements | Python with PyTorch on CUDA or Apple Silicon (MPS); downloads the Qwen3-VL base and the adapter on first use. No API key. |
| License | [Apache-2.0](https://github.com/guanxuyu-sv/Visual-Jev/blob/62f5f3a2bb34f4903763f5a15831eb7157c065df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`code/examples/quickstart.py`](https://github.com/guanxuyu-sv/Visual-Jev/blob/62f5f3a2bb34f4903763f5a15831eb7157c065df/code/examples/quickstart.py) at the pinned commit. |

## When to use

- Study or self-host Jev-style multi-question decisions over images.
- Mismatch: hosted Jev; this is an independent open model, not TypeSafe's.

## How it works

`code/examples/quickstart.py` loads Qwen3-VL with the Visual Jev adapter and answers a Jev-shaped request (`state` plus named `choice` questions, 2–16 options) about a local image; `code/examples/calibrate.py` fits a temperature and risk threshold. Integration evidence: [`code/examples/quickstart.py`](https://github.com/guanxuyu-sv/Visual-Jev/blob/62f5f3a2bb34f4903763f5a15831eb7157c065df/code/examples/quickstart.py).

## Get started

Install the requirements, then classify a local image or run the included multi-question request.

```sh
git clone https://github.com/guanxuyu-sv/Visual-Jev && cd Visual-Jev
pip install torch torchvision && pip install -r code/requirements.txt
python code/examples/quickstart.py --image assets/figures/demo_bottle.jpg --request-file code/examples/bottle_questions.json --device mps
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2609.25845](https://arxiv.org/abs/2609.25845)
- Project page: [guanxuyu-sv.github.io/Visual-Jev/](https://guanxuyu-sv.github.io/Visual-Jev/)
- 4B adapter: [huggingface.co/guanxuyu/visual-jev-4b-answer-sft](https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft)

## Limits and data handling

Runs locally; no data leaves the machine. Accuracy and latency figures are the paper's, measured on the authors' hardware, and not reproduced here. The Qwen backbone and datasets carry their own terms.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 62f5f3a2bb34](https://github.com/guanxuyu-sv/Visual-Jev/tree/62f5f3a2bb34f4903763f5a15831eb7157c065df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
