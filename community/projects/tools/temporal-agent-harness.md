# Temporal Agent Harness

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Temporal-native durable multi-agent harness whose optional `jev` extra provides `agent.jev_evaluator`, a Jev-backed auto mode for tool approvals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/temporal-community/temporal-agent-harness) |
| Maintainer | [temporal-community](https://github.com/temporal-community). Independently curated. |
| Format | Python framework for durable agents on Temporal; Jev is an optional worker extra |
| Requirements | Python with `uv`, a Temporal server, and the `jev` extra on workers (pulls in `typesafe-sdk`); `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/temporal-community/temporal-agent-harness/blob/049e01c9d726ef68bff7be857c735723b9801512/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let durable agents auto-approve low-risk tool calls while routing irreversible or uncertain ones to a human.
- Audit every evaluator decision on the workflow event stream.
- Mismatch: harness features work without Jev; the extra is only needed for Jev auto mode.

## How it works

The worker-side evaluator asks Jev a typed question about the pending tool call. Upstream states it cannot fail open: low confidence, an irreversible effect, an exception, or a TypeSafe outage escalates instead of approving.

## Get started

Install the package with the Jev extra on the worker (see upstream README for server setup):

```sh
uv add 'temporal-agent-harness[jev]==0.6.0'
# in your agent config: auto_mode_evaluator=agent.jev_evaluator()
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README examples (tic-tac-toe workflow, UI packages) and the auto-mode section.

## Limits and data handling

Tool-call context is sent to TypeSafe on each evaluation and billed. Jev's answer gates approvals; keep permissions enforced in code.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 049e01c9d726](https://github.com/temporal-community/temporal-agent-harness/tree/049e01c9d726ef68bff7be857c735723b9801512). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
