# Explore community projects

[Back to Awesome Jev](../README.md) · [Get help choosing a project](../docs/using-the-guide.md) · [Share your project](../CONTRIBUTING.md#add-a-community-project)

Browse Jev applications, developer tools, and integrations by what you want to do. Open a project page to see when it fits, how to get started, examples, and what has actually been checked. The original [README list](../README.md#community-projects) remains a quick way to reach each upstream repository.

**[Choose by the outcome you want](../docs/explore-use-cases.md)** for a guided tour with practical scenarios and guidance for a first experiment.

## Categories

- [Browser automation](#browser-automation)
- [Customer feedback and marketing](#customer-feedback-and-marketing)
- [Developer tools](#developer-tools)
- [Home automation](#home-automation)
- [SDKs and integrations](#sdks-and-integrations)
- [Search and retrieval](#search-and-retrieval)

## Browser automation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Jev Ultrafast](projects/jev-ultrafast.md) | Select browser operations and targets from the current page. | Python · browser agent and inspector |

## Customer feedback and marketing

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Notra](projects/notra.md) | Inspect brand mentions and placement in AI answers. | TypeScript · brand visibility application |
| [Testimonial miner](projects/testimonial-miner.md) | Find and review verbatim praise in email, grouped by product. | Python · CLI and local dashboard |

## Developer tools

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [fast-jev-compaction](projects/fast-jev-compaction.md) | Select which old tool calls and results remain in agent context. | TypeScript · library and Claude Code plugin |
| [Jev Belay](projects/jev-belay.md) | Block an unverified "done" until the transcript shows real evidence. | Node.js · Claude Code plugin / Stop hook |
| [Jev Commit](projects/jev-commit.md) | Check whether a commit message actually matches the staged diff. | Python · pre-commit / git hook |
| [Jev Logs](projects/jevlogs.md) | Prioritize logs for deeper analysis alongside your archive. | TypeScript · library, CLI and OpenTelemetry integration |
| [Jev Review](projects/jev-review.md) | Add experimental quality judgments to a coding agent's review loop. | Node.js · MCP server |
| [jev.nvim](projects/jev-nvim.md) | Ask a buffer a plain-language question and get a ranked quickfix list. | Lua · Neovim plugin |

## Home automation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Jev for Home Assistant](projects/ha-jev.md) | Turn household context into judgment sensors and automation responses. | Python · Home Assistant integration |

## SDKs and integrations

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Laravel AI](projects/laravel-ai.md) | Add typed classification through Laravel’s TypeSafe provider. | PHP · Laravel package |
| [TypeSafeAI.Net](projects/typesafeai-net.md) | Add typed Jev judgments to .NET applications and Microsoft.Extensions.AI pipelines. | C# · client library |

## Search and retrieval

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Jev Search](projects/jev-search.md) | Search selected sources and inspect ranked links and filters. | TypeScript · TanStack Start and Cloudflare Workers |
| [llama-index-jev](projects/llama-index-jev.md) | Rerank retrieved passages or choose a query engine in LlamaIndex. | Python · integration packages |
| [neo4jev](projects/neo4jev.md) | Explore graph paths with typed next-hop and goal judgments. | Python · Neo4j, notebooks and Streamlit |
| [pg-jev](projects/pg-jev.md) | Ask semantic questions from SQL over database rows. | PostgreSQL · PL/Python extension |

## Try a smaller example

The repository also maintains its own [four teaching examples](../examples/README.md), [Support Router](../projects/support-router/README.md), and [routing evaluation runner](../evaluations/README.md). These are useful when you want a small offline starting point before adopting a community project.

## Share or improve a project

Follow [Add a community project](../CONTRIBUTING.md#add-a-community-project) and the [project-page template](PROJECT_TEMPLATE.md). A project submission includes a detail page, a category entry here, and the existing README link. Corrections to setup instructions and limitations are welcome.

Pages summarize the linked projects; their maintainers own the upstream code and licenses. Check each page's reviewed version and [validation scope](../docs/validation.md#community-project-checks). A listing does not establish production quality or endorsement.
