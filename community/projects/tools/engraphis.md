# Engraphis

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first, inspectable memory for coding agents (MCP, code-aware recall, WebUI) with optional advisory Jev decisions via BYOK or managed hosted plans.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Coding-Dev-Tools/engraphis) |
| Product homepage | [engraphis.com](https://engraphis.com/) |
| Maintainer | [Coding-Dev-Tools](https://github.com/Coding-Dev-Tools). Independently curated. |
| Format | Python package, MCP server, and self-hosted dashboard; commercial hosted plans exist |
| Requirements | Python; `pip install "engraphis[all]"` (or `[mcp]`). BYOK decisions need `TYPESAFE_API_KEY` and explicit `byok` selection; managed decisions use a paid Cloud session. |
| License | [Apache-2.0](https://github.com/Coding-Dev-Tools/engraphis/blob/cbfd7209565d44cbc86e2188f9973ccf48d66c6d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Open-source core with paid Pro/hosted plans (trial offered upstream). Check current pricing on the vendor site. |

## When to use

- Give coding agents persistent, inspectable memory with code-aware recall over MCP.
- Add advisory Jev judgments to memory workflows with your own key, or use the vendor's managed allowance.
- Mismatch: default backend is `none`/local; Jev is not required.

## How it works

Engraphis stores memory locally; when a decision backend is enabled, advisory decisions call Jev (`jev-1.13.0` only) directly with BYOK or through the managed Cloud session. Upstream documents consent details in [HOSTED_PLANS.md](https://github.com/Coding-Dev-Tools/engraphis/blob/main/docs/HOSTED_PLANS.md).

## Get started

Install and start the self-hosted dashboard:

```sh
pip install "engraphis[all]"
engraphis-dashboard
# optional BYOK decisions: ENGRAPHIS_DECISION_BACKEND + TYPESAFE_API_KEY (see README)
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README configuration tables and hosted-plan documentation.

## Limits and data handling

Advisory decisions send memory text to TypeSafe (BYOK) or the vendor Cloud (managed). Pro/hosted plans are paid; this listing does not endorse a plan.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit cbfd7209565d](https://github.com/Coding-Dev-Tools/engraphis/tree/cbfd7209565d44cbc86e2188f9973ccf48d66c6d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
