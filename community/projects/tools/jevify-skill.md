# Jevify (Claude Code/Codex skill that audits a repo and converts fitting LLM decision calls to Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill that audits your codebase for LLM calls that are really decisions, shows the plan, then converts the ones that fit to Jev on a branch, a copy or individually.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kevin-Zhouu/jevify) |
| Maintainer | [Kevin-Zhouu](https://github.com/Kevin-Zhouu). Independently curated. |
| Format | Agent skill via `npx skills` (MIT) |
| Requirements | Claude Code or Codex, `npx skills add Kevin-Zhouu/jevify`, and a TypeSafe/OpenRouter key to run converted calls. |
| License | [MIT](https://github.com/Kevin-Zhouu/jevify/blob/bcd75922cf6241d4bf98ef711c4f115f6607b8dc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/jevify/SKILL.md`](https://github.com/Kevin-Zhouu/jevify/blob/bcd75922cf6241d4bf98ef711c4f115f6607b8dc/skills/jevify/SKILL.md) at the pinned commit. |

## When to use

- Find LLM calls that should be typed decisions.
- Migrate classification prompts to Jev safely.
- Mismatch: you review each conversion; the audit itself needs no key.

## How it works

`skills/jevify/SKILL.md` drives the audit and conversion; `scripts/preflight.py` and `with_jev_key.py` check setup, and `docs/demos/jevify-session` holds a real run producing `jev_decisions.py`. Integration evidence: [`skills/jevify/SKILL.md`](https://github.com/Kevin-Zhouu/jevify/blob/bcd75922cf6241d4bf98ef711c4f115f6607b8dc/skills/jevify/SKILL.md).

## Get started

Run `npx skills add Kevin-Zhouu/jevify`, then `/jevify` in Claude Code or `$jevify` in Codex.

```sh
npx skills add Kevin-Zhouu/jevify
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Kevin-Zhouu/jevify/blob/bcd75922cf6241d4bf98ef711c4f115f6607b8dc/README.md](https://github.com/Kevin-Zhouu/jevify/blob/bcd75922cf6241d4bf98ef711c4f115f6607b8dc/README.md)

## Limits and data handling

Converted calls send their inputs to TypeSafe/OpenRouter at runtime.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit bcd75922cf62](https://github.com/Kevin-Zhouu/jevify/tree/bcd75922cf6241d4bf98ef711c4f115f6607b8dc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
