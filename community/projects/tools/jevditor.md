# Jevditor by Nikola Balić (programmable writing linter where Jev checks your own style rules as you type)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Web editor that turns each style rule you dislike into a yes/no question: Jev flags matching sentences, passages or sections, code decides what to show, and Claude only drafts rules or rewrites a passage when you ask.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nibzard/jevditor) |
| Maintainer | [nibzard](https://github.com/nibzard). Independently curated. |
| Format | TypeScript (Hono server, React + Tiptap editor) |
| Requirements | Node 22.13+ and pnpm; a `TYPESAFE_API_KEY` for real checks (otherwise a demo word-overlap classifier) and optionally an Anthropic key for drafting and rewrites. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/server/src/classifier.ts`](https://github.com/nibzard/jevditor/blob/1d4079ac58590a935a78a83fc406fbcbb39e0075/apps/server/src/classifier.ts) at the pinned commit. |

## When to use

- Enforce a personal style guide while writing, without a chatbot rewriting your voice.
- Mismatch: grammar checking; it only checks the rules you define, and there is no license file.

## How it works

`apps/server/src/classifier.ts` uses `TypeSafeClient` from `@typesafe-ai/sdk` to ask one `noul` per saved rule for each changed segment, and a speculative `choice` that picks a predefined explanation when a rule fires; results are cached and stale answers are dropped. Integration evidence: [`apps/server/src/classifier.ts`](https://github.com/nibzard/jevditor/blob/1d4079ac58590a935a78a83fc406fbcbb39e0075/apps/server/src/classifier.ts).

## Get started

Run the dev server and web app.

```sh
git clone https://github.com/nibzard/jevditor
cd jevditor
pnpm install
cp .env.example .env   # add TYPESAFE_API_KEY
pnpm dev   # server :8787, web :5173
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nibzard/jevditor/blob/1d4079ac58590a935a78a83fc406fbcbb39e0075/README.md](https://github.com/nibzard/jevditor/blob/1d4079ac58590a935a78a83fc406fbcbb39e0075/README.md)
- Evals: [github.com/nibzard/jevditor/tree/1d4079ac58590a935a78a83fc406fbcbb39e0075/apps/server/evals](https://github.com/nibzard/jevditor/tree/1d4079ac58590a935a78a83fc406fbcbb39e0075/apps/server/evals)

## Limits and data handling

The text you write is sent to TypeSafe for rule checks (and to Claude only for requested drafts or rewrites). No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 1d4079ac5859](https://github.com/nibzard/jevditor/tree/1d4079ac58590a935a78a83fc406fbcbb39e0075). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
