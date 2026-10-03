# n8n-nodes-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

n8n community node for TypeSafe Jev: classify, route, and score workflow text (distinct from khmuhtadin and @typesafe-ai packages).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vibe-with-me-tools/n8n-nodes-jev) |
| Maintainer | [vibe-with-me-tools](https://github.com/vibe-with-me-tools). Independently curated. |
| Format | n8n community node package for TypeSafe Jev classify/route/score. |
| Requirements | Self-hosted n8n; TypeSafe credentials per upstream. |
| License | [MIT](https://github.com/vibe-with-me-tools/n8n-nodes-jev/blob/ddbfe850d5d15731aaf42b395960b12805c64942/LICENSE.md). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Distinct from khmuhtadin/n8n-nodes-jev-classification and typesafe-ai/n8n-nodes-typesafe-ai. |

## When to use

Use in self-hosted n8n when you want Jev judgments mid-workflow. Distinct from n8n-nodes-jev-classification and official n8n-nodes-typesafe-ai.

## How it works

Community node calls TypeSafe Jev for typed judgments and exposes routing outputs including low-confidence paths.

## Get started

```sh
git clone https://github.com/vibe-with-me-tools/n8n-nodes-jev.git
cd n8n-nodes-jev
git checkout ddbfe850d5d15731aaf42b395960b12805c64942
# npm install n8n-nodes-jev into n8n custom extensions — see upstream
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit ddbfe85](https://github.com/vibe-with-me-tools/n8n-nodes-jev/tree/ddbfe850d5d15731aaf42b395960b12805c64942). AI-assisted README and license inspection; install/live paths not executed.
