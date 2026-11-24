# LangChain Jev tool calling by LBKE (demo code where Jev picks the tool and a small LLM fills in the arguments, companion to a French article)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Companion code to LBKE's French article on tool calling with Jev. Jev chooses which tool to call (including parallel calls) and a small LLM only generates the arguments; a shovel demo compares this with letting an LLM do both.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lbke/langchain-jev-tool-calling) |
| Maintainer | [lbke](https://github.com/lbke). Independently curated. |
| Format | Python scripts (uv) with LangChain |
| Requirements | Python with uv; an OpenRouter key (the code calls `typesafe/jev-1.13` through OpenRouter) and an LLM key for argument generation. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_langchain_middleware.py`](https://github.com/lbke/langchain-jev-tool-calling/blob/c20f6a5b079718e65243f914f9f2e3ca734c4dbc/jev_langchain_middleware.py) at the pinned commit. |

## When to use

- See a minimal pattern for splitting tool selection (Jev) from argument generation (LLM) in LangChain.
- Mismatch: a finished agent framework; the README lists evaluation and a full agent loop as next steps.

## How it works

`jev_langchain_middleware.py` and `shovel_demo.py` send the conversation and tool list to `typesafe/jev-1.13` through OpenRouter as a Choice; the TypeSafe SDK path is present but commented out. Integration evidence: [`jev_langchain_middleware.py`](https://github.com/lbke/langchain-jev-tool-calling/blob/c20f6a5b079718e65243f914f9f2e3ca734c4dbc/jev_langchain_middleware.py).

## Get started

Clone, sync dependencies, set your keys, and run the demos.

```sh
git clone https://github.com/lbke/langchain-jev-tool-calling.git && cd langchain-jev-tool-calling
uv sync
uv run shovel_demo.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Article (French): [www.lbke.fr/formations/ressources/ia/jev-sytem-one-tool-calling](https://www.lbke.fr/formations/ressources/ia/jev-sytem-one-tool-calling)
- Parallel tool calling demo: [github.com/lbke/langchain-jev-tool-calling/blob/c20f6a5b079718e65243f914f9f2e3ca734c4dbc/jev_tool_calling.py](https://github.com/lbke/langchain-jev-tool-calling/blob/c20f6a5b079718e65243f914f9f2e3ca734c4dbc/jev_tool_calling.py)

## Limits and data handling

Reaches Jev through OpenRouter, not TypeSafe directly. Prompts go to OpenRouter/TypeSafe and the LLM provider. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit c20f6a5b0797](https://github.com/lbke/langchain-jev-tool-calling/tree/c20f6a5b079718e65243f914f9f2e3ca734c4dbc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
