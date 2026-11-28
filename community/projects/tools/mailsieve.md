# mailsieve by Jack Venberg (Gmail triage where Jev types each email and confirms every archive or trash action)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Personal Gmail triage service: Jev puts every new email into one of 23 types, a yes/no Jev check confirms the property that makes an action safe, and YAML rules then label it, archive or trash it once old enough, or mark it for unsubscribing. Starred mail, your own mail and replies are never touched, trash is Gmail's 30-day trash, and every answer is cached as an audit record. Runs on Cloud Run with Gmail push notifications.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JVenberg/mailsieve) |
| Maintainer | [Jack Venberg](https://github.com/JVenberg) (JVenberg). Independently curated. |
| Format | Python service + CLI on Google Cloud Run |
| Requirements | Python with uv, a Gmail OAuth client, an OpenRouter key and a GCP project with billing for the hosted mode. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mailsieve/jev.py`](https://github.com/JVenberg/mailsieve/blob/236f93953a15b297cda2a15daea5e396fc6f505a/mailsieve/jev.py) at the pinned commit. |

## When to use

- People who want their own Gmail inbox sorted and cleaned by auditable rules on top of Jev's answers.
- Mismatch: shared or team mailboxes; it is built for one owner's inbox.

## How it works

`mailsieve/jev.py` posts the questions from `rules.yaml` (model `~typesafe/jev-latest`) to OpenRouter's decisions endpoint with the sender, subject, list headers and the first 1,500 characters of the body. Answers are cached per message and question wording (SQLite locally, Firestore on Cloud Run), so changing rules re-decides without new calls. Integration evidence: [`mailsieve/jev.py`](https://github.com/JVenberg/mailsieve/blob/236f93953a15b297cda2a15daea5e396fc6f505a/mailsieve/jev.py).

## Get started

Log in to Gmail, then preview the rules on your inbox without changing anything.

```sh
git clone https://github.com/JVenberg/mailsieve && cd mailsieve
echo OPENROUTER_API_KEY=... > .env
uv run python -m mailsieve login
uv run python -m mailsieve classify --dry-run --query "in:inbox newer_than:14d"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Default rules: [github.com/JVenberg/mailsieve/blob/main/mailsieve/rules.yaml](https://github.com/JVenberg/mailsieve/blob/main/mailsieve/rules.yaml)
- Privacy notes: [github.com/JVenberg/mailsieve/blob/main/PRIVACY.md](https://github.com/JVenberg/mailsieve/blob/main/PRIVACY.md)

## Limits and data handling

Email excerpts go to OpenRouter (and on to TypeSafe) for classification. It needs the `gmail.modify` scope, adds labels, archives and moves mail to trash, but never sends mail or deletes permanently. The README estimates about $0.10 per 1,000 emails for a backfill. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 236f93953a15](https://github.com/JVenberg/mailsieve/tree/236f93953a15b297cda2a15daea5e396fc6f505a). Inspected the README, PRIVACY.md, `mailsieve/jev.py` and `rules.yaml` at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
