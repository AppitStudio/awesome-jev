# dot-pi by Yosi Taguri (Pi coding-agent package with Jev guardrails: auto thinking level, verify-before-done gate, loop detector)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent package with a Claude-Code-style statusline and three Jev-powered extensions: autothink rates each prompt minimal/low/medium/high and sets the thinking level, settle-gate sends unverified "done" or "tests pass" claims back to verify and turns plain-text questions into AskUserQuestion calls, and loop-detector notices a failing retry loop. Code owns the facts (what was edited, what ran, what failed), Jev only judges the language, and everything fails open.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yosit/dot-pi) |
| Maintainer | [Yosi Taguri](https://github.com/yosit) (yosit). Independently curated. |
| Format | Pi package (TypeScript extensions + prompts) |
| Requirements | The Pi coding agent and a TypeSafe API key (from the environment or a psst vault); the statusline works without one. |
| License | [MIT](https://github.com/yosit/dot-pi/blob/cf04147ca4520c277b8950261aeb116a8bc57a9a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/yosit/dot-pi/blob/cf04147ca4520c277b8950261aeb116a8bc57a9a/src/jev.ts) at the pinned commit. |

## When to use

- Pi users who want the agent to verify before claiming success and to spend reasoning only where a prompt needs it.
- Mismatch: other coding agents; the extensions use Pi's hooks.

## How it works

`src/jev.ts` posts batched questions to TypeSafe's `/v1/systemone` with the configured model and returns answers, latency and token use; the extensions in `extensions/` decide from those probabilities with confidence floors (for example, autothink takes the higher level under 60% confidence). Integration evidence: [`src/jev.ts`](https://github.com/yosit/dot-pi/blob/cf04147ca4520c277b8950261aeb116a8bc57a9a/src/jev.ts).

## Get started

Install the package into Pi and add your TypeSafe key.

```sh
pi install git:github.com/yosit/dot-pi
export TYPESAFE_API_KEY=...
# then /reload in a running pi
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example config: [github.com/yosit/dot-pi/blob/main/examples/dot-pi.json](https://github.com/yosit/dot-pi/blob/main/examples/dot-pi.json)
- Extensions: [github.com/yosit/dot-pi/tree/main/extensions](https://github.com/yosit/dot-pi/tree/main/extensions)

## Limits and data handling

Prompts, the tail of assistant messages and short tool histories go to TypeSafe on each check; autothink adds one Jev round trip (about 270 ms p50 per the README) before every turn.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit cf04147ca452](https://github.com/yosit/dot-pi/tree/cf04147ca4520c277b8950261aeb116a8bc57a9a). Inspected the README, LICENSE, `src/jev.ts` and `extensions/settle-gate.ts` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
