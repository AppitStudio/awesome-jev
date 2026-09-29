# JEV Mail Filtering

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local read-only IMAP inbox triage with TypeSafe Jev (needs reply / worth reading / scam / unsure).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/albertcas/jev-mail-filtering) |
| Maintainer | [albertcas](https://github.com/albertcas). Independently curated. |
| Format | Local IMAP read-only inbox triage UI powered by TypeSafe Jev. |
| Requirements | Node.js ≥22; IMAP access; TypeSafe API key. |
| License | [MIT](https://github.com/albertcas/jev-mail-filtering/blob/b9fd67ebab270af1ac097fd8785a27252b161de1/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use for local inbox triage with explicit uncertainty buckets. Prefer host mail rules for simple keyword filters.

## How it works

App reads IMAP read-only, asks Jev precise questions per message, and renders a dashboard. Mail content goes to TypeSafe when live.

## Get started

```sh
git clone https://github.com/albertcas/jev-mail-filtering.git
cd jev-mail-filtering
git checkout b9fd67ebab270af1ac097fd8785a27252b161de1
# follow upstream README for IMAP + TYPESAFE key setup
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit b9fd67e](https://github.com/albertcas/jev-mail-filtering/tree/b9fd67ebab270af1ac097fd8785a27252b161de1). AI-assisted README and license inspection; install/live paths not executed.
