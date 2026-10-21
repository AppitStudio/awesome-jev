# Jev Outlook Cleaner

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local web app that triages older Outlook Inbox messages into keep, review and delete candidates with Jev plus local mail signals, auto-moves only high-confidence bulk mail to Deleted Items, and never deletes permanently.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jimmyLC/jev-outlook-cleaner) |
| Maintainer | [jimmyLC](https://github.com/jimmyLC). Independently curated. |
| Format | Local web app and CLI (Python); UI partly in Chinese |
| Requirements | Python 3.10+, a TypeSafe API key, a Microsoft Entra public client app with delegated `Mail.ReadWrite` and `User.Read`. |
| License | [MIT](https://github.com/jimmyLC/jev-outlook-cleaner/blob/ff00caa35dd75e753aab59d64965499718165c04/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_outlook_cleaner.py`](https://github.com/jimmyLC/jev-outlook-cleaner/blob/ff00caa35dd75e753aab59d64965499718165c04/jev_outlook_cleaner.py) at the pinned commit. |

## When to use

- Clear out old newsletters and automated mail with a review step before anything moves.
- Protect replies, receipts, bookings and security mail without spending a Jev call.
- Mismatch: binds to 127.0.0.1 only; do not deploy it to the public internet.

## How it works

`mail_signals.py` keeps obvious mail locally; the rest goes to Jev (`jev_outlook_cleaner.py`), and only messages Jev rates bulk with confidence 0.90+ and delete candidates with 0.85+ are moved, after rechecking each message in Outlook. Integration evidence: [`jev_outlook_cleaner.py`](https://github.com/jimmyLC/jev-outlook-cleaner/blob/ff00caa35dd75e753aab59d64965499718165c04/jev_outlook_cleaner.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env   # set TYPESAFE_API_KEY and OUTLOOK_CLIENT_ID
.venv/bin/python jev_outlook_cleaner.py check
.venv/bin/python jev_outlook_cleaner.py login
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Status and handoff notes: [github.com/jimmyLC/jev-outlook-cleaner/blob/main/PROJECT_STATUS.md](https://github.com/jimmyLC/jev-outlook-cleaner/blob/main/PROJECT_STATUS.md)

## Limits and data handling

Message fields and up to 9,000 characters of plain-text body are sent to TypeSafe for classification. Moves go to Deleted Items, never permanent deletion.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit ff00caa35dd7](https://github.com/jimmyLC/jev-outlook-cleaner/tree/ff00caa35dd75e753aab59d64965499718165c04). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
