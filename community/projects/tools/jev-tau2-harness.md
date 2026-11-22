# jev-tau2-harness by Sai Vamshi Atukuri (replication code for typed Jev decisions beside the LLM on τ²-Bench Airline)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and all 16 saved runs for the preprint "System-1 Orchestration for Enterprise Conversational Agents". One Jev call per customer turn runs in parallel with the agent's LLM and decides whether a tool is needed, which reservation the turn is about, whether the customer confirmed a write and the route and date of a search; code then issues the tool calls and checks every write against airline policy. Every table and figure can be regenerated offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vamshibobby/jev-tau2-harness) |
| Maintainer | [vamshibobby](https://github.com/vamshibobby). Independently curated. |
| Format | Python research harness + saved runs |
| Requirements | Python 3.12 or 3.13 (`tau2-bench` pinned in requirements). New runs also need `OPENROUTER_API_KEY` for Jev, Vertex AI or Gemini API credentials and τ²'s airline data. |
| License | [MIT](https://github.com/vamshibobby/jev-tau2-harness/blob/fa197134d919ee62f5afedb705f3c554b9a9ab04/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/vamshibobby/jev-tau2-harness/blob/fa197134d919ee62f5afedb705f3c554b9a9ab04/jev.py) at the pinned commit. |

## When to use

- Study or reproduce a measured design for putting typed decisions beside a tool-calling agent.
- Mismatch: a drop-in agent framework; the harness is specific to τ²-Bench Airline.

## How it works

`jev.py` defines every question the harness asks (Table 1 of the paper) and calls Jev through OpenRouter's decisions endpoint (`~typesafe/jev-latest`); `agents.py` holds the model-only baseline and the Jev harness, and `policy.py` the write gate. Integration evidence: [`jev.py`](https://github.com/vamshibobby/jev-tau2-harness/blob/fa197134d919ee62f5afedb705f3c554b9a9ab04/jev.py).

## Get started

Install the requirements and regenerate the paper's tables and figures from the saved runs, with no API keys.

```sh
git clone https://github.com/vamshibobby/jev-tau2-harness && cd jev-tau2-harness
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python reproduce_tables.py   # offline, free
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How one turn works: [github.com/vamshibobby/jev-tau2-harness/blob/fa197134d919ee62f5afedb705f3c554b9a9ab04/docs/HOW_IT_WORKS.md](https://github.com/vamshibobby/jev-tau2-harness/blob/fa197134d919ee62f5afedb705f3c554b9a9ab04/docs/HOW_IT_WORKS.md)
- Saved runs: [github.com/vamshibobby/jev-tau2-harness/tree/fa197134d919ee62f5afedb705f3c554b9a9ab04/results](https://github.com/vamshibobby/jev-tau2-harness/tree/fa197134d919ee62f5afedb705f3c554b9a9ab04/results)

## Limits and data handling

Reported results are the author's (preprint; DOI to be added): on 50 tasks × 4 trials, code issued 77–84% of tool calls, pass^4 rose 10.7 points on average and policy-forbidden writes fell from 43 to 10 conversations. Jev was called between 30 September and 6 October 2026, so new runs may differ. New runs send conversation state to OpenRouter/TypeSafe and Google.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit fa197134d919](https://github.com/vamshibobby/jev-tau2-harness/tree/fa197134d919ee62f5afedb705f3c554b9a9ab04). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
