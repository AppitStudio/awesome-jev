# vibecheck-linear-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Work ledger for Claude Code, Codex, Muse, and Antigravity agents backed by Linear issues, with MCP tools for plan/claim/report and a Jev-compatible judgment adapter that checks agent reports against acceptance criteria.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mgd34msu/vibecheck-linear-jev) |
| Maintainer | [mgd34msu](https://github.com/mgd34msu). Independently curated. |
| Format | JavaScript/Bun · MCP server + agent skills |
| Requirements | Bun; Linear API; Jev-compatible endpoint/credentials per adapter README. |
| License | [MIT](https://github.com/mgd34msu/vibecheck-linear-jev/blob/a7988b19c88fadf7d2c975ddeea5d592bb6653c4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Keep multi-agent coding work auditable in Linear with an automated judgment pass.
- Mismatch: Judgment adapter is Jev-style—confirm TypeSafe wiring in your deploy.

## How it works

Agents mutate Linear via MCP; the jev-style adapter scores reports against issue goals. Evidence: [`adapters/jev-style/server.py`](https://github.com/mgd34msu/vibecheck-linear-jev/blob/a7988b19c88fadf7d2c975ddeea5d592bb6653c4/adapters/jev-style/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/mgd34msu/vibecheck-linear-jev.git
# Bun install + platform skill paths per README
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit a7988b19c88f](https://github.com/mgd34msu/vibecheck-linear-jev/tree/a7988b19c88fadf7d2c975ddeea5d592bb6653c4). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
