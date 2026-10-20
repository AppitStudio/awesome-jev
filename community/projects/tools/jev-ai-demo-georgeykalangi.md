# jev-ai-demo (Jev primitives walkthrough)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Python walkthrough of Jev's Choice, Score and Noul primitives: a quickstart, atomic scoring and confidence routing examples that replay the sample responses from TypeSafe's docs without a key, then call the live API when one is set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/georgeykalangi/jev-ai-demo) |
| Maintainer | [georgeykalangi](https://github.com/georgeykalangi). Independently curated. |
| Format | Python package with runnable examples and tests |
| Requirements | Python 3 and pip; a TypeSafe key only for live mode. |
| License | [MIT](https://github.com/georgeykalangi/jev-ai-demo/blob/c3eb49f83df2f8264e2e92194d6cf26269f55f81/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_demo/client.py`](https://github.com/georgeykalangi/jev-ai-demo/blob/c3eb49f83df2f8264e2e92194d6cf26269f55f81/jev_demo/client.py) at the pinned commit. |

## When to use

- Learn the 'ask atomic questions, decide in code' pattern before writing an integration.
- Run Jev examples offline in a workshop or CI using recorded responses.
- Mismatch: teaching demo, not a library to depend on.

## How it works

`jev_demo/client.py` posts a state and typed questions to `https://api.typesafe.ai/v1/systemone`, or replays fixtures copied from TypeSafe's published sample responses when no key is set. `jev_demo/triage.py` combines separate severity, frustration and report-quality answers with weights in Python and routes low-confidence cases to a person. Integration evidence: [`jev_demo/client.py`](https://github.com/georgeykalangi/jev-ai-demo/blob/c3eb49f83df2f8264e2e92194d6cf26269f55f81/jev_demo/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/georgeykalangi/jev-ai-demo.git && cd jev-ai-demo
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
.venv/bin/python examples/01_quickstart.py   # replays recorded docs responses
export TYPESAFE_API_KEY=...
.venv/bin/python examples/03_confidence_routing.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/01_quickstart.py, 02_atomic_scoring.py, 03_confidence_routing.py
- fixtures/ (each links to its TypeSafe docs page)

## Limits and data handling

Unofficial community demo, not affiliated with TypeSafe. Live mode sends example states to TypeSafe.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit c3eb49f83df2](https://github.com/georgeykalangi/jev-ai-demo/tree/c3eb49f83df2f8264e2e92194d6cf26269f55f81). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
