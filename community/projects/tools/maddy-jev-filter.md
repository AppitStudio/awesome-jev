# maddy-jev-filter (sort incoming mail for the maddy server into IMAP folders with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Mail filter for the maddy mail server: Jev answers a few questions about each incoming message (spam, phishing, like what you've put in Not interested) and rules in a config file turn the answers into a folder, such as Junk, Suspicious or Not interested, marked read or unread.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lesderid/maddy-jev-filter) |
| Maintainer | [lesderid](https://github.com/lesderid). Independently curated. |
| Format | Mail filter (D) |
| Requirements | maddy 0.9.6 with imapsql storage, ldc2 and rdmd; a TypeSafe API key. |
| License | [MIT](https://github.com/lesderid/maddy-jev-filter/blob/8d1f6d4c1b98b08ab9f3a5f233b4c35ba3388741/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevfilter/config.d`](https://github.com/lesderid/maddy-jev-filter/blob/8d1f6d4c1b98b08ab9f3a5f233b4c35ba3388741/jevfilter/config.d) at the pinned commit. |

## When to use

- Sort self-hosted mail by spam and phishing risk with your own rules.
- Mismatch: maddy only; written in D.

## How it works

`jevfilter/config.d` sets the default endpoint `https://api.typesafe.ai/v1/systemone`; the filter asks the configured questions per message and the rules pick a folder. Integration evidence: [`jevfilter/config.d`](https://github.com/lesderid/maddy-jev-filter/blob/8d1f6d4c1b98b08ab9f3a5f233b4c35ba3388741/jevfilter/config.d).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/lesderid/maddy-jev-filter && cd maddy-jev-filter
tools/install.sh -H mail.example.org   # see docs/setup.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup guide: [github.com/lesderid/maddy-jev-filter/blob/main/docs/setup.md](https://github.com/lesderid/maddy-jev-filter/blob/main/docs/setup.md)

## Limits and data handling

Message content goes to TypeSafe for each incoming mail.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 8d1f6d4c1b98](https://github.com/lesderid/maddy-jev-filter/tree/8d1f6d4c1b98b08ab9f3a5f233b4c35ba3388741). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
