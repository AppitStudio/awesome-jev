# Better Backlog (filter a repo's GitHub issues in your own words, with Jev deciding each match)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local web page and CLI that loads a repository's GitHub issues through your existing GitHub CLI login and filters them by a plain-language criterion; each issue gets a decision-model answer with a probability, so you can sort and threshold instead of reading the whole backlog.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BerriAI/better-backlog) |
| Maintainer | [BerriAI](https://github.com/BerriAI). Independently curated. |
| Format | Node.js web app and CLI (no npm dependencies) |
| Requirements | Node.js 22+, a logged-in GitHub CLI, and a TypeSafe API key or a compatible gateway URL and key. |
| License | [MIT](https://github.com/BerriAI/better-backlog/blob/6475d69175fa607d0a744f62a0aed28be288edcd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev.mjs`](https://github.com/BerriAI/better-backlog/blob/6475d69175fa607d0a744f62a0aed28be288edcd/lib/jev.mjs) at the pinned commit. |

## When to use

- Triage a large issue backlog by criteria that labels don't capture.
- Mismatch: reads issues only; it does not edit or label them.

## How it works

`lib/jev.mjs` sends each issue with your criterion to `https://api.typesafe.ai` (model `jev-latest`) or to a gateway base URL you set in Settings, and returns the probability that the issue matches. Integration evidence: [`lib/jev.mjs`](https://github.com/BerriAI/better-backlog/blob/6475d69175fa607d0a744f62a0aed28be288edcd/lib/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/BerriAI/better-backlog && cd better-backlog
BETTER_BACKLOG_REPO=owner/name npm start   # http://127.0.0.1:4317
node cli.mjs filter "good first issues" --json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/BerriAI/better-backlog#readme](https://github.com/BerriAI/better-backlog#readme)

## Limits and data handling

Issue titles and bodies go to TypeSafe or your configured gateway when you filter. The key is entered in the local Settings page.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 6475d69175fa](https://github.com/BerriAI/better-backlog/tree/6475d69175fa607d0a744f62a0aed28be288edcd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
