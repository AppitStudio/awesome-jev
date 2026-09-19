# Tools and integrations

[All projects](../README.md) · [Apps powered by Jev](../apps/README.md) · [Share a tool](../../../CONTRIBUTING.md#add-a-community-project)

Developer tools, libraries, SDKs, integrations, and reference implementations for building with Jev. Each full guide explains how to use the project, what needs adapting, and what was checked. For an application with its own user-facing workflow, visit the separate [app directory](../apps/README.md).

## Categories

- [Browser and computer use](#browser-and-computer-use)
- [Customer feedback and marketing](#customer-feedback-and-marketing)
- [Developer tools](#developer-tools)
- [Home automation](#home-automation)
- [SDKs and integrations](#sdks-and-integrations)
- [Search and retrieval](#search-and-retrieval)

## Browser and computer use

See the [computer-use guide](../../../docs/computer-use.md) for a comparison, form/extraction examples, native-app testing designs, and the evidence boundary around iOS demonstrations.

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Cua jev-use](cua-jev-use.md) | Compose a bounded chooser with Driver and independent fixture verification. | Python / TypeScript · integration recipe |
| [Jev Browser (tontoko)](jev-browser-tontoko.md) | Fill forms, extract records with evidence, and add semantic selection to Playwright tests. | TypeScript · SDK, CLI and MCP |
| [Jev Ultrafast](jev-ultrafast.md) | Select browser operations and targets from the current page. | Python · browser agent and inspector |
| [Jev-cu](jev-cu.md) | Study experimental Jev decisions over macOS Accessibility text in Codex; review the execution-policy limitations before use. | JavaScript · Codex skill and runtime |
| [Mobile Jev](mobile-jev.md) | Navigate an Android device and verify a dark-theme task. | JavaScript / React · Mobilerun agent and studio |
| [typesafe-computer-use](typesafe-computer-use.md) | Study OCR and Accessibility driven native macOS control. | Python · desktop CLI |

## Customer feedback and marketing

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Testimonial miner](testimonial-miner.md) | Find and review verbatim praise in email, grouped by product. | Python · CLI and local dashboard |

## Developer tools

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [fast-jev-compaction](fast-jev-compaction.md) | Select which old tool calls and results remain in agent context. | TypeScript · library and Claude Code plugin |
| [Jev Logs](jevlogs.md) | Prioritize logs for deeper analysis alongside your archive. | TypeScript · library, CLI and OpenTelemetry integration |
| [Jev Review](jev-review.md) | Add experimental quality judgments to a coding agent's review loop. | Node.js · MCP server |
| [Jev Sift](jev-sift.md) | Screen candidate content before reading it into agent context; requires a TypeSafe key, with upstream licensing unspecified. | Node.js · MCP server and agent plugin |

## Home automation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Jev for Home Assistant](ha-jev.md) | Turn household context into judgment sensors and automation responses. | Python · Home Assistant integration |

## SDKs and integrations

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Laravel AI](laravel-ai.md) | Add typed classification through Laravel’s TypeSafe provider. | PHP · Laravel package |
| [TypeSafeAI.Net](typesafeai-net.md) | Add typed Jev judgments to .NET applications and Microsoft.Extensions.AI pipelines. | C# · client library |

## Search and retrieval

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [llama-index-jev](llama-index-jev.md) | Rerank retrieved passages or choose a query engine in LlamaIndex. | Python · integration packages |
| [neo4jev](neo4jev.md) | Explore graph paths with typed next-hop and goal judgments. | Python · Neo4j, notebooks and Streamlit |
| [pg-jev](pg-jev.md) | Ask semantic questions from SQL over database rows. | PostgreSQL · PL/Python extension |

## Try a smaller example

The repository also maintains its own [teaching examples](../../../examples/README.md), [Support Router](../../../projects/support-router/README.md), and [routing evaluation runner](../../../evaluations/README.md). These are useful when you want a small offline starting point before adopting a community project.

## Share or improve a tool

Follow [Add a community project](../../../CONTRIBUTING.md#add-a-community-project) and the [project-page template](../../PROJECT_TEMPLATE.md). Put the full guide in this folder, list it once in a category above, and keep its upstream and guide links in the root README. Corrections to setup instructions and limitations are welcome.

Upstream maintainers own their code and licenses. Check each page's reviewed version and [validation scope](../../../docs/validation.md#community-project-checks); a listing does not establish production quality or endorsement.
