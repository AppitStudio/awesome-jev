# jev-navigator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python code-navigation library and `jvn` CLI for agents: a model-free index (definitions, callers, references, imports, git history) plus small typed Jev judgments — check, pick, score — composed into searches like “find the code this sentence describes”.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ajbmachon/jev-navigator) |
| Maintainer | [ajbmachon](https://github.com/ajbmachon). Independently curated. |
| Format | Python library + CLI + agent skill (install from Git; not on PyPI at review) |
| Requirements | Python 3.11+, `ast-grep`, `rg`, `git`; `TYPESAFE_API_KEY` with the `typesafe` extra for live judgments. |
| License | [MIT](https://github.com/ajbmachon/jev-navigator/blob/36033db5fe93d8d7a02b3d3e6f38a86f3fd6d9c3/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give an agent a find/trace tool that returns evidence and probabilities instead of free-text guesses.
- Use the model-free index layer alone for definitions, callers and references in a narrowed file set.
- Mismatch: it finds code; judging code quality is a layer you build on top (see docs/extending.md).

## How it works

Layer one is a deterministic index; layer two wraps Jev questions (via [`adapters/typesafe.py`](https://github.com/ajbmachon/jev-navigator/blob/36033db5fe93d8d7a02b3d3e6f38a86f3fd6d9c3/src/jev_navigator/adapters/typesafe.py)) as building blocks that return raw probabilities; layer three composes both into searches. An optional `LlmStep` adds an LLM call to your own function. The [JVN skill](https://github.com/ajbmachon/jev-navigator/blob/36033db5fe93d8d7a02b3d3e6f38a86f3fd6d9c3/skills/jvn/SKILL.md) teaches agents to use it.

## Get started

Install the CLI with uv:

```sh
uv tool install "jev-navigator[typesafe] @ git+https://github.com/ajbmachon/jev-navigator"
export TYPESAFE_API_KEY=...
jvn --help
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [JVN agent skill](https://github.com/ajbmachon/jev-navigator/blob/36033db5fe93d8d7a02b3d3e6f38a86f3fd6d9c3/skills/jvn/SKILL.md) and [docs/extending.md](https://github.com/ajbmachon/jev-navigator/blob/36033db5fe93d8d7a02b3d3e6f38a86f3fd6d9c3/docs/extending.md).
- Offline test suite (runs without a key, per README).

## Limits and data handling

Code excerpts from the narrowed file set are sent to TypeSafe for live judgments. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 36033db5fe93](https://github.com/ajbmachon/jev-navigator/tree/36033db5fe93d8d7a02b3d3e6f38a86f3fd6d9c3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
