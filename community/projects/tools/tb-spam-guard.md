# SpamGuard (tb-spam-guard)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Thunderbird MailExtension (Manifest V3, Thunderbird 128+) that scores incoming mail with language-independent header rules (display-name vs sender-domain mismatch, invisible characters, SPF/DMARC failures) and, only for borderline messages, optionally asks TypeSafe Jev for a second opinion. UI and docs are in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Helicon1968/tb-spam-guard) |
| Maintainer | [Helicon1968](https://github.com/Helicon1968). Independently curated. |
| Format | Thunderbird add-on (`.xpi` from Releases or `node tools/build.mjs`) |
| Requirements | Thunderbird 128+; optional TypeSafe API key. |
| License | [MIT](https://github.com/Helicon1968/tb-spam-guard/blob/24f94ad0d717db94b82dd2fb8699b834eea6fdf3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Catch phishing that copies legitimate mail bodies, including on POP accounts without server-side filtering.
- Mismatch: Japanese-language UI; tuned for Japanese organizations; borderline message content goes to a hosted API when Jev is enabled.

## How it works

Header rules produce a score; clear cases are tagged locally and only borderline messages are sent to Jev, then tagged and marked as junk. (Summarized from the upstream [README](https://github.com/Helicon1968/tb-spam-guard/blob/24f94ad0d717db94b82dd2fb8699b834eea6fdf3/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Download the `.xpi` from the project's Releases and install it from Thunderbird's add-on manager (unsigned add-on setting required).

## Limits and data handling

Rule checks run locally; borderline message data is sent to the TypeSafe API only when a key is configured. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 24f94ad0d717](https://github.com/Helicon1968/tb-spam-guard/tree/24f94ad0d717db94b82dd2fb8699b834eea6fdf3). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
