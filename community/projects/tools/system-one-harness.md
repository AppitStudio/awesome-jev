# System One Harness

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reproducible pilot repository that tests whether cheap System One decision models (TypeSafe Jev, OpenAI Decisions, GLiNER, Laya) can gate an expensive reasoning LLM on HTTP response triage without dropping important anomalies—synthetic data and committed outputs, one-command reproduce.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mev0lent/system-one-harness) |
| Maintainer | [mev0lent](https://github.com/mev0lent). Independently curated. |
| Format | JavaScript · experiment harness |
| Requirements | Node toolchain; provider keys when re-running live legs. |
| License | [MIT](https://github.com/mev0lent/system-one-harness/blob/8af7061ece7790033d151378aac0d1989d4f33cd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Reproduce published System One vs LLM gating numbers before adopting the pattern.
- Mismatch: Synthetic HTTP corpus—not your production traffic.

## How it works

Scripts run each decision model over fixtures and compare escalations to a reasoning baseline; Jev results committed under `results/`. Evidence: [`results/jev_test.json`](https://github.com/mev0lent/system-one-harness/blob/8af7061ece7790033d151378aac0d1989d4f33cd/results/jev_test.json).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/mev0lent/system-one-harness.git
cd system-one-harness
# npm install && reproduce per README
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 8af7061ece77](https://github.com/mev0lent/system-one-harness/tree/8af7061ece7790033d151378aac0d1989d4f33cd). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
