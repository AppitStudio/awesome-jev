# IntentLock

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Service that uses TypeSafe Jev (`TypeSafeClient`, default `https://api.typesafe.ai`) as the “smart” decision path for intent locking / approval-style checks alongside other LLM lanes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BrienAustinClayton/intentlock) |
| Maintainer | [BrienAustinClayton](https://github.com/BrienAustinClayton). Independently curated. |
| Format | Multi-service Python app |
| Requirements | Python services stack; TYPESAFE credentials; see repo for full deploy deps. |
| License | [MIT](https://github.com/BrienAustinClayton/intentlock/blob/5547a228827cea4b96bce77f6db3703db9e9f207/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`services/intentlock/app/jev.py`](https://github.com/BrienAustinClayton/intentlock/blob/5547a228827cea4b96bce77f6db3703db9e9f207/services/intentlock/app/jev.py) at the pinned commit. |

## When to use

- Route high-stakes intent checks through typed Jev.
- Want SDK-based System One calls with configurable base URL.
- Mismatch: larger multi-service repo; extract the Jev path carefully.

## How it works

`services/intentlock/app/jev.py` builds a `TypeSafeClient` with `base_url` defaulting to `https://api.typesafe.ai` and issues typed questions for the intentlock flow. Integration evidence: [`services/intentlock/app/jev.py`](https://github.com/BrienAustinClayton/intentlock/blob/5547a228827cea4b96bce77f6db3703db9e9f207/services/intentlock/app/jev.py).

## Get started

Clone and follow service README/compose instructions; set TypeSafe credentials for the smart lane.

```sh
git clone https://github.com/BrienAustinClayton/intentlock && cd intentlock
# see services/intentlock for Jev lane configuration
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- services/intentlock/app/jev.py
- services/intentlock/tests/test_jev.py

## Limits and data handling

Broader than a single Jev demo. Other LLM lanes may also process user content.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 5547a228827c](https://github.com/BrienAustinClayton/intentlock/tree/5547a228827cea4b96bce77f6db3703db9e9f207). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
