# legends-jev (Jev decision, OCR and signage-verification adapter for the cto-legends agent toolkit)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Dependency-free Python adapter in the cto-legends module set: given a short text observation and explicit candidate actions, or PNG and JPEG screenshots, documents or photos, it returns validated Choice, Score, Noul and Box answers from Jev (`jev-1.14.0`), including original-image pixel boxes; it captures and executes nothing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/avalonreset/legends-jev) |
| Maintainer | [avalonreset](https://github.com/avalonreset). Independently curated. |
| Format | Python package and CLI (no runtime dependencies) |
| Requirements | Python 3.10+; a TypeSafe API key; optionally the cto-legends manager. |
| License | [MIT](https://github.com/avalonreset/legends-jev/blob/0ec2aec18a92dbb24fc3b56c1652c21ce120e8cf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`legends_jev/provider.py`](https://github.com/avalonreset/legends-jev/blob/0ec2aec18a92dbb24fc3b56c1652c21ce120e8cf/legends_jev/provider.py) at the pinned commit. |

## When to use

- Give a coding agent typed advice on which app, browser or document action to take next.
- Locate text or verify storefront signage in an image with box coordinates.
- Mismatch: advice only; actuation stays in separate Legends kits, and the operator must check the live target.

## How it works

`provider.py` calls `https://api.typesafe.ai/v1/systemone` (and `/v1/models`) with the observation or image and validates each answer before returning it. Integration evidence: [`legends_jev/provider.py`](https://github.com/avalonreset/legends-jev/blob/0ec2aec18a92dbb24fc3b56c1652c21ce120e8cf/legends_jev/provider.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python -m legends_jev doctor
# or: cto-legends install legends-jev --apply
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/avalonreset/legends-jev#readme](https://github.com/avalonreset/legends-jev#readme)
- cto-legends: [github.com/avalonreset/cto-legends](https://github.com/avalonreset/cto-legends)

## Limits and data handling

Observations and supplied images go to TypeSafe. No screen capture, browser navigation or action execution is included.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 0ec2aec18a92](https://github.com/avalonreset/legends-jev/tree/0ec2aec18a92dbb24fc3b56c1652c21ce120e8cf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
