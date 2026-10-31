# jev-router by QuesoMan (Claude Code mod where Jev picks the model and effort for every turn and subagent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that saves money by asking Jev, before each turn and each subagent runs, which model family and effort (for example `haiku_medium`, `sonnet_high`, `opus_xhigh`) should answer. Jev sees your request, recent messages and the files in play as named fields and answers with probabilities; the routing decision itself is made in code, family first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/QuesoMan/jev-router) |
| Maintainer | [QuesoMan](https://github.com/QuesoMan). Independently curated. |
| Format | Claude Code mod (TypeScript hooks) |
| Requirements | Claude Code with mods support; a TypeSafe key or a Vercel AI Gateway key. |
| License | [MIT](https://github.com/QuesoMan/jev-router/blob/b95881daf3ab6b26b3929ce54694f2514575ab5b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/jev.ts`](https://github.com/QuesoMan/jev-router/blob/b95881daf3ab6b26b3929ce54694f2514575ab5b/hooks/jev.ts) at the pinned commit. |

## When to use

- Cut Claude Code spend by sending easy turns to smaller models automatically.
- Mismatch: routing quality depends on your policy bands; check the eval scripts before trusting it on hard work.

## How it works

`hooks/jev.ts` asks one choice question through TypeSafe's direct API (`POST /v1/systemone`) or the AI Gateway (`typesafe-ai/jev`); `hooks/provider.ts` picks the endpoint and `JEV_ROUTER_TIMEOUT_MS` bounds the wait, after which the default model is kept. Integration evidence: [`hooks/jev.ts`](https://github.com/QuesoMan/jev-router/blob/b95881daf3ab6b26b3929ce54694f2514575ab5b/hooks/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm run check-jev        # is the configured provider serving?
npm run try-prompts -- "your prompt"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- What is sent to TypeSafe: [github.com/QuesoMan/jev-router#what-is-sent-to-typesafe](https://github.com/QuesoMan/jev-router#what-is-sent-to-typesafe)

## Limits and data handling

Your prompt, recent messages and touched file names are sent to TypeSafe or the AI Gateway (or just the request with `context: request`). Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit b95881daf3ab](https://github.com/QuesoMan/jev-router/tree/b95881daf3ab6b26b3929ce54694f2514575ab5b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
