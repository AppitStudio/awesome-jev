# Better Email Filter (local Gmail triage with Jev that learns from your corrections)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Local command-line Gmail triage: Jev sorts messages into Spam, Ignore or Important, sends uncertain ones to Review, and the labels you correct in Gmail become examples for future classifications.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/miguelgarcia/better-email-filter) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/miguelgarcia/better-email-filter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; public source with no license file (no open-source license granted). Jev calls use your own TypeSafe key and are billed by TypeSafe. Checked 2026-10-25. |
| Jev evidence | [`src/better_email/jev.py`](https://github.com/miguelgarcia/better-email-filter/blob/f2923f14ee4abfcc8399f070d4ffdb4f12d4717b/src/better_email/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/MikezGarcia/status/2114024819029401879)). |
| Maintainer | [miguelgarcia](https://github.com/miguelgarcia). Independently curated. |
| Format | Python CLI and shell workflow |
| Platform and availability | macOS and Linux command line, run from source; Windows not supported. |
| Jev's role | Core: Jev classifies each message and its confidence decides whether a label or Review is used. |
| Requirements | macOS or Linux with Python 3.11+ and uv; a Google Cloud project with the Gmail API and a Desktop OAuth client; a TypeSafe API key. |
| License | No LICENSE file on the reviewed commit on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Label a noisy Gmail inbox without sending mail to a hosted triage service.
- Teach the filter with your own corrections instead of writing rules.
- Mismatch: `process.sh` moves Spam to Trash and archives Ignore and Review by default; start with `--no-cleanup`.

## How it works

`src/better_email/jev.py` posts message headers and the first words of the body (300 by default) with your preferences and past corrections to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); low-confidence answers become Review. Integration evidence: [`src/better_email/jev.py`](https://github.com/miguelgarcia/better-email-filter/blob/f2923f14ee4abfcc8399f070d4ffdb4f12d4717b/src/better_email/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/miguelgarcia/better-email-filter.git
cd better-email-filter && uv sync --locked
uv run better-email auth gmail --client private/client_secret.json
uv run better-email auth jev
./process.sh --no-cleanup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/miguelgarcia/better-email-filter#readme](https://github.com/miguelgarcia/better-email-filter#readme)
- Creator's X post: [x.com/MikezGarcia/status/2114024819029401879](https://x.com/MikezGarcia/status/2114024819029401879)

## Limits and data handling

Message excerpts go to TypeSafe. It uses the gmail.modify scope (labels, archive, Trash; no sending). The README calls it an experimental personal workflow whose tests verify mechanics, not accuracy.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit f2923f14ee4a](https://github.com/miguelgarcia/better-email-filter/tree/f2923f14ee4abfcc8399f070d4ffdb4f12d4717b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
