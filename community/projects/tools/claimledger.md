# ClaimLedger (dependency-free memory layer where Jev answers frozen typed questions about which stored decisions still govern a task, with a sealed audit log)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python memory layer for coding agents. An agent writes decisions into an append-only, hash-chained record store; for each task a deterministic selector picks at most six records, Jev answers a frozen set of typed questions about them (is each record admitted, which pairs conflict, which governs), and a deterministic policy turns the probabilities into actions such as promote or hold for review. Every judgment is written to a sealed log that can be audited and calibrated against human outcomes. It ships a CLI, a local console and an MCP server. The README says it is an engineering artifact: the original research framing was withdrawn after prior work was found.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Anhao1314/ClaimLedger) |
| Maintainer | [Anhao1314](https://github.com/Anhao1314). Independently curated. |
| Format | Python package and CLI with a local web console and MCP server (no third-party dependencies) |
| Requirements | Python and a `TYPESAFE_API_KEY` for the Jev judgments (Jev is optional for the store, selection and audit commands). |
| License | [MIT](https://github.com/Anhao1314/ClaimLedger/blob/69a4bcac9f0feffa523e27caf5dbc4b0fa13bfca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`chat_distiller/jev.py`](https://github.com/Anhao1314/ClaimLedger/blob/69a4bcac9f0feffa523e27caf5dbc4b0fa13bfca/chat_distiller/jev.py) at the pinned commit. |

## When to use

- Keep a coding agent from acting on superseded constraints, with every admit or conflict decision logged and checkable.
- Mismatch: each judgment is a 1 to 5 second model call, and the README reports small evaluation sets rather than production use.

## How it works

`chat_distiller/jev.py` is an optional zero-dependency client for `https://api.typesafe.ai/v1/systemone` (`jev-latest` default, disabled unless `TYPESAFE_API_KEY` is set); the `jev_first` package sends per-record `admit`, pairwise `relation` and `governing` questions, and deterministic policy code, not the model, decides the action. Integration evidence: [`chat_distiller/jev.py`](https://github.com/Anhao1314/ClaimLedger/blob/69a4bcac9f0feffa523e27caf5dbc4b0fa13bfca/chat_distiller/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m pip install .
python -m jev_first record --store records.jsonl --text "All storage must use PostgreSQL." --source agent
python -m jev_first decide --store records.jsonl --task "Write a storage adapter for analytics"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the architecture, evaluation tables and console screenshots: [github.com/Anhao1314/ClaimLedger#readme](https://github.com/Anhao1314/ClaimLedger#readme)
- Why Jev sits at the center: [github.com/Anhao1314/ClaimLedger/blob/69a4bcac9f0feffa523e27caf5dbc4b0fa13bfca/docs/JEV-FIRST.md](https://github.com/Anhao1314/ClaimLedger/blob/69a4bcac9f0feffa523e27caf5dbc4b0fa13bfca/docs/JEV-FIRST.md)

## Limits and data handling

Record text for the selected candidates and the task go to TypeSafe on your key. The README labels the project an engineering artifact, and its evaluation results (for example label agreement between Jev and another model on frozen pairs) were not independently reproduced here. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 69a4bcac9f0f](https://github.com/Anhao1314/ClaimLedger/tree/69a4bcac9f0feffa523e27caf5dbc4b0fa13bfca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
