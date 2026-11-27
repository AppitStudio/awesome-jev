# opencode-jev by Nicolás Hermosilla (agent skill for building with Jev through an OpenCode Go subscription)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Agent skill that teaches coding agents to build with Jev when they reach it through OpenCode Go instead of TypeSafe's API. It keeps the guidance from TypeSafe's MIT integration skill (state design, typed questions, reading probabilities) and swaps the connection details: OpenCode Go's System One endpoint, `OPENCODE_API_KEY` and `jev-1.14`. Installs with `npx skills` or as a Claude Code plugin. Unofficial; not affiliated with TypeSafe or OpenCode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nhermosilla14/opencode-jev) |
| Maintainer | [Nicolás Hermosilla](https://github.com/nhermosilla14) (nhermosilla14). Independently curated. |
| Format | Agent skill (SKILL.md) + Claude Code plugin manifest |
| Requirements | An agent that loads skills (Claude Code, OpenCode and others) and an OpenCode Go subscription key for live calls. |
| License | [MIT](https://github.com/nhermosilla14/opencode-jev/blob/bc215e9916c9406be37af1a75728e69b32c573d3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/opencode-jev/SKILL.md`](https://github.com/nhermosilla14/opencode-jev/blob/bc215e9916c9406be37af1a75728e69b32c573d3/skills/opencode-jev/SKILL.md) at the pinned commit. |

## When to use

- Developers who pay for OpenCode Go and want their coding agent to write correct Jev calls for that endpoint.
- Mismatch: direct TypeSafe accounts; use TypeSafe's own skill instead.

## How it works

`skills/opencode-jev/SKILL.md` points agents at `https://opencode.ai/inference/go/systemone/v1/systemone` with `OPENCODE_API_KEY` and `jev-1.14`; request and response bodies match TypeSafe's API. Usage is billed against the OpenCode Go allowance at Jev list price. Integration evidence: [`skills/opencode-jev/SKILL.md`](https://github.com/nhermosilla14/opencode-jev/blob/bc215e9916c9406be37af1a75728e69b32c573d3/skills/opencode-jev/SKILL.md).

## Get started

Add the skill to your agent, then check your key with the curl in the README.

```sh
npx skills add nhermosilla14/opencode-jev
# Claude Code:
# /plugin marketplace add nhermosilla14/opencode-jev
# /plugin install opencode-jev@opencode-jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skill file: [github.com/nhermosilla14/opencode-jev/blob/main/skills/opencode-jev/SKILL.md](https://github.com/nhermosilla14/opencode-jev/blob/main/skills/opencode-jev/SKILL.md)

## Limits and data handling

The README notes that TypeSafe's image and long-context headers are unverified through the gateway, and prices, models and limits can change. The LICENSE keeps TypeSafe AI's MIT copyright from the forked skill.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit bc215e9916c9](https://github.com/nhermosilla14/opencode-jev/tree/bc215e9916c9406be37af1a75728e69b32c573d3). Inspected the README, LICENSE, plugin manifests and `SKILL.md` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
