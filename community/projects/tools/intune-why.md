# intune-why (the few fixes that clear most Intune noncompliance, with Jev classifying custom settings)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reads Microsoft Intune compliance data through read-only Microsoft Graph and builds a fix plan: each step picks the setting whose fix makes the most additional devices compliant, with a what-if view of projected compliance; rules map standard settings, and custom compliance settings that no rule matches can optionally go to Jev for a remediation category. Live demo with a fictional tenant.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dallascrilley/intune-why) |
| Maintainer | [dallascrilley](https://github.com/dallascrilley). Independently curated. |
| Format | Python CLI with an HTML report |
| Requirements | Python 3.9+; read-only Graph access to your tenant; an OpenRouter key only for `--decide jev`. |
| License | [MIT](https://github.com/dallascrilley/intune-why/blob/4df2a9b43745fd7c939b4101be8dc45dccfa6f41/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/intune_why/classify.py`](https://github.com/dallascrilley/intune-why/blob/4df2a9b43745fd7c939b4101be8dc45dccfa6f41/src/intune_why/classify.py) at the pinned commit. |

## When to use

- Prioritise Intune compliance work by devices cleared, not by device list.
- Mismatch: Jev is optional and only sees custom settings no rule matches.

## How it works

`src/intune_why/classify.py` sends unmatched setting names to OpenRouter's Decisions API with `typesafe/jev-1.14` and records the category with its probability. Integration evidence: [`src/intune_why/classify.py`](https://github.com/dallascrilley/intune-why/blob/4df2a9b43745fd7c939b4101be8dc45dccfa6f41/src/intune_why/classify.py).

## Get started

From the upstream README (not run on the review host):

```sh
pipx install git+https://github.com/dallascrilley/intune-why
intune-why demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [intune-why.dallascrilley.com](https://intune-why.dallascrilley.com)
- README: [github.com/dallascrilley/intune-why#readme](https://github.com/dallascrilley/intune-why#readme)

## Limits and data handling

Setting names (not device data) go to OpenRouter and TypeSafe when `--decide jev` is used.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 4df2a9b43745](https://github.com/dallascrilley/intune-why/tree/4df2a9b43745fd7c939b4101be8dc45dccfa6f41). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
