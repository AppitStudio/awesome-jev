# Hermes-Skills jev skill (typed Jev decisions for Hermes Agent)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Hermes Agent skill pack that includes a `jev` skill, adapted from TypeSafe's upstream skill, with shell helpers to call Jev and triage requests, plus an upstream-sync check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ciberjohn/Hermes-Skills) |
| Maintainer | [ciberjohn](https://github.com/ciberjohn). Independently curated. |
| Format | Agent skill (Markdown + Bash, MIT) |
| Requirements | Hermes Agent, `curl`, and `TYPESAFE_API_KEY` in the profile `.env`. |
| License | [MIT](https://github.com/ciberjohn/Hermes-Skills/blob/0ca3df9d3cabcbb5bb979c8b73f160dbb1344130/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/scripts/jev-call.sh`](https://github.com/ciberjohn/Hermes-Skills/blob/0ca3df9d3cabcbb5bb979c8b73f160dbb1344130/jev/scripts/jev-call.sh) at the pinned commit. |

## When to use

- Give Hermes Agent typed Jev decisions for routing or gating.
- Keep a renamed copy of TypeSafe's skill in sync with upstream.
- Mismatch: mostly a repackaged upstream skill (MIT, TypeSafe AI) for Hermes.

## How it works

`jev/scripts/jev-call.sh` posts to `/v1/systemone` with the key read from the environment; `update-from-upstream.sh` compares the skill against TypeSafe's published `typesafe-ai` skill before re-syncing. Integration evidence: [`jev/scripts/jev-call.sh`](https://github.com/ciberjohn/Hermes-Skills/blob/0ca3df9d3cabcbb5bb979c8b73f160dbb1344130/jev/scripts/jev-call.sh).

## Get started

Copy the `jev/` folder into your Hermes skills directory (see the repo README for the location) and add the key to your profile `.env`.

```sh
git clone https://github.com/ciberjohn/Hermes-Skills.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skill README: [github.com/ciberjohn/Hermes-Skills/blob/0ca3df9d3cabcbb5bb979c8b73f160dbb1344130/jev/README.md](https://github.com/ciberjohn/Hermes-Skills/blob/0ca3df9d3cabcbb5bb979c8b73f160dbb1344130/jev/README.md)

## Limits and data handling

Whatever state the agent sends goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 0ca3df9d3cab](https://github.com/ciberjohn/Hermes-Skills/tree/0ca3df9d3cabcbb5bb979c8b73f160dbb1344130). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
