# Jev vehicle classifier (Korean 12-class traffic survey)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Episode 1 of a Korean ITS series: vision-style features (axles, units, trailer type, load tons) become a JSON state and Jev picks one of the 12 official Korean road-traffic vehicle classes with probabilities; low confidence goes to an unclassified bucket for review (README in Korean).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kh20134/jev-vehicle-classifier) |
| Maintainer | [kh20134](https://github.com/kh20134). Independently curated. |
| Format | Python package and CLI (`python -m jev_vehicle`) |
| Requirements | Python 3.10+; mock mode needs no key, live mode needs `TYPESAFE_API_KEY` and the TypeSafe SDK. |
| License | [MIT](https://github.com/kh20134/jev-vehicle-classifier/blob/7a53fd242d84e1390e09e4b6ad2340a4354455d8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_vehicle/classifier.py`](https://github.com/kh20134/jev-vehicle-classifier/blob/7a53fd242d84e1390e09e4b6ad2340a4354455d8/src/jev_vehicle/classifier.py) at the pinned commit. |

## When to use

- Map detector output onto a fixed official class table without training a classifier for the last step.
- Keep the Jev question and class codes stable while the vision front end changes in later episodes.
- Mismatch: no camera model yet; episode 1 uses hand-made feature JSON and a mock extractor.

## How it works

`VehicleFeatures.to_state()` turns axles, units and load into a state, and `classifier.py` asks one Jev Choice over `class_01` to `class_12` through `TypeSafeClient(model="jev-latest")`. Out-of-table or low-confidence answers are counted as unclassified with `needs_review` set. Integration evidence: [`src/jev_vehicle/classifier.py`](https://github.com/kh20134/jev-vehicle-classifier/blob/7a53fd242d84e1390e09e4b6ad2340a4354455d8/src/jev_vehicle/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python -m jev_vehicle classify --sample semi5 --mock
python -m jev_vehicle classify --sample sedan --live   # needs TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample vehicles (sedan, bus, trucks, semi and full trailers) in the README.
- Series plan: `docs/SERIES.md`.

## Limits and data handling

Live mode sends only the feature JSON to TypeSafe on your key; no images in this episode.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 7a53fd242d84](https://github.com/kh20134/jev-vehicle-classifier/tree/7a53fd242d84e1390e09e4b6ad2340a4354455d8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
