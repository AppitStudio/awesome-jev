# opencode-auto-approval-plugin (OpenCode plugin that sends tool operations to a read-only reviewer before approving them, with a Jev decision backend)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that reviews each tool operation before it is automatically approved. The reviewer is one of three backends: a read-only agent session, a single chat-model call, or a decision model over HTTP, where TypeSafe's Jev (or Cloudflare's Clef) picks allow, deny or escalate with probabilities in one call. It supports OpenCode 2.x and 1.18.29 and later, and includes usage statistics commands.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dyoshikawa/opencode-auto-approval-plugin) |
| Maintainer | [dyoshikawa](https://github.com/dyoshikawa). Independently curated. |
| Format | OpenCode plugin (TypeScript, npm) |
| Requirements | OpenCode 1.18.29+ or 2.x and a reviewer backend: a model for the agent or chat backends, or a Jev key (`TYPESAFE_API_KEY`) for the decision backend. |
| License | [MIT](https://github.com/dyoshikawa/opencode-auto-approval-plugin/blob/9f429d4a4e970cf1bd5d27de244ee35da5eda9da/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/dyoshikawa/opencode-auto-approval-plugin/blob/9f429d4a4e970cf1bd5d27de244ee35da5eda9da/src/config.ts) at the pinned commit. |

## When to use

- Cut permission prompts for routine operations while risky ones are denied or escalated to you.
- Mismatch: Jev is one of three reviewer backends, and the README itself compares models that allowed or denied risky operations differently.

## How it works

`src/config.ts` defines the `decision` backend with a `typesafe` provider (base URL `https://api.typesafe.ai`, `jev-latest` by default, optional long-context header for large operations); the answer is mapped to allow, deny or escalate. Integration evidence: [`src/config.ts`](https://github.com/dyoshikawa/opencode-auto-approval-plugin/blob/9f429d4a4e970cf1bd5d27de244ee35da5eda9da/src/config.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install opencode-auto-approval-plugin
# add the package to opencode.json (2.x: `plugins`), set reviewer.backend to "decision" and provider "typesafe"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the backends, config and statistics commands: [github.com/dyoshikawa/opencode-auto-approval-plugin#readme](https://github.com/dyoshikawa/opencode-auto-approval-plugin#readme)

## Limits and data handling

Operation details (redacted by the plugin's redaction step) go to whichever reviewer backend you pick, including TypeSafe when the decision backend uses Jev. A reviewer helps with approvals but is not a sandbox. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 9f429d4a4e97](https://github.com/dyoshikawa/opencode-auto-approval-plugin/tree/9f429d4a4e970cf1bd5d27de244ee35da5eda9da). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
