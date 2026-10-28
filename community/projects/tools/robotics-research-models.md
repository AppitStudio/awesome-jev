# Robotics research models (which robot models cs.RO papers use, with a Jev survey of architecture trends)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Study of which robotics models appear in arXiv cs.RO papers since January 2023 and what share of papers name each release (each release its own row), following the Interconnects arXiv-mentions method, with a site of charts. Separate surveys use Jev to classify architectural trends in titles and abstracts and frontier-LLM and Jev usage; analysis runs on Modal.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bkolligs/robotics-research-models) |
| Maintainer | [bkolligs](https://github.com/bkolligs). Independently curated. |
| Format | Python package (uv) with published charts |
| Requirements | Python with uv; AWS access for bulk paper downloads; a TypeSafe API key only to rerun the Jev surveys. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/TheRobotHerder/status/2115307563143385209)). |
| Jev evidence | [`src/mentions/survey.py`](https://github.com/bkolligs/robotics-research-models/blob/b687aff4cb868b15ae88ae629b7b8c34bb1dd117/src/mentions/survey.py) at the pinned commit. |

## When to use

- See which robot foundation models researchers actually use.
- Mismatch: no license file, so reuse rights are not granted; figures are the author's.

## How it works

`src/mentions/survey.py` posts each paper's title and abstract to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`) with architecture questions; it does not change mention counts. Integration evidence: [`src/mentions/survey.py`](https://github.com/bkolligs/robotics-research-models/blob/b687aff4cb868b15ae88ae629b7b8c34bb1dd117/src/mentions/survey.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bkolligs/robotics-research-models && cd robotics-research-models
uv sync
# see README for harvest, scan and survey commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Charts and methodology: [bkolligs.github.io/robotics-research-models/](https://bkolligs.github.io/robotics-research-models/)
- README: [github.com/bkolligs/robotics-research-models#readme](https://github.com/bkolligs/robotics-research-models#readme)

## Limits and data handling

Paper titles and abstracts (public) go to TypeSafe during the survey.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit b687aff4cb86](https://github.com/bkolligs/robotics-research-models/tree/b687aff4cb868b15ae88ae629b7b8c34bb1dd117). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
