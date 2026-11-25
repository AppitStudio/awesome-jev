# Jev Heuristic Adapter by Shichao Song (compiles fixed decision tasks into reusable local Python programs that return TypeSafe SDK answers)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python adapter with the same `system_one()` call as TypeSafe's System One Adapter, plus a `compile()` step: an LLM writes a reusable Python program for each fixed question from examples, and later states run locally in microseconds to milliseconds, returning TypeSafe SDK answer types. A cost and latency alternative for stable, repetitive decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ki-Seki/jev-heuristic-adapter) |
| Maintainer | [Shichao Song](https://github.com/Ki-Seki). Independently curated. |
| Format | Python library (PyPI `jev-heuristic-adapter`) |
| Requirements | Python with `typesafe-sdk` 0.7.1+; an OpenAI key (optional extra) for compilation. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_heuristic_adapter/_client.py`](https://github.com/Ki-Seki/jev-heuristic-adapter/blob/5c340a4eed550b192601a0afcb1e92112650f338/src/jev_heuristic_adapter/_client.py) at the pinned commit. |

## When to use

- Replace a paid per-call decision with a cached local program when the task is fixed and simple.
- Mismatch: for open-ended or shifting decisions; accuracy is task-dependent.

## How it works

`src/jev_heuristic_adapter/_client.py` returns `typesafe_sdk` `ChoiceAnswer`, `NoulAnswer` and `ScoreAnswer` objects from compiled programs; it does not call Jev itself, so existing Jev code can swap clients. Integration evidence: [`src/jev_heuristic_adapter/_client.py`](https://github.com/Ki-Seki/jev-heuristic-adapter/blob/5c340a4eed550b192601a0afcb1e92112650f338/src/jev_heuristic_adapter/_client.py).

## Get started

Install with the OpenAI provider and open the example notebook.

```sh
uv add "jev-heuristic-adapter[openai]"
# then see example.ipynb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example notebook: [github.com/Ki-Seki/jev-heuristic-adapter/blob/5c340a4eed550b192601a0afcb1e92112650f338/example.ipynb](https://github.com/Ki-Seki/jev-heuristic-adapter/blob/5c340a4eed550b192601a0afcb1e92112650f338/example.ipynb)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Compiled programs are LLM-generated Python executed in-process; review them before trusting the output. Compilation sends your questions and examples to OpenAI (non-TypeSafe).

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 5c340a4eed55](https://github.com/Ki-Seki/jev-heuristic-adapter/tree/5c340a4eed550b192601a0afcb1e92112650f338). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
