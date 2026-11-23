# GeoDecisions by Wilson Wongso et al. (UNSW benchmark of spatial awareness and geographic bias in decision models, including Jev-1.14)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and results for "Seeing Is Locating: Spatial Awareness and Geographic Bias in Decision Language Models" (UNSW Sydney and HKUST Guangzhou). Task 1 classifies satellite images, everyday photos and species photos given the image, coordinates or both; Task 2 rates 2,000 world locations on 11 topics. It adds shuffle-corrected geo-bias scores and a training-free location prior, and compares Jev-1.14 with GPT-6 Luna, open decision models and base LLMs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cruiseresearchgroup/GeoDecisions) |
| Maintainer | [cruiseresearchgroup](https://github.com/cruiseresearchgroup). Independently curated. |
| Format | Python benchmark harness + results |
| Requirements | Python 3.11+; large dataset downloads (iNat, YFCC, fMoW; hundreds of GB streamed); a TypeSafe API key to run Jev-1.14. |
| License | [Apache-2.0](https://github.com/cruiseresearchgroup/GeoDecisions/blob/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/modules/typesafe_jev.py`](https://github.com/cruiseresearchgroup/GeoDecisions/blob/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577/src/modules/typesafe_jev.py) at the pinned commit. |

## When to use

- Check how Jev and other decision models use location and where they show geographic bias, before relying on them for image or place judgments.
- Mismatch: a quick test; full runs need large datasets.

## How it works

`src/modules/typesafe_jev.py` wraps TypeSafe Jev as a `DecisionModel` that posts to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`; the pinned run config is `configs/runs/jev-1.14.yaml`. Closed-source models default to a fixed 2,000-sample subset per Task 1 dataset. Integration evidence: [`src/modules/typesafe_jev.py`](https://github.com/cruiseresearchgroup/GeoDecisions/blob/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577/src/modules/typesafe_jev.py).

## Get started

Install the environment, prepare the datasets with the provided scripts, then run the Jev config.

```sh
git clone https://github.com/cruiseresearchgroup/GeoDecisions && cd GeoDecisions
cp .env.example .env   # TYPESAFE_API_KEY
# follow the README's data preparation steps, then run configs/runs/jev-1.14.yaml
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/cruiseresearchgroup/GeoDecisions/blob/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577/RESULTS.md](https://github.com/cruiseresearchgroup/GeoDecisions/blob/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577/RESULTS.md)
- Jev run config: [github.com/cruiseresearchgroup/GeoDecisions/blob/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577/configs/runs/jev-1.14.yaml](https://github.com/cruiseresearchgroup/GeoDecisions/blob/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577/configs/runs/jev-1.14.yaml)

## Limits and data handling

Results are the authors' measurements (Jev-1.14 on 2,000-sample subsets). Images and prompts are sent to each provider you run.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 6d228a63fa5c](https://github.com/cruiseresearchgroup/GeoDecisions/tree/6d228a63fa5ce3b2bab498f6ecaa6bd403e33577). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
