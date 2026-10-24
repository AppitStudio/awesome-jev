# AGIW MCP (careful coding workflow on local models, with consent-gated Jev checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local MCP server for Claude Code, Factory or OpenCode: a readiness check, a Nisi workflow where one local model drafts, tests run and a second reviews, and optional advisory Jev questions before and after a task (risk, missing detail, unbacked claims) that send nothing until you consent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/louiscalata/agiw-mcp) |
| Maintainer | [louiscalata](https://github.com/louiscalata). Independently curated. |
| Format | MCP server (Python standard library, Node.js for Nisi) |
| Requirements | Python 3.10+, Node.js 22+, an OpenAI-compatible local model server with two models; a TypeSafe key for the optional Jev checks. |
| License | [Apache-2.0](https://github.com/louiscalata/agiw-mcp/blob/bf211140dc71da26c281ae1cfb70931616c432a9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/agiw_mcp/jev.py`](https://github.com/louiscalata/agiw-mcp/blob/bf211140dc71da26c281ae1cfb70931616c432a9/src/agiw_mcp/jev.py) at the pinned commit. |

## When to use

- Run a draft-test-review loop on your own local models from an MCP assistant.
- Ask Jev for a quick risk check on a task only when you choose to.
- Mismatch: Jev checks are advisory and need explicit consent each time.

## How it works

`src/agiw_mcp/consent.py` gates calls to `https://api.typesafe.ai/v1/systemone`; `jev.py` sends the questions with `jev-1.14.0` by default and checks the served model version. Integration evidence: [`src/agiw_mcp/jev.py`](https://github.com/louiscalata/agiw-mcp/blob/bf211140dc71da26c281ae1cfb70931616c432a9/src/agiw_mcp/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pipx install git+https://github.com/louiscalata/agiw-mcp
# then save config.json with your local author and reviewer models (see README)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/louiscalata/agiw-mcp#readme](https://github.com/louiscalata/agiw-mcp#readme)

## Limits and data handling

Code stays on your local models; with consent, the task summary goes to TypeSafe. No telemetry per the README.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit bf211140dc71](https://github.com/louiscalata/agiw-mcp/tree/bf211140dc71da26c281ae1cfb70931616c432a9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
