# Shepherd (self-hosted mission control for Claude Code with an opt-in TypeSafe Jev stop-classifier judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted mission control for interactive Claude Code (herdr + Bun + SvelteKit); an opt-in judge routes the autopilot stop classifier through TypeSafe Jev, with an eval harness and drift gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/erwins-enkel/shepherd) |
| Maintainer | [erwins-enkel](https://github.com/erwins-enkel). Independently curated. |
| Format | Bun/SvelteKit server (BUSL-1.1, source available) |
| Requirements | Bun, Claude Code, and `JEV_API_KEY` plus `SHEPHERD_JUDGE=true`. |
| License | [BUSL-1.1](https://github.com/erwins-enkel/shepherd/blob/7310bd0d31b822847644f02b76afb2b429f2f138/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Source available under the Business Source License 1.1 (not OSI open source). |
| Jev evidence | [`scripts/eval-jev.ts`](https://github.com/erwins-enkel/shepherd/blob/7310bd0d31b822847644f02b76afb2b429f2f138/scripts/eval-jev.ts) at the pinned commit. |

## When to use

- Decide when a Claude Code autopilot should stop with Jev.
- Evaluate classifier drift nightly.
- Mismatch: Business Source License, not OSI open source.

## How it works

With `SHEPHERD_JUDGE` and `JEV_API_KEY` set, the stop classifier calls `https://api.typesafe.ai` with pinned `jev-1.13.0`, falling back to a `claude` spawn on any failure; `scripts/eval-jev.ts` evaluates it. Integration evidence: [`scripts/eval-jev.ts`](https://github.com/erwins-enkel/shepherd/blob/7310bd0d31b822847644f02b76afb2b429f2f138/scripts/eval-jev.ts).

## Get started

Deploy per README, then set `SHEPHERD_JUDGE=true` and `JEV_API_KEY` in `~/.shepherd/env`.

```sh
git clone https://github.com/erwins-enkel/shepherd.git && cd shepherd
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/erwins-enkel/shepherd/blob/7310bd0d31b822847644f02b76afb2b429f2f138/README.md](https://github.com/erwins-enkel/shepherd/blob/7310bd0d31b822847644f02b76afb2b429f2f138/README.md)

## Limits and data handling

Session snippets for the stop classifier go to TypeSafe when the judge is armed.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 7310bd0d31b8](https://github.com/erwins-enkel/shepherd/tree/7310bd0d31b822847644f02b76afb2b429f2f138). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
