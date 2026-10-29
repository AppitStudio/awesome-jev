# Jev for Marketers (free guide, Claude skill and recipes for marketing-ops decisions with Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Free, hands-on guide to using Jev for the small yes/no calls in marketing ops (route this lead, tag this asset, is this reply interested), plus a Claude skill with four editable recipes (lead routing, reply triage, on-message check, asset tagging), a no-install batch script that runs a recipe over a CSV, and a 50-lead sample with an answer key for scoring.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brent-phillips/jev-for-marketers) |
| Maintainer | [brent-phillips](https://github.com/brent-phillips). Independently curated. |
| Format | Guide, Claude skill and Python scripts |
| Requirements | Python 3 and a TypeSafe API key (or Jev through Vercel AI Gateway). |
| License | [MIT](https://github.com/brent-phillips/jev-for-marketers/blob/9608d87b56ef9589779b89dfaf08f6d75e44da69/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-marketing-decisions/scripts/jev_batch.py`](https://github.com/brent-phillips/jev-for-marketers/blob/9608d87b56ef9589779b89dfaf08f6d75e44da69/jev-marketing-decisions/scripts/jev_batch.py) at the pinned commit. |

## When to use

- Replace a large LLM for routine lead, reply and asset decisions in marketing ops.
- Mismatch: recipes are starting points to adapt to your ICP and messaging.

## How it works

`jev_batch.py` posts each CSV row with the recipe's questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default, with a `--dry-run` mode), and `score_results.py` grades the output against an answer key. Integration evidence: [`jev-marketing-decisions/scripts/jev_batch.py`](https://github.com/brent-phillips/jev-for-marketers/blob/9608d87b56ef9589779b89dfaf08f6d75e44da69/jev-marketing-decisions/scripts/jev_batch.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/brent-phillips/jev-for-marketers && cd jev-for-marketers
export TYPESAFE_API_KEY=...
python3 jev-marketing-decisions/scripts/jev_batch.py jev-marketing-decisions/recipes/lead-routing.json examples/sample-leads.csv --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README walkthrough: [github.com/brent-phillips/jev-for-marketers#readme](https://github.com/brent-phillips/jev-for-marketers#readme)
- Question design notes: [github.com/brent-phillips/jev-for-marketers/blob/main/jev-marketing-decisions/references/question-design.md](https://github.com/brent-phillips/jev-for-marketers/blob/main/jev-marketing-decisions/references/question-design.md)

## Limits and data handling

Lead and reply text in your CSV goes to TypeSafe in live runs. Sample data is made up.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 9608d87b56ef](https://github.com/brent-phillips/jev-for-marketers/tree/9608d87b56ef9589779b89dfaf08f6d75e44da69). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
