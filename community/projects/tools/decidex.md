# DecideX

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Industrial System One decision foundation with TypeSafe Jev provider, confidence gating, and deterministic fallbacks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dengyie/decidex) |
| Maintainer | [dengyie](https://github.com/dengyie). Independently curated. |
| Format | Python decision-foundation library |
| Requirements | Python 3.10+; TypeSafe or compatible System One provider. |
| License | [MIT](https://github.com/dengyie/decidex/blob/a87d34eebb12a053ff8582e5fabbff54161e408e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`src/decidex/providers/typesafe.py`](https://github.com/dengyie/decidex/blob/a87d34eebb12a053ff8582e5fabbff54161e408e/src/decidex/providers/typesafe.py) at the pinned commit. |

## When to use

- Use when you need: Industrial System One decision foundation with TypeSafe Jev provider, confidence gating, a…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/decidex/providers/typesafe.py`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/decidex/providers/typesafe.py.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit a87d34eebb12](https://github.com/dengyie/decidex/tree/a87d34eebb12a053ff8582e5fabbff54161e408e). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
