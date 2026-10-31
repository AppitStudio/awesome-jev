# jev-router by pyxl-dev (Claude Code mod where Jev picks the reasoning effort of each message)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Claude Code mod: on every prompt one Jev choice question rates how much effort the task needs (`low`, `medium`, `high`) in about half a second, and when Jev is at least 60% sure the main loop runs at that effort. The model is never switched, so the prompt cache is kept; a band shows Jev's pick, confidence and the effort actually used.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pyxl-dev/jev-router) |
| Maintainer | [pyxl-dev](https://github.com/pyxl-dev). Independently curated. |
| Format | Claude Code mod (TypeScript/TSX hook) |
| Requirements | Claude Code with mods support; an OpenRouter key (macOS keychain fallback). |
| License | [MIT](https://github.com/pyxl-dev/jev-router/blob/80c168baf80a916463cdf84c0d8cdb0e56e67cba/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/register.tsx`](https://github.com/pyxl-dev/jev-router/blob/80c168baf80a916463cdf84c0d8cdb0e56e67cba/hooks/register.tsx) at the pinned commit. |

## When to use

- Spend less thinking time on trivial prompts without changing models.
- Mismatch: only effort is routed; subagents, slash commands and very short messages are left alone.

## How it works

`hooks/register.tsx` calls `typesafe/jev-1.13` on OpenRouter with a 0.6 confidence threshold and a 3 s wait cap; slow or failed calls leave the message unchanged. Integration evidence: [`hooks/register.tsx`](https://github.com/pyxl-dev/jev-router/blob/80c168baf80a916463cdf84c0d8cdb0e56e67cba/hooks/register.tsx).

## Get started

From the upstream README (not run on the review host):

```sh
# install the mod per the README, then set the OpenRouter key in the plugin options
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/pyxl-dev/jev-router#readme](https://github.com/pyxl-dev/jev-router#readme)

## Limits and data handling

Each prompt is sent to OpenRouter for the effort question. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 80c168baf80a](https://github.com/pyxl-dev/jev-router/tree/80c168baf80a916463cdf84c0d8cdb0e56e67cba). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
