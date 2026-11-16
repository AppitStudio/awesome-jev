# pi-sieve (Pi coding agent suite with semantic model routing, hybrid compaction and guardrails, using Jev or other decision classifiers when available)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Extension suite for the Pi coding agent: semantic routing that picks a model for each turn, two-stage hybrid compaction (deterministic masking of duplicate and bulky tool output, classifier rescue of ambiguous output, then a summary cascade), durable tabs, internal tooling and guardrails. Routing and compaction detect and cascade across every System One / decision classifier Pi knows about, with Jev as the first choice; with none configured it falls back to deterministic heuristics.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DrMkdaddy/pi-sieve) |
| Maintainer | [DrMkdaddy](https://github.com/DrMkdaddy). Independently curated. |
| Format | Pi agent extension package (TypeScript, MIT) |
| Requirements | Node.js 22.18+, the Pi coding agent CLI and a chat model provider; for Jev an OpenCode login (free `jev-1.13-free`) or an OpenRouter, Cloudflare, Vercel AI Gateway or TypeSafe key. |
| License | [MIT](https://github.com/DrMkdaddy/pi-sieve/blob/bc2491cb12b4bf250b704bc4ca9428a2304ee813/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classifier-adapter.ts`](https://github.com/DrMkdaddy/pi-sieve/blob/bc2491cb12b4bf250b704bc4ca9428a2304ee813/src/classifier-adapter.ts) at the pinned commit. |

## When to use

- Keep long Pi sessions cheaper and on track with typed routing and compaction decisions.
- Mismatch: other coding agents; it is built on Pi's extension API.

## How it works

`src/classifier-adapter.ts` lists the classifier cascade: `opencode/jev-1.13-free` first, then OpenRouter `typesafe/jev-1.14` and `typesafe/jev-1.13`, Workers AI `typesafe/jev-1.14.0`, TypeSafe direct `jev-latest`, and Clef and local System One endpoints. Integration evidence: [`src/classifier-adapter.ts`](https://github.com/DrMkdaddy/pi-sieve/blob/bc2491cb12b4bf250b704bc4ca9428a2304ee813/src/classifier-adapter.ts).

## Get started

Install the package into Pi and run the doctor to see which classifiers it found.

```sh
pi install git:github.com/DrMkdaddy/pi-sieve
# inside Pi:
/sieve-doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DrMkdaddy/pi-sieve/blob/bc2491cb12b4bf250b704bc4ca9428a2304ee813/README.md](https://github.com/DrMkdaddy/pi-sieve/blob/bc2491cb12b4bf250b704bc4ca9428a2304ee813/README.md)

## Limits and data handling

Jev is optional: without a decision classifier it uses deterministic heuristics, and Clef or local models can replace Jev. With Jev, prompts and tool-output snippets go to the chosen provider on your login or key. Benchmarks in the README are the maker's own.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit bc2491cb12b4](https://github.com/DrMkdaddy/pi-sieve/tree/bc2491cb12b4bf250b704bc4ca9428a2304ee813). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
