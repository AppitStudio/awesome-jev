# opencode-permission-reviewer (OpenCode plugin where a tool-free reviewer, optionally Jev, allows, denies or escalates each permission request)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial OpenCode plugin that adds a Codex-Guardian-style reviewer to every `ask` permission. A tool-free model backend reads the pending request, bounded transcript evidence and a policy you control, then allows it, denies it with feedback, or escalates to you. Actions classed as critical are never auto-approved, and failures lead to manual review or denial. Jev models use a direct typed request instead of a child session.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/warc0s/opencode-permission-reviewer) |
| Maintainer | [warc0s](https://github.com/warc0s). Independently curated. |
| Format | OpenCode plugin (TypeScript, Bun; npm package) |
| Requirements | Bun 1.3.14+ and OpenCode (V1 1.18.29+ or V2); a model provider you configure, or a Jev key. |
| License | [Apache-2.0](https://github.com/warc0s/opencode-permission-reviewer/blob/9c7f8c45aa5fe05ecf551a991034fd81ba848ea5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/system-one/backend.ts`](https://github.com/warc0s/opencode-permission-reviewer/blob/9c7f8c45aa5fe05ecf551a991034fd81ba848ea5/src/system-one/backend.ts) at the pinned commit. |

## When to use

- Stop safe, routine permission prompts from waiting on a keystroke while risky ones are still blocked or surfaced.
- Mismatch: Jev is one of several supported reviewer backends, and wrapper nesting beyond a fixed budget is not fully analysed.

## How it works

`src/system-one/backend.ts` uses the `@typesafe-ai/sdk` client to send the review as typed System One questions and delegates only valid but difficult decisions onward; normal chat models instead run in a tool-free child session. Integration evidence: [`src/system-one/backend.ts`](https://github.com/warc0s/opencode-permission-reviewer/blob/9c7f8c45aa5fe05ecf551a991034fd81ba848ea5/src/system-one/backend.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun add opencode-permission-reviewer   # or: npm install opencode-permission-reviewer
bunx opencode-permission-reviewer init --host auto --npm --tui --yes
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the policy file, review flow and limits: [github.com/warc0s/opencode-permission-reviewer#readme](https://github.com/warc0s/opencode-permission-reviewer#readme)

## Limits and data handling

Requests, command text and bounded session evidence go to the reviewer provider you configure, including TypeSafe when a Jev model is selected. It is an unofficial plugin, not affiliated with OpenCode's maker; a reviewer is advice for permissions, not a sandbox. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 9c7f8c45aa5f](https://github.com/warc0s/opencode-permission-reviewer/tree/9c7f8c45aa5fe05ecf551a991034fd81ba848ea5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
