# sasacode jev-guard (terminal coding agent plugin that asks Jev before tool calls run)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for the sasacode terminal coding agent that adds a Jev judgment after its rules and permission mode, stopping risky calls that would run unasked and handing safe soft-denied calls to you.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sasanokusa/sasacode) |
| Maintainer | [sasanokusa](https://github.com/sasanokusa). Independently curated. |
| Format | sasacode plugin (TypeScript/Bun, Apache-2.0) |
| Requirements | sasacode (plugin API ^1.8.0) and one Jev backend key: `TYPESAFE_API_KEY`, Command Code `CMD_API_KEY`, OpenRouter or Vercel AI Gateway. |
| License | [Apache-2.0](https://github.com/sasanokusa/sasacode/blob/dfd6fdfdbaa701c5d959bac3c4a38436339e5307/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/jev-guard/index.ts`](https://github.com/sasanokusa/sasacode/blob/dfd6fdfdbaa701c5d959bac3c4a38436339e5307/plugins/jev-guard/index.ts) at the pinned commit. |

## When to use

- Add a fast second opinion before a terminal agent runs shell or edit tools.
- Compare Jev with a chat-model judge on the same permission flow.
- Mismatch: main docs are in Japanese (an English README is included); the repo's own benchmark notes are author-reported.

## How it works

`plugins/jev-guard/index.ts` sends only harness-gathered facts about the pending call to Jev and maps the probabilities onto allow/ask/deny; `backends.ts` covers TypeSafe (`jev-latest`), Command Code, OpenRouter Decisions, Vercel AI Gateway or a chat-model fallback. Off by default; `/jev on` enables it per session. Integration evidence: [`plugins/jev-guard/index.ts`](https://github.com/sasanokusa/sasacode/blob/dfd6fdfdbaa701c5d959bac3c4a38436339e5307/plugins/jev-guard/index.ts).

## Get started

Install sasacode, install the plugin, then turn it on in the TUI with `/jev on`.

```sh
curl -fsSL https://sasanokusa.com/sasacode/install.sh | sh
sasacode plugin install sasacode-plugin-jev-guard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author benchmark of jev-guard on 5,135 real session commands: [github.com/sasanokusa/sasacode/blob/dfd6fdfdbaa701c5d959bac3c4a38436339e5307/docs/benchmarks.md](https://github.com/sasanokusa/sasacode/blob/dfd6fdfdbaa701c5d959bac3c4a38436339e5307/docs/benchmarks.md)

## Limits and data handling

The pending command and nearby context go to the chosen Jev backend. Permission checks are not a sandbox; isolate untrusted code at the OS level.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit dfd6fdfdbaa7](https://github.com/sasanokusa/sasacode/tree/dfd6fdfdbaa701c5d959bac3c4a38436339e5307). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
