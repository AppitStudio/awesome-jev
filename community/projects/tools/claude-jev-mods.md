# claude-jev-mods (Claude Code mod that routes models and guards reads with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that asks Jev 1.14 (through OpenRouter) on every prompt and subagent whether the work is planning, medium coding or a clearly defined task to route it to Opus, Sonnet or Haiku, and checks guarded `Read`, `Grep`, `Glob` and `Bash` calls, blocking credential reads by rule and off-task source reads by Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/joshaustintech/claude-jev-mods) |
| Maintainer | [joshaustintech](https://github.com/joshaustintech). Independently curated. |
| Format | Claude Code plugin (TypeScript, Apache-2.0) |
| Requirements | Claude Code with plugin support and `OPENROUTER_API_KEY` in the environment Claude Code starts from; without it the mod stays silent. |
| License | [Apache-2.0](https://github.com/joshaustintech/claude-jev-mods/blob/606736757407757935219bba4524ccff7cc7f57a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/hooks/decisions.ts`](https://github.com/joshaustintech/claude-jev-mods/blob/606736757407757935219bba4524ccff7cc7f57a/jev/hooks/decisions.ts) at the pinned commit. |

## When to use

- Send easy turns to cheaper Claude models while planning stays on Opus.
- Stop an agent from reading secrets or unrelated source files.
- Mismatch: Claude Code only; relies on OpenRouter's alpha decisions endpoint.

## How it works

`jev/hooks/decisions.ts` posts the state and typed questions to OpenRouter's decisions endpoint with model `typesafe/jev-1.14`; unsure answers fall back to Opus for routing, and anything short of a clear no is blocked for guarded reads. Integration evidence: [`jev/hooks/decisions.ts`](https://github.com/joshaustintech/claude-jev-mods/blob/606736757407757935219bba4524ccff7cc7f57a/jev/hooks/decisions.ts).

## Get started

Install the plugin from the repo's marketplace inside Claude Code.

```sh
/plugin install jev --marketplace joshaustintech/claude-jev-mods
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/joshaustintech/claude-jev-mods/blob/606736757407757935219bba4524ccff7cc7f57a/README.md](https://github.com/joshaustintech/claude-jev-mods/blob/606736757407757935219bba4524ccff7cc7f57a/README.md)

## Limits and data handling

Prompts, subagent tasks and guarded tool-call details go to OpenRouter/TypeSafe on your key; Haiku rewrites subagent briefs.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 606736757407](https://github.com/joshaustintech/claude-jev-mods/tree/606736757407757935219bba4524ccff7cc7f57a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
