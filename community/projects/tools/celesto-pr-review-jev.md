# Celesto PR review with Jev (secure agent computer example comparing an LLM and TypeSafe Jev as PR-finding evaluators)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Example in CelestoAI's secure, persistent computer-for-agents repo: a PR reviewer whose candidate findings are evaluated by both an LLM and TypeSafe Jev (via Vercel AI Gateway or direct TypeSafe).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CelestoAI/celesto) |
| Maintainer | [CelestoAI](https://github.com/CelestoAI). Independently curated. |
| Format | Python example + Node helper (Apache-2.0) |
| Requirements | Python 3.12+, uv, Celesto (local or cloud), model credentials and either `AI_GATEWAY_API_KEY` or `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/CelestoAI/celesto/blob/28599cba3f96d7ef36071833b9874d8e319b277a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/pr-review-jev/config.py`](https://github.com/CelestoAI/celesto/blob/28599cba3f96d7ef36071833b9874d8e319b277a/examples/pr-review-jev/config.py) at the pinned commit. |

## When to use

- Filter noisy PR-review findings with typed Jev questions.
- Compare LLM and Jev evaluators side by side.
- Mismatch: needs a Celesto sandbox.

## How it works

Each candidate finding gets three questions (introduced by the PR, supported by evidence, actionable); `config.py` selects gateway or direct TypeSafe (`jev-latest`) and `gateway-evaluate.mjs` calls `typesafe-ai/jev` through AI SDK evaluation. Integration evidence: [`examples/pr-review-jev/config.py`](https://github.com/CelestoAI/celesto/blob/28599cba3f96d7ef36071833b9874d8e319b277a/examples/pr-review-jev/config.py).

## Get started

Open `examples/pr-review-jev`, follow its README, and run the reviewer against a PR.

```sh
git clone https://github.com/CelestoAI/celesto.git && cd celesto
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example README: [github.com/CelestoAI/celesto/blob/28599cba3f96d7ef36071833b9874d8e319b277a/examples/pr-review-jev/README.md](https://github.com/CelestoAI/celesto/blob/28599cba3f96d7ef36071833b9874d8e319b277a/examples/pr-review-jev/README.md)

## Limits and data handling

PR diffs and findings go to your model provider and to Jev (gateway or TypeSafe).

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 28599cba3f96](https://github.com/CelestoAI/celesto/tree/28599cba3f96d7ef36071833b9874d8e319b277a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
