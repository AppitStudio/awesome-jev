# Cruise (Claude Code context, progress and effort plugin)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin from NTConsult with context warnings, a progress band above the prompt and an optional effort judge that picks a lower reasoning effort for small requests, where the judge can be Haiku, Jev on TypeSafe or a local Laya model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FranciscoPrestes/cruise) |
| Maintainer | [FranciscoPrestes](https://github.com/FranciscoPrestes). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code; a TypeSafe API key only if you choose the Jev judge. |
| License | [MIT](https://github.com/FranciscoPrestes/cruise/blob/12d83d6aeb48f9bc4e1c40d6bd4b7f592f484429/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/effort.ts`](https://github.com/FranciscoPrestes/cruise/blob/12d83d6aeb48f9bc4e1c40d6bd4b7f592f484429/hooks/effort.ts) at the pinned commit. |

## When to use

- Avoid running a one-line edit at high reasoning effort.
- Get context warnings before quality drops in long sessions.
- Mismatch: the effort judge is off by default and only ever lowers effort.

## How it works

`hooks/effort.ts` asks the configured judge for an effort level per prompt; for Jev it calls `https://api.typesafe.ai/v1/systemone` (`jev-latest` unless set), with your key kept in Claude Code's secure storage. Integration evidence: [`hooks/effort.ts`](https://github.com/FranciscoPrestes/cruise/blob/12d83d6aeb48f9bc4e1c40d6bd4b7f592f484429/hooks/effort.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add FranciscoPrestes/cruise
/plugin install cruise@prestes
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Settings table in the README: [github.com/FranciscoPrestes/cruise#readme](https://github.com/FranciscoPrestes/cruise#readme)
- Judge evaluation script: [github.com/FranciscoPrestes/cruise/blob/main/eval/judge_eval.py](https://github.com/FranciscoPrestes/cruise/blob/main/eval/judge_eval.py)

## Limits and data handling

With the Jev judge on, prompt text is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 12d83d6aeb48](https://github.com/FranciscoPrestes/cruise/tree/12d83d6aeb48f9bc4e1c40d6bd4b7f592f484429). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
