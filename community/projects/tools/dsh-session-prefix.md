# dsh-session-prefix (DeepSeek Harness session status emojis classified by Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness plugin that keeps the session sidebar readable by putting status emoji prefixes on session titles: Jev classifies each session's phase from the latest instruction and output summary (for example debugging, ready for review or done), and the agent can also set badges through a `session_prefix` tool.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/john-walks-slow/dsh-session-prefix) |
| Maintainer | [john-walks-slow](https://github.com/john-walks-slow). Independently curated. |
| Format | DSH plugin (TypeScript) |
| Requirements | DeepSeek Harness; a key for the configured Jev route (default: OpenRouter's decisions endpoint). Without a key, Jev classification is skipped. |
| License | [MIT](https://github.com/john-walks-slow/dsh-session-prefix/blob/ab1f3fcc9ced734b3146375d48aa2ac16c5df409/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/john-walks-slow/dsh-session-prefix/blob/ab1f3fcc9ced734b3146375d48aa2ac16c5df409/src/jev.ts) at the pinned commit. |

## When to use

- Spot at a glance which DSH sessions need review or are finished.
- Classify sessions without adding instructions to your main model's context.
- Mismatch: Jev classification is silently skipped without a key; tool-driven badges still work.

## How it works

`src/jev.ts` sends the current instruction and output summary (never the full history) with a phase Choice to `https://openrouter.ai/api/alpha/decisions` by default, using `typesafe/jev-1.13`; the endpoint and model are configurable in the settings tab. Integration evidence: [`src/jev.ts`](https://github.com/john-walks-slow/dsh-session-prefix/blob/ab1f3fcc9ced734b3146375d48aa2ac16c5df409/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile web add dsh-session-prefix
# or: dsh plugin --profile web add github:john-walks-slow/dsh-session-prefix
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/john-walks-slow/dsh-session-prefix#readme](https://github.com/john-walks-slow/dsh-session-prefix#readme)

## Limits and data handling

Instruction and output summaries go to OpenRouter (or the endpoint you set) and on to TypeSafe; Jev is reached through OpenRouter by default.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit ab1f3fcc9ced](https://github.com/john-walks-slow/dsh-session-prefix/tree/ab1f3fcc9ced734b3146375d48aa2ac16c5df409). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
