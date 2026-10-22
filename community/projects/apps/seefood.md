# SeeFood (food recognizer with EmbeddingGemma and Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web app inspired by the hot dog app from Silicon Valley that recognizes many dishes: EmbeddingGemma 2 retrieves candidate foods from mean-centered visual prototypes, and Jev image picks among them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/krjadhav/seefood) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://seefood.verygoodproduct.company/) |
| Pricing and access | Free live demo; no license file in the repository, so the source is viewable but not open source. Checked 2026-10-22. |
| Jev evidence | [`server/jev.py`](https://github.com/krjadhav/seefood/blob/24557ef67f908ecda797f94682fa5b1ad245ce6e/server/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/kj4dh4v/status/2113196809149632738)). |
| Maintainer | [krjadhav](https://github.com/krjadhav). Independently curated. |
| Format | Web app (Python backend, web frontend) |
| Platform and availability | Web, at seefood.verygoodproduct.company. |
| Jev's role | Jev looks at the photo and chooses the dish among the candidates retrieved by EmbeddingGemma. |
| Requirements | A browser for the live site; to run locally, Node.js 20.19+ or 22.12+, Python 3.11+, the EmbeddingGemma 2 weights and a Jev key. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Identify a dish from a photo, including many Indian dishes.
- Read a clear write-up of retrieval plus a decision model for image classification.
- Mismatch: no open-source license; treat the code as reference only.

## How it works

`server/jev.py` is the decision stage: it sends the photo and the retrieved candidate dishes to Jev's image API with `JEV_API_KEY` (or `TYPESAFE_API_KEY`) and returns the chosen dish. Integration evidence: [`server/jev.py`](https://github.com/krjadhav/seefood/blob/24557ef67f908ecda797f94682fa5b1ad245ce6e/server/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
# Use the live site, or follow the README to run the backend and frontend locally
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [seefood.verygoodproduct.company/](https://seefood.verygoodproduct.company/)
- Build journey in the README: [github.com/krjadhav/seefood#readme](https://github.com/krjadhav/seefood#readme)

## Limits and data handling

Uploaded photos are sent to the app's server and to TypeSafe. No license file was found at the reviewed commit.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 24557ef67f90](https://github.com/krjadhav/seefood/tree/24557ef67f908ecda797f94682fa5b1ad245ce6e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
