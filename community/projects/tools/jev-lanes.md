# jev-lanes (confidence-based routing and escalation for Jev in LangGraph)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python library that routes each Jev classification into lanes by confidence: accept, retry with a fallback LLM, or pause for a resumable human review in a LangGraph StateGraph, with a serializable trace of every route.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EricMariano/jev-lanes) |
| Maintainer | [EricMariano](https://github.com/EricMariano). Independently curated. |
| Format | Python library (LangGraph) |
| Requirements | Python with uv; a TypeSafe key and any LangChain chat model for live use (offline fakes included). |
| License | [MIT](https://github.com/EricMariano/jev-lanes/blob/8d072915da13cf4149d56eabf65998ac0da72efd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_lanes/adapters.py`](https://github.com/EricMariano/jev-lanes/blob/8d072915da13cf4149d56eabf65998ac0da72efd/src/jev_lanes/adapters.py) at the pinned commit. |

## When to use

- Add a human-review lane for low-confidence decisions in a LangGraph app.
- Test routing policies offline before spending on live calls.
- Mismatch: v0.1 release candidate, not on PyPI; its own Banking77 test found no benefit from the fallback model.

## How it works

`adapters.py` defines `JevClassifier`, which calls TypeSafe through the alpha `langchain-typesafe` package and maps the confidence into the configured bands. Integration evidence: [`src/jev_lanes/adapters.py`](https://github.com/EricMariano/jev-lanes/blob/8d072915da13cf4149d56eabf65998ac0da72efd/src/jev_lanes/adapters.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync --locked --dev
uv run python examples/router_offline.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Banking77 report: [github.com/EricMariano/jev-lanes/blob/main/benchmarks/results/banking77/report.md](https://github.com/EricMariano/jev-lanes/blob/main/benchmarks/results/banking77/report.md)
- README: [github.com/EricMariano/jev-lanes#readme](https://github.com/EricMariano/jev-lanes#readme)

## Limits and data handling

Inputs go to TypeSafe and, on fallback, to your chat model. Thresholds are not calibrated for you.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 8d072915da13](https://github.com/EricMariano/jev-lanes/tree/8d072915da13cf4149d56eabf65998ac0da72efd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
