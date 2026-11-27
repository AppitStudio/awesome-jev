# Memworthy by Afnan Hussain (Python library where Jev decides which agent memories to store, update, reject or send for review)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Python library that sits between whatever proposes agent memories and the memory store. Each candidate goes through code checks, one batch of typed Jev questions and an editable YAML policy that picks store, update, merge, supersede, reject, review, redact or store_labeled, so trips are not saved as home addresses and retractions roll back. Every decision lands in an auditable ledger that can be replayed under a changed policy. Includes a Mem0 wrapper and a CLI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AfnanHussain10/Memworthy) |
| Maintainer | [Afnan Hussain](https://github.com/AfnanHussain10) (AfnanHussain10). Independently curated. |
| Format | Python library + CLI (PyPI `memworthy`) |
| Requirements | Python 3.10+, `pip install "memworthy[jev]"` and a TypeSafe key for live judging; recorded answers let you run the bundled templates without a key. |
| License | [Apache-2.0](https://github.com/AfnanHussain10/Memworthy/blob/094edac26ecd17d689bf95dd0588c41b51cc5354/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/memworthy/judges/jev.py`](https://github.com/AfnanHussain10/Memworthy/blob/094edac26ecd17d689bf95dd0588c41b51cc5354/src/memworthy/judges/jev.py) at the pinned commit. |

## When to use

- Agent builders whose memory store fills up with temporary states, guesses or other people's facts and who want an auditable gate before writing.
- Mismatch: a retrieval or vector store; Memworthy only decides what gets written.

## How it works

`src/memworthy/judges/jev.py` is the default judge: it posts one System One request per candidate to `https://api.typesafe.ai/v1` (`jev-1.13.0` by default) and the policy engine applies ordered rules to the returned probabilities. OpenAI Decisions, Microsoft-Decision-1 on Foundry or your own System One-compatible provider can be swapped in; the author notes their probabilities are on a different scale. Integration evidence: [`src/memworthy/judges/jev.py`](https://github.com/AfnanHussain10/Memworthy/blob/094edac26ecd17d689bf95dd0588c41b51cc5354/src/memworthy/judges/jev.py).

## Get started

Install with the Jev extra and gate a few messages, or replay the bundled recorded answers without a key.

```sh
pip install "memworthy[jev]"
export TYPESAFE_API_KEY=...
memworthy test personal-memory --judge recorded   # offline
memworthy run personal-memory chat.json --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Policy templates: [github.com/AfnanHussain10/Memworthy/tree/main/src/memworthy/templates](https://github.com/AfnanHussain10/Memworthy/tree/main/src/memworthy/templates)
- Evaluation: [github.com/AfnanHussain10/Memworthy/tree/main/eval](https://github.com/AfnanHussain10/Memworthy/tree/main/eval)

## Limits and data handling

Candidate text and nearby context go to the configured judge (TypeSafe by default). Template thresholds were tuned on Jev; re-run `memworthy eval` before trusting them with another provider. Sensitive items (health, finances, precise location) are routed to review, not auto-stored.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 094edac26ecd](https://github.com/AfnanHussain10/Memworthy/tree/094edac26ecd17d689bf95dd0588c41b51cc5354). Inspected the README, LICENSE, `src/memworthy/judges/jev.py` and `systemone.py` at the pinned commit and confirmed the `memworthy` package (0.3.0) on PyPI; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
