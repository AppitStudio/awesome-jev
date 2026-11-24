# Contextual Guard by Abed Al-Kibbe (authorization check for agent actions with Jev, plus an AgentDojo replay benchmark)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Python library: give it your policy, the visible conversation, tool definitions and a proposed agent action, and Jev (or a local Clef-Flash model) answers `authorized`, `unauthorized` or `insufficient_evidence`. The repo also ships the benchmark: 10,357 static replay decisions on AgentDojo traces with human-adjudicated disagreements, where the author reports Jev still allowed 130 of 171 unauthorized actions and concludes neither model is a reliable sole gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yogur/contextual-guard) |
| Maintainer | [Abed Al-Kibbe](https://github.com/yogur). Independently curated. |
| Format | Python library (`jev_guard`, PyPI release pending) and benchmark |
| Requirements | Python 3.11 to 3.14 and a TypeSafe API key (or a local Clef-Flash runtime). |
| License | [MIT](https://github.com/yogur/contextual-guard/blob/1c30488704bf8abacc34202d4429aee3b704c0f3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_guard/__init__.py`](https://github.com/yogur/contextual-guard/blob/1c30488704bf8abacc34202d4429aee3b704c0f3/src/jev_guard/__init__.py) at the pinned commit. |

## When to use

- Add a context-aware second opinion before an agent runs a tool call, and measure it on your own traces.
- Mismatch: as a sole security control; the author's own results say it is not reliable enough.

## How it works

`src/jev_guard/__init__.py` builds one choice question from a versioned authorization prompt and calls Jev through `typesafe-sdk`; the application decides whether to execute, block or ask. Integration evidence: [`src/jev_guard/__init__.py`](https://github.com/yogur/contextual-guard/blob/1c30488704bf8abacc34202d4429aee3b704c0f3/src/jev_guard/__init__.py).

## Get started

Build the wheel from a clone (PyPI release pending), then run the example, which prints the request without a model call.

```sh
git clone https://github.com/yogur/contextual-guard.git && cd contextual-guard
uv sync --locked
uv run python examples/assess.py   # prints the request; no model call
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/yogur/contextual-guard/blob/1c30488704bf8abacc34202d4429aee3b704c0f3/benchmark/docs/RESULTS.md](https://github.com/yogur/contextual-guard/blob/1c30488704bf8abacc34202d4429aee3b704c0f3/benchmark/docs/RESULTS.md)
- Usage: [github.com/yogur/contextual-guard/blob/1c30488704bf8abacc34202d4429aee3b704c0f3/docs/USAGE.md](https://github.com/yogur/contextual-guard/blob/1c30488704bf8abacc34202d4429aee3b704c0f3/docs/USAGE.md)

## Limits and data handling

Static replay only, not live attack prevention; human review in the benchmark was supplied by the owner. Policy, conversation and tool data go to TypeSafe when the hosted provider is used.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 1c30488704bf](https://github.com/yogur/contextual-guard/tree/1c30488704bf8abacc34202d4429aee3b704c0f3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
