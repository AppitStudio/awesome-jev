# Jevlytics by Saee Gore (payments analytics assistant on fictional data where Jev classifies scope and picks the tool and a policy engine decides)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Ask plain-English questions about a merchant's card payments (declines, settlements, chargebacks). A regex screen runs first, Jev labels scope and risk and picks a tool from a closed list, a policy engine checks the choice, and Claude only turns questions into parameters and writes the answer from approved figures. Fictional data, with a documented decision log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saee-gore/Jevlytics) |
| Maintainer | [saee-gore](https://github.com/saee-gore). Independently curated. |
| Format | Python (FastAPI) backend, PostgreSQL and web dashboard |
| Requirements | Python, PostgreSQL and Node.js per GETTING_STARTED; TypeSafe and Anthropic API keys (fails closed without them). |
| License | [MIT](https://github.com/saee-gore/Jevlytics/blob/d460f281783d79e8e4c0c80c2bbc7fbeecef1c6c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/jev/adapter.py`](https://github.com/saee-gore/Jevlytics/blob/d460f281783d79e8e4c0c80c2bbc7fbeecef1c6c/app/jev/adapter.py) at the pinned commit. |

## When to use

- Study a fail-closed pattern where Jev classifies but never authorises.
- Mismatch: real payment data; it is a local demo on fictional data.

## How it works

`app/jev/adapter.py` is the only module that maps TypeSafe SDK calls (`TypeSafeClient`, `Choice`, `Noul`) to project decisions: one call for scope and risk, a second for tool selection from the server registry. Integration evidence: [`app/jev/adapter.py`](https://github.com/saee-gore/Jevlytics/blob/d460f281783d79e8e4c0c80c2bbc7fbeecef1c6c/app/jev/adapter.py).

## Get started

Follow GETTING_STARTED.md (about 45 minutes on first run).

```sh
git clone https://github.com/saee-gore/Jevlytics.git && cd Jevlytics
# then follow GETTING_STARTED.md (database, .env, backend, dashboard)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Getting started: [github.com/saee-gore/Jevlytics/blob/d460f281783d79e8e4c0c80c2bbc7fbeecef1c6c/GETTING_STARTED.md](https://github.com/saee-gore/Jevlytics/blob/d460f281783d79e8e4c0c80c2bbc7fbeecef1c6c/GETTING_STARTED.md)

## Limits and data handling

User questions and the caller's merchant id are sent to TypeSafe and Anthropic. Fictional data only; thresholds are provisional per the README.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit d460f281783d](https://github.com/saee-gore/Jevlytics/tree/d460f281783d79e8e4c0c80c2bbc7fbeecef1c6c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
