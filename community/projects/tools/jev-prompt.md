# jev-prompt (Claude Code mod that grades the prompt you are typing, live, and shows one advisory line about what it lacks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that waits for a pause while you type, grades the draft with Jev through OpenRouter, and shows one line above the prompt box naming the kind of prompt and what seems missing (for example `bug fix · missing: expected result, the failing command`). It is advisory only: it never blocks a submit or rewrites your text, and it stays quiet when uncertain. The README calls it a reference mod and says the hints are not shown to improve prompts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/filip-a-9/jev-prompt) |
| Maintainer | [filip-a-9](https://github.com/filip-a-9). Independently curated. |
| Format | Claude Code mod and plugin marketplace entry (TypeScript) |
| Requirements | Claude Code 2.1.287+ with mods turned on (early-access API) and an OpenRouter API key. |
| License | [MIT](https://github.com/filip-a-9/jev-prompt/blob/477678029afd450a7068b8d651a7ad3db417aef5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/filip-a-9/jev-prompt/blob/477678029afd450a7068b8d651a7ad3db417aef5/src/jev.ts) at the pinned commit. |

## When to use

- See a working example of grading text live inside a Claude Code mod with a decision model.
- Mismatch: the OpenRouter decisions endpoint is alpha, and whether the hints improve prompts has not been shown.

## How it works

`src/jev.ts` sends each draft with typed questions to `https://openrouter.ai/api/alpha/decisions` using a dated Jev model pin; `src/rubric.ts` holds the questions, and the grades are shown only when the model is confident. Integration evidence: [`src/jev.ts`](https://github.com/filip-a-9/jev-prompt/blob/477678029afd450a7068b8d651a7ad3db417aef5/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add filip-a-9/jev-prompt
/plugin install jev-prompt@jev-prompt
/plugin configure jev-prompt@jev-prompt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the rubric, privacy notes and evidence section: [github.com/filip-a-9/jev-prompt#readme](https://github.com/filip-a-9/jev-prompt#readme)

## Limits and data handling

Each grade sends the draft prompt (after the mod's redaction step) to OpenRouter on your key. The endpoint is alpha, the dated model pin may be retired, and changing the model gives uncalibrated grades. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 477678029afd](https://github.com/filip-a-9/jev-prompt/tree/477678029afd450a7068b8d651a7ad3db417aef5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
