# action-scheduler-triage by Hamza Ahmad Aslam (CLI that groups WooCommerce Action Scheduler failures and asks Jev which are safe to retry unchanged)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reads failed Action Scheduler actions exported with WP-CLI, groups them by hook and masked error in code, and asks Jev the cause, whether running them again unchanged is safe (no repeated payment, refund or email) and how urgent they are. Groups land in safe to retry, fix first or review, with WP-CLI commands for you to run by hand.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/action-scheduler-triage) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (not needed for `--dry-run`). |
| License | [MIT](https://github.com/hamzaahmadaslam/action-scheduler-triage/blob/e6f6391a2033b7bca4a60e28254fd622324a8dca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/action-scheduler-triage/blob/e6f6391a2033b7bca4a60e28254fd622324a8dca/src/jev.mjs) at the pinned commit. |

## When to use

- WooCommerce or WordPress site owners facing a pile of failed background actions.
- Mismatch: automatic retries; the tool is read-only and never runs WP-CLI or touches the database.

## How it works

`src/jev.mjs` posts batches to `https://api.typesafe.ai/v1/systemone` with typed `choice`, `noul` and `score` questions, and code applies one `--threshold` (default 0.8) to place each item or send it to review. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/action-scheduler-triage/blob/e6f6391a2033b7bca4a60e28254fd622324a8dca/src/jev.mjs).

## Get started

Export the failed actions with WP-CLI (Action Scheduler 3.9.1+), then run the triage on the JSON file.

```sh
npm install -g @hamzaahmadaslam/action-scheduler-triage
wp action-scheduler action list --status=failed --per_page=1000 --fields=id,hook,status,group,recurring,scheduled_date,args,log_entries --format=json > failed-actions.json
export TYPESAFE_API_KEY=...
action-scheduler-triage failed-actions.json --dry-run
action-scheduler-triage failed-actions.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Worked example in the README: [github.com/hamzaahmadaslam/action-scheduler-triage#example](https://github.com/hamzaahmadaslam/action-scheduler-triage#example)

## Limits and data handling

Grouped error text goes to TypeSafe after ids, amounts, dates and emails are masked; names in free text are sent as written, so check `--dry-run`. It sees only the export, not whether a remote service is back. English log lines work best; about 50 groups fit in one request.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit e6f6391a2033](https://github.com/hamzaahmadaslam/action-scheduler-triage/tree/e6f6391a2033b7bca4a60e28254fd622324a8dca). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit; npm package version 1.0.0 confirmed. The CLI was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
