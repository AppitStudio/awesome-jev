# Jev Unpack

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex/Claude Code Stop hook where Jev detects multi-topic, multi-ask agent messages and makes the agent pace them one ask at a time.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lucaminudel/jev-unpack-hook) |
| Maintainer | [lucaminudel](https://github.com/lucaminudel). Independently curated. |
| Format | Agent Stop hook |
| Requirements | Codex or Claude Code; Jev API access. |
| License | [MIT](https://github.com/lucaminudel/jev-unpack-hook/blob/1ddb13922e066abc6972b3b0a8e770786f3e91ac/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Reduce cognitive load from long multi-question agent handovers.
- Mismatch: adds a Jev call per agent message.

## How it works

On each agent message the hook asks Jev whether it bundles several disparate asks; if so the agent is told to present them one at a time with context. (Summarized from the upstream [README](https://github.com/lucaminudel/jev-unpack-hook/blob/1ddb13922e066abc6972b3b0a8e770786f3e91ac/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Follow the install steps in the upstream README.

## Limits and data handling

Agent messages are sent to Jev for classification. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 1ddb13922e06](https://github.com/lucaminudel/jev-unpack-hook/tree/1ddb13922e066abc6972b3b0a8e770786f3e91ac). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
