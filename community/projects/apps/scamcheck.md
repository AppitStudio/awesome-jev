# ScamCheck

[All projects](../README.md) · [Web apps](README.md#web-apps)

Paste a suspicious message and get a scam verdict and risk score: one TypeSafe Jev call answers about eleven typed questions, and code can only raise the risk.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AkashNaickar/scamcheck) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/AkashNaickar/scamcheck#readme) (source-built app; no separate website verified). |
| Pricing and access | No app purchase fee for the source build; requires your own TypeSafe API key and TypeSafe usage charges. Checked 2026-10-05. |
| Jev evidence | [Upstream README](https://github.com/AkashNaickar/scamcheck/blob/89c2794dbe7c050f253422c1e3d35806470bcb13/README.md) documents the single typed Jev call and question set; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [AkashNaickar](https://github.com/AkashNaickar). Independently curated. |
| Format | Web app, HTTP API, and Manifest V3 browser extension (source build) |
| Platform and availability | Source build; local web app at `http://localhost:8787` plus an MV3 extension. No hosted instance verified. |
| Jev's role | One `systemOne` call per check with Noul/Choice/Score questions (e.g. `is_scam`); reasons and advice come from templates keyed by Jev's answers, and URL findings can only raise risk. |
| Requirements | Node.js 20+ and a TypeSafe API key. |
| License | [MIT](https://github.com/AkashNaickar/scamcheck/blob/89c2794dbe7c050f253422c1e3d35806470bcb13/LICENSE). |

## When to use

- Check SMS, email, or chat messages for scam signals before acting on them.
- Study a pattern where the model never writes user-facing text and code applies risk floors.
- Mismatch: a verdict is a risk signal, not a guarantee; do not use it as the only fraud control.

## How it works

The server redacts PII, makes one Jev call with a typed question set, and combines the probability with URL findings; code can raise but never lower risk. If Jev is unreachable it returns a degraded URL-only result marked `degraded: true`, never a green verdict.

## Get started

Clone, install, and run locally (live Jev calls need a key):

```sh
git clone https://github.com/AkashNaickar/scamcheck.git
cd scamcheck
npm install
# set the TypeSafe API key per upstream README
npm run dev   # http://localhost:8787
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `npm test` runs 100 offline tests with a fake judge; `npm run eval` reports real-Jev accuracy over 36 fixtures (needs a key).

## Limits and data handling

Message text (after PII redaction) is sent to TypeSafe; each check is billed. Accuracy figures are the maintainer's; none were reproduced here.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 89c2794dbe7c](https://github.com/AkashNaickar/scamcheck/tree/89c2794dbe7c050f253422c1e3d35806470bcb13). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
