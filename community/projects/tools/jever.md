# Jever

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Notebook companion to the article 'Your AI Agent Needs a Bouncer': a LangChain middleware where Jev labels each message as direct, decomposable, enrichable or needs clarification before a supervisor agent delegates to subagents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tituslhy/Jever) |
| Maintainer | [tituslhy](https://github.com/tituslhy). Independently curated. |
| Format | Python notebook (LangChain, Deep Agents, `langchain_typesafe`) |
| Requirements | Python 3.14+ and uv; OpenAI, Tavily, TypeSafe and LangSmith keys. |
| License | [MIT](https://github.com/tituslhy/Jever/blob/f85a59110e595023a0ccd644d0e405136495ab96/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`notebooks/agent.ipynb`](https://github.com/tituslhy/Jever/blob/f85a59110e595023a0ccd644d0e405136495ab96/notebooks/agent.ipynb) at the pinned commit. |

## When to use

- Add a cheap triage step in front of a supervisor agent so simple questions pass straight through.
- See how a confidence threshold (default 80%) keeps the middleware from acting on unsure labels.
- Mismatch: a learning notebook with two demo subagents, not a packaged library.

## How it works

The notebook defines a `QueryEnrichmentMiddleware` that calls `TypeSafeClassifier` from `langchain_typesafe` with four Choice labels and only splits, rewrites or asks for clarification when Jev is at least 80% confident; the supervisor is built with LangChain's `create_agent` and delegates to forex and web-search subagents. Integration evidence: [`notebooks/agent.ipynb`](https://github.com/tituslhy/Jever/blob/f85a59110e595023a0ccd644d0e405136495ab96/notebooks/agent.ipynb).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tituslhy/Jever.git
cd Jever
uv sync
cp .env.example .env   # add the four keys
uv run jupyter lab notebooks/agent.ipynb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Article: [medium.com/@tituslhy/your-ai-agent-needs-a-bouncer-f115d5ddac55](https://medium.com/@tituslhy/your-ai-agent-needs-a-bouncer-f115d5ddac55)

## Limits and data handling

Messages go to TypeSafe for triage and to OpenAI and Tavily for the agent; runs are traced in LangSmith when enabled.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit f85a59110e59](https://github.com/tituslhy/Jever/tree/f85a59110e595023a0ccd644d0e405136495ab96). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
