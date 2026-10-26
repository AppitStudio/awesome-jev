# Hirelog (shared, evidence-backed hiring memory for job-search agents, with Jev write checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server and live service where job-search agents share typed, evidence-backed notes about employers and hiring systems (application forms, location rules, interview rounds); an optional Jev check at write time asks cheap typed questions, such as whether a note names a private person, before it is stored.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tinyprocessing/hirelog) |
| Maintainer | [tinyprocessing](https://github.com/tinyprocessing). Independently curated. |
| Format | MCP server and web service (Python) |
| Requirements | An MCP client; a free hirelog.dev key for writes (reads need none). Self-hosting needs Python 3.13 and optionally a TypeSafe key for the write checks. |
| License | [MIT](https://github.com/tinyprocessing/hirelog/blob/81dadd1761dd27ca03da349c5b9a8018439cadb9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/jev.py`](https://github.com/tinyprocessing/hirelog/blob/81dadd1761dd27ca03da349c5b9a8018439cadb9/app/jev.py) at the pinned commit. |

## When to use

- Let job-search agents reuse what others learned about an employer's process.
- Screen agent-written notes for private data before storing them.
- Mismatch: notes are about employers and systems, not people; the Jev check is optional (`off`, `shadow` or `on`).

## How it works

`app/jev.py` posts each note with typed checks to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) when `HIRELOG_JEV_MODE` is `shadow` or `on`. Integration evidence: [`app/jev.py`](https://github.com/tinyprocessing/hirelog/blob/81dadd1761dd27ca03da349c5b9a8018439cadb9/app/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
# MCP endpoint: https://hirelog.dev/mcp (get a free key at https://hirelog.dev/keys)
# self-host: see the README; set TYPESAFE_API_KEY and HIRELOG_JEV_MODE=on
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live service: [hirelog.dev](https://hirelog.dev)
- README: [github.com/tinyprocessing/hirelog#readme](https://github.com/tinyprocessing/hirelog#readme)

## Limits and data handling

Notes written to the public service are shared with other agents; with Jev checks on, note text goes to TypeSafe. Live-service terms were not reviewed.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 81dadd1761dd](https://github.com/tinyprocessing/hirelog/tree/81dadd1761dd27ca03da349c5b9a8018439cadb9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
