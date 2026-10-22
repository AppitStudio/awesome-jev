# jev-mail-triage (Gmail and Fastmail filing with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Files each new Gmail, Google Workspace or Fastmail message with one Jev-chosen label (political asks, newsletters, receipts, junk and more), archives or spams only above set thresholds, and ships a small web console for editing rules and correcting mistakes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pnwprojects/jev-mail-triage) |
| Maintainer | [pnwprojects](https://github.com/pnwprojects). Independently curated. |
| Format | Python service on Google Cloud (Cloud Run, Pub/Sub, Firestore) with a web console |
| Requirements | A Google Cloud project with billing; a Gmail or Workspace mailbox (the console needs Workspace); a TypeSafe API key. |
| License | [MIT](https://github.com/pnwprojects/jev-mail-triage/blob/50fb56f3a596c4db9f7d98f9c6ea794445fc346e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`triage/classifier.py`](https://github.com/pnwprojects/jev-mail-triage/blob/50fb56f3a596c4db9f7d98f9c6ea794445fc346e/triage/classifier.py) at the pinned commit. |

## When to use

- Keep political fundraising and rotating-domain marketing out of the inbox.
- Tune categories and thresholds as settings rather than code.
- Mismatch: needs your own Google Cloud deployment, not a hosted service.

## How it works

`triage/classifier.py` calls Jev through the official `typesafe-sdk` (`POST https://api.typesafe.ai/v1/systemone`) with one choice question over the message; low-confidence results get `AI/Review` instead of being moved. Integration evidence: [`triage/classifier.py`](https://github.com/pnwprojects/jev-mail-triage/blob/50fb56f3a596c4db9f7d98f9c6ea794445fc346e/triage/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
gcloud auth login && gcloud auth application-default login
pip install -r requirements-dev.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Full Google Cloud setup and console guide in the README: [github.com/pnwprojects/jev-mail-triage#readme](https://github.com/pnwprojects/jev-mail-triage#readme)

## Limits and data handling

Message content is sent to TypeSafe; Google Cloud and TypeSafe usage are billed to you.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 50fb56f3a596](https://github.com/pnwprojects/jev-mail-triage/tree/50fb56f3a596c4db9f7d98f9c6ea794445fc346e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
