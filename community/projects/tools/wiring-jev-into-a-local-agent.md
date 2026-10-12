# Wiring Jev into a local agent

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Educational companion code for Old Nain episode 001: a small local email agent where Jev, not the drafting model, makes the judgment calls (label, needs a reply, friend/relative flag) before any draft is written.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ghosthat-studio/wiring-jev-into-a-local-agent) |
| Maintainer | [ghosthat-studio](https://github.com/ghosthat-studio). Independently curated. |
| Format | Python teaching example (uv) |
| Requirements | uv (Python 3.12+); a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/ghosthat-studio/wiring-jev-into-a-local-agent/blob/38844567653d8dc295597c15298b8b66f6afaf7b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Learn the pattern of separating judgment (Jev) from generation in an agent loop.
- Run against a synthetic inbox before wiring real mail.
- Mismatch: Educational only; mail and drafting model are placeholders you implement.

## How it works

The loop checks local state first, then one Jev request returns the label, a needs-reply probability and a personal-contact flag; drafting runs only if the gate passes. Jev integration: [`src/inbox_agent/gate.py`](https://github.com/ghosthat-studio/wiring-jev-into-a-local-agent/blob/38844567653d8dc295597c15298b8b66f6afaf7b/src/inbox_agent/gate.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ghosthat-studio/wiring-jev-into-a-local-agent
cd wiring-jev-into-a-local-agent
export TYPESAFE_API_KEY=...
uv run python -m inbox_agent --fresh --runs 3
```

## Limits and data handling

Synthetic inbox by default; message text goes to TypeSafe on live runs. Not hardened for production (per maintainer). Not run on the review host. Video: [Old Nain episode 001](https://www.youtube.com/watch?v=cm_4AmKAtmo).

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 38844567653d](https://github.com/ghosthat-studio/wiring-jev-into-a-local-agent/tree/38844567653d8dc295597c15298b8b66f6afaf7b). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
