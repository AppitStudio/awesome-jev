# Jev apps and community projects

[Back to Awesome Jev](../README.md) · [Get help choosing a project](../docs/using-the-guide.md) · [Share your project](../CONTRIBUTING.md#add-a-community-project)

Discover apps powered by Jev, then browse developer tools and integrations by what you want to build. Open a project page to see when it fits, how to get started, examples, and what has actually been checked. The original [README list](../README.md#community-projects) remains a quick way to reach each upstream project.

**[Choose by the outcome you want](../docs/explore-use-cases.md)** for a guided tour with practical scenarios and guidance for a first experiment.

## Categories

- [Apps powered by Jev](#apps-powered-by-jev)
- [Browser and computer use](#browser-and-computer-use)
- [Customer feedback and marketing](#customer-feedback-and-marketing)
- [Developer tools](#developer-tools)
- [Home automation](#home-automation)
- [SDKs and integrations](#sdks-and-integrations)
- [Search and retrieval](#search-and-retrieval)

## Apps powered by Jev

Applications you can use through their own interface, with Jev powering a concrete part of the experience. An app can use other models too; each listing explains Jev's role. Source-built apps belong here alongside hosted products. Availability describes the reviewed version, not a guarantee of service or production readiness.

| App | What you can do | What Jev powers | Platform and access |
| --- | --- | --- | --- |
| [Jev Search](projects/jev-search.md) | Search selected sources and inspect ranked links and filters. | Query/source selection and relevance judgments. | Web · hosted app or self-host; self-hosting needs TypeSafe and Search1API keys. |
| [Notra](projects/notra.md) | Track how AI answers describe and position your brand. | Brand sentiment and list-position judgments within a larger analytics app. | Web · hosted account or self-host; database, auth, and provider setup required for self-hosting. |
| [TipTour](projects/tiptour.md) | Type a request to click controls in a macOS app. | Target and click-type selection, completion and missing-target judgments. | macOS 14.2+ · build with Xcode; bring a TypeSafe key. Gemini key for optional voice mode. |

**[Share your app](../CONTRIBUTING.md#list-a-jev-powered-app)** — self-submissions are welcome. Include a working product or source link, platform, access/cost requirements, evidence of Jev use, and your affiliation. Open-source, closed-source, free, and paid apps can qualify under the same review criteria.

## Browser and computer use

See the [computer-use guide](../docs/computer-use.md) for a comparison, form/extraction examples, native-app testing designs, and the evidence boundary around iOS demonstrations.

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Cua jev-use](projects/cua-jev-use.md) | Compose a bounded chooser with Driver and independent fixture verification. | Python / TypeScript · integration recipe |
| [Jev Browser (tontoko)](projects/jev-browser-tontoko.md) | Fill forms, extract records with evidence, and add semantic selection to Playwright tests. | TypeScript · SDK, CLI and MCP |
| [Jev Ultrafast](projects/jev-ultrafast.md) | Select browser operations and targets from the current page. | Python · browser agent and inspector |
| [Mobile Jev](projects/mobile-jev.md) | Navigate an Android device and verify a dark-theme task. | JavaScript / React · Mobilerun agent and studio |
| [typesafe-computer-use](projects/typesafe-computer-use.md) | Study OCR and Accessibility driven native macOS control. | Python · desktop CLI |

## Customer feedback and marketing

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Testimonial miner](projects/testimonial-miner.md) | Find and review verbatim praise in email, grouped by product. | Python · CLI and local dashboard |

## Developer tools

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [fast-jev-compaction](projects/fast-jev-compaction.md) | Select which old tool calls and results remain in agent context. | TypeScript · library and Claude Code plugin |
| [Jev Logs](projects/jevlogs.md) | Prioritize logs for deeper analysis alongside your archive. | TypeScript · library, CLI and OpenTelemetry integration |
| [Jev Review](projects/jev-review.md) | Add experimental quality judgments to a coding agent's review loop. | Node.js · MCP server |

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
| [llama-index-jev](projects/llama-index-jev.md) | Rerank retrieved passages or choose a query engine in LlamaIndex. | Python · integration packages |
| [neo4jev](projects/neo4jev.md) | Explore graph paths with typed next-hop and goal judgments. | Python · Neo4j, notebooks and Streamlit |
| [pg-jev](projects/pg-jev.md) | Ask semantic questions from SQL over database rows. | PostgreSQL · PL/Python extension |

## Try a smaller example

The repository also maintains its own [teaching examples](../examples/README.md), [Support Router](../projects/support-router/README.md), and [routing evaluation runner](../evaluations/README.md). These are useful when you want a small offline starting point before adopting a community project.

## Share or improve a project

Follow [Add a community project](../CONTRIBUTING.md#add-a-community-project) and the [project-page template](PROJECT_TEMPLATE.md). A project submission includes a detail page, a category entry here, and the existing README link. Corrections to setup instructions and limitations are welcome.

Pages summarize the linked projects; their maintainers own the upstream code and licenses. Check each page's reviewed version and [validation scope](../docs/validation.md#community-project-checks). A listing does not establish production quality or endorsement.
