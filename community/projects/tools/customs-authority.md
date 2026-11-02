# Customs Authority (Claude Code toolkit that finds where Jev fits in your app and ships a confidence-gated hybrid)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that walks a project's decision points, triages each one as code, Jev or LLM, helps write typed questions, proves them against an answer key, and drops in a gated hybrid router that sends low-confidence items to a person or a larger model. Includes a dependency-light Python Jev client and TypeScript templates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Robot-Friends-Community/customs-authority) |
| Maintainer | [Robot-Friends-Community](https://github.com/Robot-Friends-Community). Independently curated. |
| Format | Claude Code plugin (skills, Python scripts, templates) |
| Requirements | Claude Code; Python with httpx; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Robot-Friends-Community/customs-authority/blob/9c5cfeffb0f8154c2a5fec66464f1b6d4565d3a2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev_client.py`](https://github.com/Robot-Friends-Community/customs-authority/blob/9c5cfeffb0f8154c2a5fec66464f1b6d4565d3a2/scripts/jev_client.py) at the pinned commit. |

## When to use

- Find the classification, routing and scoring steps in an app that Jev could take over.
- Mismatch: opinionated workflow; you still need your own answer key.

## How it works

`scripts/jev_client.py` calls TypeSafe System One with a pinned model (default `jev-1.13.0`), logs usage and cost, and retries; `scripts/jev_eval.py` scores questions against an answer key and `templates/hybrid_router.py` gates on confidence. Integration evidence: [`scripts/jev_client.py`](https://github.com/Robot-Friends-Community/customs-authority/blob/9c5cfeffb0f8154c2a5fec66464f1b6d4565d3a2/scripts/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add Robot-Friends-Community/customs-authority
claude plugin install customs-authority@customs-authority
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Commands: /customs, /jev-fit and more, listed in the README

## Limits and data handling

Your examples and inputs are sent to TypeSafe when you run evaluations. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 9c5cfeffb0f8](https://github.com/Robot-Friends-Community/customs-authority/tree/9c5cfeffb0f8154c2a5fec66464f1b6d4565d3a2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
