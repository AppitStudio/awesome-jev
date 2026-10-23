# Jev IDS

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev IDS is a network intrusion detection experiment that shows Jev one network flow plus a few labeled examples and gets back whether the flow is an attack and which kind, benchmarked on NSL-KDD against an LLM, a Random Forest and an Isolation Forest.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jev-sec/jev-ids) |
| Maintainer | [jev-sec](https://github.com/jev-sec). Independently curated. |
| Format | Python benchmark and detector CLI |
| Requirements | Python 3.13+; a TypeSafe API key; the NSL-KDD dataset. |
| License | [MIT](https://github.com/jev-sec/jev-ids/blob/6aa5ac4570db1d6d9b88f769f7d16c1cd2c3784a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Evaluate few-shot typed decisions for security flow classification against classic baselines.
- Mismatch: a research benchmark, not a production IDS; speed, cost and accuracy figures are the maintainer's own results.

## How it works

Each flow is serialized as state with a handful of labeled examples per category; Jev answers attack yes/no and attack-type choice questions, and the harness scores results across seeds and example counts. (Summarized from the upstream [README](https://github.com/jev-sec/jev-ids/blob/6aa5ac4570db1d6d9b88f769f7d16c1cd2c3784a/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Clone the repository, install the Python package, set your TypeSafe key, and run the detector over NSL-KDD as described.

## Limits and data handling

Flow features are sent to the TypeSafe API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 6aa5ac4570db](https://github.com/jev-sec/jev-ids/tree/6aa5ac4570db1d6d9b88f769f7d16c1cd2c3784a). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Jev in-context casebooks: test examples before you trust them](../../knowledge-base/articles/jev-in-context-casebooks.md) — Independently suggested by JevList; not an endorsement by David Bressler. See a harness that varies the number of labelled examples in Jev's state and compares against trained baselines.
<!-- knowledge:backlinks:end -->
