# ruling

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Turns an open local chat model into a Jev-style decision engine served on `/v1/systemone`, with training, eval, and calibration commands; independent of TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bradAGI/ruling) |
| Maintainer | [bradAGI](https://github.com/bradAGI). Independently curated. |
| Format | Local decision server + training/eval CLI |
| Requirements | Python with `uv`; first start downloads a ~2.3 GB model; training modules need a GPU or MLX per upstream README. |
| License | [MIT](https://github.com/bradAGI/ruling/blob/28c05802755ab44a0259e97e112b6a2547ace7d7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Prototype System One-style decisions offline or on-prem with an open model.
- Fine-tune and calibrate a local decision model on your own labeled decisions.
- Mismatch: not affiliated with TypeSafe and not a validated substitute for hosted Jev.

## How it works

ruling scores option probabilities from a local model instead of generating text and exposes them through a `/v1/systemone`-shaped API. Upstream reports a comparison against Jev on 256 public judgments (231 vs 238 correct, not significant); that is the maintainer's result.

## Get started

Install and serve locally (no TypeSafe key needed):

```sh
git clone https://github.com/bradAGI/ruling.git
cd ruling
uv sync
uv run ruling serve   # downloads ~2.3 GB model on first start; serves http://127.0.0.1:8010
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README comparison charts and train/eval/calibrate commands.

## Limits and data handling

Text only; no images or audio. Local model accuracy depends on your data; upstream results were not reproduced here.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 28c05802755a](https://github.com/bradAGI/ruling/tree/28c05802755ab44a0259e97e112b6a2547ace7d7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
