# fin (agent-first double-entry finance ledger where Jev proposes matches and categories)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Gives your AI agent a trustworthy place to manage your money: a double-entry ledger with an agent-first CLI and a web view a human can check at a glance. Code classifies what it can first (learned UPI IDs, transfers, card patterns, who owes whom); Jev handles the remaining closed-set judgments such as 'same payment?' and categories, and only proposes; it never writes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tanushmahalka/fin) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/tanushmahalka/fin#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you pay any Cloudflare and TypeSafe usage. Checked 2026-10-31. |
| Jev evidence | [`worker/jev.ts`](https://github.com/tanushmahalka/fin/blob/4f02fbf7f7cf0e32859bff91021a349fe865988f/worker/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tanushmahalka](https://github.com/tanushmahalka). Independently curated. |
| Format | Web app on Cloudflare Workers (D1) + `fin` CLI |
| Platform and availability | Self-hosted web app (Cloudflare Workers) plus CLI; no hosted instance verified. |
| Jev's role | Proposes payment matches and categories for lines code rules could not classify. |
| Requirements | Node.js and Wrangler; `TYPESAFE_API_KEY` in `.dev.vars` to turn Jev on (everything else works without it). |
| License | [MIT](https://github.com/tanushmahalka/fin/blob/4f02fbf7f7cf0e32859bff91021a349fe865988f/LICENSE) |

## When to use

- Let an agent reconcile statements and receipts while a human reviews the ledger.
- Mismatch: Jev only proposes; numbers, dates and policy stay in code.

## How it works

`worker/jev.ts` uses `@typesafe-ai/sdk` with `jev-latest` to judge candidate pairs and uncategorized lines in small batches after the code rules have run; results stay proposals until accepted. Integration evidence: [`worker/jev.ts`](https://github.com/tanushmahalka/fin/blob/4f02fbf7f7cf0e32859bff91021a349fe865988f/worker/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run db:reset && npm run dev   # http://localhost:5180
npm run build:cli && npm link     # installs `fin`
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README section 'Jev (TypeSafe) — where it helps': [github.com/tanushmahalka/fin#readme](https://github.com/tanushmahalka/fin#readme)

## Limits and data handling

Transaction descriptions sent for judgment go to TypeSafe. Handle bank data carefully. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 4f02fbf7f7cf](https://github.com/tanushmahalka/fin/tree/4f02fbf7f7cf0e32859bff91021a349fe865988f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
