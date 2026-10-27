# JEV Shield by JamesANZ (Jev-scored prompt-injection and command gate for coding agents)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Guard that sits outside the model: it scores incoming prompts and pasted text for injection with Jev, and checks proposed shell commands (local rules first, Jev for the rest), then ordinary code maps the probabilities to allow, ask or block, including as a Claude Code permission hook; the README walks through a Gandalf password-game test.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JamesANZ/JevPromptShield) |
| Maintainer | [JamesANZ](https://github.com/JamesANZ). Independently curated. |
| Format | Node.js CLI and library (npm `jev-shield`) |
| Requirements | Node.js 20+; a TypeSafe API key. |
| License | [MIT](https://github.com/JamesANZ/JevPromptShield/blob/9704add57be26d0ed805cdbdfd46070a2a9aba47/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/engine/questions.ts`](https://github.com/JamesANZ/JevPromptShield/blob/9704add57be26d0ed805cdbdfd46070a2a9aba47/src/engine/questions.ts) at the pinned commit. |

## When to use

- Add an outside check on prompts and Bash commands for Claude Code or your own agent.
- Keep the final allow/ask/block decision in code.
- Mismatch: distinct from the separately listed jev-shield by caiovicentino.

## How it works

`src/engine/questions.ts` builds Noul and Choice question sets with `@typesafe-ai/sdk` (pinned `jev-1.13.0` in `src/config.ts`); thresholds in code turn the answers into a decision. Integration evidence: [`src/engine/questions.ts`](https://github.com/JamesANZ/JevPromptShield/blob/9704add57be26d0ed805cdbdfd46070a2a9aba47/src/engine/questions.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install --global jev-shield
# or from source: npm install && npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/JamesANZ/JevPromptShield#readme](https://github.com/JamesANZ/JevPromptShield#readme)

## Limits and data handling

Prompts, pasted text and commands that are not settled locally go to TypeSafe. Test figures are the author's.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 9704add57be2](https://github.com/JamesANZ/JevPromptShield/tree/9704add57be26d0ed805cdbdfd46070a2a9aba47). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
