# neuras (conversational agent experiment where Jev decides and an LLM writes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experiment in splitting judgment from generation: a local Ollama LLM only writes candidate notes and replies, while one Jev request per turn appraises the message (correction, worth a note, hostile, affect scores, contradictions with stored notes) and picks among candidates, keeping a persistent self file and traces with ablations to score the effect.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saembit/neuras) |
| Maintainer | [saembit](https://github.com/saembit). Independently curated. |
| Format | Python package and CLI |
| Requirements | Python with uv; Ollama with a model such as qwen2.5:7b; a TypeSafe API key. |
| License | [MIT](https://github.com/saembit/neuras/blob/3e88888f0f339fc48f8638859994d0a8a77e6726/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/neuras/jev.py`](https://github.com/saembit/neuras/blob/3e88888f0f339fc48f8638859994d0a8a77e6726/src/neuras/jev.py) at the pinned commit. |

## When to use

- Study whether a decision model keeps a chat agent consistent and less prone to inventing facts about the user.
- Run the scripted conversations with and without Jev components using ablations.
- Mismatch: research experiment; first numbers are the author's own.

## How it works

`src/neuras/jev.py` posts appraisal and selection questions to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`); the LLM is never asked to judge. Integration evidence: [`src/neuras/jev.py`](https://github.com/saembit/neuras/blob/3e88888f0f339fc48f8638859994d0a8a77e6726/src/neuras/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/saembit/neuras && cd neuras
uv venv && uv pip install -e ".[dev]"
ollama pull qwen2.5:7b
export TYPESAFE_API_KEY=...
neuras chat --show
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/saembit/neuras#readme](https://github.com/saembit/neuras#readme)

## Limits and data handling

Messages and stored notes go to TypeSafe for appraisal; generation stays on your local Ollama model. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 3e88888f0f33](https://github.com/saembit/neuras/tree/3e88888f0f339fc48f8638859994d0a8a77e6726). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
