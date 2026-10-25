# langgraph-regression-guard (LangGraph PR regression checks with node cassettes and a Jev KPI judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Early-stage regression guard for LangGraph agents: records each node's inputs and outputs as cassettes and replays them on every PR to separate root from propagated drift, scores KPIs with a typed Jev judge whose low-confidence verdicts defer to a human, and keeps an accept, reject or override review loop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AMOHYZ/langgraph-regression-guard) |
| Maintainer | [AMOHYZ](https://github.com/AMOHYZ). Independently curated. |
| Format | Python package (uv) |
| Requirements | Python with uv; `JEV_API_URL` and `JEV_API_KEY` for the judge layer (the offline tests use a fake judge). |
| License | [MIT](https://github.com/AMOHYZ/langgraph-regression-guard/blob/b0ae3b042e568e4c01a1a9e873fbc8c853618702/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lgcov/jev_judge.py`](https://github.com/AMOHYZ/langgraph-regression-guard/blob/b0ae3b042e568e4c01a1a9e873fbc8c853618702/src/lgcov/jev_judge.py) at the pinned commit. |

## When to use

- Catch prompt changes that silently degrade downstream LangGraph nodes while CI stays green.
- Send uncertain judge verdicts to a reviewer instead of guessing.
- Mismatch: early; the GitHub Action and calibration loop are on the roadmap.

## How it works

`jev_judge.py` sends one node's input and output as `state` with one typed question per KPI (`jev-latest`) to the URL in `JEV_API_URL`, and keeps the key out of logs and errors. Integration evidence: [`src/lgcov/jev_judge.py`](https://github.com/AMOHYZ/langgraph-regression-guard/blob/b0ae3b042e568e4c01a1a9e873fbc8c853618702/src/lgcov/jev_judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # JEV_API_URL / JEV_API_KEY
uv sync
uv run pytest          # offline, fake judge
uv run graph-diff old.json new.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/AMOHYZ/langgraph-regression-guard#readme](https://github.com/AMOHYZ/langgraph-regression-guard#readme)

## Limits and data handling

With the Jev judge on, recorded node inputs and outputs go to the configured Jev endpoint. Cassettes are stored in the repository you run it in.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit b0ae3b042e56](https://github.com/AMOHYZ/langgraph-regression-guard/tree/b0ae3b042e568e4c01a1a9e873fbc8c853618702). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
