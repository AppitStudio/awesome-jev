# systemone-vision-test (Landolt-ring eye-chart test for Jev and local System One models)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Japanese-documented benchmark that shows Landolt-ring eye-chart images, degraded by simulated vision modes, to System One models (local `clef` and `clef-flash`, or hosted Jev) and measures down to which acuity each model still answers the ring's direction, with a GUI and measured direction-bias notes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/naraba/systemone-vision-test) |
| Maintainer | [naraba](https://github.com/naraba). Independently curated. |
| Format | Python benchmark with GUI |
| Requirements | Python 3.10+; a System One-compatible endpoint (local by default); a Jev API key for the hosted model, through OpenRouter by default. |
| License | [MIT](https://github.com/naraba/systemone-vision-test/blob/7dfadb8b46f733e81cedebaa52180f10ffb36f57/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone_vision_test/config.py`](https://github.com/naraba/systemone-vision-test/blob/7dfadb8b46f733e81cedebaa52180f10ffb36f57/src/systemone_vision_test/config.py) at the pinned commit. |

## When to use

- Probe how well Jev reads small image details compared with local System One models.
- Reuse the degradation filters and direction-bias analysis for your own vision checks.
- Mismatch: README is in Japanese; this is a toy acuity test, not a medical one.

## How it works

`config.py` defines a local `/v1/systemone` endpoint for `clef` and the hosted Jev route (OpenRouter's `/api/v1/systemone` by default, or `https://api.typesafe.ai/v1/systemone`); each image is asked one direction Choice question. Integration evidence: [`src/systemone_vision_test/config.py`](https://github.com/naraba/systemone-vision-test/blob/7dfadb8b46f733e81cedebaa52180f10ffb36f57/src/systemone_vision_test/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -e ".[dev]"
# set JEV_API_KEY (or .jev_api_key), then:
python -m systemone_vision_test.benchmark --models jev --repeats 1 --visions 2.0 1.0 0.5
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Spec (Japanese): [github.com/naraba/systemone-vision-test/blob/main/docs/spec.md](https://github.com/naraba/systemone-vision-test/blob/main/docs/spec.md)
- Direction bias notes: [github.com/naraba/systemone-vision-test/blob/main/docs/landolt_direction_bias.md](https://github.com/naraba/systemone-vision-test/blob/main/docs/landolt_direction_bias.md)

## Limits and data handling

With the hosted model selected, generated test images go to OpenRouter or TypeSafe. The default run includes Jev and incurs API charges; local models only are free.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 7dfadb8b46f7](https://github.com/naraba/systemone-vision-test/tree/7dfadb8b46f733e81cedebaa52180f10ffb36f57). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
