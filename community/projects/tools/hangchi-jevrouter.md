# JevRouter by HangChi (agent runtime where the LLM understands, Jev routes with probabilities, and a policy engine decides what may run)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python agent runtime (README in Chinese) that splits each step across three roles: an LLM understands the goal and fills tool parameters, Jev answers four typed routing questions over the candidate actions (choice, risk, needs confirmation, done), and a local policy engine decides whether to execute, ask a human, or hand back to the LLM. Model output never grants execution rights.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HangChi/JevRouter) |
| Maintainer | [HangChi](https://github.com/HangChi). Independently curated. |
| Format | Python service (FastAPI) + library |
| Requirements | Python with `uv`; a TypeSafe key and an LLM provider key. |
| License | [MIT](https://github.com/HangChi/JevRouter/blob/ed96ed276273fdbcb397799285ab07a90d8d72fa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_router/clients/jev.py`](https://github.com/HangChi/JevRouter/blob/ed96ed276273fdbcb397799285ab07a90d8d72fa/jev_router/clients/jev.py) at the pinned commit. |

## When to use

- Gate tool calls in an agent by risk class and Jev probabilities.
- Mismatch: research-grade runtime; the README is in Chinese.

## How it works

`jev_router/clients/jev.py` posts routing questions to `https://api.typesafe.ai` and returns probabilities; the policy engine executes read tools within thresholds, sends write/external tools or low-confidence steps to human confirmation, and a verifier checks completion probability before stopping. Integration evidence: [`jev_router/clients/jev.py`](https://github.com/HangChi/JevRouter/blob/ed96ed276273fdbcb397799285ab07a90d8d72fa/jev_router/clients/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/HangChi/JevRouter.git && cd JevRouter
uv sync --all-groups
uv run --env-file .env uvicorn apps.api.app:create_app --factory --port 8000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/HangChi/JevRouter#readme](https://github.com/HangChi/JevRouter#readme)

## Limits and data handling

Goals and candidate actions are sent to TypeSafe and the configured LLM. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit ed96ed276273](https://github.com/HangChi/JevRouter/tree/ed96ed276273fdbcb397799285ab07a90d8d72fa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
