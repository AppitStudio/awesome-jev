# DeepORG by Vikram Rangnekar (open-source company data agent, formerly GraphJin, that can use Jev to pick the tables and skill guides it needs before it answers)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source agent and engine (formerly GraphJin) that answers questions and makes changes across your databases, warehouses, APIs, files and code, checking every query against your access rules and holding changes for approval by default. An optional decision stage can run on Jev: it ranks catalog tables, columns and skill guides before the main agent starts, so the agent begins with the right schema.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dosco/deeporg) |
| Maintainer | [Vikram Rangnekar](https://github.com/dosco) (dosco). Independently curated. |
| Format | Go server, CLI and library (npm, Homebrew, Docker) |
| Requirements | The `deeporg` binary (npm, Homebrew, Docker or release archive), a database or the sample data, a model for the main agent; for the Jev stage a TypeSafe key in `JEV_API_KEY`. |
| License | [Apache-2.0](https://github.com/dosco/deeporg/blob/7e3f05c1c785332fb5f5a66cd790839e07274854/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/dosco/status/2125851420830343471)). |
| Jev evidence | [`agent/selection.go`](https://github.com/dosco/deeporg/blob/7e3f05c1c785332fb5f5a66cd790839e07274854/agent/selection.go) at the pinned commit. |

## When to use

- Teams that want one agent over several databases and APIs and want a fast decision model to narrow the schema before an expensive model runs.
- Mismatch: a Jev-only tool; Jev is an optional speed-up stage, and the main agent still needs a general model.

## How it works

With `agent.selection` enabled and `provider: typesafe`, `model: jev-latest`, `agent/selection.go` asks Jev typed decisions about which catalog roots, columns and skill guides fit the request, then a second decision checks that the chosen starting tables match the requested scope. Calls go through the author's Ax library; the stage is off by default, has a 2-second startup budget and falls back to normal discovery when a decision fails. Integration evidence: [`agent/selection.go`](https://github.com/dosco/deeporg/blob/7e3f05c1c785332fb5f5a66cd790839e07274854/agent/selection.go).

## Get started

Install, start the setup page, connect a database or the sample data, then turn on the Jev selection stage in the config.

```sh
npm install -g deeporg     # or: brew install dosco/deeporg/deeporg
deeporg                    # opens the setup page
# config: agent.selection.enabled: true, provider: typesafe, model: jev-latest, api_key_env: JEV_API_KEY
export JEV_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [deeporg.io](https://deeporg.io)
- Selection stage docs: [github.com/dosco/deeporg/blob/7e3f05c1c785332fb5f5a66cd790839e07274854/website/content/agentic/server-agent.md](https://github.com/dosco/deeporg/blob/7e3f05c1c785332fb5f5a66cd790839e07274854/website/content/agentic/server-agent.md)

## Limits and data handling

Jev sees catalog metadata (table, column and guide names and descriptions) plus the request, not query results. The selection stage is disabled by default and its benefit is measured with the project's own evaluation harness; benchmark scores on deeporg.io are the author's. Changes made by the agent are held for approval by default, but read access follows the rules you configure.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 7e3f05c1c785](https://github.com/dosco/deeporg/tree/7e3f05c1c785332fb5f5a66cd790839e07274854). Inspected the README, LICENSE, `website/content/agentic/server-agent.md` ("Fast catalog discovery and skill selection") and `agent/selection.go` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
