# carlosziegler/model-routing (Claude Code skill: TypeSafe Jev picks the cheapest verified model lane)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill that classifies each coding task with TypeSafe Jev, routes it to the cheapest model lane that can still be verified, runs headless workers, and cross-checks with a multi-vendor review panel plus a cost ledger.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CarlosZiegler/model-routing) |
| Maintainer | [CarlosZiegler](https://github.com/CarlosZiegler). Independently curated. |
| Format | Claude Code skill (TypeScript, MIT) |
| Requirements | Claude Code (or compatible host) and a TypeSafe API key file at `~/.config/typesafe/key` (or TYPESAFE_KEY_FILE). |
| License | [MIT](https://github.com/CarlosZiegler/model-routing/blob/b8dbe9cb02f42031538226222427a67ac8350dd4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/model-routing/route.ts`](https://github.com/CarlosZiegler/model-routing/blob/b8dbe9cb02f42031538226222427a67ac8350dd4/skills/model-routing/route.ts) at the pinned commit. |

## When to use

- Route coding tasks to cheaper models with Jev classification.
- Keep a cross-vendor review panel and cost ledger.
- Mismatch: skill/workflow pack; not a standalone IDE.

## How it works

`skills/model-routing/route.ts` POSTs to `https://api.typesafe.ai/v1/systemone` with model `jev-latest`, reading the key from `~/.config/typesafe/key`. Integration evidence: [`skills/model-routing/route.ts`](https://github.com/CarlosZiegler/model-routing/blob/b8dbe9cb02f42031538226222427a67ac8350dd4/skills/model-routing/route.ts).

## Get started

Install the skill per README and place your TypeSafe key in `~/.config/typesafe/key`.

```sh
git clone https://github.com/CarlosZiegler/model-routing.git && cd model-routing
# place TYPESAFE_API_KEY in ~/.config/typesafe/key
# follow skills/model-routing/SKILL.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/CarlosZiegler/model-routing/blob/b8dbe9cb02f42031538226222427a67ac8350dd4/README.md](https://github.com/CarlosZiegler/model-routing/blob/b8dbe9cb02f42031538226222427a67ac8350dd4/README.md)

## Limits and data handling

Task briefs are sent to TypeSafe on your key; worker models incur their own provider costs.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit b8dbe9cb02f4](https://github.com/CarlosZiegler/model-routing/tree/b8dbe9cb02f42031538226222427a67ac8350dd4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
