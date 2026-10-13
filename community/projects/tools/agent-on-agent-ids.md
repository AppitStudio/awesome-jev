# agent-on-agent-ids

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Intrusion detection for tool-using AI agents: a portable judge spec reads your observability traces (Comet Opik today) and flags prompt injection and resulting actions; TypeSafe Jev is one supported cheap judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stanibaj/agent-on-agent-ids) |
| Maintainer | [stanibaj](https://github.com/stanibaj). Independently curated. |
| Format | Python runner + judge YAML spec |
| Requirements | Python; Comet Opik; TypeSafe or Anthropic key. |
| License | [Apache-2.0](https://github.com/stanibaj/agent-on-agent-ids/blob/0f55ef8c2dcc8f4add35acf11300e7d59ceaffa4/LICENSE) |
| Jev evidence | [`judge/aoa-ids.judge.yaml`](https://github.com/stanibaj/agent-on-agent-ids/blob/0f55ef8c2dcc8f4add35acf11300e7d59ceaffa4/judge/aoa-ids.judge.yaml) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Alert when an agent acts on an injected instruction found in logs, pages or tickets.
- Mismatch: Opik is the only native integration today; detection figures are on bundled traces.

## How it works

The judge reads trace spans, asks the configured model whether tool calls follow injected instructions, and raises alerts. (Summarized from the upstream [README](https://github.com/stanibaj/agent-on-agent-ids/blob/0f55ef8c2dcc8f4add35acf11300e7d59ceaffa4/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): run the one-command Opik installer and configure a judge model per the README.

## Limits and data handling

Trace contents go to the judge provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 0f55ef8c2dcc](https://github.com/stanibaj/agent-on-agent-ids/tree/0f55ef8c2dcc8f4add35acf11300e7d59ceaffa4). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
