# Slator Localization Request Readiness Inbox

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local inbox dashboard for enterprise translation intake: it reads unread Gmail or Outlook messages (read-only OAuth), uses Jev to identify translation requests, analyses supported source attachments, infers target languages and deadlines, and shows brief completeness, capacity and clarification points beside each email.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexslator/Localization-Email-Analysis) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/alexslator/Localization-Email-Analysis#readme) (self-hosted local dashboard). |
| Pricing and access | Free source build; requires your own TypeSafe API key and a Gmail or Outlook OAuth app you create. Checked 2026-10-08. |
| Jev evidence | [`email_inference.py`](https://github.com/alexslator/Localization-Email-Analysis/blob/acd3a39afdadf77672a1910a0ff0a72099d94c61/email_inference.py) sends email content to TypeSafe for typed analysis; README states data is sent to Jev. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [alexslator](https://github.com/alexslator). Independently curated. |
| Format | Python local web app (`python3 app.py`) |
| Platform and availability | macOS, Windows or Linux with Python 3.10+; any browser. |
| Jev's role | Classifies and assesses each incoming email as a localization request. |
| Requirements | Python 3.10+; TypeSafe API key; Gmail API or Microsoft Entra app registration for read access. |
| License | [Apache-2.0](https://github.com/alexslator/Localization-Email-Analysis/blob/acd3a39afdadf77672a1910a0ff0a72099d94c61/LICENSE). |

## When to use

- Triage translation requests in a shared inbox.
- Mismatch: sends email and attachment content to TypeSafe; needs an admin-approved OAuth app.

## How it works

The app fetches unread messages via [`mail_clients.py`](https://github.com/alexslator/Localization-Email-Analysis/blob/acd3a39afdadf77672a1910a0ff0a72099d94c61/mail_clients.py), runs Jev questions per email and renders results in a local dashboard.

## Get started

Install (README *Fresh installation*):

```sh
git clone https://github.com/alexslator/Localization-Email-Analysis.git && cd Localization-Email-Analysis
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add TYPESAFE_API_KEY
python3 app.py
```

Jev usage per analysed email on your key.

## Examples and demos

- Sample brief: [`examples/request-brief.txt`](https://github.com/alexslator/Localization-Email-Analysis/blob/acd3a39afdadf77672a1910a0ff0a72099d94c61/examples/request-brief.txt).

## Limits and data handling

Email bodies and supported attachments go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit acd3a39afdad](https://github.com/alexslator/Localization-Email-Analysis/tree/acd3a39afdadf77672a1910a0ff0a72099d94c61). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
