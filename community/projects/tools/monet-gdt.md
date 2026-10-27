# monet_gdt (5.5 MB on-device wallpaper model for mood, colors and shapes, trained on Jev labels)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

On-device wallpaper model for libmonet apps: from a wallpaper it scores 10 mood words, picks a three-colour theme and scores 29 decorative shapes in one 5.55 MB ONNX graph (10-15 ms on one Apple-silicon core). Training labels come from Jev's vision questions on CC0, public-domain or Apache-generated images, distilled through a teacher into a small student. Weights on Hugging Face.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Telosnex/monet_gdt) |
| Maintainer | [Telosnex](https://github.com/Telosnex). Independently curated. |
| Format | ONNX model with Python training scripts |
| Requirements | onnxruntime to use the model; a TypeSafe API key only to relabel with Jev. |
| License | [MIT](https://github.com/Telosnex/monet_gdt/blob/813045222efb8965eb3c3cc72c11de72f06b327a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev.py`](https://github.com/Telosnex/monet_gdt/blob/813045222efb8965eb3c3cc72c11de72f06b327a/scripts/jev.py) at the pinned commit. |

## When to use

- Distil Jev's image judgments into a tiny model that runs offline.
- Mismatch: built for libmonet's mood words and shapes.

## How it works

`scripts/jev.py` sends images with mood, colour and shape questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0` in the experiments); the labels train the teacher and student. Integration evidence: [`scripts/jev.py`](https://github.com/Telosnex/monet_gdt/blob/813045222efb8965eb3c3cc72c11de72f06b327a/scripts/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install onnxruntime pillow numpy
# download monet_gdt.onnx from https://huggingface.co/Telosnex/monet_gdt, then see the README usage
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model: [huggingface.co/Telosnex/monet_gdt](https://huggingface.co/Telosnex/monet_gdt)
- README: [github.com/Telosnex/monet_gdt#readme](https://github.com/Telosnex/monet_gdt#readme)

## Limits and data handling

Using the model sends nothing anywhere. Relabelling sends training images to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 813045222efb](https://github.com/Telosnex/monet_gdt/tree/813045222efb8965eb3c3cc72c11de72f06b327a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
