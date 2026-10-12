# mail-classifier (Outlook)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local web app that fetches unread Outlook mail via Microsoft Graph, classifies each message with TypeSafe Jev (`typesafe-sdk`), and flags, files or trashes it only after you confirm; also shows per-mail latency and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MichaelRingelstein/mail-classifier) |
| Maintainer | [MichaelRingelstein](https://github.com/MichaelRingelstein). Independently curated. |
| Format | Python local web app |
| Requirements | Python; Microsoft Graph app registration; TypeSafe key. |
| License | [MIT](https://github.com/MichaelRingelstein/mail-classifier/blob/16833bf017c6ced5e2c4e38ba81d53d62d1fb373/LICENSE) |
| Jev evidence | [`app/classify.py`](https://github.com/MichaelRingelstein/mail-classifier/blob/16833bf017c6ced5e2c4e38ba81d53d62d1fb373/app/classify.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Triage an Outlook inbox with a human confirmation step and visible Jev timings.
- Mismatch: Outlook/Graph only for now.

## How it works

`app/outlook.py` reads unread mail via Graph; `app/classify.py` asks Jev for categories; actions run after confirmation. (Summarized from the upstream [README](https://github.com/MichaelRingelstein/mail-classifier/blob/16833bf017c6ced5e2c4e38ba81d53d62d1fb373/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): set Graph and TypeSafe credentials per the README and start the local app.

## Limits and data handling

Mail content goes to TypeSafe; mailbox access via your Graph token. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 16833bf017c6](https://github.com/MichaelRingelstein/mail-classifier/tree/16833bf017c6ced5e2c4e38ba81d53d62d1fb373). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
