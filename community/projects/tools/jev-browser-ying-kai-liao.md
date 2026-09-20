# Jev Browser (Ying-Kai-Liao)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

A JavaScript browser library, CLI, and MCP server that lets a calling agent specify one outcome while Jev selects browser actions and targets from structured page observations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ying-Kai-Liao/jev-browser) |
| Maintainer | [Ying-Kai Liao](https://github.com/Ying-Kai-Liao). Independent project, not affiliated with TypeSafe. |
| Format | Node.js library, CLI, and MCP server; npm package `jev-browser`, version 0.1.1 at review. |
| Jev's role | Chooses tools, elements, and caller-supplied values, and judges completion, errors, login barriers, and irreversible actions. Playwright executes the selected actions. |
| Requirements | Node.js 20+, Playwright Chromium, and `TYPESAFE_API_KEY` for live judgments. An MCP client or calling agent supplies goals and any text to enter. |
| Access | MIT source; TypeSafe and any calling-agent usage can incur separate charges. |
| License | [MIT](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/LICENSE). |
| Disclosure | AI-assisted independent catalog review; contributor affiliation/commercial relationships were not supplied. Inclusion is not an endorsement. |

## When to use

Use this when an agent can name a small, observable browser outcome but would otherwise repeatedly read page snapshots and choose individual elements. It supports direct actions and snapshots for manual takeover alongside Jev-driven steps.

Split compound tasks into separate outcomes. For counting, ordering, and consequential changes, verify the actual result independently; a completion probability is not proof. This is a different implementation from [Jev Browser (tontoko)](jev-browser-tontoko.md).

## How it works

The [session loop](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/src/session.mjs) waits for page activity to settle, gathers visible text and numbered elements, and sends the goal, supplied values, recent action history, and page state to Jev. One request asks several typed questions; large pages use group selection followed by element selection, and some actions require follow-up judgments.

Code reconciles the selected tool with suitable targets and executes through Playwright. A step defaults to ten action rounds; the MCP interface accepts at most thirty. This is not a strict API-call or spending limit: selection stages, follow-ups, and retries can add requests.

The [HTTP client](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/src/jev.mjs) calls `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default. `JEV_API_URL` and `JEV_MODEL` override those settings. Returned statuses distinguish `done`, `likely_done`, `needs_confirmation`, `needs_login`, `ambiguous`, `blocked`, `error`, `stuck`, and exhausted action rounds.

## Get started

Start with the local fixture tests. Dependency and Chromium installation require downloads; the tests themselves use a local HTML fixture and fake judgments, without a TypeSafe key:

```sh
git clone https://github.com/Ying-Kai-Liao/jev-browser.git
cd jev-browser
git checkout 578cff6e701a131733d03256078bb559a45ad188
npm ci --ignore-scripts
npx playwright install chromium
npm test
```

For live use, privately configure `TYPESAFE_API_KEY` in the server environment. The source client also looks for it in `.env` in the working directory and source root. Configure your MCP client to launch `node` with the absolute path to `bin/jev-browser-mcp.mjs`; see the [upstream setup](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/README.md#setup-from-source).

Use `browser_open` to open your test page, then `browser_do` for one outcome. `browser_snapshot` and `browser_act` provide direct inspection and control; `browser_check` still calls Jev and returns a probability. Submitting a live goal transfers page/task data to TypeSafe and can incur charges. A caller must authorize any consequential action separately from the model's classification.

## Examples and demos

- [Fixture tests](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/test/page.test.mjs): local forms, labels, frames, shadow DOM, page differences, stale targets, and dialog handling.
- [Example flows](https://github.com/Ying-Kai-Liao/jev-browser/tree/578cff6e701a131733d03256078bb559a45ad188/examples/flows): JSON workflows for the CLI. These are live browser tasks, not offline simulations.
- [Upstream results](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/RESULTS.md): author-reported live-site runs. Their accuracy, timing, and context-size comparisons were not independently reproduced here.

## Limits and data handling

- **Supplied values can include credentials.** The session sends the complete `values` object as task state. The [page collector](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/src/page-script.mjs) also collects populated input values without a password-field exclusion. Do not assume passwords, private form data, or authenticated-page content are redacted before reaching TypeSafe.
- Pages receive the browser's actions and entered values; file-upload actions can send files to the visited site. `JEV_BROWSER_PROFILE` persists browser state, including sessions. Optional logging and MCP results can expose page text and decision details to the caller.
- Irreversibility and completion checks are model judgments. `allow_irreversible` can bypass the semantic pause, and direct actions do not use the full goal loop. The integration is not an authorization boundary or prompt-injection defense.
- The client retries network failures, HTTP 429, and server errors up to two times by default. It does not validate a complete successful-response schema before consumers read the answers. The host needs an error and review path.
- Live MCP integration, website coverage, and model quality were not validated by the catalog review. No generalized speed or token-saving claim is established.

## Review and maintenance

Reviewed on **2026-09-20** at commit [`578cff6e701a131733d03256078bb559a45ad188`](https://github.com/Ying-Kai-Liao/jev-browser/commit/578cff6e701a131733d03256078bb559a45ad188), package **0.1.1**. Inspected the README, MIT license, package metadata, HTTP client, session loop, page collection, CLI/MCP entry points, examples, and fixture tests. Installed dependencies with lifecycle scripts disabled and installed the matching Playwright Chromium in a separate temporary directory. On macOS with Node.js 24.19.0 and a credential-free environment, `npm test` passed all **23 local fixture tests**. The initial attempt lacked the required Chromium revision; it passed after that browser was installed. These checks exercise local page handling and fake judgments; no live Jev request, live MCP workflow, or external-site benchmark was run. Catalog checks are recorded in the publication pull request.

Related: [Cua jev-use](cua-jev-use.md) emphasizes independent fixture verification; [computer-use guide](../../../docs/computer-use.md) compares other browser and desktop integrations.
