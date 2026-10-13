# dsh-jev (iptton-ai)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin (Chinese docs) registering `jev_evaluate` for mixed Noul/Choice/Score questions over text or JSON with TypeSafe Jev—distinct from [dsh-jev](dsh-jev.md) by noetion and other dsh-jev* plugins.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iptton-ai/dsh-jev) |
| Maintainer | [iptton-ai](https://github.com/iptton-ai). Independently curated. |
| Format | DeepSeek Harness bundle plugin |
| Requirements | DSH 0.2.0-rc.2+; Node.js 22; TypeSafe key. |
| License | [MIT](https://github.com/iptton-ai/dsh-jev/blob/875a3ad86332fd59765f1028c2abe51ccb896ac3/LICENSE) |
| Jev evidence | [`lib/client.js`](https://github.com/iptton-ai/dsh-jev/blob/875a3ad86332fd59765f1028c2abe51ccb896ac3/lib/client.js) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Give DSH agents one tool for structured yes/no, choice and score judgments with probabilities.
- Mismatch: overlaps several other DSH Jev plugins; docs in Chinese.

## How it works

The plugin calls the TypeSafe HTTP API directly and returns raw answers, distributions, confidence and token usage to the agent. (Summarized from the upstream [README](https://github.com/iptton-ai/dsh-jev/blob/875a3ad86332fd59765f1028c2abe51ccb896ac3/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the bundle URL in DSH's plugin manager (or link a local clone) and set the key.

## Limits and data handling

Evaluated text/JSON goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 875a3ad86332](https://github.com/iptton-ai/dsh-jev/tree/875a3ad86332fd59765f1028c2abe51ccb896ac3). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
