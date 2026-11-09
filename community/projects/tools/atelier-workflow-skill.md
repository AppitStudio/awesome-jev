# Atelier (Claude Code workflow-template skill that uses Jev for model routing and judgment calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill (formerly pbi-orchestration-jev) that runs development as a nine-stage template, splitting work into PBIs for sub-agents; Jev reads short briefs to help pick models and make judgment calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/reeschan/atelier) |
| Maintainer | [reeschan](https://github.com/reeschan). Independently curated. |
| Format | Claude Code skill (MIT) |
| Requirements | Claude Code, the sub-agent CLIs you use, and a TypeSafe key for Jev. |
| License | [MIT](https://github.com/reeschan/atelier/blob/df1925e94471613de64be976639f0dd847d7db21/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/atelier/jev/jev.py`](https://github.com/reeschan/atelier/blob/df1925e94471613de64be976639f0dd847d7db21/skills/atelier/jev/jev.py) at the pinned commit. |

## When to use

- Orchestrate sub-agents with a repeatable workflow.
- Pick a model per task with a decision table plus Jev.
- Mismatch: Jev informs routing; it does not decide pass/fail.

## How it works

`skills/atelier/jev/jev.py` and `jev.mjs` send short text to TypeSafe; `select_model.py` combines counted facts with Jev's reading of novelty and coupling, while pass/fail stays with real verification commands. Integration evidence: [`skills/atelier/jev/jev.py`](https://github.com/reeschan/atelier/blob/df1925e94471613de64be976639f0dd847d7db21/skills/atelier/jev/jev.py).

## Get started

Install the skill per the README and copy `jev.config.template.json` with your key.

```sh
git clone https://github.com/reeschan/atelier.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/reeschan/atelier/blob/df1925e94471613de64be976639f0dd847d7db21/README.md](https://github.com/reeschan/atelier/blob/df1925e94471613de64be976639f0dd847d7db21/README.md)

## Limits and data handling

Short task briefs are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit df1925e94471](https://github.com/reeschan/atelier/tree/df1925e94471613de64be976639f0dd847d7db21). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
