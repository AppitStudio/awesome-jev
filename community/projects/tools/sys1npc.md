# sys1npc

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Hot-swap scripted game NPC decision points with System One models (Jev / OpenAI Decisions) and confidence-gated fallbacks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SafiullahRattar/sys1npc) |
| Maintainer | [SafiullahRattar](https://github.com/SafiullahRattar). Independently curated. |
| Format | Python library / game AI protocol |
| Requirements | Python 3.10+; Jev or OpenAI Decisions credentials. |
| License | [MIT](https://github.com/SafiullahRattar/sys1npc/blob/b443594f0d42fda554f54f3feaf7105cdfee8cc7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`src/sys1npc/providers/jev.py`](https://github.com/SafiullahRattar/sys1npc/blob/b443594f0d42fda554f54f3feaf7105cdfee8cc7/src/sys1npc/providers/jev.py) at the pinned commit. |

## When to use

- Use when you need: Hot-swap scripted game NPC decision points with System One models (Jev / OpenAI Decisions)…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/sys1npc/providers/jev.py`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/sys1npc/providers/jev.py.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit b443594f0d42](https://github.com/SafiullahRattar/sys1npc/tree/b443594f0d42fda554f54f3feaf7105cdfee8cc7). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
