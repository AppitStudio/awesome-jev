# jev-harness (Jev judgment gates for Claude Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin with judgment gates: a Stop gate that catches turns ending by announcing work not yet done, and tool gates that keep secret files away from non-Anthropic providers, with rules first, Jev only where a rule cannot decide, and shadow mode before enforcement.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ysys143/jev-harness) |
| Maintainer | [ysys143](https://github.com/ysys143). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code; a TypeSafe API key for the Jev-backed gates. |
| License | [MIT](https://github.com/ysys143/jev-harness/blob/378120117ae7f0348eb0ba710108d6c414c2705a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/jev.ts`](https://github.com/ysys143/jev-harness/blob/378120117ae7f0348eb0ba710108d6c414c2705a/hooks/jev.ts) at the pinned commit. |

## When to use

- Stop an agent from ending a turn with "Next, I will..." instead of doing the work.
- Classify tool calls in sessions served by other providers before they touch secrets.
- Mismatch: everything is off by default; you enable each gate in off, shadow or active mode.

## How it works

`hooks/jev.ts` posts to `https://api.typesafe.ai/v1/systemone`; the Stop gate asks a two-way `announce` or `report` choice on the scrubbed last paragraph and, in active mode, sends the model back when the probability reaches `stopThreshold` (0.7). Integration evidence: [`hooks/jev.ts`](https://github.com/ysys143/jev-harness/blob/378120117ae7f0348eb0ba710108d6c414c2705a/hooks/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin install jev-harness --marketplace ysys143/jev-harness
# then enable gates under /config or settings.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Gate table and settings in the README: [github.com/ysys143/jev-harness#readme](https://github.com/ysys143/jev-harness#readme)

## Limits and data handling

In shadow or active mode the scrubbed last paragraph, and for the Jev tool gate the tool name and scrubbed path or first 200 characters of a command, are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 378120117ae7](https://github.com/ysys143/jev-harness/tree/378120117ae7f0348eb0ba710108d6c414c2705a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
