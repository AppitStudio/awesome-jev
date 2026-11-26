# fedi-report-triage by Hamza Ahmad Aslam (read-only CLI that sorts a Mastodon server's open reports into a severity queue with Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

For Mastodon moderators: reads open reports with your own `admin:read:reports` token and prints them as a queue sorted by severity, with the kind of problem each shows and whether the reporter's comment matches the reported posts. Jev answers narrow typed questions per report; unsure reports go to a review list and every action stays with you in Mastodon.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/fedi-report-triage) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (not needed for `--dry-run`). |
| License | [MIT](https://github.com/hamzaahmadaslam/fedi-report-triage/blob/ac49ef22ef8adc846cd91483535f96a99035f67d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/fedi-report-triage/blob/ac49ef22ef8adc846cd91483535f96a99035f67d/src/jev.mjs) at the pinned commit. |

## When to use

- Moderators of a Mastodon server who want urgent reports at the top instead of newest first.
- Mismatch: automated moderation; it never resolves reports or acts on accounts.

## How it works

`src/jev.mjs` posts batches to `https://api.typesafe.ai/v1/systemone` with typed `choice`, `noul` and `score` questions, and code applies one `--threshold` (default 0.8) to place each item or send it to review. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/fedi-report-triage/blob/ac49ef22ef8adc846cd91483535f96a99035f67d/src/jev.mjs).

## Get started

Create a token with only `admin:read:reports`, then run it against your server URL.

```sh
npm install -g @hamzaahmadaslam/fedi-report-triage
export MASTODON_TOKEN=...      # admin:read:reports only
export TYPESAFE_API_KEY=...
fedi-report-triage https://mastodon.example --dry-run
fedi-report-triage https://mastodon.example
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Worked example in the README: [github.com/hamzaahmadaslam/fedi-report-triage#example](https://github.com/hamzaahmadaslam/fedi-report-triage#example)

## Limits and data handling

Reported post text, content warnings, media descriptions and the reporter's comment go to TypeSafe; names, handles, dates and IDs do not, and followers-only and direct posts are excluded unless you pass `--include-private`. Jev reads text only and judges the attached posts against fixed descriptions, not your server's rules. Tested against Mastodon 4.x API docs with synthetic data.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit ac49ef22ef8a](https://github.com/hamzaahmadaslam/fedi-report-triage/tree/ac49ef22ef8adc846cd91483535f96a99035f67d). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit; npm package version 1.0.0 confirmed. The CLI was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
