# Agent-Workflow by Nate G. (durable orchestration engine for coding-agent work with optional TypeSafe Jev decision modes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Headless orchestration for coding-agent runs: delegation, isolated execution, durable messaging, evidence, review, recovery and acceptance that survive restarts. Deterministic code keeps control; an optional TypeSafe provider can supply bounded routing evidence, or run in comparative mode next to deterministic control.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ngallodev-software/agent-workflow) |
| Maintainer | [ngallodev-software](https://github.com/ngallodev-software). Independently curated. |
| Format | Python CLI and library |
| Requirements | Python 3.11+; the `typesafe` extra and `TYPESAFE_API_KEY` only for the `typesafe` or `comparative` decision modes. |
| License | [Apache-2.0](https://github.com/ngallodev-software/agent-workflow/blob/db2919d3bcc34d2be7a6ea6803c10edf2e3257b4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/agent_workflow/semantic/typesafe.py`](https://github.com/ngallodev-software/agent-workflow/blob/db2919d3bcc34d2be7a6ea6803c10edf2e3257b4/src/agent_workflow/semantic/typesafe.py) at the pinned commit. |

## When to use

- Add restart-safe orchestration and evidence to coding-agent work, with Jev as optional bounded routing evidence.
- Mismatch: a quick script; this is a large engine with many concepts.

## How it works

`src/agent_workflow/semantic/typesafe.py` is the TypeSafe semantic provider (default `jev-latest`); `decisions.py` enforces the decision modes, confidence thresholds and receipts, and `comparative` records Jev's candidate against deterministic control without letting it decide. Integration evidence: [`src/agent_workflow/semantic/typesafe.py`](https://github.com/ngallodev-software/agent-workflow/blob/db2919d3bcc34d2be7a6ea6803c10edf2e3257b4/src/agent_workflow/semantic/typesafe.py).

## Get started

Install from a checkout with the TypeSafe extra and set a decision policy in the config (see DECISION_MODES.md).

```sh
git clone https://github.com/ngallodev-software/agent-workflow.git && cd agent-workflow
python -m pip install '.[typesafe]'
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision modes: [github.com/ngallodev-software/agent-workflow/blob/db2919d3bcc34d2be7a6ea6803c10edf2e3257b4/DECISION_MODES.md](https://github.com/ngallodev-software/agent-workflow/blob/db2919d3bcc34d2be7a6ea6803c10edf2e3257b4/DECISION_MODES.md)
- Benchmark evidence: [github.com/ngallodev-software/agent-workflow-benchmark-results](https://github.com/ngallodev-software/agent-workflow-benchmark-results)
- Case study: [ngallodev-software.uk/projects/agent-workflow](https://ngallodev-software.uk/projects/agent-workflow)

## Limits and data handling

Jev is optional; in typesafe or comparative mode, task summaries go to TypeSafe. Version 0.13.0 at review.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit db2919d3bcc3](https://github.com/ngallodev-software/agent-workflow/tree/db2919d3bcc34d2be7a6ea6803c10edf2e3257b4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
