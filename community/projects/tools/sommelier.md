# sommelier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin (Chinese and English READMEs) that has Jev judge reasoning depth per request and picks model and effort, upgrading freely but downgrading cautiously for cache reasons.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wide3751/sommelier) |
| Maintainer | [wide3751](https://github.com/wide3751). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code with mods API, TypeSafe API key (stored in macOS Keychain or env). |
| License | [MIT](https://github.com/wide3751/sommelier/blob/889dc416da9fd52fdf67fb4a564d7df15ca2c90e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/register.ts`](https://github.com/wide3751/sommelier/blob/889dc416da9fd52fdf67fb4a564d7df15ca2c90e/hooks/register.ts) at the pinned commit. |

## When to use

- Automatically send lookups to Haiku and design work to Opus inside Claude Code.
- Mismatch: macOS Keychain flow is the documented default.

## How it works

Jev scores reasoning depth L0–L3 and related judgments; code maps levels to model/effort presets and applies a cache-aware upgrade/downgrade policy. Integration evidence: [`hooks/register.ts`](https://github.com/wide3751/sommelier/blob/889dc416da9fd52fdf67fb4a564d7df15ca2c90e/hooks/register.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add wide3751/sommelier
claude plugin install sommelier@sommelier
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: `README.en.md`.
- Eval script: `eval/run_eval.py`.

## Limits and data handling

Request text goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 889dc416da9f](https://github.com/wide3751/sommelier/tree/889dc416da9fd52fdf67fb4a564d7df15ca2c90e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
