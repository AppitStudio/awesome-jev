# dotpals

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Desktop pal and notch that shows what coding agents (Claude Code, Codex and others) actually did: test results read from the output, faked passes caught, and Claude Code sent back to fix what it broke. An opt-in double-check sends unclear test runs to TypeSafe Jev (through `@typesafe-ai/sdk`) or to a local Laya model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rikinshah787/dotpals) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [dotpals.vercel.app](https://dotpals.vercel.app) |
| Pricing and access | Free npm package (`npx dotpals@latest setup`). The optional Cloud (Jev) check needs your own TypeSafe API key (billed by TypeSafe); Local Laya and Off need no key. Checked 2026-10-09. |
| Jev evidence | [`bridge/checker.js`](https://github.com/Rikinshah787/dotpals/blob/2ddc2ed4ecc233db04844918413477b3e00c0bc4/bridge/checker.js) implements the Cloud (Jev via `@typesafe-ai/sdk`, `jev-1.13.0`) and local Laya `/v1/systemone` checkers, adapted from claude-referee. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. App not run on the review host. |
| Maintainer | [Rikinshah787](https://github.com/Rikinshah787). Independently curated. |
| Format | Electron desktop window + local bridge + Claude Code plugin (npm) |
| Platform and availability | Desktop (Node 20+; Electron runtime downloaded on first run). |
| Jev's role | Optional: judges test-run output the local parsers mark as unclear; everything else is deterministic parsing. |
| Requirements | Node 20+; optional TypeSafe API key for the Cloud check. |
| License | [MIT](https://github.com/Rikinshah787/dotpals/blob/2ddc2ed4ecc233db04844918413477b3e00c0bc4/LICENSE). |

## When to use

- Keep an eye on several coding-agent sessions and catch edited-to-pass tests.
- Mismatch: Jev only covers the optional unclear-result double-check.

## How it works

A local bridge on `127.0.0.1` reads Claude Code hook events and transcripts and Codex session logs; parsers summarise test results per session. If you choose Cloud (Jev), only the end of an unclear test output is sent after redacting secrets, emails and IPs.

## Get started

From the upstream README (not run on the review host):

```sh
npx dotpals@latest setup
```

## Limits and data handling

Runs locally; nothing leaves the machine unless Cloud (Jev) is enabled, which sends redacted test output to TypeSafe. History is a local JSON file in `~/.dotpals`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 2ddc2ed4ecc2](https://github.com/Rikinshah787/dotpals/tree/2ddc2ed4ecc233db04844918413477b3e00c0bc4). Inspected the upstream README, LICENSE status, and the Jev integration files linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
