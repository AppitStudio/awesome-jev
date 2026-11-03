# pm-decisions (Claude Code plugin that gives Claude nine product-manager decisions as Jev-backed tools, with local redaction)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin and local MCP server that hands Claude nine bounded product-management calls as tools: feedback triage, duplicate finding, story readiness, risk flags for review, priority scoring, standup status, meeting-note labels, release-note classification and a sensitive-content check. Jev answers each as typed questions with confidence, Claude writes the human-facing text, and anything uncertain goes back to you. An offline mock mode is available.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/geektuhin123/pm-decisions) |
| Maintainer | [geektuhin123](https://github.com/geektuhin123). Independently curated. |
| Format | Claude Code plugin with a local stdio MCP server (Python) |
| Requirements | Claude Code and Python 3.10+ as `python3`; a TypeSafe API key for live Jev. |
| License | [MIT](https://github.com/geektuhin123/pm-decisions/blob/0a9039aa7d1a61ab4e5bdfe4b4940ef8a7ec6750/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/pm_jev/backends.py`](https://github.com/geektuhin123/pm-decisions/blob/0a9039aa7d1a61ab4e5bdfe4b4940ef8a7ec6750/src/pm_jev/backends.py) at the pinned commit. |

## When to use

- Let Claude make the quick yes/no and category calls in a PM workflow without writing prose for them.
- Mismatch: Jev works best in English and is weak at arithmetic and comparing dates, so keep those in code.

## How it works

`src/pm_jev/backends.py` wraps `TypeSafeClient.system_one` from the official SDK (`jev-latest` unless `PM_JEV_MODEL` is set) and returns plain dicts to the MCP tools; each decision is split into narrow questions with a none-or-other option where it matters. Integration evidence: [`src/pm_jev/backends.py`](https://github.com/geektuhin123/pm-decisions/blob/0a9039aa7d1a61ab4e5bdfe4b4940ef8a7ec6750/src/pm_jev/backends.py).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add geektuhin123/pm-decisions
/plugin install pm-decisions@pm-decisions
# Claude Code then asks for your TypeSafe API key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the nine decisions, data handling and known limits: [github.com/geektuhin123/pm-decisions#readme](https://github.com/geektuhin123/pm-decisions#readme)

## Limits and data handling

Text you pass to a tool goes to TypeSafe after local redaction of emails, phone numbers, keys, tokens and similar patterns; review TypeSafe's terms before using customer data. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 0a9039aa7d1a](https://github.com/geektuhin123/pm-decisions/tree/0a9039aa7d1a61ab4e5bdfe4b4940ef8a7ec6750). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
