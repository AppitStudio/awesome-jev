# jev-gmail-filter

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local, self-hosted Gmail filter: describe topics in plain English; jevfilter + TypeSafe Jev judge mail; a localhost UI labels, tracks items, and flags quiet threads.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/damiensmith1/jev-gmail-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/damiensmith1/jev-gmail-filter#readme) |
| Pricing and access | MIT source build with uv; bring TypeSafe API key and your own Google OAuth client. No app fee; Gmail API + TypeSafe usage separate. Early development. Checked **2026-09-26**. |
| Jev evidence | Pipeline uses jevfilter/TypeSafe Jev ([`src/jev_gmail_filter/pipeline.py`](https://github.com/damiensmith1/jev-gmail-filter/blob/29713874375edc92088168887d7f608f2b5a54a9/src/jev_gmail_filter/pipeline.py)); localhost UI under [`src/jev_gmail_filter/web/`](https://github.com/damiensmith1/jev-gmail-filter/tree/29713874375edc92088168887d7f608f2b5a54a9/src/jev_gmail_filter/web). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live install/provider paths not run on the review host. Companion to listed jevfilter; distinct from Gmail Chrome extensions. |
| Maintainer | [damiensmith1](https://github.com/damiensmith1). Independently curated. |
| Format | Python app (CLI + localhost web UI). |
| Platform and availability | Localhost only; data under `./data`. Not a Chrome extension. |
| Jev's role | Judges topic match / uncertainty via jevfilter helpers; app owns labels, items board, and spend caps. |
| Requirements | Python 3.12+; uv; TypeSafe API key; Google Cloud OAuth client for Gmail. |
| License | [MIT](https://github.com/damiensmith1/jev-gmail-filter/blob/29713874375edc92088168887d7f608f2b5a54a9/LICENSE). |

## When to use

Use for a **local Gmail topic workspace** powered by jevfilter. Prefer Chrome Gmail badge extensions when you only want inline scores.

## How it works

Onboarding wizard stores keys and OAuth locally; sync reads selected Gmail categories; uncertain mails land in Needs you.

## Get started

```sh
git clone https://github.com/damiensmith1/jev-gmail-filter.git
cd jev-gmail-filter
git checkout 29713874375edc92088168887d7f608f2b5a54a9
uv sync
uv run jev-gmail-filter ui
```

## Examples and demos

- Upstream CI badge and UI screens (Overview, Needs you, Topics).
- Dry-run judge-without-labelling option during onboarding.

## Limits and data handling

Email content judged by Jev goes to TypeSafe. OAuth tokens and SQLite stay in `./data` (gitignored). Early development.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 2971387](https://github.com/damiensmith1/jev-gmail-filter/tree/29713874375edc92088168887d7f608f2b5a54a9). AI-assisted source inspection; live paths not executed.
