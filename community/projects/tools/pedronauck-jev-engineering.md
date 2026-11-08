# jev-engineering skill by pedronauck (agent skill for designing and building with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill in pedronauck's skills collection for designing Jev use cases, POCs and production systems, with design modes, archetypes and reference Python/TypeScript clients.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pedronauck/skills) |
| Maintainer | [pedronauck](https://github.com/pedronauck). Independently curated. |
| Format | Agent skill (SKILL.md + clients) |
| Requirements | An agent that loads SKILL.md files, and a TypeSafe key for the reference clients. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/mine/jev-engineering/assets/jev_client.py`](https://github.com/pedronauck/skills/blob/682e7388ba61ae21ede674f5577bd81eb2e863b7/skills/mine/jev-engineering/assets/jev_client.py) at the pinned commit. |

## When to use

- Have a coding agent design a Jev integration.
- Study the reference Python/TypeScript clients.
- Mismatch: no license; ask the author before reuse.

## How it works

SKILL.md guides design (modes, archetypes, statuses/budget/cache) and ships `assets/jev_client.py` / `jev-client.ts` reference clients for the System One API; facts were checked live by the author on 2026-11-02. Integration evidence: [`skills/mine/jev-engineering/assets/jev_client.py`](https://github.com/pedronauck/skills/blob/682e7388ba61ae21ede674f5577bd81eb2e863b7/skills/mine/jev-engineering/assets/jev_client.py).

## Get started

Read `skills/mine/jev-engineering/SKILL.md` upstream; the repository grants no license, so ask the author before copying or redistributing it.

```sh
git clone https://github.com/pedronauck/skills.git && cd skills
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- SKILL.md: [github.com/pedronauck/skills/blob/682e7388ba61ae21ede674f5577bd81eb2e863b7/skills/mine/jev-engineering/SKILL.md](https://github.com/pedronauck/skills/blob/682e7388ba61ae21ede674f5577bd81eb2e863b7/skills/mine/jev-engineering/SKILL.md)

## Limits and data handling

The reference clients send state you supply to TypeSafe.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 682e7388ba61](https://github.com/pedronauck/skills/tree/682e7388ba61ae21ede674f5577bd81eb2e863b7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
