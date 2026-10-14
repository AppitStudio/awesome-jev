# jes

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source guardrails for AI agents that ask Jev to judge prompts, retrieved content, tool calls and responses for prompt injection, jailbreaks and secret/PII leaks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/everafterlabs/jes) |
| Maintainer | [everafterlabs](https://github.com/everafterlabs). Independently curated. |
| Format | Python library, CLI and agent hooks (PyPI `jes`) |
| Requirements | Python 3.11+, TypeSafe API key. |
| License | [Apache-2.0](https://github.com/everafterlabs/jes/blob/d65630a285c593b3f01840de55df362f4197bcb8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jes/backend.py`](https://github.com/everafterlabs/jes/blob/d65630a285c593b3f01840de55df362f4197bcb8/src/jes/backend.py) at the pinned commit. |

## When to use

- Put a decision-model check in front of each agent step (prompt, retrieved page, tool call, response).
- Block or flag secret and PII leaks without asking a generative model to grade itself.
- Mismatch: a guardrail layer, not a full agent framework.

## How it works

jes turns each checkpoint into typed questions that Jev answers with probabilities; the guard compares them against configured thresholds and blocks, warns or allows. Agent hook commands wire it into coding agents and read the key from `TYPESAFE_API_KEY`. Integration evidence: [`src/jes/backend.py`](https://github.com/everafterlabs/jes/blob/d65630a285c593b3f01840de55df362f4197bcb8/src/jes/backend.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install jes
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs and cookbook: [docs.getjes.dev](https://docs.getjes.dev)
- Project site: [getjes.dev](https://getjes.dev)

## Limits and data handling

Checked text (prompts, retrieved content, tool arguments, responses) is sent to TypeSafe for each judgment; calls are billed to your key. Thresholds are yours to tune.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit d65630a285c5](https://github.com/everafterlabs/jes/tree/d65630a285c593b3f01840de55df362f4197bcb8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
