# chat-safety (typed conversational risk assessments with a pluggable Jev adapter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Early-stage Python framework that takes content, context and a caller-owned risk registry and returns model evidence (top-N families, subfamily follow-ups, separate message/session scores). Ships a Jev OpenRouter Decisions adapter; thresholds and chat actions stay with the caller.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BahulamAI/chat-safety) |
| Maintainer | [BahulamAI](https://github.com/BahulamAI). Independently curated. |
| Format | Python package (MIT) |
| Requirements | Python and an OpenRouter/TypeSafe-compatible key for the Jev adapter. |
| License | [MIT](https://github.com/BahulamAI/chat-safety/blob/e20e34755599a2945b8be273bbb404a729393b70/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/chat_safety/adapters/jev.py`](https://github.com/BahulamAI/chat-safety/blob/e20e34755599a2945b8be273bbb404a729393b70/src/chat_safety/adapters/jev.py) at the pinned commit. |

## When to use

- Add evidence-only risk scoring to a chat product you control.
- Keep family vocabularies and thresholds outside the package.
- Mismatch: no approved production thresholds yet; privacy controls still to verify per upstream.

## How it works

`src/chat_safety/adapters/jev.py` talks to OpenRouter's Decisions API with a pinned `typesafe/jev-1.14` model and strict response parsing. Integration evidence: [`src/chat_safety/adapters/jev.py`](https://github.com/BahulamAI/chat-safety/blob/e20e34755599a2945b8be273bbb404a729393b70/src/chat_safety/adapters/jev.py).

## Get started

Install the package, load a risk registry JSON, and construct `RiskAssessor` with `JevRiskEvaluator`.

```sh
pip install -e .
# see README for RiskAssessor + JevRiskEvaluator example
export OPENROUTER_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/BahulamAI/chat-safety/blob/e20e34755599a2945b8be273bbb404a729393b70/README.md](https://github.com/BahulamAI/chat-safety/blob/e20e34755599a2945b8be273bbb404a729393b70/README.md)

## Limits and data handling

Chat content and history (bounded) are sent to the decision provider on your key. Early-stage; no durable session store shipped.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit e20e34755599](https://github.com/BahulamAI/chat-safety/tree/e20e34755599a2945b8be273bbb404a729393b70). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
