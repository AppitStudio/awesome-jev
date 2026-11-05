# jev-enconvo (Enconvo extension and skill for running Jev judge and classify steps in chat, computer-use and browser-use workflows)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Enconvo plugin with a `jev-enconvo` skill and three no-view commands for running Jev inside Enconvo: `uses: judge` and `uses: classify` workflow steps, TypeSafe primitive-to-Enconvo mapping, option label maps, threshold and branch patterns, and notes on billing, dry runs and where Jev does not belong.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Iteractive-Development/jev-enconvo) |
| Maintainer | [Iteractive-Development](https://github.com/Iteractive-Development). Independently curated. |
| Format | Enconvo extension (TypeScript, built with tsup) plus a Claude-style skill |
| Requirements | Enconvo on macOS, Node.js with dev dependencies for the build, and a TypeSafe key. |
| License | [MIT](https://github.com/Iteractive-Development/jev-enconvo/blob/e9ac96fa6272f604c323442dc72195aa82ead1d3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/jev.ts`](https://github.com/Iteractive-Development/jev-enconvo/blob/e9ac96fa6272f604c323442dc72195aa82ead1d3/src/lib/jev.ts) at the pinned commit. |

## When to use

- Add Jev judgment steps to Enconvo workflows without browser or app host.
- Reuse the documented threshold and branch patterns in your own flows.
- Mismatch: installs as a source build into a running Enconvo, not from a marketplace.

## How it works

`src/lib/jev.ts` is the Jev client used by the extension commands in `src/` (inbox triage, content and vision screening, drift check); the skill in `skills/jev-enconvo/SKILL.md` documents how to call Jev from workflow steps. Integration evidence: [`src/lib/jev.ts`](https://github.com/Iteractive-Development/jev-enconvo/blob/e9ac96fa6272f604c323442dc72195aa82ead1d3/src/lib/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cd marketplace/plugins/jev-enconvo
npm install --include=dev
npm run build   # enconvo plugin build installs it
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README and install notes: [github.com/Iteractive-Development/jev-enconvo/blob/e9ac96fa6272f604c323442dc72195aa82ead1d3/README.md](https://github.com/Iteractive-Development/jev-enconvo/blob/e9ac96fa6272f604c323442dc72195aa82ead1d3/README.md)
- Skill with workflow patterns: [github.com/Iteractive-Development/jev-enconvo/blob/e9ac96fa6272f604c323442dc72195aa82ead1d3/skills/jev-enconvo/SKILL.md](https://github.com/Iteractive-Development/jev-enconvo/blob/e9ac96fa6272f604c323442dc72195aa82ead1d3/skills/jev-enconvo/SKILL.md)

## Limits and data handling

Workflow content and screenshots you route through the steps go to TypeSafe on your key and may consume Enconvo points; measurements in the skill are the author's own.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit e9ac96fa6272](https://github.com/Iteractive-Development/jev-enconvo/tree/e9ac96fa6272f604c323442dc72195aa82ead1d3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
