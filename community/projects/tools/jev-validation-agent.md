# Jev_validation_agent

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python **Jev Guard** (`jev_guard`): double-check LLM answers with TypeSafe Jev Noul/Score/Choice checks (on-topic, contradicts-source, format) before showing them to users, plus a local/demo UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/omkarchougule19/Jev_validation_agent) |
| Maintainer | [omkarchougule19](https://github.com/omkarchougule19). Independently curated. |
| Format | Python package under `src/jev_guard` + demo app; optional hosted demo link in README. |
| Requirements | Python 3.11+; TypeSafe API key for live guards. |
| License | [MIT](https://github.com/omkarchougule19/Jev_validation_agent/blob/1148239c77e5203e67080bf5c78d457f3f316d12/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live demo/TypeSafe and published comparison charts not re-run. Distinct from other JevGuard listings by different owners. |

## When to use

Use it as a **cheap answer guardrail** before user-visible responses. Prefer [agent-chaperone](agent-chaperone.md) / tool firewalls when the concern is tool calls rather than final answers.

## How it works

[`guard()`](https://github.com/omkarchougule19/Jev_validation_agent/blob/1148239c77e5203e67080bf5c78d457f3f316d12/src/jev_guard/guard.py) runs configured checks via [`client.py`](https://github.com/omkarchougule19/Jev_validation_agent/blob/1148239c77e5203e67080bf5c78d457f3f316d12/src/jev_guard/client.py); overall verdict is the worst of pass/flag/block. API errors can flag or block per `on_error`.

## Get started

```sh
git clone https://github.com/omkarchougule19/Jev_validation_agent.git
cd Jev_validation_agent
git checkout 1148239c77e5203e67080bf5c78d457f3f316d12
# pip install -e .  / follow README; set TYPESAFE_API_KEY for live guard()
```

## Examples and demos

- README `guard()` snippet; upstream comparison chart (not re-measured).
- Demo app under `src/jev_guard/demo/`; README mentions [jev-guard-demo.onrender.com](https://jev-guard-demo.onrender.com) (availability not re-verified).

## Limits and data handling

Answer/question/context text go to TypeSafe. Catch-rate/latency figures are upstream-reported. Error defaults to flag unless configured fail-closed.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 1148239](https://github.com/omkarchougule19/Jev_validation_agent/tree/1148239c77e5203e67080bf5c78d457f3f316d12). AI-assisted README + `jev_guard` layout inspection.

Related: [blacksinisterx JevGuard](blacksinisterx-jev-guard.md), [agent-chaperone](agent-chaperone.md), [clear-head](clear-head.md).
