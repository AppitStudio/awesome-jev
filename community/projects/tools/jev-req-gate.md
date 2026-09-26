# jev-req-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Quality gate for AI-generated requirements: TypeSafe Jev MECE questions route PASS/REVIEW/BLOCK with calibrated probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thomaszta/jev-req-gate) |
| Maintainer | [thomaszta](https://github.com/thomaszta). Independently curated. |
| Format | Python CLI, library, agent skill, and GitHub Action. |
| Requirements | Python; typesafe-sdk + TYPESAFE_API_KEY for live gates; `--demo` and browser playground work without a key. |
| License | [MIT](https://github.com/thomaszta/jev-req-gate/blob/f56adc5077f707d2053bbfd15ef31d6560b16fb0/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use to **batch-check LLM requirements** before they enter backlog. Prefer human review alone for tiny one-off specs.

## How it works

Packs requirement + context into parallel Choice/Score/Noul questions across five MECE faces; calibrated thresholds route pass/review/block; SQLite caches judgments.

## Get started

```sh
git clone https://github.com/thomaszta/jev-req-gate.git
cd jev-req-gate
git checkout f56adc5077f707d2053bbfd15ef31d6560b16fb0
# python3 reqgate.py --demo unrealistic  # offline; live needs TYPESAFE_API_KEY
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit f56adc5](https://github.com/thomaszta/jev-req-gate/tree/f56adc5077f707d2053bbfd15ef31d6560b16fb0). AI-assisted README and license inspection; install/live paths not executed.
