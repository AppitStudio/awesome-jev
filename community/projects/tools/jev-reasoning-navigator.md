# JEV Reasoning Navigator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python middleware/runtime for autonomous LLM agents that separates TypeSafe Jev semantic judgment from operational PolicyEngine decisions, capability receipts, and sandboxed tool execution (loop prevention / anti-hallucination framing).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AndreuVM/jev-reasoning-navigator) |
| Maintainer | [AndreuVM](https://github.com/AndreuVM). Independently curated. |
| Format | Python package (`jev_navigator`) with demo and tests. |
| Requirements | Python 3.11+; TypeSafe/System One access for live judgment paths. |
| License | No LICENSE file at the reviewed tip—reuse terms unspecified. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. README primarily Spanish. No LICENSE at tip. Live agent loops not run. |

## When to use

Use when you need **formal separation** of semantic probability vs hard policy vs physical tool execution. Prefer lighter hook guards ([muratcakmak jev-guard](muratcakmak-jev-guard.md), [agent-chaperone](agent-chaperone.md)) for Claude Code-only firewalls.

## How it works

Jev scores semantic success probability; PolicyEngine emits ALLOW/BLOCK/REPLAN/ABSTAIN; SecureExecutor requires a fresh DecisionReceipt matching action/state hashes before sandboxed tools run.

## Get started

```sh
git clone https://github.com/AndreuVM/jev-reasoning-navigator.git
cd jev-reasoning-navigator
git checkout db378acd5c6bd5bd7f92267fcbdff8f00c5a069f
# install per pyproject.toml; see demo.py and tests/
```

## Examples and demos

- Upstream badge claims 130 tests (not re-run here).
- `demo.py` and `data/` fixtures.

## Limits and data handling

No LICENSE at tip. Tool commands still carry OS risk if policy misconfigured. Spanish-primary docs.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit db378ac](https://github.com/AndreuVM/jev-reasoning-navigator/tree/db378acd5c6bd5bd7f92267fcbdff8f00c5a069f). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [agent-chaperone](agent-chaperone.md), [muratcakmak-jev-guard](muratcakmak-jev-guard.md).
