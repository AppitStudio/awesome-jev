# jev-mnist

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Shows all 10,000 MNIST test digits to Jev 1.14's image input as a 0 to 9 Choice question: 92.45% accuracy at 0.17 s per image, with a confusion matrix that shows a strong bias toward answering 7.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kaitoy/jev-mnist) |
| Maintainer | [kaitoy](https://github.com/kaitoy). Independently curated. |
| Format | Python CLI (uv) with results CSV and an HTML report |
| Requirements | Python and uv (mise optional); a TypeSafe API key. The MNIST data is downloaded by the tool. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/kaitoy3_/status/2111667474878140846)). |
| Jev evidence | [`jev_mnist/classify.py`](https://github.com/kaitoy/jev-mnist/blob/4ae6a16ba49df03a5ad78fe42ecbb371eed1a704/jev_mnist/classify.py) at the pinned commit. |

## When to use

- Get a quick, reproducible sense of how Jev's experimental image input handles a classic vision task.
- Reuse the error analysis: per-digit accuracy and which wrong answers Jev prefers.
- Mismatch: image input is a TypeSafe preview feature, and handwritten digits are far from most production images.

## How it works

Each 28x28 image is upscaled (10x by default), encoded as PNG and sent in `state` as a `typesafe_sdk.Image` with a Choice question over the ten digits; the tool records the top answer, its probability, latency and token use, then writes the confusion matrix. Integration evidence: [`jev_mnist/classify.py`](https://github.com/kaitoy/jev-mnist/blob/4ae6a16ba49df03a5ad78fe42ecbb371eed1a704/jev_mnist/classify.py).

## Get started

From the upstream README (not run on the review host):

```sh
mise install
uv sync --extra test
cp .env.example .env     # add your TypeSafe API key
uv run jev-mnist --limit 10000 --output results.csv
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Report page: [kaitoy.github.io/jev-mnist/](https://kaitoy.github.io/jev-mnist/)
- Author's X post (Japanese): [x.com/kaitoy3_/status/2111667474878140846](https://x.com/kaitoy3_/status/2111667474878140846)

## Limits and data handling

Only public MNIST images go to TypeSafe, on your key (the full run used about 5.9 million input tokens). No LICENSE file on the reviewed commit, so the code is source-available only.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 4ae6a16ba49d](https://github.com/kaitoy/jev-mnist/tree/4ae6a16ba49df03a5ad78fe42ecbb371eed1a704). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
