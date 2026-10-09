# jev-triage (OpenClaw)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenClaw plugin that puts TypeSafe Jev in front of the agent's main model: each incoming message is classified thanks/spam/question/incident plus urgent yes/no, so thanks and spam end without waking the main model and other messages arrive with Jev's triage prepended; every decision is logged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CodeCave0000/jev-triage) |
| Maintainer | [CodeCave0000](https://github.com/CodeCave0000). Independently curated. |
| Format | OpenClaw plugin (`before_dispatch` hook) |
| Requirements | OpenClaw 2026.9.6+; official TypeSafe plugin; TypeSafe API key. |
| License | [MIT](https://github.com/CodeCave0000/jev-triage/blob/6360e217e61d469fd4cb4798c1d81dc6b722534f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Cut main-model calls on chatty agent channels.
- Mismatch: fixed 0.9 threshold and labels; adapt for other channels.

## How it works

See the upstream [README](https://github.com/CodeCave0000/jev-triage/blob/6360e217e61d469fd4cb4798c1d81dc6b722534f/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/CodeCave0000/jev-triage.git   # then install per README
```

## Limits and data handling

Incoming message text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 6360e217e61d](https://github.com/CodeCave0000/jev-triage/tree/6360e217e61d469fd4cb4798c1d81dc6b722534f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
