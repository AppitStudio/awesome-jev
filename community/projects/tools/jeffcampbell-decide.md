# decide (jeffcampbell)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Dependency-free Python 3.11+ CLI and library that asks System One models — hosted TypeSafe Jev by default, or `clef-flash` locally in Ollama — typed yes/no, choice and score questions about files and text; `decide triage` tells a coding agent which files are worth reading before they enter its context. Distinct from the listed *decide (vsekhar)*.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jeffcampbell/Decide) |
| Maintainer | [jeffcampbell](https://github.com/jeffcampbell). Independently curated. |
| Format | Python package with `decide` CLI (install from GitHub) |
| Requirements | Python 3.11+; `TYPESAFE_API_KEY` for Jev (get keys at console.typesafe.ai), or Ollama with `clef-flash` for local runs. |
| License | [MIT](https://github.com/jeffcampbell/Decide/blob/16c7c7fc2e2674dd880b996563df80ebf928c4e2/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Pre-filter files for an agent so irrelevant ones never enter its context window.
- Send cheap classification decisions from an agent framework and save LLM calls for unsure cases.
- Mismatch: file contents are sent to the chosen backend.

## How it works

[`src/decide/config.py`](https://github.com/jeffcampbell/Decide/blob/16c7c7fc2e2674dd880b996563df80ebf928c4e2/src/decide/config.py) defines the Jev backend (`https://api.typesafe.ai/v1/systemone`, `jev-latest`) and an Ollama backend; [`src/decide/commands/triage.py`](https://github.com/jeffcampbell/Decide/blob/16c7c7fc2e2674dd880b996563df80ebf928c4e2/src/decide/commands/triage.py) chunks files and asks relevance questions, with a local cache.

## Get started

Install from GitHub (README *Install*):

```sh
pip install git+https://github.com/jeffcampbell/Decide.git
export TYPESAFE_API_KEY=...
decide --help
```

Jev calls are billed to your TypeSafe key; the Ollama backend is local.

## Examples and demos

- README *`decide triage`* and *Using it from a coding agent*; [Yamanote](https://github.com/jeffcampbell/yamanote) uses it as a library.

## Limits and data handling

File text goes to TypeSafe (or stays local with Ollama); README section *What gets sent, and what never does* documents boundaries. The README's API-key link points to a third-party site (jevtypesafeai.com); TypeSafe's own console is console.typesafe.ai. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 16c7c7fc2e26](https://github.com/jeffcampbell/Decide/tree/16c7c7fc2e2674dd880b996563df80ebf928c4e2). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
