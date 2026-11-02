# LadingLens (shipping inbox control that checks Shipping Instructions against draft Bills of Lading, with Jev classifying)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hackathon-built shipping-operations inbox that accounts for every received email, reconciles expected shipments against what arrived, and compares each Shipping Instruction with its draft Bill of Lading over seven fields, leaving every consequential decision to a named person. Jev decides email categories, document roles and textual field equivalence; Gemini reads the documents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/M1KUAPP/LadingLens) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://averis-222536409832.asia-southeast1.run.app) |
| Pricing and access | Free guest live demo (hackathon deployment, no account needed); free source build under MIT with your own TypeSafe and Gemini keys. Checked 2026-11-02. |
| Jev evidence | [`apps/api/app/jev.py`](https://github.com/M1KUAPP/LadingLens/blob/3be955a220f26a36a5e69e3f9edd940195e2734a/apps/api/app/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [M1KUAPP](https://github.com/M1KUAPP). Independently curated. |
| Format | Web app (FastAPI API + web front end) |
| Platform and availability | Web (live demo); self-host from source. |
| Jev's role | Classifies emails and document roles and judges whether SI and BL field values match. |
| Requirements | A browser for the live demo; Python and Node.js to self-host; `TYPESAFE_API_KEY` and a Gemini key for live decisions. |
| License | [MIT](https://github.com/M1KUAPP/LadingLens/blob/3be955a220f26a36a5e69e3f9edd940195e2734a/LICENSE) |

## When to use

- See a fail-closed, human-signed-off document check for shipping operations.
- Mismatch: built for the Averis x Monash Hackathon 2026 with a seeded demo bundle; not a hosted product.

## How it works

`apps/api/app/jev.py` calls Jev `jev-1.13.0` through `typesafe-sdk` for email classification, document-role and field-equivalence questions with validated probability distributions; any Gemini or Jev failure is audited and shown as a failure with a retry, never a verdict. Integration evidence: [`apps/api/app/jev.py`](https://github.com/M1KUAPP/LadingLens/blob/3be955a220f26a36a5e69e3f9edd940195e2734a/apps/api/app/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/M1KUAPP/LadingLens.git
cd LadingLens
# follow the README's apps/api and web setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo (guest sign-in): [averis-222536409832.asia-southeast1.run.app](https://averis-222536409832.asia-southeast1.run.app)
- Video presentation: [youtu.be/U5_-aXgpJdU](https://youtu.be/U5_-aXgpJdU)

## Limits and data handling

Email and document text is sent to TypeSafe and Google Gemini. The live demo is a hackathon deployment with seeded data and may go away. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 3be955a220f2](https://github.com/M1KUAPP/LadingLens/tree/3be955a220f26a36a5e69e3f9edd940195e2734a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
