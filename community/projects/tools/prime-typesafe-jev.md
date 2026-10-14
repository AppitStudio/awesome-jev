# prime-typesafe-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Host bridge for Prime Agent that adds Jev decisions behind a Unix-socket credential boundary, deterministic hard blocks, egress redaction and daily budget caps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/japorto100/prime-typesafe-jev) |
| Maintainer | [japorto100](https://github.com/japorto100). Independently curated. |
| Format | Prime Agent extension (TypeScript) + Python skill |
| Requirements | Prime Agent v0.9.8+, Linux/macOS, TypeSafe API key or a local System One server. |
| License | [MIT](https://github.com/japorto100/prime-typesafe-jev/blob/0a0b1a5e59bc32ed0639004e1b2c8dc02dc453d6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extension/hooks/tool-gate.ts`](https://github.com/japorto100/prime-typesafe-jev/blob/0a0b1a5e59bc32ed0639004e1b2c8dc02dc453d6/extension/hooks/tool-gate.ts) at the pinned commit. |

## When to use

- Add an advisory Jev tool-gate to Prime Agent without exposing the API key to Python skills.
- Mismatch: v0.1.0; probabilistic decisions only apply in an advisory grey zone.

## How it works

Code enforces hard blocks for destructive actions; Jev judges only grey-zone cases. Modes go from `off` (default) to explicit approval, shadow and on. Receipts are content-free. Integration evidence: [`extension/hooks/tool-gate.ts`](https://github.com/japorto100/prime-typesafe-jev/blob/0a0b1a5e59bc32ed0639004e1b2c8dc02dc453d6/extension/hooks/tool-gate.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
# see README: enable mode via PRIME_JEV_* environment variables
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture: `docs/ARCHITECTURE.md`.
- Tests: `extension/tests/`, `skill/tests/`.

## Limits and data handling

Redacted context goes to TypeSafe or your local server; budget kill-switch documented upstream.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 0a0b1a5e59bc](https://github.com/japorto100/prime-typesafe-jev/tree/0a0b1a5e59bc32ed0639004e1b2c8dc02dc453d6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
