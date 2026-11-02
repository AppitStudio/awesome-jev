# AI-Core Engineering Workbench (15-lesson course code ending in a guarded issue-to-patch workflow with Jev routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Runnable companion to a 15-part bilingual course on anirach.com: lessons go from plain functions to a guarded issue-to-patch workbench where Jev gives a typed route and bypass judgment, checks inspect the candidate patch, and a separate quality gate reviews the explanation. Runs offline with scripted fixtures by default; real Jev calls are optional.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Anirach/ai-core-engineering-workbench) |
| Maintainer | [Anirach](https://github.com/Anirach). Independently curated. |
| Format | Python course code and labs (stdlib only) |
| Requirements | Python 3.11+; an optional `TYPESAFE_API_KEY` for real Jev decisions. |
| License | [MIT](https://github.com/Anirach/ai-core-engineering-workbench/blob/18cdfcd4156d3d02acb8badf3b3a0a823113e0ed/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`workbench/jev.py`](https://github.com/Anirach/ai-core-engineering-workbench/blob/18cdfcd4156d3d02acb8badf3b3a0a823113e0ed/workbench/jev.py) at the pinned commit. |

## When to use

- Learn how to put a typed decision step inside a guarded agent workflow.
- Mismatch: default decisions are scripted fixtures, so they show control flow, not Jev accuracy.

## How it works

`workbench/jev.py` is an optional HTTP adapter that posts the state and questions to TypeSafe `/v1/systemone` (model `jev-1.14.0`) and validates the response before the workbench interprets its uncertainty. Integration evidence: [`workbench/jev.py`](https://github.com/Anirach/ai-core-engineering-workbench/blob/18cdfcd4156d3d02acb8badf3b3a0a823113e0ed/workbench/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Anirach/ai-core-engineering-workbench.git && cd ai-core-engineering-workbench
python3 -m unittest discover -v
python3 -m workbench.lesson all
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Course series: [anirach.com/blog/#series-ai-engineering](https://anirach.com/blog/#series-ai-engineering)

## Limits and data handling

Offline by default; with a key, lesson states are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 18cdfcd4156d](https://github.com/Anirach/ai-core-engineering-workbench/tree/18cdfcd4156d3d02acb8badf3b3a0a823113e0ed). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
