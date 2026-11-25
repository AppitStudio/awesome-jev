# jev-guard by Breadway (OpenCode plugin where Jev allows, denies or escalates each non-read-only tool call)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode permission plugin. Read-only tools skip classification; every other tool call (shell, edit, subagent, web fetch, MCP tools) goes to Jev, which returns allow, deny or escalate. Hard-coded denies for destructive commands such as `rm -rf /` or `mkfs` apply even without a key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Breadway/jev-guard) |
| Maintainer | [Breadway](https://github.com/Breadway). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode and an OpenCode Zen API key (`OPENCODE_ZEN_API_KEY`). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.ts`](https://github.com/Breadway/jev-guard/blob/e4450e1d6974bcdc6c533d916c0ccc2366acfcb7/index.ts) at the pinned commit. |

## When to use

- Let Jev pre-screen risky tool calls in OpenCode instead of approving each one.
- Mismatch: if you need a TypeSafe-direct integration; this uses OpenCode Zen.

## How it works

`index.ts` sends the action, up to 8 resource strings, the agent ID and recent user and assistant text to Jev 1.13 (free tier first) at `https://opencode.ai/zen/v1/systemone`, OpenCode's hosted Jev endpoint. Verdicts are cached per action and resource. Integration evidence: [`index.ts`](https://github.com/Breadway/jev-guard/blob/e4450e1d6974bcdc6c533d916c0ccc2366acfcb7/index.ts).

## Get started

Add your OpenCode Zen key and restart the OpenCode service.

```sh
export OPENCODE_ZEN_API_KEY="..."
opencode service restart
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Breadway/jev-guard/blob/e4450e1d6974bcdc6c533d916c0ccc2366acfcb7/README.md](https://github.com/Breadway/jev-guard/blob/e4450e1d6974bcdc6c533d916c0ccc2366acfcb7/README.md)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Requests (including recent transcript slices) and your key go to OpenCode Zen, a third-party Jev host, not to TypeSafe directly. Without a key the plugin fails open apart from the hard denies. A model verdict is not a reliable sole security boundary.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit e4450e1d6974](https://github.com/Breadway/jev-guard/tree/e4450e1d6974bcdc6c533d916c0ccc2366acfcb7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
