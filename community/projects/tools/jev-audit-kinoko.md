# jev-audit by KiNoTch (Japanese CLI and MCP server that uses Jev for a fast first-pass audit of a repository before deeper review)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Windows-first (PowerShell) tool that scans the current directory or a repository and asks Jev to flag concrete suspicious spots, spec and implementation mismatches and regressions, as a wide, shallow screen before LLM review or tests. Supports `--changed-only`, audit profiles, an MCP server and local history. Docs are in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kinoko34077/jev-audit) |
| Maintainer | [KiNoTch.](https://github.com/kinoko34077). Independently curated. |
| Format | Python CLI and MCP server |
| Requirements | Python 3.10+, the `typesafe-sdk` package and a TypeSafe API key; PowerShell setup scripts. |
| License | [MIT](https://github.com/kinoko34077/jev-audit/blob/c5144c83d0059b7d1984e150fae486543aadab2b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_audit/jev_gateway.py`](https://github.com/kinoko34077/jev-audit/blob/c5144c83d0059b7d1984e150fae486543aadab2b/jev_audit/jev_gateway.py) at the pinned commit. |

## When to use

- Narrow down where to look first in a large or unfamiliar repository.
- Mismatch: if you need a complete audit; the README says it is a first screen only.

## How it works

`jev_audit/jev_gateway.py` calls Jev through the official `typesafe-sdk` `TypeSafeClient`, pinned by default to `jev-1.13.0` (override with `TYPESAFE_DEFAULT_MODEL` or `--model`). Integration evidence: [`jev_audit/jev_gateway.py`](https://github.com/kinoko34077/jev-audit/blob/c5144c83d0059b7d1984e150fae486543aadab2b/jev_audit/jev_gateway.py).

## Get started

Run the setup script, then audit a repository.

```sh
.\setup.ps1
cd C:\path\to\repo
jev-audit
jev-audit --changed-only
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage guide: [github.com/kinoko34077/jev-audit/tree/c5144c83d0059b7d1984e150fae486543aadab2b/docs](https://github.com/kinoko34077/jev-audit/tree/c5144c83d0059b7d1984e150fae486543aadab2b/docs)

## Limits and data handling

Source text is sent to TypeSafe (up to 5,000,000 characters per run). File-name exclusion is not full DLP, so secrets written in source can be sent; keep DEBUG logging off for sensitive audits. Japanese-only docs.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit c5144c83d005](https://github.com/kinoko34077/jev-audit/tree/c5144c83d0059b7d1984e150fae486543aadab2b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
