# inbox-jev

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Self-hosted Gmail triage: every few minutes it asks Jev which category each new email belongs to, then labels, archives, unsubscribes from verified marketing and cold outreach, moves scams to Spam and leaves uncertain mail in the inbox for review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hellolitebox/litebox-inbox-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://inboxjev.dev) |
| Pricing and access | Free and MIT-licensed; self-hosted, you pay your own TypeSafe usage. Checked 2026-10-17. |
| Jev evidence | [`src/inbox_jev/classifier.py`](https://github.com/hellolitebox/litebox-inbox-jev/blob/f950ada1c7cab76620df67815da5d5a4aa38a4c0/src/inbox_jev/classifier.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/guillegonzaleza/status/2111123830983028758)). |
| Maintainer | [hellolitebox](https://github.com/hellolitebox). Independently curated. |
| Format | Python CLI and scheduled service (PyPI `inbox-jev`; systemd units included) |
| Platform and availability | Linux/macOS server or desktop (self-hosted Python service) |
| Jev's role | Jev classifies each new email with a calibrated confidence; code applies per-category thresholds and actions. |
| Requirements | Python 3.11+ (uv or pipx), a Gmail account authorized through OAuth, a TypeSafe API key; optional Slack webhook for the daily digest. |
| License | [MIT](https://github.com/hellolitebox/litebox-inbox-jev/blob/f950ada1c7cab76620df67815da5d5a4aa38a4c0/LICENSE) |

## When to use

- Clear receipts, notifications, newsletters and cold pitches out of a busy Gmail inbox while keeping personal and action-needed mail in view.
- Start in dry-run mode, review what it would do, then let it act and learn sender rules from your corrections.
- Mismatch: Gmail only; categories and thresholds reflect one person's defaults and need tuning in your copy of `categories.yaml`.

## How it works

Allowlists and learned sender rules decide first; otherwise the classifier sends the useful headers, the start of the body and whether you have written to the sender before to Jev through the TypeSafe SDK, and only acts when the answer clears each category's `min_confidence` (0.80 to 0.90 by default). Every action is recorded in SQLite so it can be audited and undone. Integration evidence: [`src/inbox_jev/classifier.py`](https://github.com/hellolitebox/litebox-inbox-jev/blob/f950ada1c7cab76620df67815da5d5a4aa38a4c0/src/inbox_jev/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install inbox-jev    # or: pipx install inbox-jev
inbox-jev init               # guided setup, then an optional first dry run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [inboxjev.dev](https://inboxjev.dev)
- Plain-language guide: `docs/guide.md`; full decision spec: `docs/how-it-decides.md`.

## Limits and data handling

Email headers and the start of each body go to TypeSafe on your key; OAuth tokens and the action log stay on your machine. It can archive, unsubscribe and move mail to Spam, so start with `--mode dry_run`.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit f950ada1c7ca](https://github.com/hellolitebox/litebox-inbox-jev/tree/f950ada1c7cab76620df67815da5d5a4aa38a4c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
