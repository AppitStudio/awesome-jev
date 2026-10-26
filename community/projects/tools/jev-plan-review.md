# jev-plan-review (Claude Code plugin that checks a plan keeps every requirement you stated)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that collects what you said (prompts, answers, rejected-plan feedback, pasted text), splits it into statements and has Jev check each one against the plan, flagging anything missing or contradicted with a confidence score; it runs as a plan-mode hook or a review command and also lists decisions you never asked for.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chinmayakelkar/jev-plan-review) |
| Maintainer | [chinmayakelkar](https://github.com/chinmayakelkar). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code; a TypeSafe API key, or an OpenRouter key. |
| License | [MIT](https://github.com/chinmayakelkar/jev-plan-review/blob/7706cae8949d90b3cbae0003f049f841e9969218/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/chinmayakelkar/jev-plan-review/blob/7706cae8949d90b3cbae0003f049f841e9969218/src/jev.ts) at the pinned commit. |

## When to use

- Catch requirements Claude dropped before you approve a plan.
- See which assumptions in a plan you never agreed to.
- Mismatch: checks plans, not code; the hook sends fixes back to Claude, the command never edits the plan.

## How it works

`src/jev.ts` posts your statements and the plan to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`), or to OpenRouter's System One route when configured; only what came after the last `/clear` and approved plan is collected. Integration evidence: [`src/jev.ts`](https://github.com/chinmayakelkar/jev-plan-review/blob/7706cae8949d90b3cbae0003f049f841e9969218/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add chinmayakelkar/jev-plan-review
claude plugin install jev-plan-review@jev-plan-review
# set TYPESAFE_API_KEY in Claude Code settings env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/chinmayakelkar/jev-plan-review#readme](https://github.com/chinmayakelkar/jev-plan-review#readme)

## Limits and data handling

Your statements and the plan text go to TypeSafe or OpenRouter. The plugin does not store or log the key.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 7706cae8949d](https://github.com/chinmayakelkar/jev-plan-review/tree/7706cae8949d90b3cbae0003f049f841e9969218). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
