# Where the Image Sits by Youzhi333 (paper code: image placement in the prompt flips Jev-style decisions read from open vision-language models)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and results for the paper *Where the Image Sits: Vision–Text Order Bias in Jev*. It reads System One style decisions (one prefill, a softmax over option labels) from seven open vision-language checkpoints and shows that moving the image from the start to the end of the prompt flips 41% of decisions across six datasets, then tests cheaper stable readouts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Youzhi333/Visual_Tex_Order_Bias_Jev) |
| Maintainer | [Youzhi333](https://github.com/Youzhi333). Independently curated. |
| Format | Python research code (PyTorch) |
| Requirements | Python 3.10+, PyTorch with CUDA, and the open checkpoints (Qwen3-VL, Qwen2.5-VL, LLaVA-OneVision and others). |
| License | [Apache-2.0](https://github.com/Youzhi333/Visual_Tex_Order_Bias_Jev/blob/3f70ed038943c8884fcfbe796c7806dba39990c0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`code/anyjev/__init__.py`](https://github.com/Youzhi333/Visual_Tex_Order_Bias_Jev/blob/3f70ed038943c8884fcfbe796c7806dba39990c0/code/anyjev/__init__.py) at the pinned commit. |

## When to use

- Design multimodal decision prompts that are stable to image placement.
- Mismatch: if you want measurements of TypeSafe's Jev; this studies open models.

## How it works

`code/anyjev/` turns open LLMs into Jev-style deciders by reading next-token logits; it states it is not affiliated with or derived from TypeSafe AI or Jev. No TypeSafe calls are made, so the results do not describe TypeSafe's hosted Jev. Integration evidence: [`code/anyjev/__init__.py`](https://github.com/Youzhi333/Visual_Tex_Order_Bias_Jev/blob/3f70ed038943c8884fcfbe796c7806dba39990c0/code/anyjev/__init__.py).

## Get started

Set up the environment, then reproduce one model and dataset cell.

```sh
pip install -r requirements.txt
export PYTHONPATH="$PWD/code:$PWD/code/scripts"
python code/research2visualtexorder/run_order.py --dataset aokvqa  # see README for the full flags
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Third-party notices: [github.com/Youzhi333/Visual_Tex_Order_Bias_Jev/blob/3f70ed038943c8884fcfbe796c7806dba39990c0/THIRD_PARTY.md](https://github.com/Youzhi333/Visual_Tex_Order_Bias_Jev/blob/3f70ed038943c8884fcfbe796c7806dba39990c0/THIRD_PARTY.md)

## Limits and data handling

Results are the authors' own; the README stresses the robust finding is decision instability, not a uniform accuracy loss, and the accuracy effect depends on the dataset. Needs a GPU.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 3f70ed038943](https://github.com/Youzhi333/Visual_Tex_Order_Bias_Jev/tree/3f70ed038943c8884fcfbe796c7806dba39990c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
