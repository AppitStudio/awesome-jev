# claude-mods by kzarzycki (Claude Code mods rebuilding oh-my-pi features, with a shared Jev decision model for effort, stop and rule checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugins that run inside Claude Code's engine through its in-process hook API, installed one by one from the repo's marketplace. The first set rebuilds features of the oh-my-pi coding harness. `decision-model` gives other mods `$.decision.ask({ state, questions })` with System One choice, noul and score questions, Jev by default. `auto-effort` asks it how open-ended each prompt is and sets that turn's effort; `resume-on-stop` spots a turn that stops on "let me run the tests next" without acting and gives it one resume turn; `ttsr-rules` applies oh-my-pi rule files to tool calls. Other mods (compaction methods, agent hub, eval kernel) need no decision model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kzarzycki/claude-mods) |
| Maintainer | [kzarzycki](https://github.com/kzarzycki). Independently curated. |
| Format | Claude Code plugin marketplace (TypeScript, MIT) |
| Requirements | Claude Code 2.1.288+ (tested on 2.1.326) and an OpenRouter or TypeSafe key for the decision model; without a key a small Claude model answers the same questions as text. |
| License | [MIT](https://github.com/kzarzycki/claude-mods/blob/ebc4b416e3da112ff87a4cee833fe48b4302a155/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/decision-model/hooks/register.ts`](https://github.com/kzarzycki/claude-mods/blob/ebc4b416e3da112ff87a4cee833fe48b4302a155/plugins/decision-model/hooks/register.ts) at the pinned commit. |

## When to use

- Set Claude Code's effort per prompt and recover turns that stop early, using cheap Jev checks.
- Mismatch: older Claude Code versions; the mods need the in-process hook API.

## How it works

`plugins/decision-model/hooks/register.ts` defines presets for OpenRouter's decisions API (`~typesafe/jev-latest`, the default) and `https://api.typesafe.ai/v1/systemone` (`jev-latest`), or any URL that speaks the protocol, keyed by `OPENROUTER_API_KEY` or `TYPESAFE_API_KEY`. Integration evidence: [`plugins/decision-model/hooks/register.ts`](https://github.com/kzarzycki/claude-mods/blob/ebc4b416e3da112ff87a4cee833fe48b4302a155/plugins/decision-model/hooks/register.ts).

## Get started

Add the marketplace and install the mods you want; mods that decide pull in `decision-model`.

```sh
claude plugin marketplace add kzarzycki/claude-mods
claude plugin install auto-effort@claude-mods     # pulls in decision-model
claude plugin install resume-on-stop@claude-mods
export OPENROUTER_API_KEY=...   # or TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kzarzycki/claude-mods/blob/ebc4b416e3da112ff87a4cee833fe48b4302a155/README.md](https://github.com/kzarzycki/claude-mods/blob/ebc4b416e3da112ff87a4cee833fe48b4302a155/README.md)

## Limits and data handling

Prompts, turn endings and tool calls the mods check are sent to OpenRouter/TypeSafe on your key. Parts are adapted from oh-my-pi (MIT), as the license notes.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit ebc4b416e3da](https://github.com/kzarzycki/claude-mods/tree/ebc4b416e3da112ff87a4cee833fe48b4302a155). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
