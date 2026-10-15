# system-one skill (magnus919)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent Skills-format skill for designing, integrating, evaluating and troubleshooting typed System One decisions with TypeSafe Jev (and open models such as Laya), keeping policy and side effects in code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/magnus919/agent-skills) |
| Maintainer | [magnus919](https://github.com/magnus919). Independently curated. |
| Format | Agent skill (Agent Skills format) inside the `agent-skills` collection |
| Requirements | An agent that supports Agent Skills (e.g. via `npx skills`); TypeSafe key only for live examples. |
| License | [MIT](https://github.com/magnus919/agent-skills/blob/122cb54fac8f9fa04ffa91eb75a5c0d641d46546/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/KlingonYellow/status/2110590602978934937)). |
| Jev evidence | [`system-one/SKILL.md`](https://github.com/magnus919/agent-skills/blob/122cb54fac8f9fa04ffa91eb75a5c0d641d46546/system-one/SKILL.md) at the pinned commit. |

## When to use

- Give a coding agent a checklist for Choice/Score/Noul question design, calibration and confidence-based escalation.
- Review an existing Jev integration for boundaries between model judgment and deterministic policy.
- Mismatch: guidance, not a library; the wider collection covers many unrelated skills.

## How it works

The skill frames each integration as authorized state + trusted typed questions -> validated answers -> deterministic policy -> act, wait, review or abstain, and ships references, templates, examples and evals for Jev and open-weight System One models. Integration evidence: [`system-one/SKILL.md`](https://github.com/magnus919/agent-skills/blob/122cb54fac8f9fa04ffa91eb75a5c0d641d46546/system-one/SKILL.md).

## Get started

From the upstream README (not run on the review host):

```sh
npx skills add magnus919/agent-skills --skill system-one
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skill folder: `system-one/` (references, templates, examples, evals).

## Limits and data handling

The skill itself sends nothing; any live examples you run send data to TypeSafe or the provider you choose.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 122cb54fac8f](https://github.com/magnus919/agent-skills/tree/122cb54fac8f9fa04ffa91eb75a5c0d641d46546). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
