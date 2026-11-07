# Jev Email Labels (Gmail labels and action views powered by TypeSafe Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Chrome extension plus local FastAPI service that labels Gmail conversations (Important, Routine, Spam, custom) and builds To do / Deadline / Waiting views with TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vishnugamini/email-jev-labeller) |
| Maintainer | [vishnugamini](https://github.com/vishnugamini). Independently curated. |
| Format | Chrome extension + Python service (no SPDX license file on the reviewed commit) |
| Requirements | Chrome, Python 3, and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`service/engine.py`](https://github.com/vishnugamini/email-jev-labeller/blob/6f97432c007c0aae1b7dfd2e676564ff01958c4d/service/engine.py) at the pinned commit. |

## When to use

- Triage a busy Gmail inbox with custom labels.
- See which messages need action or have deadlines.
- Mismatch: no OSI license on the reviewed commit.

## How it works

`service/engine.py` uses `typesafe_sdk.AsyncTypeSafeClient` with `Choice`/`Noul` questions over visible conversation text. Integration evidence: [`service/engine.py`](https://github.com/vishnugamini/email-jev-labeller/blob/6f97432c007c0aae1b7dfd2e676564ff01958c4d/service/engine.py).

## Get started

Clone, set TYPESAFE_API_KEY in `.env`, start the service, and load the extension.

```sh
git clone https://github.com/vishnugamini/email-jev-labeller.git && cd email-jev-labeller
export TYPESAFE_API_KEY=...
pip install -r service/requirements.txt && python service/app.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/vishnugamini/email-jev-labeller/blob/6f97432c007c0aae1b7dfd2e676564ff01958c4d/README.md](https://github.com/vishnugamini/email-jev-labeller/blob/6f97432c007c0aae1b7dfd2e676564ff01958c4d/README.md)

## Limits and data handling

Email text is sent to the hosted Jev API on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 6f97432c007c](https://github.com/vishnugamini/email-jev-labeller/tree/6f97432c007c0aae1b7dfd2e676564ff01958c4d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
