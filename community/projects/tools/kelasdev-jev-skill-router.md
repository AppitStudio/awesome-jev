# Jev Skill Router (kelasdev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode V2 plugin that follows TypeSafe's skill-suggestion cookbook: two gated Jev calls pick at most one `SKILL.md` to inject into the main model prompt, or inject nothing on failure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kelasdev/jev-skill-router) |
| Maintainer | [kelasdev](https://github.com/kelasdev). Independently curated. |
| Format | TypeScript · OpenCode plugin |
| Requirements | OpenCode; TypeSafe credentials for `/v1/systemone`. |
| License | [MIT](https://github.com/kelasdev/jev-skill-router/blob/3e5169edb10ff3d11a8fa5471be7d8a62aa7c537/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Large OpenCode skill catalogs where injecting the wrong skill wastes context.
- Mismatch: Distinct from Claude Code `jev-skill-suggestion` and from `jev-skill-router-bench`.

## How it works

User message → local pre-check → roster of skills → Choice rank → second gated pass; inject one or none. Jev client: [`src/jev.ts`](https://github.com/kelasdev/jev-skill-router/blob/3e5169edb10ff3d11a8fa5471be7d8a62aa7c537/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# install as OpenCode plugin per upstream README
git clone https://github.com/kelasdev/jev-skill-router.git
```

## Limits and data handling

Prompt and skill descriptions go to TypeSafe when calls run; billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 3e5169edb10f](https://github.com/kelasdev/jev-skill-router/tree/3e5169edb10ff3d11a8fa5471be7d8a62aa7c537). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
