# jev-ai-use-cases (atliq)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hands-on LangChain notebook of TypeSafe Jev patterns: support triage, model routing, reply guardrails, tool selection, and finance-inbox fraud checks—“an LLM writes; Jev decides.”

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atliq/jev-ai-use-cases) |
| Maintainer | [atliq](https://github.com/atliq). Independently curated. |
| Format | Jupyter notebook (`jev_decision_guide.ipynb`) + Colab badge. |
| Requirements | `langchain-typesafe[experimental]`, `langchain-groq`, `python-dotenv`, `pandas`; `OPENROUTER_API_KEY` (Jev via OpenRouter) and `GROQ_API_KEY`. |
| License | [MIT](https://github.com/atliq/jev-ai-use-cases/blob/f8ebee950a1f919b7d7d7c171686e5a42aa8f04d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Notebook cells / live provider calls not executed. `langchain-typesafe` noted as early alpha upstream. |

## When to use

Use as a **teaching cookbook** for LangChain + Jev decision middleware. Prefer [langchain-jev-tutorial](https://github.com/PromptEngineer48/langchain-jev-tutorial) style step scripts when you want a multi-file agent walkthrough (if listed) or official TypeSafe LangChain docs for API reference.

## How it works

The notebook walks through triage, routing, guardrails, tool selection, and finance checks using typed Jev answers with probabilities instead of free-form classification text (per README).

## Get started

```sh
git clone https://github.com/atliq/jev-ai-use-cases.git
cd jev-ai-use-cases
git checkout f8ebee950a1f919b7d7d7c171686e5a42aa8f04d
pip install "langchain-typesafe[experimental]" langchain-groq python-dotenv pandas
# Create .env with OPENROUTER_API_KEY and GROQ_API_KEY
# Open jev_decision_guide.ipynb
```

Colab: [open notebook](https://colab.research.google.com/github/atliq/jev-ai-use-cases/blob/main/jev_decision_guide.ipynb).

## Examples and demos

- Committed notebook with outputs from a real upstream run (per README).

## Limits and data handling

Ticket/document text in the notebook reaches OpenRouter (Jev) and Groq (LLM). Experimental middleware APIs may change.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit f8ebee9](https://github.com/atliq/jev-ai-use-cases/tree/f8ebee950a1f919b7d7d7c171686e5a42aa8f04d). AI-assisted README and LICENSE inspection; notebook not re-executed.
