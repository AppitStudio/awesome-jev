# AutoRouter (claude-autorouter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Independent local gateway that routes each Claude Code request across Haiku, Sonnet and Opus after an evaluator rates it — a local Ollama `/v1/systemone` model by default, or hosted TypeSafe Jev with `--evaluator jev` — checking model compatibility and context capacity first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frapposelli/claude-autorouter) |
| Product homepage | [www.npmjs.com](https://www.npmjs.com/package/claude-autorouter) |
| Maintainer | [frapposelli](https://github.com/frapposelli). Independently curated. |
| Format | CLI + local gateway (npm `claude-autorouter`, 0.5.2 at review) |
| Requirements | Node.js 22+, macOS or Linux/WSL, the official `claude` CLI with your own subscription login or Anthropic key; Ollama 0.35+ (default) or `TYPESAFE_API_KEY` for the Jev evaluator. |
| License | [Apache-2.0](https://github.com/frapposelli/claude-autorouter/blob/ea930c247626ce2af5ccdad721b5121417bf4ad8/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Mix Haiku/Sonnet/Opus per request in Claude Code without switching models by hand.
- Compare a local Ollama evaluator with hosted Jev using `doctor --evaluate-local` and the evaluation report.
- Mismatch: Jev is optional, not the default; the gateway forwards your own Claude credentials (see upstream integration boundaries).

## How it works

`claude-autorouter claude` launches the unmodified official Claude Code against a local gateway. Per request the router asks the evaluator for a tier ([`src/router.mjs`](https://github.com/frapposelli/claude-autorouter/blob/ea930c247626ce2af5ccdad721b5121417bf4ad8/src/router.mjs) defines the Jev question set; [`src/config.mjs`](https://github.com/frapposelli/claude-autorouter/blob/ea930c247626ce2af5ccdad721b5121417bf4ad8/src/config.mjs) sets `AUTOROUTER_JEV_URL` default `https://api.typesafe.ai/v1/systemone`, model `jev-latest`), then checks compatibility and context before forwarding.

## Get started

Install, set up with the Jev evaluator, and launch inside a project:

```sh
npm install -g claude-autorouter
claude-autorouter setup --evaluator jev   # prompts for TYPESAFE_API_KEY; default setup uses local Ollama
claude-autorouter doctor
cd /path/to/project && claude-autorouter claude
```

Jev evaluations are billed by TypeSafe; Claude usage follows your subscription or API billing.

## Examples and demos

- [Ollama evaluation guide](https://github.com/frapposelli/claude-autorouter/blob/ea930c247626ce2af5ccdad721b5121417bf4ad8/docs/ollama-evaluation.md) and `scripts/evaluate.mjs`.
- README `config`, `sessions` and `doctor` commands.

## Limits and data handling

Not affiliated with Anthropic; the README states subscription forwarding is a technical integration, not a claim of provider approval — review its integration boundaries. With the Jev evaluator, request summaries go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit ea930c247626](https://github.com/frapposelli/claude-autorouter/tree/ea930c247626ce2af5ccdad721b5121417bf4ad8). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
