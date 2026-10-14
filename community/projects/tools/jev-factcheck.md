# jev-factcheck

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill (English and Ukrainian) that asks Jev whether a verbatim source excerpt supports, contradicts or says nothing about a specific claim, keeping provenance.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maksym771/jev-factcheck) |
| Maintainer | [maksym771](https://github.com/maksym771). Independently curated. |
| Format | Agent skill + Python script |
| Requirements | Python; OpenRouter or TypeSafe API key. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`en/scripts/check_claims.py`](https://github.com/maksym771/jev-factcheck/blob/832db0578eeb481a0a58745e05e9f50cb12686f5/en/scripts/check_claims.py) at the pinned commit. |

## When to use

- Check claims against quoted sources in an agent workflow.
- Mismatch: no LICENSE file; small skill.

## How it works

Code pairs claims with source excerpts; Jev returns supports / contradicts / says_nothing with confidence; provenance is preserved in the output. Integration evidence: [`en/scripts/check_claims.py`](https://github.com/maksym771/jev-factcheck/blob/832db0578eeb481a0a58745e05e9f50cb12686f5/en/scripts/check_claims.py).

## Get started

From the upstream README (not run on the review host):

```sh
python en/scripts/check_claims.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Ukrainian version: `uk/`.

## Limits and data handling

Claims and excerpts go to OpenRouter/TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 832db0578eeb](https://github.com/maksym771/jev-factcheck/tree/832db0578eeb481a0a58745e05e9f50cb12686f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
