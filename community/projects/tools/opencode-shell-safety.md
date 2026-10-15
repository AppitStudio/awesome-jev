# opencode-shell-safety

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode v2 plugin that asks Jev to classify shell permission requests against the active agent definition and its filesystem policy, via OpenCode Zen or the TypeSafe API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexandru/opencode-shell-safety) |
| Maintainer | [alexandru](https://github.com/alexandru). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode v2; an OpenCode Zen token or `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/alexandru/opencode-shell-safety/blob/521a336b4d4fd2d1c6ad042ca535d0c120b14141/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.ts`](https://github.com/alexandru/opencode-shell-safety/blob/521a336b4d4fd2d1c6ad042ca535d0c120b14141/src/index.ts) at the pinned commit. |

## When to use

- Auto-approve or block shell commands for read-only agents (e.g. an Explorer agent) based on their policy.
- Use Jev through OpenCode Zen without a separate TypeSafe account.
- Mismatch: a permission classifier; keep hard sandboxing in place.

## How it works

When OpenCode requests shell permission, the plugin sends the command, the agent definition and its filesystem policy to a System One endpoint (`/v1/systemone`, model `jev-1.13` via Zen or `jev-1.13.0` via TypeSafe) and maps the typed answer to allow or deny. Integration evidence: [`src/index.ts`](https://github.com/alexandru/opencode-shell-safety/blob/521a336b4d4fd2d1c6ad042ca535d0c120b14141/src/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# ~/.config/opencode/opencode.jsonc (TypeSafe route)
{ "plugins": [ { "package": "opencode-shell-safety",
  "options": { "endpoint": "https://api.typesafe.ai/v1/systemone", "model": "jev-1.13.0", "apiKeyEnv": "TYPESAFE_API_KEY" } } ] }
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Used in the author's OpenCode configuration: [github.com/alexandru/opencode-config](https://github.com/alexandru/opencode-config)

## Limits and data handling

Shell commands and agent policy text are sent to OpenCode Zen or TypeSafe, billed to that account.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 521a336b4d4f](https://github.com/alexandru/opencode-shell-safety/tree/521a336b4d4fd2d1c6ad042ca535d0c120b14141). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
