# jev-calibration

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reliability diagram and ECE for TypeSafe Jev on 240 hand-labelled agent tool calls (labels + scripts published).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/themsquared/jev-calibration) |
| Maintainer | [themsquared](https://github.com/themsquared). Independently curated. |
| Format | Calibration study: reliability diagram and ECE on 240 labeled agent tool calls for TypeSafe Jev. |
| Requirements | Python per upstream; published labels/responses for offline plots. |
| License | [Apache-2.0](https://github.com/themsquared/jev-calibration/blob/4c0eac17618bd77e69fc6af689839d4934454b7a/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when studying whether Jev confidence tracks accuracy. Prefer product docs for production SLOs.

## How it works

Repo publishes labels, raw responses, and plotting scripts for jev-latest/jev-preview.

## Get started

```sh
git clone https://github.com/themsquared/jev-calibration.git
cd jev-calibration
git checkout 4c0eac17618bd77e69fc6af689839d4934454b7a
# follow upstream for offline plot reproduction
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 4c0eac1](https://github.com/themsquared/jev-calibration/tree/4c0eac17618bd77e69fc6af689839d4934454b7a). AI-assisted README and license inspection; install/live paths not executed.
