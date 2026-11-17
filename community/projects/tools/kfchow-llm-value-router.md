# kfchow-llm-value-router by KFChow AI Lab (Hermes Agent plugin where Jev picks the cheapest good-enough model for each turn)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin that routes each turn to the cheapest model good enough for it and can escalate hard turns to a premium rung. On the first provider call of a turn it asks Jev whether the turn is routine or needs a strong model, with confidence, and reapplies that decision to the turn's later calls and retries. The model rungs are resolved from the author's value leaderboard (kfchow.com/llm), not hardcoded. Ships in shadow mode (logs decisions only) until you switch it to live, and fails open so a failed check leaves the request byte-identical. Also ships the rung resolver as a standalone Hermes skill.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kfchow-ai/kfchow-llm-value-router) |
| Maintainer | [kfchow-ai](https://github.com/kfchow-ai). Independently curated. |
| Format | Hermes Agent plugin and skill (Python standard library, MIT) |
| Requirements | Hermes Agent; `JEVI_API_KEY` with a TypeSafe key for the classifier (omit it to run resolver-only). |
| License | [MIT](https://github.com/kfchow-ai/kfchow-llm-value-router/blob/dd5315479ac26436bd9840d77a432675fada559a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/KFChowAI/status/2122556775476117766)). |
| Jev evidence | [`scripts/jev_client.py`](https://github.com/kfchow-ai/kfchow-llm-value-router/blob/dd5315479ac26436bd9840d77a432675fada559a/scripts/jev_client.py) at the pinned commit. |

## When to use

- Cut a Hermes agent's model spend by sending routine turns to cheaper models, after checking shadow-mode logs.
- Mismatch: harnesses other than Hermes Agent.

## How it works

`scripts/jev_client.py` is a dependency-free client that posts `{state, model, questions}` to `https://api.typesafe.ai/v1/systemone`, chunks large choice sets, retries only on 429/529/network errors and meters cost from provider-counted tokens. Integration evidence: [`scripts/jev_client.py`](https://github.com/kfchow-ai/kfchow-llm-value-router/blob/dd5315479ac26436bd9840d77a432675fada559a/scripts/jev_client.py).

## Get started

Install the plugin from the repo, set the key, and copy the example config; it starts in shadow mode.

```sh
git clone https://github.com/kfchow-ai/kfchow-llm-value-router.git
hermes plugins install ./kfchow-llm-value-router
export JEVI_API_KEY=...   # TypeSafe key; omit for resolver-only
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kfchow-ai/kfchow-llm-value-router/blob/dd5315479ac26436bd9840d77a432675fada559a/README.md](https://github.com/kfchow-ai/kfchow-llm-value-router/blob/dd5315479ac26436bd9840d77a432675fada559a/README.md)

## Limits and data handling

A short summary of each turn goes to TypeSafe on your key. Model choices depend on the author's own leaderboard; savings are not independently measured.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit dd5315479ac2](https://github.com/kfchow-ai/kfchow-llm-value-router/tree/dd5315479ac26436bd9840d77a432675fada559a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
