# Founder CRM

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Local SQLite CRM for an early startup's first customers, conversations and promises, with a dashboard, Claude over MCP to propose updates, and optional Jev checks on whether the evidence supports each proposed change before you approve it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shlok97/founder-crm) |
| Maintainer | [shlok97](https://github.com/shlok97). Independently curated. |
| Format | Python app (SQLite dashboard + MCP) |
| Requirements | Python 3.11+; optional TypeSafe or OpenRouter key for Jev checks. |
| License | [MIT](https://github.com/shlok97/founder-crm/blob/5e9e796a2cb4ede4d98b9004771a06d06c409a17/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`founder_crm/judge.py`](https://github.com/shlok97/founder-crm/blob/5e9e796a2cb4ede4d98b9004771a06d06c409a17/founder_crm/judge.py) at the pinned commit. |

## When to use

- Track early customer relationships locally and let Claude help keep them current.
- Want a second check before AI-proposed CRM edits are saved.
- Mismatch: starting point to clone and customize, not a hosted CRM.

## How it works

Claude proposes updates over MCP from source evidence; proposals freeze their context and wait for review. `founder_crm/judge.py` asks Jev (TypeSafe `/v1/systemone` with `jev-latest`, or OpenRouter) for a supported, unsupported or insufficient judgment. Jev only advises and never applies changes. Integration evidence: [`founder_crm/judge.py`](https://github.com/shlok97/founder-crm/blob/5e9e796a2cb4ede4d98b9004771a06d06c409a17/founder_crm/judge.py).

## Get started

From the upstream README: clone and run the launcher for a demo workspace, or `--empty` for your own.

```sh
git clone https://github.com/shlok97/founder-crm.git && cd founder-crm
python3 scripts/start.py   # http://127.0.0.1:4780
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/architecture.md
- Demo workspace with fictional data

## Limits and data handling

Proposal evidence goes to the Jev provider when checks are on; model sharing defaults off. Built by Altys.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 5e9e796a2cb4](https://github.com/shlok97/founder-crm/tree/5e9e796a2cb4ede4d98b9004771a06d06c409a17). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
