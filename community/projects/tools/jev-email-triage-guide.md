# Jev + Claude email triage guide (step-by-step: set up Jev with Claude Code and build a read-only Gmail follow-up sorter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A guide for people who don't write code: install Claude Code and the TypeSafe skill, try Jev on sample emails, connect Gmail read-only, and get a ranked report of the last two weeks sorted into piles such as Reply needed, Waiting on them, Check and Possible phishing. Includes a guided /setup command, customisation and an honest-testing chapter. Tested on Windows; Mac steps written but untested.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/byui-library/jev-email-triage) |
| Maintainer | [byui-library](https://github.com/byui-library). Independently curated. |
| Format | Guide plus Python script |
| Requirements | Python, Claude Code, a TypeSafe API key and a Google account for read-only Gmail access. |
| License | [MIT](https://github.com/byui-library/jev-email-triage/blob/6d67007e4b535aebb6c2ad12f8271982e839d9dd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`email_triage/questions.py`](https://github.com/byui-library/jev-email-triage/blob/6d67007e4b535aebb6c2ad12f8271982e839d9dd/email_triage/questions.py) at the pinned commit. |

## When to use

- Learn how Jev and a chat model split the work on a real, personal sorting task.
- Mismatch: Gmail only; Outlook and Codex versions are planned.

## How it works

`email_triage/questions.py` builds one `jev-latest` request per email with the pile questions; `email_triage/run.py` reads Gmail read-only and writes the ranked report. Integration evidence: [`email_triage/questions.py`](https://github.com/byui-library/jev-email-triage/blob/6d67007e4b535aebb6c2ad12f8271982e839d9dd/email_triage/questions.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/byui-library/jev-email-triage && cd jev-email-triage
claude   # then type /setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Guide chapters: [github.com/byui-library/jev-email-triage/tree/main/guide](https://github.com/byui-library/jev-email-triage/tree/main/guide)

## Limits and data handling

Email senders, subjects and snippets are sent to TypeSafe when you run it; the Gmail scope is read-only.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 6d67007e4b53](https://github.com/byui-library/jev-email-triage/tree/6d67007e4b535aebb6c2ad12f8271982e839d9dd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
