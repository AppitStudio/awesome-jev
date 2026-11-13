# Smart Question Router (small demo where Jev classifies a neuroscience question and Python rules pick the expert prompt)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Streamlit playground for a simple pattern: Jev returns a brain-region category and confidence for each scientific question, deterministic Python rules choose a route (asking for clarification below 0.70 or for mixed and out-of-scope questions), and one OpenAI model answers with the chosen region's prompt; includes a 28-question evaluation set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suvrazastrovision/question_router) |
| Maintainer | [suvrazastrovision](https://github.com/suvrazastrovision). Independently curated. |
| Format | Streamlit demo (Python with uv, MIT) |
| Requirements | Python 3.12+, uv, a TypeSafe key and an OpenAI key. |
| License | [MIT](https://github.com/suvrazastrovision/question_router/blob/2219915886fd614ff846c8823a1f7d682242505f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`classifier.py`](https://github.com/suvrazastrovision/question_router/blob/2219915886fd614ff846c8823a1f7d682242505f/classifier.py) at the pinned commit. |

## When to use

- See the 'Jev judges, code decides' routing pattern in a small, readable codebase.
- Mismatch: real scientific advice; it is the author's learning experiment.

## How it works

`classifier.py` uses the TypeSafe Python SDK with `jev-1.14.0` by default; the module docstring states Jev judges the domain while code decides the route. `evaluate.py` runs 28 billable Jev calls; the unit tests run offline. Integration evidence: [`classifier.py`](https://github.com/suvrazastrovision/question_router/blob/2219915886fd614ff846c8823a1f7d682242505f/classifier.py).

## Get started

Sync dependencies, add both keys to `.env` and start the app.

```sh
uv sync --locked
cp .env.example .env   # TYPESAFE_API_KEY, OPENAI_API_KEY
uv run --locked streamlit run app.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/suvrazastrovision/question_router/blob/2219915886fd614ff846c8823a1f7d682242505f/README.md](https://github.com/suvrazastrovision/question_router/blob/2219915886fd614ff846c8823a1f7d682242505f/README.md)
- Evaluation results: [github.com/suvrazastrovision/question_router/blob/2219915886fd614ff846c8823a1f7d682242505f/evaluation-results.json](https://github.com/suvrazastrovision/question_router/blob/2219915886fd614ff846c8823a1f7d682242505f/evaluation-results.json)

## Limits and data handling

Your questions go to TypeSafe and OpenAI on your keys.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 2219915886fd](https://github.com/suvrazastrovision/question_router/tree/2219915886fd614ff846c8823a1f7d682242505f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
