# Jev Claude Router by Darkisu Su (Claude Code plugin where Jev picks the skills, model and effort for each prompt)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin marketplace with one plugin, jev-router. On each new prompt it asks Jev which local skills fit and which Claude model and effort to use, and it adds a typed decision tool so Claude can consult Jev on its own decisions during a task. Routing starts in dry-run mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DarkisuSu/Jev-Claude-Router) |
| Maintainer | [DarkisuSu](https://github.com/DarkisuSu). Independently curated. |
| Format | TypeScript Claude Code plugin (hooks) |
| Requirements | Claude Code 2.1.287+ (the VS Code Claude extension is also supported) and a TypeSafe API key set in the plugin settings. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/jev-router/hooks/questions.ts`](https://github.com/DarkisuSu/Jev-Claude-Router/blob/ba130a9588a7266fd90b5810fa59ef3edf700b29/plugins/jev-router/hooks/questions.ts) at the pinned commit. |

## When to use

- Let Jev pick Claude model, effort and skills per prompt, with a dry run before it changes anything.
- Mismatch: if you don't use Claude Code.

## How it works

`plugins/jev-router/hooks/questions.ts` builds the skill and model questions and posts them to `https://api.typesafe.ai/v1/systemone`; `router.ts` applies the answers, starting in dry-run until you run `/jev-model on`. Integration evidence: [`plugins/jev-router/hooks/questions.ts`](https://github.com/DarkisuSu/Jev-Claude-Router/blob/ba130a9588a7266fd90b5810fa59ef3edf700b29/plugins/jev-router/hooks/questions.ts).

## Get started

Install from the plugin marketplace inside Claude Code, set your key in the plugin settings, and check `/jev-model`.

```sh
/plugin install jev-router --marketplace DarkisuSu/Jev-Claude-Router#main
/reload-plugins
/jev-model   # prints "model routing: dry-run"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DarkisuSu/Jev-Claude-Router/blob/ba130a9588a7266fd90b5810fa59ef3edf700b29/README.md](https://github.com/DarkisuSu/Jev-Claude-Router/blob/ba130a9588a7266fd90b5810fa59ef3edf700b29/README.md)

## Limits and data handling

Each prompt and your local skill list are sent to TypeSafe. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit ba130a9588a7](https://github.com/DarkisuSu/Jev-Claude-Router/tree/ba130a9588a7266fd90b5810fa59ef3edf700b29). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
