# redpanda-connect-jev (typed Jev decisions inside Redpanda Connect pipelines)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Processors and examples that embed typed TypeSafe Jev decisions in Redpanda Connect pipelines, with offline decision fixtures that assert the upstream URL is `https://api.typesafe.ai/v1/systemone`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/redpanda-connect-jev) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python / Redpanda Connect components (MIT) |
| Requirements | Redpanda Connect as documented upstream, Python for the helpers, and `TYPESAFE_API_KEY` for live pipelines. |
| License | [MIT](https://github.com/gbesse/redpanda-connect-jev/blob/0f427f233a635f83605786423a0b972fba710e7e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_core.py`](https://github.com/gbesse/redpanda-connect-jev/blob/0f427f233a635f83605786423a0b972fba710e7e/jev_core.py) at the pinned commit. |

## When to use

- Gate or enrich streaming records with typed Jev answers.
- Test pipelines offline with recorded decisions.
- Mismatch: you still own Connect deployment and keys.

## How it works

`jev_core.py` builds TypeSafe systemone requests; offline examples assert the production URL and keep keys out of fixtures. Integration evidence: [`jev_core.py`](https://github.com/gbesse/redpanda-connect-jev/blob/0f427f233a635f83605786423a0b972fba710e7e/jev_core.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
# follow README to drop the processor into a Connect pipeline
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/redpanda-connect-jev/blob/0f427f233a635f83605786423a0b972fba710e7e/README.md](https://github.com/gbesse/redpanda-connect-jev/blob/0f427f233a635f83605786423a0b972fba710e7e/README.md)

## Limits and data handling

Pipeline payloads you send for judgment go to TypeSafe on live runs.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 0f427f233a63](https://github.com/gbesse/redpanda-connect-jev/tree/0f427f233a635f83605786423a0b972fba710e7e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
