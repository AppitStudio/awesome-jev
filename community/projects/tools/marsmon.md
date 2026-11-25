# MarsMon by Çağatay (field report on the Mars rovers built from NASA raw images, with Jev answering typed questions about each picture)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open working notebook that turns NASA's public Perseverance and Curiosity raw images and route data into a weekly field report. Jev answers one typed question per image (which terrain, is the arm touching a rock), plain code does every count and decision, hand labels measure how often Jev is right, and Claude writes the weekly text from computed tables.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cagataycode/marsmon) |
| Maintainer | [Çağatay](https://github.com/cagataycode). Independently curated. |
| Format | Python (standard library only) |
| Requirements | Python 3.10+ and a TypeSafe API key for the Jev steps. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`marsmon/jev.py`](https://github.com/cagataycode/marsmon/blob/5cb05b7468b12be6ac4b27e7fb27885b15d552b3/marsmon/jev.py) at the pinned commit. |

## When to use

- See a careful, logged example of using Jev as an image judge inside a code-owned pipeline.
- Mismatch: if you want a finished report; this is an early build.

## How it works

`marsmon/jev.py` posts images and questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, image header enabled) and maps Noul probabilities to yes, no or unsettled with fixed thresholds. Questions live in `marsmon/questions.py`. Integration evidence: [`marsmon/jev.py`](https://github.com/cagataycode/marsmon/blob/5cb05b7468b12be6ac4b27e7fb27885b15d552b3/marsmon/jev.py).

## Get started

Pull route stops and images, pick terrain frames, then label a sample.

```sh
python3 -m marsmon.ingest route --rover m20
python3 -m marsmon.ingest images --rover m20 --camera NAVCAM_LEFT
python3 -m marsmon.select_terrain --rover m20
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Work log: [github.com/cagataycode/marsmon/blob/5cb05b7468b12be6ac4b27e7fb27885b15d552b3/docs/LOG.md](https://github.com/cagataycode/marsmon/blob/5cb05b7468b12be6ac4b27e7fb27885b15d552b3/docs/LOG.md)
- Concept: [github.com/cagataycode/marsmon/blob/5cb05b7468b12be6ac4b27e7fb27885b15d552b3/docs/CONCEPT.md](https://github.com/cagataycode/marsmon/blob/5cb05b7468b12be6ac4b27e7fb27885b15d552b3/docs/CONCEPT.md)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Early build (November 2026): only a first 22-frame Jev probe has run, and accuracy against the hand labels is not yet reported.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 5cb05b7468b1](https://github.com/cagataycode/marsmon/tree/5cb05b7468b12be6ac4b27e7fb27885b15d552b3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
