# adaptive-effort by Murilo Rocha (Claude Code plugin where Jev picks each turn's reasoning effort and measures the tokens saved)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that asks Jev which reasoning effort each new prompt needs (low to max) and sends that turn's requests at the chosen level, leaving the session setting unchanged. A share of turns is held out at the session's effort, so the savings line under each answer is estimated from measured turns rather than an assumed ratio.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/smurilosrocha/adaptive-effort) |
| Maintainer | [Murilo Rocha](https://github.com/smurilosrocha). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code with plugin support and a TypeSafe API key (plugin option, `TYPESAFE_API_KEY`, or the DSH `jev/api-key` record). |
| License | [MIT](https://github.com/smurilosrocha/adaptive-effort/blob/14de456d4ccfb0961b8cf6824eebf35e009c190e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/register.ts`](https://github.com/smurilosrocha/adaptive-effort/blob/14de456d4ccfb0961b8cf6824eebf35e009c190e/hooks/register.ts) at the pinned commit. |

## When to use

- Claude Code users who keep a high default effort and want routine turns to run cheaper.
- Mismatch: guaranteed savings; the estimate is per model and task class and needs baseline samples first.

## How it works

`hooks/register.ts` posts the first 4,000 characters of the prompt plus up to six recent messages to `https://api.typesafe.ai/v1/systemone` (model `jev-latest`) with one `choice` question; lowering effort applies at any confidence, raising it needs 0.55 by default. Timeouts, errors or no key leave the turn at the session's effort. Integration evidence: [`hooks/register.ts`](https://github.com/smurilosrocha/adaptive-effort/blob/14de456d4ccfb0961b8cf6824eebf35e009c190e/hooks/register.ts).

## Get started

Add the author's marketplace and install the plugin, then give it your TypeSafe key.

```sh
claude plugin install adaptive-effort --marketplace smurilosrocha/adaptive-effort
export TYPESAFE_API_KEY=...   # or enter it on the install screen
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How the savings are estimated: [github.com/smurilosrocha/adaptive-effort#how-the-savings-are-estimated](https://github.com/smurilosrocha/adaptive-effort#how-the-savings-are-estimated)

## Limits and data handling

Prompt text (first 4,000 characters) and up to 2,400 characters of prior conversation go to TypeSafe for every new prompt unless the folder is listed in `excludeFolders`. About 500 Jev tokens per prompt in the author's measurement; identical prompts within 15 minutes reuse the verdict.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 14de456d4ccf](https://github.com/smurilosrocha/adaptive-effort/tree/14de456d4ccfb0961b8cf6824eebf35e009c190e). Inspected the README, LICENSE and `hooks/register.ts` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
