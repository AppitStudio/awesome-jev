# Blueprint Support Ticket Triage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Trida AI open blueprint for a support ticket triage agent: calibrated typed decisions behind a port (TypeSafe Jev, LLM, or offline), with routing/priority computed in code and a human gate before action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tridaai/blueprint-support-ticket-triage) |
| Maintainer | [tridaai](https://github.com/tridaai). Independently curated. |
| Format | Python · agent blueprint |
| Requirements | Python 3; TypeSafe key when using the Jev backend. |
| License | [Apache-2.0](https://github.com/tridaai/blueprint-support-ticket-triage/blob/acc5e34df3746bf45a14e176b039e3fcf04529e5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Start a human-gated support triage agent with swappable System One backends.
- Mismatch: Blueprint—wire your ticket source and policies.

## How it works

Decision port answers typed questions; application code maps answers to routing/priority and stops for human approval. Evidence: [`src/support_triage/decisions.py`](https://github.com/tridaai/blueprint-support-ticket-triage/blob/acc5e34df3746bf45a14e176b039e3fcf04529e5/src/support_triage/decisions.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tridaai/blueprint-support-ticket-triage.git
cd blueprint-support-ticket-triage
# install per README
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit acc5e34df374](https://github.com/tridaai/blueprint-support-ticket-triage/tree/acc5e34df3746bf45a14e176b039e3fcf04529e5). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
