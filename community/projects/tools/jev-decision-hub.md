# JEV Decision Hub

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Toolkit around TypeSafe Jev: a zero-dependency Python client with API-key pool rotation, a web dashboard, and example workflows (spam moderation, model routing, trade signals, agent supervision). Mentions third-party free-credit signup via jev-ai.pro.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbonnet65923/jev-decision-hub) |
| Maintainer | [gbonnet65923](https://github.com/gbonnet65923). Independently curated. |
| Format | Python · client + dashboard + examples |
| Requirements | Python 3; TypeSafe API key(s). |
| License | [MIT](https://github.com/gbonnet65923/jev-decision-hub/blob/8aa4b45bd54d543ab3a6b404244e3329483ed2fd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Bootstrap multiple Jev-backed agent examples with shared client plumbing.
- Mismatch: Third-party credit portal is independent of TypeSafe; verify keys yourself.

## How it works

Examples call [`jev_client.py`](https://github.com/gbonnet65923/jev-decision-hub/blob/8aa4b45bd54d543ab3a6b404244e3329483ed2fd/jev_client.py) to post typed questions to TypeSafe and display results in the dashboard.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gbonnet65923/jev-decision-hub.git
cd jev-decision-hub
python jev_client.py  # see README for dashboard
```

## Limits and data handling

Prompts/state go to TypeSafe; billed. Optional third-party signup sites are not verified here. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 8aa4b45bd54d](https://github.com/gbonnet65923/jev-decision-hub/tree/8aa4b45bd54d543ab3a6b404244e3329483ed2fd). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
