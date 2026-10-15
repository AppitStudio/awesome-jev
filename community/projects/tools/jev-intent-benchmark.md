# jev-intent-benchmark

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Research check for indirect prompt injection at the moment an agent acts: asks Jev whether the act carries out something a tool result asked for but the user did not, with a benchmark script on InjecAgent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/minitru/jev-intent-benchmark) |
| Maintainer | [minitru](https://github.com/minitru). Independently curated. |
| Format | Node.js library/CLI and benchmark scripts |
| Requirements | Node.js; TypeSafe API key for live checks (tests use a fake classifier). |
| License | [MIT](https://github.com/minitru/jev-intent-benchmark/blob/260bb616e8816edca94150c6fcb340d6c83c1603/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`actcheck.js`](https://github.com/minitru/jev-intent-benchmark/blob/260bb616e8816edca94150c6fcb340d6c83c1603/actcheck.js) at the pinned commit. |

## When to use

- Add an act-time injection check in a tool-boundary hook for coding or browsing agents.
- Reproduce the author's InjecAgent benchmark with your own key.
- Mismatch: research code from the xChk project, not a product or guarantee.

## How it works

The check reads the session's request, the previous tool answer and the pending act, then asks Jev two typed questions (carries / off-intent) and flags when both agree, returning both probabilities either way. Integration evidence: [`actcheck.js`](https://github.com/minitru/jev-intent-benchmark/blob/260bb616e8816edca94150c6fcb340d6c83c1603/actcheck.js).

## Get started

From the upstream README (not run on the review host):

```sh
node cli.js examples/cases.json
npm test   # fake classifier; no key needed
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark: `bench/injecagent.js` against the public InjecAgent set.

## Limits and data handling

Request, tool answer and act text are sent to TypeSafe for each check, billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 260bb616e881](https://github.com/minitru/jev-intent-benchmark/tree/260bb616e8816edca94150c6fcb340d6c83c1603). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
