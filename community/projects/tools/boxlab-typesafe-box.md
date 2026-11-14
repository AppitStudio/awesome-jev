# boxlab (experiment suite for Jev 1.14's Box question type: how accurately it locates things in images)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Eight experiments on TypeSafe's Box primitive ("where is this thing in the image?") using images the suite draws itself, so every true box is known: baseline tightness, small targets and crop-then-Box, absent targets with a yes/no check, ambiguous twins, document fields, operational limits, and a picture as the target. Scored by intersection over union; about 160 requests for a full run, with committed results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/earchibald/typesafe-ai-box) |
| Maintainer | [earchibald](https://github.com/earchibald). Independently curated. |
| Format | Python experiment suite with results (uv) |
| Requirements | Python and uv; a `TYPESAFE_API_KEY` (`--mock` runs the pipeline without calls). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`boxlab/api.py`](https://github.com/earchibald/typesafe-ai-box/blob/2e16bcc5f9943f349a12d2d8af86510a8512f16c/boxlab/api.py) at the pinned commit. |

## When to use

- Check whether Jev's Box answers are tight enough for your cropping or field-extraction step.
- Mismatch: real photos; all test images are synthetic.

## How it works

`boxlab/api.py` posts to `https://api.typesafe.ai/v1/systemone` with the model pinned to `jev-1.14.0` (Box needs Jev 1.14); `run.py` runs the experiments and `analyze.py` writes the summary and overlays. Integration evidence: [`boxlab/api.py`](https://github.com/earchibald/typesafe-ai-box/blob/2e16bcc5f9943f349a12d2d8af86510a8512f16c/boxlab/api.py).

## Get started

Add your key, run the experiments, then analyze.

```sh
git clone https://github.com/earchibald/typesafe-ai-box && cd typesafe-ai-box
echo 'TYPESAFE_API_KEY=...' > .env
uv run run.py
uv run analyze.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/earchibald/typesafe-ai-box/blob/2e16bcc5f9943f349a12d2d8af86510a8512f16c/README.md](https://github.com/earchibald/typesafe-ai-box/blob/2e16bcc5f9943f349a12d2d8af86510a8512f16c/README.md)
- Results: [github.com/earchibald/typesafe-ai-box/tree/2e16bcc5f9943f349a12d2d8af86510a8512f16c/results](https://github.com/earchibald/typesafe-ai-box/tree/2e16bcc5f9943f349a12d2d8af86510a8512f16c/results)

## Limits and data handling

Generated test images go to TypeSafe on your key. The linked write-up and slides are hosted outside the repository. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 2e16bcc5f994](https://github.com/earchibald/typesafe-ai-box/tree/2e16bcc5f9943f349a12d2d8af86510a8512f16c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
