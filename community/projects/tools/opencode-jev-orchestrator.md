# opencode-jev-orchestrator (OpenCode plugin where Jev decides when to escalate hard turns)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that keeps the session on a cheap sticky model so the prompt cache stays warm, and asks Jev on each managed turn whether to stay, escalate a hard turn to a stronger child subagent, or run cheap parallel children.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aaronshaf/opencode-jev-orchestrator) |
| Maintainer | [aaronshaf](https://github.com/aaronshaf). Independently curated. |
| Format | OpenCode plugin (TypeScript, MIT) |
| Requirements | OpenCode (built for OpenCode Go; Claude/Codex tier examples included) and a Jev key saved in `~/.config/opencode/opencode-jev-orchestrator.key`. |
| License | [MIT](https://github.com/aaronshaf/opencode-jev-orchestrator/blob/ffe76fed66b3d544f218cacff1947fc191688c3a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/aaronshaf/opencode-jev-orchestrator/blob/ffe76fed66b3d544f218cacff1947fc191688c3a/src/jev.ts) at the pinned commit. |

## When to use

- Save scarce strong-model quota by escalating only the turns Jev flags as hard.
- Keep a warm cache on a cheap parent model in long coding sessions.
- Mismatch: OpenCode only; an orchestrator, not a per-turn model switcher.

## How it works

`src/jev.ts` uses `@typesafe-ai/sdk` to send the session state (current model, context size, available models) with a `model_tier` choice question; the plugin acts only on confident answers and releases the strong child when Jev is down or unsure. Integration evidence: [`src/jev.ts`](https://github.com/aaronshaf/opencode-jev-orchestrator/blob/ffe76fed66b3d544f218cacff1947fc191688c3a/src/jev.ts).

## Get started

Install the plugin globally, save your Jev key to the key file, restart OpenCode and check `/jev-status`.

```sh
opencode plugin opencode-jev-orchestrator -g
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/aaronshaf/opencode-jev-orchestrator/blob/ffe76fed66b3d544f218cacff1947fc191688c3a/README.md](https://github.com/aaronshaf/opencode-jev-orchestrator/blob/ffe76fed66b3d544f218cacff1947fc191688c3a/README.md)
- npm: [www.npmjs.com/package/opencode-jev-orchestrator](https://www.npmjs.com/package/opencode-jev-orchestrator)

## Limits and data handling

Session metadata and the current turn go to TypeSafe on your key for each managed turn; coding work goes to the model providers you configured.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit ffe76fed66b3](https://github.com/aaronshaf/opencode-jev-orchestrator/tree/ffe76fed66b3d544f218cacff1947fc191688c3a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
