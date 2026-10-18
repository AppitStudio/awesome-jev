# typesafe-decisions

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Typed Python helpers for semantic scoring, classification, and routing on top of TypeSafe System One (`TypeSafeClient`), with docs site examples.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kaischinnen/typesafe-decisions) |
| Maintainer | [kaischinnen](https://github.com/kaischinnen). Independently curated. |
| Format | Python library + docs site |
| Requirements | Python; TypeSafe API key via typesafe-sdk / env. |
| License | [MIT](https://github.com/kaischinnen/typesafe-decisions/blob/6bcbc0ad51fa0c715115d61d93d27449941eb9dc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/typesafe_decisions/client.py`](https://github.com/kaischinnen/typesafe-decisions/blob/6bcbc0ad51fa0c715115d61d93d27449941eb9dc/src/typesafe_decisions/client.py) at the pinned commit. |

## When to use

- Prefer thin typed helpers over raw System One payloads.
- Need scoring/classification/routing helpers sharing one client.
- Mismatch: helper library; not an official TypeSafe SDK.

## How it works

`client.py` imports `TypeSafeClient` / `TypeSafeAPIError` and exposes helpers that issue typed System One questions for common decision patterns. Integration evidence: [`src/typesafe_decisions/client.py`](https://github.com/kaischinnen/typesafe-decisions/blob/6bcbc0ad51fa0c715115d61d93d27449941eb9dc/src/typesafe_decisions/client.py).

## Get started

Install from the repo and open the docs site examples.

```sh
git clone https://github.com/kaischinnen/typesafe-decisions && cd typesafe-decisions
pip install -e .
# https://kaischinnen.github.io/typesafe-decisions/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [kaischinnen.github.io/typesafe-decisions/](https://kaischinnen.github.io/typesafe-decisions/)
- src/typesafe_decisions/client.py

## Limits and data handling

Unofficial helper. Behavior follows the installed typesafe-sdk and model pin you choose.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 6bcbc0ad51fa](https://github.com/kaischinnen/typesafe-decisions/tree/6bcbc0ad51fa0c715115d61d93d27449941eb9dc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
