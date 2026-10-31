# pi-skill-audit (Pi extension that reviews skills for tool conversion with Jev, the chat model, or both)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension with two advisory commands: `/skill-audit` reviews existing skills for possible conversion into tools or hybrid workflows using your current Pi chat model, TypeSafe's Jev classifier, or a side-by-side compare; `/skill-review` looks for a reusable procedure in the session that might deserve a new skill. Nothing is changed or executed automatically.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jamelwa/pi-skill-audit) |
| Maintainer | [jamelwa](https://github.com/jamelwa). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi 1.4.0+ with model-registry classifier support; `TYPESAFE_API_KEY` for Jev mode. |
| License | [MIT](https://github.com/jamelwa/pi-skill-audit/blob/491d76caa242da633e6f75e579b28ee43381ea14/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/skill-audit/index.ts`](https://github.com/jamelwa/pi-skill-audit/blob/491d76caa242da633e6f75e579b28ee43381ea14/extensions/skill-audit/index.ts) at the pinned commit. |

## When to use

- Triage a growing skills folder for things that should be deterministic tools.
- Mismatch: advisory only; it does not prove safety or verification.

## How it works

`extensions/skill-audit/index.ts` looks up Pi's built-in `typesafe/jev-latest` classifier and asks it typed questions about each skill; `compare` mode shows Jev and the chat model's answers together, after you confirm which files are sent. Integration evidence: [`extensions/skill-audit/index.ts`](https://github.com/jamelwa/pi-skill-audit/blob/491d76caa242da633e6f75e579b28ee43381ea14/extensions/skill-audit/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/jamelwa/pi-skill-audit
/skill-audit run --mode jev ./skills/example/SKILL.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jamelwa/pi-skill-audit#readme](https://github.com/jamelwa/pi-skill-audit#readme)

## Limits and data handling

Skill file contents are sent to TypeSafe only after explicit confirmation. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 491d76caa242](https://github.com/jamelwa/pi-skill-audit/tree/491d76caa242da633e6f75e579b28ee43381ea14). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
