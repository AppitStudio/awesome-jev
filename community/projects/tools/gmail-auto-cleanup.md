# gmail-auto-cleanup

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python tool that sorts a Gmail inbox with a System One model — TypeSafe Jev (tested on ~27,000 emails) or experimental local Laya — answering typed yes/no questions per email while plain Python rules act; actions are archive + label with a 7-day hold before Trash, and the OAuth scope cannot permanently delete mail.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nani-stack/gmail-auto-cleanup) |
| Maintainer | [nani-stack](https://github.com/nani-stack). Independently curated. |
| Format | Python package `gmail_cleanup` run from a clone (venv + requirements) |
| Requirements | Python 3, your own Google Cloud OAuth desktop client with the Gmail API enabled (`credentials.json`), `typesafe-sdk` + `TYPESAFE_API_KEY` for Jev, or `laya` for local runs. |
| License | [MIT](https://github.com/nani-stack/gmail-auto-cleanup/blob/52d60790b7e81779788e3d543f227034c348331d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Clear a backlog inbox (upstream: ~13,000 of 18,000 messages archived for about $1 of inference) and keep it clear weekly.
- Express what you care about as rules and questions instead of hand-built filters.
- Mismatch: upstream marks the local Laya backend experimental and notes the two backends do not behave identically.

## How it works

[`gmail_cleanup/gmail.py`](https://github.com/nani-stack/gmail-auto-cleanup/blob/52d60790b7e81779788e3d543f227034c348331d/gmail_cleanup/gmail.py) reads mail via the Gmail API; [`judge.py`](https://github.com/nani-stack/gmail-auto-cleanup/blob/52d60790b7e81779788e3d543f227034c348331d/gmail_cleanup/judge.py) asks the model one probability per question per email; [`rules.py`](https://github.com/nani-stack/gmail-auto-cleanup/blob/52d60790b7e81779788e3d543f227034c348331d/gmail_cleanup/rules.py) turns probabilities into archive/label actions. Labelled mail sits 7 days before moving to Trash, where Gmail keeps it 30 more days.

## Get started

Set up from the README:

```sh
git clone https://github.com/nani-stack/gmail-auto-cleanup && cd gmail-auto-cleanup
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/pip install typesafe-sdk          # for Jev
export TYPESAFE_API_KEY=...
# add credentials.json (Google OAuth desktop client), write your rules, then run per README
```

Upstream reports about $0.00006 per email with Jev; Laya runs locally for free.

## Examples and demos

- README *How a decision gets made* and *Nothing is deleted without a long delay*.
- README *Laya is experimental* (backend comparison).

## Limits and data handling

Email content (as selected by the tool) is sent to TypeSafe when using Jev; nothing leaves the machine with Laya. You create and own the Google OAuth app (unverified-app warning expected). Cost figures are upstream's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 52d60790b7e8](https://github.com/nani-stack/gmail-auto-cleanup/tree/52d60790b7e81779788e3d543f227034c348331d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
