# kblam by hungryboygeorge (flat-file knowledge base for research agents where Jev checks whether a new finding restates, extends or contradicts older ones)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Knowledge base for LLM research and coding agents, mainly through Claude Code hooks: each finding is a Markdown file with YAML front matter holding one claim with its evidence and scope. Before a write, heuristics and BM25 or Ollama embeddings find similar findings, and Jev judges whether the new claim restates, extends or contradicts each one, so duplicates and silent revisions are rejected or sent to review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hungryboygeorge/kblam) |
| Maintainer | [hungryboygeorge](https://github.com/hungryboygeorge). Independently curated. |
| Format | Python CLI with Claude Code and Git hooks (uv) |
| Requirements | Python 3.11+ and uv; an OpenRouter key for the Jev check; Ollama optional for embeddings. |
| License | [VibeCoded AI-Slop License v1.0 (custom permissive terms)](https://github.com/hungryboygeorge/kblam/blob/abd7a558a8f90bc6d8bee6fb9bc51ceb061e9306/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/kblam/jev.py`](https://github.com/hungryboygeorge/kblam/blob/abd7a558a8f90bc6d8bee6fb9bc51ceb061e9306/src/kblam/jev.py) at the pinned commit. |

## When to use

- Stop research agents from piling up duplicate or contradictory findings files.
- Mismatch: if you need audited software; the author says it was written entirely by LLMs and may not be maintained.

## How it works

`src/kblam/jev.py` calls Jev through the official `typesafe_sdk` pointed at OpenRouter (`https://openrouter.ai/api/v1/systemone`) and `jev_prompts.py` holds the claim-pair questions; `kblam check`, `kblam put` and `kblam cost` run and track the checks. Integration evidence: [`src/kblam/jev.py`](https://github.com/hungryboygeorge/kblam/blob/abd7a558a8f90bc6d8bee6fb9bc51ceb061e9306/src/kblam/jev.py).

## Get started

Install with uv, add your OpenRouter key, and initialise a knowledge base inside a git repository.

```sh
uv tool install git+https://github.com/hungryboygeorge/kblam
# put your OpenRouter key in OPENROUTER_API_KEY, then inside a git repo:
kblam init
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Spec: [github.com/hungryboygeorge/kblam/blob/abd7a558a8f90bc6d8bee6fb9bc51ceb061e9306/SPEC.md](https://github.com/hungryboygeorge/kblam/blob/abd7a558a8f90bc6d8bee6fb9bc51ceb061e9306/SPEC.md)

## Limits and data handling

Licensed under the custom 'VibeCoded AI-Slop License v1.0', which grants broad permission but is not an OSI licence. The README states the code was written by LLMs, nobody fully understands it and it may have security problems. Claims go to OpenRouter (a third-party host) for the Jev check.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit abd7a558a8f9](https://github.com/hungryboygeorge/kblam/tree/abd7a558a8f90bc6d8bee6fb9bc51ceb061e9306). Inspected the README, LICENSE and the Jev client at the pinned commit; the tool was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
