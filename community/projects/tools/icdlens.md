# ICDLens

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python SDK for WHO ICD-10 catalogue lookup with reviewable coding suggestions: TypeSafe Jev (or Cloudflare Clef) evaluates catalogue candidates with typed questions instead of generating codes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Advaidv121/icdlens) |
| Maintainer | [Advaidv121](https://github.com/Advaidv121). Independently curated. |
| Format | Python SDK + local CLI |
| Requirements | Python; TypeSafe key (or Cloudflare credentials) for AI lookup; local catalogue needs none. |
| License | [MIT](https://github.com/Advaidv121/icdlens/blob/d2437fdedd3c9739115079c7ae352e17d15211c7/LICENSE) |
| Jev evidence | [`src/icdjev/jev.py`](https://github.com/Advaidv121/icdlens/blob/d2437fdedd3c9739115079c7ae352e17d15211c7/src/icdjev/jev.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Suggest ICD-10 codes from clinical text with scores a coder can review.
- Mismatch: suggestions for human review, not automated medical coding.

## How it works

`get_icd(text)` traverses the catalogue hierarchy, asks Jev typed support questions per candidate, and returns scores, cutoffs and a review report. (Summarized from the upstream [README](https://github.com/Advaidv121/icdlens/blob/d2437fdedd3c9739115079c7ae352e17d15211c7/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `pip install` per the README, then call `get_icd(text)` or use the CLI.

## Limits and data handling

Clinical text goes to TypeSafe or Cloudflare when AI lookup is used; avoid sending identifiable data. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit d2437fdedd3c](https://github.com/Advaidv121/icdlens/tree/d2437fdedd3c9739115079c7ae352e17d15211c7). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
