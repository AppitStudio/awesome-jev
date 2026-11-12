# Snooper (MCP safety gate and flight recorder for agent purchases on PayPal, judged by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Remote MCP server between an AI agent and PayPal: the agent calls `propose_purchase`, code checks amounts, payees, caps and duplicates, Jev answers five semantic questions (cart match, injected payment changes, injection likelihood, reviewer routing, shareable fields), and every step goes to a tamper-evident trail before the purchase is cleared, sent to review or blocked.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mikeyliow/snooper) |
| Maintainer | [mikeyliow](https://github.com/mikeyliow). Independently curated. |
| Format | MCP server (TypeScript, MIT); PayPal AI Hackathon 2026 project |
| Requirements | Node.js, a PayPal sandbox app, `TYPESAFE_API_KEY`, and an MCP client. |
| License | [MIT](https://github.com/mikeyliow/snooper/blob/12499b702b69c48b67375cdfdefb2dc191bcd993/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/mikeyliow/snooper/blob/12499b702b69c48b67375cdfdefb2dc191bcd993/src/jev.ts) at the pinned commit. |

## When to use

- Let an agent propose purchases without holding PayPal credentials.
- Catch prompt injection that tries to change who gets paid.
- Mismatch: built against the PayPal sandbox for a hackathon.

## How it works

`src/jev.ts` uses `@typesafe-ai/sdk` to send one `systemOne` request per proposal with Noul, Score and Choice questions; thresholds in `src/config.ts` follow TypeSafe's guardrails cookbook, and Jev errors or timeouts fail closed. Integration evidence: [`src/jev.ts`](https://github.com/mikeyliow/snooper/blob/12499b702b69c48b67375cdfdefb2dc191bcd993/src/jev.ts).

## Get started

Install, build and start the server locally, then point an MCP client at it; `npm run jev:check` sends eight sample proposals to Jev.

```sh
npm ci
npm run build
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo (UI needs an admin token): [snooper-production-c0acfe19.up.railway.app](https://snooper-production-c0acfe19.up.railway.app)

## Limits and data handling

Proposal details and untrusted text are sent to TypeSafe on your key; the audit trail is stored locally as hash-chained JSONL.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 12499b702b69](https://github.com/mikeyliow/snooper/tree/12499b702b69c48b67375cdfdefb2dc191bcd993). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
